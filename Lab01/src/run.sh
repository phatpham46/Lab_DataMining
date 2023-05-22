# Question 1: Extract columns with missing values
python3 question1.py house-prices.csv

# Question 2: Count the number of lines with missing data
python3 question2.py house-prices.csv

# Question 3: Fill in the missing value using mean, median (for numeric properties) and mode (for the categorical attribute)
python3 question3.py house-prices.csv --method=mean --columns=LotFrontage --out=fill_nan_values.csv

# Question 4: Deleting rows containing more than a particular number of missing values (Example: delete rows with the number of missing values is more than 50% of the number of attributes)
python3 question4.py house-prices.csv --threshold=0.5 --out=del_rows.csv

# Question 5: Deleting columns containing more than a particular number of missing values (Example: delete columns with the number of missing values is more than 50% of the number of samples)
python3 question5.py house-prices.csv --threshold=0.5 --out=del_cols.csv

# Question 6. Delete duplicate samples
python3 question6.py house-prices.csv --out=del_dup.csv

# Question 7: Normalize a numeric attribute using min-max and Z-score methods.
python3 question7.py house-prices.csv --method=min-max --columns=LotFrontage --out=normalize.csv

# Question 8: Performing addition, subtraction, multiplication, and division between two numerical attributes
python3 question8.py house-prices.csv --method=add --columns=LotFrontage,1stFlrSF --out=add.csv
python3 question8.py house-prices.csv --method=sub --columns=LotFrontage,1stFlrSF --out=sub.csv
python3 question8.py house-prices.csv --method=mul --columns=LotFrontage,1stFlrSF --out=mul.csv
python3 question8.py house-prices.csv --method=div --columns=LotFrontage,1stFlrSF --out=div.csv

