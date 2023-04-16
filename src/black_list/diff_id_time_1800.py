import pandas as pd
import random
from datetime import datetime, timedelta


# Define the function to generate flow IDs and ingestion times
def generate_flow_id_and_ingestion_time(arrival_time, n_ids):
    # Generate n_ids random 5-digit integers as the flow IDs
    flow_ids = random.sample(range(10000, 99999), n_ids)
    # Add a random offset to the arrival time to generate unique ingestion times
    ingestion_times = [arrival_time + timedelta(seconds=random.randint(1, 3600)) for i in range(n_ids)]
    # Convert the ingestion times to strings in the desired format
    ingestion_time_strs = [t.strftime('%Y-%m-%d %H:%M:%S.%f') for t in ingestion_times]
    # Return the flow IDs and ingestion times as tuples
    return list(zip(flow_ids, ingestion_time_strs))


# Assume that you have a list of flows with their arrival times
flows = [(1, datetime(2023, 1, 5, 13, 30, 0)),  # same day arrival and ingestion
         (2, datetime(2023, 1, 4, 20, 0, 0)),  # ingestion on day+1
         (3, datetime(2023, 1, 6, 8, 0, 0))]  # same day arrival and ingestion

# Generate flow IDs and ingestion times for each flow
flow_data = []
for flow in flows:
    for i in range(3):  # Generate 3 IDs for each flow
        flow_data.extend(generate_flow_id_and_ingestion_time(flow[1], 200))

# Create a DataFrame from the flow data
df = pd.DataFrame(flow_data, columns=['Flow ID', 'Ingestion Time'])
print(df)

