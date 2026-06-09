import pandas as pd

df = pd.read_parquet("data/sample.parquet")
print("Columns:", list(df.columns))
print()
print(df.to_string(index=False))