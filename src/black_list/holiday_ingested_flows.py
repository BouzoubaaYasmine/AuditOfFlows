import datetime
import random

# Define the start and end dates for the time intervals
start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2023, 1, 31)

# Define the different intervals for each ID
id_intervals = {
    29845: [1, 2, 3, 4, 5, 6, 7],  # Monday to Sunday
    83749: [2, 3, 4, 5, 6],       # Tuesday to Saturday
    42016: [1, 3, 5],             # Monday, Wednesday, Friday
    70124: [2, 4, 6],             # Tuesday, Thursday, Saturday
    29847: [10, 11, 12, 13, 14, 15, 17],  # Monday to Sunday
    83709: [2, 3, 4, 5, 6],       # Tuesday to Saturday
    42056: [1, 3, 5],             # Monday, Wednesday, Friday
    79124: [2, 4, 6],             # Tuesday, Thursday, Saturday
}

# Define the holidays in Morocco for January 2023
moroccan_holidays = [datetime.date(2023, 1, 1), datetime.date(2023, 1, 11), datetime.date(2023, 1, 30)]

# Initialize an empty list to store the results
results = []

# Loop through each ID and its corresponding intervals
for id_, intervals in id_intervals.items():
    for day in intervals:
        # Calculate the date for the current day in the interval
        current_date = start_date + datetime.timedelta(days=day-1)

        # Check if the current date is within the specified month
        if current_date.month != start_date.month:
            continue

        # Generate a random ingestion time for the current day
        ingestion_time = datetime.datetime(current_date.year, current_date.month, current_date.day,
                                            random.randint(0, 23), random.randint(0, 59), random.randint(0, 59),
                                            random.randint(0, 999999))

        # Check if the ingestion time is on a holiday
        if current_date in moroccan_holidays:
            # Add the result to the list
            results.append({'ID': str(id_), 'Ingestion Time': ingestion_time})

# Shuffle the results randomly
random.shuffle(results)

# Print the results as a table
print('{:<10}{}'.format('ID', 'Ingestion Time'))
for result in results:
    print('{:<10}{}'.format(result['ID'], result['Ingestion Time']))
