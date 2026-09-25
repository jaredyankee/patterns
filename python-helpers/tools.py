# tools
# things used in other python scripts
#
# Overloaded with optional paramter
# values - 2D list of values for each column
#  - *values must be the same length as columns
#  - *all subarrays in values must have same length* 
#
#
def create_dataframe_template (columns, values = []):
    # validate values
    use_values = None
    if len(values):
        use_values = (
            len(values) == len(columns) 
            and all(len(v) == len(values[0]) for v in values)
        )

    result = {}
    if (use_values):
        # uses enumerate if necessay
        for i, c in enumerate(columns):
            result[c] = values[i]
    else:
        for c in columns:
            result[c] = []
    return result


# returns dataframe as a 2d array
def get_all_columns (df):
    all_columns = []
    for c in list(df.columns):
        # convert column to a list and add to all_columns
        all_columns.append(list(df[c]))
    return all_columns

