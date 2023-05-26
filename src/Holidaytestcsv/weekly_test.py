import pandas as pd
from datetime import datetime, timedelta
import holidays

df = pd.read_csv("weekly.csv")

df["time"] = pd.to_datetime(df["time"])

min_date = df["time"].min().date()
max_date = df["time"].max().date()

all_sundays = [d for d in pd.date_range(start='2022-10-30', end='2023-05-07') if d.weekday() == 6]

missing_sundays = [d for d in all_sundays if d.date() not in df["time"].dt.date.tolist()]

morocco_holidays = holidays.Morocco()

for sunday in all_sundays:
    if sunday in df["time"].dt.date.tolist():
        if sunday in morocco_holidays:
            print(f" the flow of {sunday.strftime('%Y-%m-%d')} was ingested in holiday ({morocco_holidays[sunday]}).")

for sunday in missing_sundays:
    if sunday in morocco_holidays:
        print(f"{sunday.strftime('%Y-%m-%d')} is a holiday ({morocco_holidays[sunday]}) and is missing from the table.")
    else:
        print(f"{sunday.strftime('%Y-%m-%d')} ({sunday.strftime('%A')}) is missing from the table.")