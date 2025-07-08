# This file is not part of the ELT pipeline it is only used for uploading the data to render.com.
import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# Load environment variables
load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

# Create SQLAlchemy engine
db_url = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}?sslmode=require"
engine = create_engine(db_url)

# Path to the data folder (RegTech/data)
regtech_dir = Path(__file__).resolve().parent.parent
data_dir = regtech_dir / "data"

# Map CSV filenames (without extension) to Postgres table names
csv_to_table_map = {
    "dim_empresa": "dim_empresa",
    "dim_cliente": "dim_cliente",
    "dim_pix": "dim_pix",
    "fato_contato": "fato_contato"
}

# Loop through each CSV file and upload
for csv_file, table_name in csv_to_table_map.items():
    csv_path = data_dir / f"{csv_file}.csv"
    if not csv_path.exists():
        print(f"CSV file not found: {csv_path}")
        continue

    # Read CSV into dataframe
    df = pd.read_csv(csv_path)
    print(f"Uploading {csv_path.name} -> {table_name} ({len(df)} rows)")

    # Upload to PostgreSQL (replace table)
    df.to_sql(table_name, engine, if_exists='replace', index=False, method='multi')

print("All CSV files uploaded successfully to PostgreSQL.")
