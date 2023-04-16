import pandas as pd
from datetime import datetime, timedelta

# Load the data into a pandas DataFrame
flows = pd.read_csv("bank_flow.txt", sep="\t")

# Convert the "Date" column to a pandas datetime object
flows["Date"] = pd.to_datetime(flows["Date"], format="%Y-%m-%d")

# Filter the data to only include the month of January 2023 and Morocco holiday
january_flows = flows.loc[(flows["Date"].dt.month == 1) & (flows["Country"] == "Morocco") & (flows["Holiday"] == True)]

# Group the data by day and calculate the total flows ingested on each day
daily_flows = january_flows.groupby(january_flows["Date"].dt.day)["Flows"].sum()

# Create a table that shows the total flows ingested on each day in January 2023
table = []
for day in range(1, 32):
    if day in daily_flows.index:
        count_str = f"{int(daily_flows.loc[day]):05d}"
    else:
        count_str = "00000"
    time_str = datetime(2023, 1, day, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S.%f')
    table.append((count_str, time_str))

# Print the table header
print("| Count | Time                |")
print("|-------|---------------------|")

# Print each row of the table
for row in table:
    print(f"| {row[0]} | {row[1]:<19} |")
