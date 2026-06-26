import pandas as pd

# List of CSV files
files = [
    "Axis_Bluechip.csv",
    "ICICI_Bluechip.csv",
    "Kotak_Bluechip.csv",
    "Nippon_LargeCap.csv",
    "SBI_Bluechip.csv",
    "hdfc_top100_live_nav.csv"
]

# Read each file and display basic information
for file in files:
    print("=" * 50)
    print(f"File: {file}")

    df = pd.read_csv(f"data/raw/{file}")
    df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")
    print("Shape:", df.shape)
    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nRows with Missing Values:")
    print(df[df.isnull().any(axis=1)])

    print("\nDuplicate Rows:", df.duplicated().sum())
    df.to_csv(f"data/processed/{file}", index=False)
    print(f"{file} saved successfully.")
    print("=" * 50)