import pandas as pd
from sqlalchemy import create_engine

#  Database connection details
DB_NAME = "BDBIDB"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "localhost"  # Change to your server's IP if remote
DB_PORT = "5432"

#  Load cleaned dataset
file_path = "cleaned_data.csv"
df = pd.read_csv(file_path)

#  Define table name
table_name = "ecommerce_data"

#  Create a PostgreSQL connection using SQLAlchemy
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

#  Ensure column names match exactly before loading
expected_columns = [
    "item_id", "status", "created_at", "sku", "price", "qty_ordered", "grand_total", 
    "increment_id", "category_name_1", "discount_amount", 
    "payment_method", "Working Date", "BI Status", "MV", "Year", "Month", 
    "Customer Since", "M-Y", "FY", "Customer ID"
]

#  Load dataset into PostgreSQL
try:
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f" Cleaned data successfully loaded into PostgreSQL table '{table_name}'.")
except Exception as e:
    print(f" Error loading data: {e}")