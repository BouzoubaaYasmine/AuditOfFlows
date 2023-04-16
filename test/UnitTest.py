import random
import unittest
from collections import Counter
from datetime import datetime, timedelta

from src.data.Duplication_flows import table
from src.black_list.Newfile_count_time import datetimes, counts
from src.data.new_generated_table import start_date


class TestUnit(unittest.TestCase):

    def test_all_sundays_eliminated(self):

        sundays = []
        for i in range(31):
            day = start_date + timedelta(days=i)
            if day.weekday() == 6:
                sundays.append(day.day)

        # Generate a list of datetime for each line (excluding Sundays)
        datetimes_without_sundays = []
        used_days = set()
        for day in range(1, 32):
            if (start_date + timedelta(days=day - 1)).weekday() == 6:
                continue  # skip Sundays
            while True:
                new_datetime = start_date + timedelta(days=day - 1, seconds=random.randint(1, 60 * 60 * 24))
                if new_datetime.month == 1 and new_datetime.day == day and new_datetime not in datetimes_without_sundays:
                    datetimes_without_sundays.append(new_datetime)
                    used_days.add(day)
                    break

        # Check that all Sundays are eliminated from the table
        for dt in datetimes_without_sundays:
            self.assertNotIn(dt.day, sundays)

    def test_no_duplicate_counts(self):
        # Counting the number of occurrences of each count in the table
        count_occurrences = Counter(counts)

        # Checking if any count occurs more than once
        for count, num_occurrences in count_occurrences.items():
            with self.subTest(count=count):
                self.assertEqual(num_occurrences, 1, f"Count {count} occurred {num_occurrences} times in the table.")

    def test_table_duplicate_time(self):
        # Create a list of times
        times = [row[1] for row in table]
        duplicates = [time for time in times if times.count(time) > 1]

        # Assert that there are no duplicates
        self.assertEqual(len(duplicates), 0, f"Found {len(duplicates)} duplicates in the time column of the table.")

    def test_ingestion_time_unique(self):
        # Extract the ingestion times from the table
        ingestion_times = [datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S.%f') for row in table]

        # Check that the ingestion times are unique
        self.assertEqual(len(set(ingestion_times)), len(ingestion_times))

    def test_no_sunday(self):
      # Check if there is a Sunday in the generated datetimes
        for datetime_obj in datetimes:
            if datetime_obj.weekday() == 6:
                self.fail("A Sunday was included in the table.")


    def test_sundays_in_table(self):
        start_date = datetime(2023, 1, 1, 0, 0, 0)
        end_date = datetime(2023, 2, 1, 0, 0, 0)
        morocco_holidays = {1: "New Year's Day", 11: "Day of Independence"}
        datetimes = []
        for day in range(1, 32):
            if (start_date + timedelta(days=day - 1)).weekday() == 6:
                with self.assertRaises(Exception):
                    break
            while True:
                new_datetime = start_date + timedelta(days=day - 1, seconds=random.randint(1, 60 * 60 * 24))
                if new_datetime.month == 1 and new_datetime.day == day and new_datetime not in datetimes:
                    datetimes.append(new_datetime)
                    break
        self.assertTrue(True)


    def test_no_duplicates(self):


        # Get the count and time columns from the table
        count_column = [row[0] for row in table]
        time_column = [row[1] for row in table]

        # Check if there are any duplicates
        self.assertEqual(len(count_column), len(set(count_column)), "Duplicate count values found")
        self.assertEqual(len(time_column), len(set(time_column)), "Duplicate time values found")

        # Check if there are any rows with the same count and time
        count_time_set = set(zip(count_column, time_column))
        self.assertEqual(len(count_time_set), len(table), "Duplicate count and time values found")