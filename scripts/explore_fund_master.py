import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/fund_master.csv")

print("========== Fund Houses ==========")
print(df["fund_house"].unique())

print("\n========== Categories ==========")
print(df["category"].unique())

print("\n========== Sub Categories ==========")
print(df["sub_category"].unique())

print("\n========== Risk Categories ==========")
print(df["risk_category"].unique())

print("\n========== Summary ==========")
print("Number of Fund Houses:", df["fund_house"].nunique())
print("Number of Categories:", df["category"].nunique())
print("Number of Sub Categories:", df["sub_category"].nunique())
print("Number of Risk Categories:", df["risk_category"].nunique())