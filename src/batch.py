# Copyright (c) 2024 Daniel Seichter
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

import logging_config  # Setup the logging  # noqa: F401
import logging

logger = logging.getLogger(__name__)

columns = ["key1", "key2", "ownvat", "foreignvat", "company", "street", "zip", "town"]


def validatebatch(inputfile, outputfile="", type="vies", lang="en"):
    """
    Validate the batch file and write the results to the output file.
    """
    # get the file extension
    ext = inputfile.split(".")[-1].lower()

    # if the output file is not set, use the input file with a different extension
    # using the UI, this error can't happen, because the user has to select the output file
    if not outputfile:
        outputfile = inputfile.replace(ext, f"log.{ext}")

    match ext:
        case "csv":
            resultcode = processcsv(inputfile, outputfile, type, lang)
            return resultcode
        case "xlsx":
            resultcode = processxlsx(inputfile, outputfile, type, lang)
            return resultcode
        case "json":
            resultcode = processjson(inputfile, outputfile, type, lang)
            return resultcode
        case _:
            logger.error("Unsupported file format")
            return 127


def processcsv(inputfile, outputfile, type, lang):
    try:
        # read csv with columns
        data = pd.read_csv(
            inputfile,
            names=columns,
            delimiter=settings.load_value_from_json_file("delimiter"),
        )
        # create a list to store the results
        results = []
        # iterate over the rows
        for index, row in data.iterrows():
            # skip first line, because it contains the column names
            if index == 0:
                continue
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
                type=type,
                lang=lang
            )

            # parse everything as string to easily replace newlines
            tempstring = json.dumps(message)
            tempstring = tempstring.replace('\\n', ' ').replace('\\r', ' ')
            tempstring = tempstring.replace('  ', ' ')
            message = json.loads(tempstring)

            # append the result to the results list
            results.append(message)

        # load the results into a DataFrame
        dataframe = pd.DataFrame(results)

        # save the dateframe to a csv file
        dataframe.to_csv(outputfile, index=False, header=False)

        return 0

    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        return 1
    except pd.errors.EmptyDataError as e:
        logging.error(f"Empty data error: {e}")
        return 2
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return 99


def processxlsx(inputfile, outputfile, type, lang):
    try:
        # read the input file
        data = pd.read_excel(inputfile, usecols=columns)
        # create a list to store the results
        results = []
        # iterate over the rows
        for index, row in data.iterrows():
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
                type=type,
                lang=lang
            )
            # append the result to the results list
            results.append(message)

        # load the results into a DataFrame
        dataframe = pd.DataFrame(results)

        # save the dateframe to a xlsx file
        dataframe.to_excel(outputfile, index=False, header=False)

        return 0

    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        return 1
    except pd.errors.EmptyDataError as e:
        logging.error(f"Empty data error: {e}")
        return 2
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return 99


def processjson(inputfile, outputfile, type, lang):
    try:
        data = pd.read_json(inputfile)
        # create a list to store the results
        results = []
        # iterate over the rows
        for index, row in data.iterrows():
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
                type=type,
                lang=lang
            )
            # append the result to the results list
            results.append(message)

        # load the results into a DataFrame
        dataframe = pd.DataFrame(results)

        # save the dateframe to a json file
        dataframe.to_json(outputfile, orient="records", lines=False, indent=2)

        return 0

    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        return 1
    except pd.errors.EmptyDataError as e:
        logging.error(f"Empty data error: {e}")
        return 2
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return 99
