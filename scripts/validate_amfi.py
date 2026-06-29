import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/fund_master.csv")
nav_history = pd.read_csv("data/raw/nav_history.csv")

# Get unique AMFI codes
fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

# Find missing codes
missing_codes = fund_codes - nav_codes

print("========== AMFI Code Validation ==========")

if len(missing_codes) == 0:
    print("✅ All AMFI codes in fund_master.csv exist in nav_history.csv.")
else:
    print("❌ Missing AMFI Codes:")
    print(missing_codes)

print("\nTotal Fund Master Codes :", len(fund_codes))
print("Total NAV History Codes :", len(nav_codes))