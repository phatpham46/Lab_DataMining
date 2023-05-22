from utils import *

# 6. Delete duplicate samples
def delete_duplicate(data):
   # convert data to list
   new_data = data.values.tolist()

   new_list = []
   for row in new_data:
      for i in range(len(row)):
         if isinstance(row[i], float) and row[i] != row[i]:
            row[i] = None
      if row not in new_list:
         new_list.append(row)
   return pd.DataFrame(new_list, columns=data.columns)

def main():
   # Read data from CSV file
   data, args = read_data_by_arg()

   # Delete duplicate samples
   new_data = delete_duplicate(data)
   print('Question 6: Delete duplicate samples successfully!')
   print('------------------------------------')

   # Write result to output CSV file
   write_data_by_arg(new_data, args.out)
   
if __name__ == '__main__':
   main()