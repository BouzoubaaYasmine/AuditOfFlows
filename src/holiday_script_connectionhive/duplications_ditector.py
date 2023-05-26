import pandas as pd

df = pd.read_csv("../Holidaytestcsv/monthly.csv")
duplicates = df.duplicated(subset=["_c0"], keep=False)

duplicate_rows = df[duplicates]

print("Duplicate rows based on _c0:")
print(duplicate_rows)

