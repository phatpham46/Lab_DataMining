from utils import *

# 3. Fill in the missing value using mean, median (for numeric properties) and mode (for the categorical attribute).

# define median of all values in column
def median_of_column(df, column):
    df.sort_values(by=column, inplace=True)
    num_not_null = len(df[column]) - count_null_values(df, column)
    
    if num_not_null % 2 == 0:
        return (df[column].iloc[num_not_null // 2] + df[column].iloc[num_not_null // 2 - 1]) / 2
    return df[column].iloc[num_not_null // 2]
    
# define mode of all values in column
def mode_of_column(df, column):
    mode = {}
    for val in df[column]:
        if val in mode:
            mode[val] += 1
        else:
            mode[val] = 1
    max_count = 0
    max_val = None
    for key in mode:
        if mode[key] > max_count:
            max_count = mode[key]
            max_val = key
    return max_val

def fill_missing_values(df, method, column):
    df_copy = df.copy()
    for i in range(len(df_copy[column])):
        if pd.isnull(df_copy[column][i]):
            if method == 'mean':
                df_copy.loc[i, column] = mean_of_column(df, column)
            elif method == 'median':
                df_copy.loc[i, column] = median_of_column(df, column)
            elif method == 'mode':
                df_copy.loc[i, column] = mode_of_column(df, column)
    return df_copy

def is_numeric_column(df, column):
    for val in df[column]:
        if not isinstance(val, (int, float)):
            return False
    return True

def main():
    data, args = read_data_by_arg()
    
    # Fill missing values
    if is_numeric_column(data, args.columns):
        data = fill_missing_values(data, args.method, args.columns)
    else:
        print('Not numeric column, cannot fill missing values by this method.')
    print('Question 3: Fill missing values by method = ', args.method, 'for column = ', args.columns, ' successfully!')
    print('------------------------------------')
    
    # Write result to output CSV file
    write_data_by_arg(data, args.out)

if __name__ == "__main__":
    main()  