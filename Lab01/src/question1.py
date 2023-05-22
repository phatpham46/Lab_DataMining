from utils import *

def list_missing_columns(data):
    missing_cols = []
    # Loop through each column in the data
    for col in data.columns:
        for val in data[col]:
            # Check if value is missing in column and add to list of missing columns 
            if pd.isnull(val):
                missing_cols.append(col)
                break
                
    return missing_cols   

def main():
    data, args = read_data_by_arg()
    print("Question 1: List of columns with any missing values:\n", list_missing_columns(data))
    print('------------------------------------')
    
if __name__ == '__main__':
    main()