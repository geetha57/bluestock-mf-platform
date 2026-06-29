import pandas as pd

files = [
    "investor_transactions.csv",
    "scheme_performance.csv"
]

for file in files:
    print("=" * 60)
    print(file)

    df = pd.read_csv(f"data/raw/{file}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nData Types:")
    print(df.dtypes)

    print("\n")