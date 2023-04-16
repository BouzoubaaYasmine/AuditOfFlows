import random
import datetime

# Set the month and year
month = 1
year = 2023

# Create a list of all the days in the month
days_in_month = [datetime.date(year, month, day) for day in range(1, 32)]

# Generate unique numeric IDs for each flow
flow_ids = list(range(1, 10))
random.shuffle(flow_ids)

# Generate random counts and ingestion times for each flow
flow_counts = {}
flow_times = {}
for flow_id in flow_ids:
    count = random.randint(10000, 99999)
    flow_counts[flow_id] = count
    times = []
    for _ in range(count):
        day = random.choice(days_in_month)
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        microsecond = random.randint(0, 999999)
        ingestion_time = datetime.datetime(year, month, day.day, hour, minute, second, microsecond)
        times.append(ingestion_time)
    flow_times[flow_id] = times

# Generate the table
table = []
for flow_id in flow_ids:
    for ingestion_time in flow_times[flow_id]:
        table.append((flow_id, ingestion_time))

# Print the table
print("Flow ID\t\tIngestion Time")
for flow_id, ingestion_time in table:
    print(f"{flow_id:05d}\t{ingestion_time}")

# Print the flow counts
print("\nFlow Counts:")
for flow_id, count in flow_counts.items():
    print(f"{flow_id:05d}: {count}")