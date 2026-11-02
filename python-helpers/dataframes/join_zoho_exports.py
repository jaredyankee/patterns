# join_zoho_exports.py
from .dataframes import create_dataframe_template
import pandas as pd
import os.path


# to leave NaN in blank cells pass fill_na = None
def join_csvs (paths = [], fill_na = "", return_on_fail = True):
    if not len(paths):
        return "No files provided."
    df = None
    data = None
    for path in paths:
        try:
            df = pd.read_csv(path)
            if fill_na != None:
                df = df.fillna(fill_na)
            # initialize 'data' based on first df
            if not data:
                data = create_dataframe_template(df)

            for c in list(df.columns):
                data[c] = data[c] + list(df[c]) # concats list from df column to data

        except Exception as err:
            print(f"An error occurred with file '{filename}': err")
            if return_on_fail:
                return {
                    "ok": False,
                    "message": err
                }
    return pd.DataFrame(data)

# extension of join csvs:
# When creating exports in Zoho, files are broken up at 25000 lines to limit file sizes
#   You'll received a zip file including "Prefix00.csv", "Prefix01.csv". etc..
#
# This script will work in general for any set of sheets with the same prefix and an incrementing number after them like above.
#
# Takes a path to the first file
# tries to find all files with the suffix incrementing by one until nothing found
# then joins the sheets
def join_zoho_sheets (path):
    if not os.path.exists(path):
        return {
            "ok": False,
            "message": f"No file found at path {path}"
        }

    


    

    
