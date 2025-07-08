import os
import csv
from pathlib import Path
from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build

from pathlib import Path

# Full path to current script: RegTech/export_sheets.py
script_dir = Path(__file__).resolve().parent
regtech_dir = Path(__file__).resolve().parent.parent

# Go up to the project root
project_root = Path(__file__).resolve().parents[2]
load_dotenv(dotenv_path=project_root / ".env")

# Path to credentials.json at project root
SERVICE_ACCOUNT_FILE = Path(__file__).resolve().parents[2] / "credentials.json"


SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# Spreadsheet ID from .env

SPREADSHEET_ID = os.getenv("GOOGLE_SHEET_ID")
print("Loaded SPREADSHEET_ID:", SPREADSHEET_ID)
if not SPREADSHEET_ID:
    raise ValueError("GOOGLE_SHEET_ID not found in .env or is empty")

# Sheets to export
sheets_to_export = ["dim_empresa", "dim_cliente", "dim_pix", "fato_contato"]

# Data folder inside RegTech/
output_dir = regtech_dir / "data"
output_dir.mkdir(parents=True, exist_ok=True)

# Authenticate
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build("sheets", "v4", credentials=credentials)
sheet_api = service.spreadsheets()

# Fetch and save each sheet
for sheet_name in sheets_to_export:
    result = sheet_api.values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=sheet_name
    ).execute()

    values = result.get("values", [])

    if not values:
        print(f"No data found in sheet: {sheet_name}")
        continue

    csv_path = output_dir / f"{sheet_name}.csv"
    with open(csv_path, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(values)

    print(f"Saved: {csv_path}")
