from utils import *

# 8. Performing addition, subtraction, multiplication, and division between two numerical attributes
def perform_arithmetic_operation(data, op, attr1, attr2):
   if is_numeric_column(data, attr1) and is_numeric_column(data, attr2):
      if op == 'add':
         data[attr1] = data[attr1] + data[attr2]
      elif op == 'sub':
         data[attr1] = data[attr1] - data[attr2]
      elif op == 'mul':
         data[attr1] = data[attr1] * data[attr2]
      elif op == 'div':
         data[attr1] = data[attr1] / data[attr2]
   else:
      if not is_numeric_column(data, attr1):
         print(attr1 + ' is not a numeric column')
      if not is_numeric_column(data, attr2):
         print(attr2 + ' is not a numeric column')
   return data

def main():
   # Read data from CSV file
   data, args = read_data_by_arg()

   # Perform arithmetic operation
   cols_str = args.columns.split(',')
   results = perform_arithmetic_operation(data, args.method, cols_str[0], cols_str[1])
   print('Question 8: Performing ' + args.method + ' between two numerical attributes successfully!')
   print('------------------------------------')

   # Write result to output CSV file
   write_data_by_arg(results, args.out)

if __name__ == '__main__':
   main()
    