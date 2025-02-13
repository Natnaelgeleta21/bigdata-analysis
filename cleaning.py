import pandas as pd

# Load the CSV file 
df = pd.read_csv("Large Ecommerce Dataset.csv", low_memory=False)
# Remove empty rows 
df = df.dropna(how="all")
# Remove duplicate rows
df = df.drop_duplicates()
# Remove unwanted columns 
df = df.drop(columns=["Unnamed: 21", "Unnamed: 22", "Unnamed: 23", "Unnamed: 24", "Unnamed: 25","sales_commission_code"])
# Save the cleaned data
df.to_csv("cleaned_data.csv", index=False)
print("Duplicates, empty rows, and unwanted columns removed. Cleaned data saved as 'cleaned_data.csv'.")
