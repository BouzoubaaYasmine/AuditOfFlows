import datetime
import random
import pandas as pd

# start and end date

start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2023, 1, 31)

# Define the different intervals for each ID
# Define a dictionary to map IDs to flow names

id_intervals = {
    29845: [1, 2, 3, 4, 5, 6, 7],  # Monday to Sunday
    83749: [2, 3, 4, 5, 6],  # Tuesday to Saturday
    42016: [1, 3, 5],  # Monday, Wednesday, Friday
    70124: [2, 4, 6],  # Tuesday, Thursday, Saturday
    29847: [1, 2, 3, 4, 5, 6, 7],  # Monday to Sunday
    83709: [2, 3, 4, 5, 6],  # Tuesday to Saturday
    42056: [1, 3, 5],  # Monday, Wednesday, Friday
    79124: [2, 4, 6],  # Tuesday, Thursday, Saturday
}

# Initialize an empty list to store the results
results = []

# Initialize a dictionary to keep track of the number of results added for each ID
num_results = {id_: 0 for id_ in id_intervals}

# Loop through each ID and its corresponding intervals
while id_intervals:
    # Choose a random ID from the remaining IDs
    id_ = random.choice(list(id_intervals.keys()))

    # Check if we have already added all the results for this ID
    if num_results[id_] == len(id_intervals[id_]):
        # If so, mark the ID as used and remove it from the dictionary
        del id_intervals[id_]
        continue

    # Choose a random day from the remaining days for this ID
    day = random.choice(id_intervals[id_])

    # Calculate the date for the current day in the interval
    current_date = start_date + datetime.timedelta(days=day - 1)

    # Check if the current date is within the specified month
    if current_date.month != start_date.month:
        continue

    # Generate a random ingestion time for the current day
    ingestion_time = datetime.datetime(current_date.year, current_date.month, current_date.day,
                                       random.randint(0, 23), random.randint(0, 59), random.randint(0, 59),
                                       random.randint(0, 999999))

    # Add the result to the list
    results.append({'ID': str(id_), 'Ingestion Time': ingestion_time})

    # Update the number of results added for this ID
    num_results[id_] += 1
# Shuffle the results randomly
random.shuffle(results)

# Print the results as a table
print('{:<10}{}'.format('ID', 'Ingestion Time'))
for result in results:
    print('{:<10}{}'.format(result['ID'], result['Ingestion Time']))

# Store the results in a DataFrame
df = pd.DataFrame(results)
print(df)

# Store the results in a CSV file
df.to_csv('ingested_flows.csv', index=False)
    