import unittest
from datetime import datetime
from src.data.Newfile_count_time import table

class TestTableIngestionTime(unittest.TestCase):
    def test_ingestion_time(self):
        # Get the ingestion time for each row in the table
        ingestion_times = []
        for row in table:
            ingestion_times.append(datetime.now())

        # Check if all ingestion times are different
        self.assertEqual(len(set(ingestion_times)), len(table), "The ingestion time should be different for each row "
                                                                "in the table.")
