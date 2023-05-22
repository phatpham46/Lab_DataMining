from utils import *

# 4. Deleting rows containing more than a particular number of missing values (Example: delete rows with the number of missing values is more than 50% of the number of attributes).

def num_nan_in_row(row):
   num_nan = 0
   for i in range(len(row)):
      if pd.isnull(row[i]):
         num_nan += 1
   return num_nan

def delete_rows_contain_nan(data, threshold):
   # convert threshold to float type
   result = data.copy()
   threshold = float(threshold)
   if threshold < 0 or threshold > 1:
      print('Threshold must be between 0 and 1')
      return result
   
   num_attributes = len(data.columns)
   max_missing_values = int(num_attributes * threshold)
   
   # loop through all rows in data and delete rows containing more than a particular number of missing values
   for i in range(len(data)):
      num_missing_values = num_nan_in_row(data.iloc[i])
      if num_missing_values > max_missing_values:
         result = result[result.index != i]
         
   return result
   
      
def main():
   # Read data from CSV file
   data, args = read_data_by_arg()

   # Delete rows containing more than a particular number of missing values
   results = delete_rows_contain_nan(data, args.threshold)
   print('Question 4: Deleting rows containing more than a particular number of missing values with threshold ' + str(args.threshold) + ' successfully!')
   print('------------------------------------')

   # Write result to output CSV file
   write_data_by_arg(results, args.out)

if __name__ == '__main__':
   main()