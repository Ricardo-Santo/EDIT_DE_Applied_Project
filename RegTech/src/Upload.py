# This file is not part of the ELT pipeline it is only used for uploading the data to render.com.
import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine


# Load from environment variables
load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT") 
db_name = os.getenv("DB_NAME")

# Create SQLAlchemy engine
db_url = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}?sslmode=require"
engine = create_engine(db_url)

# Load Excel file
excel_file = "RegTech/data/dw_prospeccao_comercial.xlsx"

# Map sheet names to table names
sheet_to_table_map = {
    "dim_empresa": "dim_empresa",
    "dim_cliente": "dim_cliente",
    "dim_pix": "dim_pix",
    "fato_contato": "fato_contato"
}

# Loop through through different sheets and upload
for sheet_name, table_name in sheet_to_table_map.items():
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    print(f"Uploading {sheet_name} -> {table_name} ({len(df)} rows)")
    df.to_sql(table_name, engine, if_exists='replace', index=False, method='multi')

print("All sheets uploaded successfully to Render PostgreSQL.")
