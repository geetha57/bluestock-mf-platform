import pandas as pd
import os

# Create processed folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

# ==============================
# Clean nav_history.csv
# ==============================

print("Loading nav_history.csv...")

# Load dataset
nav = pd.read_csv("data/raw/nav_history.csv")

# Convert date column to datetime (DD-MM-YYYY)
nav["date"] = pd.to_datetime(
    nav["date"],
    dayfirst=True,
    errors="coerce"
)

# Remove rows with invalid dates
nav = nav.dropna(subset=["date"])

# Sort by AMFI code and date
nav = nav.sort_values(by=["amfi_code", "date"])

# Forward-fill missing NAV values within each scheme
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

# Remove duplicate rows
nav = nav.drop_duplicates()

# Keep only positive NAV values
nav = nav[nav["nav"] > 0]

# Save cleaned dataset
nav.to_csv("data/processed/nav_history.csv", index=False)

print("✅ nav_history.csv cleaned successfully")
print("Rows:", len(nav))
print("Saved to: data/processed/nav_history.csv")

# ==============================
# Clean investor_transactions.csv
# ==============================

print("\nLoading investor_transactions.csv...")

transactions = pd.read_csv("data/raw/investor_transactions.csv")

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"],
    dayfirst=True,
    errors="coerce"
)

transactions = transactions.dropna(subset=["transaction_date"])

transactions["transaction_type"] = transactions["transaction_type"].str.strip().str.title()

transactions = transactions[
    transactions["transaction_type"].isin(["Sip", "Lumpsum", "Redemption"])
]

transactions = transactions[transactions["amount_inr"] > 0]

transactions["kyc_status"] = transactions["kyc_status"].str.strip().str.title()

transactions = transactions.drop_duplicates()

transactions.to_csv(
    "data/processed/investor_transactions.csv",
    index=False
)

print("✅ investor_transactions.csv cleaned successfully")
print("Rows:", len(transactions))

# ==============================
# Clean scheme_performance.csv
# ==============================

print("\nLoading scheme_performance.csv...")

performance = pd.read_csv("data/raw/scheme_performance.csv")

# Convert return columns to numeric
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

for col in return_columns:
    performance[col] = pd.to_numeric(
        performance[col],
        errors="coerce"
    )

# Flag expense ratio anomalies
performance["expense_ratio_flag"] = (
    (performance["expense_ratio_pct"] < 0.1) |
    (performance["expense_ratio_pct"] > 2.5)
)

# Remove duplicate rows
performance = performance.drop_duplicates()

# Save cleaned file
performance.to_csv(
    "data/processed/scheme_performance.csv",
    index=False
)

print("✅ scheme_performance.csv cleaned successfully")
print("Rows:", len(performance))
print("Expense Ratio Anomalies:", performance["expense_ratio_flag"].sum())

# ==============================
# Clean fund_master.csv
# ==============================

print("\nLoading fund_master.csv...")

fund = pd.read_csv("data/raw/fund_master.csv")

# Convert launch_date to datetime
fund["launch_date"] = pd.to_datetime(
    fund["launch_date"],
    dayfirst=True,
    errors="coerce"
)

# Remove duplicate rows
fund = fund.drop_duplicates()

# Remove rows with missing AMFI codes
fund = fund.dropna(subset=["amfi_code"])

# Save cleaned file
fund.to_csv(
    "data/processed/fund_master.csv",
    index=False
)

print("✅ fund_master.csv cleaned successfully")
print("Rows:", len(fund))

# ==============================
# Clean portfolio_holdings.csv
# ==============================

print("\nLoading portfolio_holdings.csv...")

holdings = pd.read_csv("data/raw/portfolio_holdings.csv")

# Remove duplicate rows
holdings = holdings.drop_duplicates()

# Remove rows with missing AMFI codes
holdings = holdings.dropna(subset=["amfi_code"])

# Keep only positive sector weights
holdings = holdings[holdings["weight_pct"] >= 0]

# Save cleaned file
holdings.to_csv(
    "data/processed/portfolio_holdings.csv",
    index=False
)

print("✅ portfolio_holdings.csv cleaned successfully")
print("Rows:", len(holdings))

# ==============================
# Clean aum_by_fund_house.csv
# ==============================

print("\nLoading aum_by_fund_house.csv...")

aum = pd.read_csv("data/raw/aum_by_fund_house.csv")

# Remove duplicate rows
aum = aum.drop_duplicates()

# Remove rows with missing fund house
aum = aum.dropna(subset=["fund_house"])

# Keep only positive AUM values
aum = aum[aum["aum_crore"] > 0]

# Save cleaned file
aum.to_csv(
    "data/processed/aum_by_fund_house.csv",
    index=False
)

print("✅ aum_by_fund_house.csv cleaned successfully")
print("Rows:", len(aum))