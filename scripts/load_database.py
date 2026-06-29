import sqlite3
import pandas as pd

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect("bluestock_mf.db")

print("Connected to SQLite database.")

# Load cleaned datasets
fund = pd.read_csv("data/processed/fund_master.csv")
nav = pd.read_csv("data/processed/nav_history.csv")
transactions = pd.read_csv("data/processed/investor_transactions.csv")
performance = pd.read_csv("data/processed/scheme_performance.csv")
aum = pd.read_csv("data/processed/aum_by_fund_house.csv")

# Load into SQLite tables
fund.to_sql("dim_fund", conn, if_exists="replace", index=False)

nav.to_sql("fact_nav", conn, if_exists="replace", index=False)

transactions.to_sql("fact_transactions", conn, if_exists="replace", index=False)

performance.to_sql("fact_performance", conn, if_exists="replace", index=False)

aum.to_sql("fact_aum", conn, if_exists="replace", index=False)

print("All datasets loaded successfully!")

# Verify row counts
tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum"
]

print("\nRow Counts:")

for table in tables:
    count = pd.read_sql_query(
        f"SELECT COUNT(*) AS total_rows FROM {table}",
        conn
    )
    print(f"{table}: {count['total_rows'][0]} rows")

conn.close()

print("\nDatabase saved as bluestock_mf.db")