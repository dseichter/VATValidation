# Copyright (c) 2024-2026 Daniel Seichter
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

# Import the VATValidation library
import single
import settings

# import common libraries
import json
import pandas as pd
import pathlib

import logging_config  # Setup the logging  # noqa: F401
import logging


logger = logging.getLogger(__name__)

COLUMNS = ["key1", "key2", "ownvat", "foreignvat", "company", "street", "zip", "town"]


def validatebatch(inputfile, outputfile="", lang="en", statusupdate=False):
    """
    Validate the batch file and write the results to the output file.
    """
    # get the file extension
    ext = pathlib.Path(inputfile).suffix[1:].lower() 

    # if the output file is not set, use the input file with a different extension
    # using the UI, this error can't happen, because the user has to select the output file
    if not outputfile:
        outputfile = inputfile.replace(ext, f"log.{ext}")

    match ext:
        case "csv":
            resultcode = processcsv(inputfile, outputfile, lang, statusupdate)
            return resultcode
        case "xlsx":
            resultcode = processxlsx(inputfile, outputfile, lang, statusupdate)
            return resultcode
        case "json":
            resultcode = processjson(inputfile, outputfile, lang, statusupdate)
            return resultcode
        case _:
            logger.error("Unsupported file format")
            return 127


def _load_data_from_file(inputfile, ext):
    """Load data from file based on extension. Returns (data, error_code) tuple."""
    try:
        if ext == "csv":
            # read the file and check if all rows have the same number of columns
            with open(inputfile, 'r') as f:
                first_line = f.readline().strip()
                # check if the first line is empty
                if not first_line:
                    logger.error("Input file is empty.")
                    return None, 2

                delimiter = settings.load_value_from_json_file("delimiter")
                # check if the first line ends with the delimiter
                if first_line.endswith(delimiter):
                    logger.error("First line ends with the delimiter.")
                    return None, 5

                split_columns = first_line.split(delimiter)
                if len(split_columns) != len(COLUMNS):
                    logger.error(f"Expected {len(COLUMNS)} columns, but found {len(split_columns)}.")
                    return None, 4

            # read csv with columns
            data = pd.read_csv(
                inputfile,
                names=COLUMNS,
                delimiter=settings.load_value_from_json_file("delimiter"),
            )
        elif ext == "xlsx":
            # read the input file
            data = pd.read_excel(inputfile, usecols=COLUMNS)
            # check, if all columns are present
            for column in COLUMNS:
                if column not in data.columns:
                    logger.error(f"Missing column: {column}")
                    return None, 4
        elif ext == "json":
            data = pd.read_json(inputfile)
        else:
            return None, 127

        return data, 0

    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        return None, 1
    except pd.errors.EmptyDataError as e:
        logging.error(f"Empty data error: {e}")
        return None, 2
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None, 99


def _save_results_to_file(dataframe, outputfile, ext):
    """Save results DataFrame to file based on extension."""
    try:
        if ext == "csv":
            dataframe.to_csv(outputfile, index=False, header=True, sep=settings.load_value_from_json_file("delimiter"))
        elif ext == "xlsx":
            dataframe.to_excel(outputfile, index=False, header=False)
        elif ext == "json":
            dataframe.to_json(outputfile, orient="records", lines=False, indent=2)
    except Exception as e:
        logging.error(f"Error saving file: {e}")
        return 99
    return 0


def _process_batch_data(data, lang, statusupdate, skip_header=False):
    """Process batch data and return validation results."""
    results = []
    write_status_update(statusupdate, len(data), 0)
    
    for index, row in data.iterrows():
        # skip first line only if it contains the column names
        if skip_header and index == 0 and all(str(row[col]).strip() == col for col in COLUMNS):
            continue
        
        # write statistics
        write_status_update(statusupdate, len(data), index)
        
        # validate the row
        message = single.validatesingle(
            key1=row["key1"],
            key2=row["key2"],
            ownvat=row["ownvat"],
            foreignvat=row["foreignvat"],
            company=row["company"],
            street=row["street"],
            zip=row["zip"],
            town=row["town"],
            lang=lang
        )

        # parse everything as string to easily replace newlines
        tempstring = json.dumps(message)
        tempstring = tempstring.replace('\\n', ' ').replace('\\r', ' ')
        tempstring = tempstring.replace('  ', ' ')
        message = json.loads(tempstring)

        # append the result to the results list
        results.append(message)

    return results


def processcsv(inputfile, outputfile, lang, statusupdate):
    """Process CSV file for batch validation."""
    ext = "csv"
    data, error_code = _load_data_from_file(inputfile, ext)
    
    if error_code != 0:
        return error_code

    results = _process_batch_data(data, lang, statusupdate, skip_header=True)
    dataframe = pd.DataFrame(results)
    
    return _save_results_to_file(dataframe, outputfile, ext)


def processxlsx(inputfile, outputfile, lang, statusupdate):
    """Process XLSX file for batch validation."""
    ext = "xlsx"
    data, error_code = _load_data_from_file(inputfile, ext)
    
    if error_code != 0:
        return error_code

    results = _process_batch_data(data, lang, statusupdate, skip_header=False)
    dataframe = pd.DataFrame(results)
    
    return _save_results_to_file(dataframe, outputfile, ext)


def processjson(inputfile, outputfile, lang, statusupdate):
    """Process JSON file for batch validation."""
    ext = "json"
    data, error_code = _load_data_from_file(inputfile, ext)
    
    if error_code != 0:
        return error_code

    results = _process_batch_data(data, lang, statusupdate, skip_header=False)
    dataframe = pd.DataFrame(results)
    
    return _save_results_to_file(dataframe, outputfile, ext)


def write_status_update(statusupdate, total, current):
    if statusupdate:
        with open('batchstatus.json', 'w') as f:
            data = {
                "total": total,
                "current": current + 1
            }
            json.dump(data, f)
