import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# List of cleaned CSV files
files = [
    "Axis_Bluechip.csv",
    "ICICI_Bluechip.csv",
    "Kotak_Bluechip.csv",
    "Nippon_LargeCap.csv",
    "SBI_Bluechip.csv",
    "hdfc_top100_live_nav.csv"
]

# Load each CSV into the database
for file in files:
    df = pd.read_csv(f"data/processed/{file}")

    table_name = file.replace(".csv", "").lower()

    df.to_sql(table_name, engine, if_exists="replace", index=False)

    print(f"{table_name} table created successfully!")

print("\nDatabase created successfully!")