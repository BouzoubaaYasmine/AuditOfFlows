
# Files description:
1.Newfile_count_time:
    This code generates a table with three columns: count, time, and holiday. The count column contains a random integer count for each row, the time column contains a random datetime for each row within a specific range, and the holiday column contains the name of a holiday (if the datetime corresponds to a holiday) or is blank (if the datetime is not a holiday).

2.Eliminate_holiday:
    This code eliminates the rows in the table that correspond to holidays.

3.All_sundays_are_included:
This code checks if any Sundays in January 2023 were not used to generate data in the table. It gets all the Sundays in January 2023, then subtracts the Sundays that were used to generate data in the table (which is obtained from the used_days variable imported from another file). If there are any unused Sundays, it prints a message listing them. If all Sundays were used, it prints a message indicating so.

4.holiday_or_not:
    This code checks if the date is a holiday or not. If it is a holiday, it prints the name of the holiday. If it is not a holiday, it prints a message indicating so.

5.new_generated_table:
    This code generates a new table with the same columns as the original table, but with the rows corresponding to holidays eliminated, and generate each count with a unique time.


# UnitTest description:
1.test_all_sundays_eliminated: This test checks if all Sundays are eliminated from a list of datetime objects generated within a specific range.

2.test_no_duplicate_counts: This test checks if there are no duplicate counts in a given list of counts.

3.test_table_duplicate_time: This test checks if there are no duplicate times in a table.

4.test_ingestion_time_unique: This test checks if all the ingestion times in a table are unique.

5.test_no_sunday: This test checks if there are no Sundays in a list of datetime objects.

6.test_sundays_in_table: This test checks if any Sunday is included in the table.

7.test_no_duplicates: This test checks if there are no duplicate count and time values in a table.