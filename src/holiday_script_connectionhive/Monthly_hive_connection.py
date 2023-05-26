import pandas as pd
import holidays
from datetime import date

df = pd.read_csv("../Holidaytestcsv/monthly.csv")
df['time'] = pd.to_datetime(df['time'])

monthly_counts = df.resample('M', on='time').count()

# Find missing months
missing_months = monthly_counts[monthly_counts['_c0'] == 0].index

if len(missing_months) > 0:
    print("-Missing months:")
    for month in missing_months:
        print(month.strftime('%Y-%m'))

        morocco_holidays = holidays.Morocco()

        # Check if any holiday falls within the missing month and print the names of the holidays
        holiday_dates = []
        for date in morocco_holidays[date(year=month.year, month=month.month, day=1):date(year=month.year, month=month.month, day=31)]:
            holiday_dates.append(date.strftime('%Y-%m-%d') + ' (' + morocco_holidays.get(date) + ')')
        if len(holiday_dates) > 0:
            print("-Holidays in {}: {}".format(month.strftime('%Y-%m'), ", ".join(holiday_dates)))
        else:
            print("-No holidays in {}".format(month.strftime('%Y-%m')))
