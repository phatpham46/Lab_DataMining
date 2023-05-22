from utils import *

# 5. Deleting columns containing more than a particular number of missing values (Example: delete columns with the number of missing values is more than 50% of the number of samples)

# function to delete columns if the number of missing values is more than threshold * number of samples
def del_columns(df, threshold):
    print('Number of columns before deleting: ', len(df.columns))
    for col in df.columns:
        if count_null_values(df, col) > threshold * len(df[col]):
            print('Deleting column: ', col)
            del df[col]
    print('Number of columns after deleting: ', len(df.columns))
    return df

def main():
    # Read data from CSV file
    data, args = read_data_by_arg()

    # Delete columns
    data = del_columns(data, float(args.threshold))
    print('Question 5: Delete columns with more than ', args.threshold, ' missing values successfully!')
    print('------------------------------------')
    # Write result to output CSV file
    write_data_by_arg(data, args.out)

if __name__ == "__main__":
    main() 
