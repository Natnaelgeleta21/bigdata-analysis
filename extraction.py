import pandas as pd

file_path = 'Large Ecommerce Dataset.csv'
# Read the CSV file
df = pd.read_csv(file_path)

# Display the number of rows
print("Number of rows in the CSV file:", len(df))
