import random
import pandas as pd
from datetime import datetime, timedelta

# Define the number of flows to generate
num_flows = 10

# Generate the flow IDs
flow_ids = [f"flow_{i + 1}" for i in range(num_flows)]

# Generate the bank flows
flow_data = []
for flow_id in flow_ids:
    # Generate a random date and time in January 2023
    date_str = f"2023-01-{random.randint(1, 31):02d}"
    time_str = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}.{random.randint(0, 999):03d}"
    timestamp_str = f"{date_str} {time_str}"
    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S.%f')

    # Generate a random count of elements in the flow
    count = random.randint(1, 100)

    # Append the flow data to the list
    flow_data.append((flow_id, timestamp, count))

# Add a column for the count of elements in each flow
count_col = [t[2] for t in flow_data]

# Add a column for the total number of elements processed up to that point
total_count = 0
cumulative_count_col = []
for count in count_col:
    total_count += count
    cumulative_count_col.append(total_count)

# Add the count and cumulative count columns to the flow data
flow_data = [(*t, count_col[i], cumulative_count_col[i]) for i, t in enumerate(flow_data)]

# Write the flow data to a text file
df = pd.DataFrame(flow_data, columns=['Flow ID', 'Ingestion Time', 'Flow', 'Count', 'Cumulative Count'])
df.to_csv("bank_flow.txt", sep='\t', index=False)
print(df)

