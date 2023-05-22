from utils import *

# 2. Count the number of lines with missing data
def count_rows_with_missing_data(data):
    count = 0
    for row in range(len(data)):
        for col in data.columns:
            if pd.isnull(data[col][row]):
                count += 1
                break
    return count

def main():
    data, args = read_data_by_arg()
    print(f'Question 2: Number of rows with missing values: {count_rows_with_missing_data(data)} samples')
    print('------------------------------------')

if __name__ == '__main__':
    main()