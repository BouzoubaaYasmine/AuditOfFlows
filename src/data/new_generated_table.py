import random
import unittest
from datetime import datetime, timedelta

start_date = datetime(2023, 1, 1, 0, 0, 0)
end_date = datetime(2023, 2, 1, 0, 0, 0)

morocco_holidays = {
    1: "New Year's Day",
    11: "Day of Independence",
}

# Generate a list of datetimes for each line (excluding Sundays)
datetimes = []
used_days = set()
for day in range(1, 32):
    if (start_date + timedelta(days=day-1)).weekday() == 6:
        continue
    while True:
        new_datetime = start_date + timedelta(days=day-1, seconds=random.randint(1, 60*60*24))
        if new_datetime.month == 1 and new_datetime.day == day and new_datetime not in datetimes:
            datetimes.append(new_datetime)
            used_days.add(day)
            break

counts = [random.randint(1, 99999) for _ in range(len(datetimes))]

table = []
for i in range(len(datetimes)):
    time_str = datetimes[i].strftime('%Y-%m-%d %H:%M:%S.%f')
    count_str = f"{counts[i]:05d}"
    day = datetimes[i].day
    if day in morocco_holidays:
        holiday = morocco_holidays[day]
        table.append((count_str, time_str, holiday))
    else:
        table.append((count_str, time_str, ""))

print("| Count | Time                       | Holiday                               |")
print("|-------|---------------------------|---------------------------------------|")

for row in table:
    count_str, time_str, holiday = row
    print(f"| {count_str} | {time_str:<26} | {holiday:<37} |")


print(f"\nGenerated table with {len(table)} rows.")


class TestTableGenerator(unittest.TestCase):
    def test_table_duplicate_time(self):
        times = [row[1] for row in table]

        duplicates = [time for time in times if times.count(time) > 1]
        self.assertEqual(len(duplicates), 0, f"Found {len(duplicates)} duplicates in the time column of the table.")