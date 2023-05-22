import sys
import pandas as pd
import argparse

def lenght(df, option):
   count = 0
   if option == 'row':
      for row in df:
         count += 1
   elif option == 'column':
      for column in df:
         count += 1
   return count

# define sum of all values in column
def sum_of_column(df, column):
   sum = 0 
   for val in df[column]:
      if not pd.isnull(val):
         sum = sum + val
   return sum

# function count null values in column
def count_null_values(df, column):
   count = 0
   for val in df[column]:
      if pd.isnull(val):
         count += 1
   return count

# define mean of all values in column
def is_numeric_column(df, column):
   for val in df[column]:
      if not isinstance(val, (int, float)):
         return False
   return True

# min function
def min_of_column(df, column):
    min_val = df[column][0]
    for val in df[column][1:]:
        if val < min_val:
            min_val = val
    return min_val

# max function
def max_of_column(df, column):
    max_val = df[column][0]
    for val in df[column][1:]:
        if val > max_val:
            max_val = val
    return max_val

# mean of all values in column
def mean_of_column(df, column):
   sum = sum_of_column(df, column)
   num_not_null = len(df[column]) - count_null_values(df, column)
   return round(sum / num_not_null, 2)

def read_data_by_arg():
   parser = argparse.ArgumentParser()
   parser.add_argument("input_file", default="house-prices.csv", help="input CSV file")
   parser.add_argument("--method", help="method to fill nan values(mean, median, mode)")
   parser.add_argument("--columns", help="name of columns")
   parser.add_argument("--threshold", default=0.5, help="threshold for deleting columns")
   parser.add_argument("--out", default= "fill_nan_values.csv", help="output CSV file")
   args = parser.parse_args()
   
   # read the data from the csv file by argument
   if len(sys.argv) > 1:
      path_file = '../data/' + args.input_file
      data = pd.read_csv(path_file)
      return data, args
   else:
      print('Please provide the path of the csv file as argument')
      sys.exit(1)
      
def write_data_by_arg(data, output_file):
   path_file = '../data/' + output_file
   data.to_csv(path_file, index=False)