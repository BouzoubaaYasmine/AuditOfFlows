import random
from datetime import datetime, timedelta

# Define the start and end dates for the data
start_date = datetime(2023, 1, 1, 0, 0, 0)
end_date = datetime(2023, 2, 1, 0, 0, 0)

# list of holidays in Morocco for January 2023
morocco_holidays = [1, 11, 16]

#list of datetimes for each line (excluding Sundays and holidays)
datetimes = []
used_days = set()
unused_holidays = set(morocco_holidays)
for day in range(1, 32):
    if (start_date + timedelta(days=day - 1)).weekday() == 6:
        continue  # skip Sundays
    if day in morocco_holidays:
        unused_holidays.remove(day)
        continue  # skip holidays
    while True:
        new_datetime = start_date + timedelta(days=day - 1, seconds=random.randint(1, 60 * 60 * 24))
        if new_datetime.month == 1 and new_datetime.day == day and new_datetime not in datetimes:
            datetimes.append(new_datetime)
            used_days.add(day)
            break

#  list of counts for each line
counts = [random.randint(1, 99999) for _ in range(len(datetimes))]

# Combine the lists into a table
table = []
for i in range(len(datetimes)):
    time_str = datetimes[i].strftime('%Y-%m-%d %H:%M:%S.%f')
    count_str = f"{counts[i]:05d}"
    table.append((count_str, time_str))

print("| Count | Time                |")
print("|-------|---------------------|")

# Print each row of the table
for row in table:
    print(f"| {row[0]} | {row[1]:<19} |")

# Print the unused holidays
if unused_holidays:
    print("The following holidays were not included in the table:")
    for day in unused_holidays:
        print(day)
else:
    print("All holidays in January 2023 were included in the table.")

