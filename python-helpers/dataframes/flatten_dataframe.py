# flatten-rows.py
#
# Flattens rows in a CSV based on a column with duplicate values
import pandas as pd
import json
from tools import create_dataframe_template
# 
# @param df - pd DataFrame 
# @param flatten_header - string
# @
###
#   {
#        flatten_header: str 
#        sum_header: str || [],
#   }
###
# NOT WORKING IN-PLACE 
#   Creates and returns new DataFrame
#
def flatten_dataframe(df, flatten_header, sum_headers = []):
    df = df.fillna("") # fill empty cells with ""
    columns = list(df.columns)
    
    # columns will be flattened based on flatten_header
    while flatten_header not in columns:
        flatten_header = input("This column header is not present in the dataframe. Try typing it here: ")
    
    # remove flatten header from the columns we iterate
    columns.remove(flatten_header)
    
    # @todo '*' wildcard to sum all float columns
    # converts string to array with length 1
    if isinstance(sum_headers, str):
        if sum_headers != "":
            sum_headers = [sum_headers]
    
    data = {}
    data[flatten_header] = list(set(list(df[flatten_header])))
    
    # iterate through collapsable values
    for flatten_value in data[flatten_header]:
        # sub_df has only rows containing flatten_value in flatten_header column
        sub_df = df.loc[df[flatten_header] == flatten_value].reset_index()
        
        for c in list(columns):
            # if there are different values we can't identify which row has the one to keep,
            # drop it from data and columns (so we stop adding it to data) 
            if (c not in data):
                data[c] = []
            if c not in sum_headers and len(list(set(list(df[c])))) != 1:
                print(f"Removing column {c}")
                columns.remove(c)
                if c in data:
                    data.pop(c)
            # add to data if not there yet
            else:
                if c in sum_headers:
                    # sum all of the rows
                    temp = pd.to_numeric(sub_df[c], errors="coerce").sum()
                    data[c].append(pd.to_numeric(sub_df[c], errors="coerce").sum()) # sets all non-flaots to NaN. For those who don't know, NaN is, ironically, a number
                elif c in data:
                    data[c].append(sub_df[c][0])
            
    df_out = pd.DataFrame(data)
    return df_out



                


                
        


     




    
