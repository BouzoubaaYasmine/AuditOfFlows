from datetime import datetime, timedelta

from src.data.Newfile_count_time import used_days

# Define the start and end dates for the data
start_date = datetime(2023, 1, 1, 0, 0, 0)
end_date = datetime(2023, 2, 1, 0, 0, 0)

# all Sundays in January 2023
sundays = []
for i in range(31):
    day = start_date + timedelta(days=i)
    if day.weekday() == 6:
        sundays.append(day.day)

#  Sundays that were not used
unused_sundays = set(sundays) - used_days

# Print the unused Sundays
if unused_sundays:
    print("The following Days are sunday:")
    for day in unused_sundays:
        print(day)
else:
    print("All Sundays in January 2023 were included in the table.")


