import pandas as pd
import os

data_folder = "data/raw"

files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

print(f"Total CSV Files Found: {len(files)}")

for file in files:

    print("\n" + "="*60)
    print("Dataset:", file)

    file_path = os.path.join(data_folder, file)

    df = pd.read_csv(file_path)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())