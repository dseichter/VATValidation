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
import pandas as pd

columns = ["key1", "key2", "ownvat", "foreignvat", "company", "street", "zip", "town"]


def validatebatch(inputfile, outputfile="", type="vies", lang="en", iscli=False):
    """
    Validate the batch file and write the results to the output file.
    """
    # get the file extension
    ext = inputfile.split(".")[-1].lower()

    # if the output file is not set, use the input file with a different extension
    if not outputfile:
        outputfile = inputfile.replace(ext, f"log.{ext}")

    match ext:
        case "csv":
            resultcode = processcsv(inputfile, outputfile, type, lang)
            if iscli:
                return resultcode
        case "xlsx":
            resultcode = processxlsx(inputfile, outputfile, type, lang)
            if iscli:
                return resultcode
        case "json":
            resultcode = processjson(inputfile, outputfile, type, lang)
            if iscli:
                return resultcode
        case _:
            print("Unsupported file format")
            return 127


def processcsv(inputfile, outputfile, type, lang):
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
            lang=lang,
            iscli=True
        )
        # append the result to the results list
        results.append(message)

    # load the results into a DataFrame
    dataframe = pd.DataFrame(results)

    # save the dateframe to a csv file
    dataframe.to_csv(outputfile, index=False, header=False)

    return True


def processxlsx(inputfile, outputfile, type, lang):
    # read the input file
    data = pd.read_excel(inputfile, usecols=columns)
    # create a list to store the results
    results = []
    # iterate over the rows
    for index, row in data.iterrows():
        # validate the row
        _, message = single.validatesingle(
            key1=row["key1"],
            key2=row["key2"],
            ownvat=row["ownvat"],
            foreignvat=row["foreignvat"],
            company=row["company"],
            street=row["street"],
            zip=row["zip"],
            town=row["town"],
            type=type,
            lang=lang,
            iscli=True,
        )
        # append the result to the results list
        results.append(message)

    # load the results into a DataFrame
    dataframe = pd.DataFrame(results)

    # save the dateframe to a csv file
    dataframe.to_excel(outputfile, index=False, header=False)


def processjson(inputfile, outputfile, type, lang):
    data = pd.read_json(inputfile)
    # create a list to store the results
    results = []
    # iterate over the rows
    for index, row in data.iterrows():
        # validate the row
        _, message = single.validatesingle(
            key1=row["key1"],
            key2=row["key2"],
            ownvat=row["ownvat"],
            foreignvat=row["foreignvat"],
            company=row["company"],
            street=row["street"],
            zip=row["zip"],
            town=row["town"],
            type=type,
            lang=lang,
            iscli=True,
        )
        # append the result to the results list
        results.append(message)

    # load the results into a DataFrame
    dataframe = pd.DataFrame(results)

    # save the dateframe to a json file
    dataframe.to_json(outputfile, orient="records", lines=False, indent=2)
