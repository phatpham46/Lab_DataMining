from utils import *

# 7. Normalize a numeric attribute using min-max and Z-score methods.

# standard deviation of all not null values in column
def standard_deviation(df, column):
    mean = mean_of_column(df, column)
    sum = 0
    for val in df[column]:
        if not pd.isnull(val):
            sum += (val - mean) ** 2
    return round((sum / (len(df[column]) - 1)) ** 0.5, 2)

# normalize using min-max
def normalize_min_max(df, column):
    min = min_of_column(df, column)
    max = max_of_column(df, column)
    df_norm = df.copy()
    for i in range(len(df[column])):
        df_norm.loc[i, column] = (df_norm[column].iloc[i] - min) / (max - min)
    return df_norm

# normalize using z-score
def normalize_z_score(df, column):
    mean = mean_of_column(df, column)
    std = standard_deviation(df, column)
    for i in range(len(df[column])):
        df[column].iloc[i] = (df[column].iloc[i] - mean) / std
    return df

def main():
    # # Load input CSV file
    data, args = read_data_by_arg()

    if is_numeric_column(data, args.columns):
        if args.method == 'min-max':
            data = normalize_min_max(data, args.columns)
        elif args.method == 'z-score':
            data = normalize_z_score(data, args.columns)
            
    print('Question 7: Normalize data by ' + args.method + ' method' + ' for column ' + args.columns + ' successfully')
    print('------------------------------------')
    
    # Write result to output CSV file
    write_data_by_arg(data, args.out)

if __name__ == "__main__":
    main() 