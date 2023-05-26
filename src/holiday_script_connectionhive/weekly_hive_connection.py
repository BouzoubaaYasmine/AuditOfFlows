import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from datetime import datetime, timedelta
import holidays
import findspark

findspark.init()
spark = SparkSession.builder \
    .appName("MissingSundays") \
    .config("hive.metastore.uris", "thrift://192.168.56.103:9083") \
    .enableHiveSupport() \
    .getOrCreate()

df = spark.table("default.weekly")
df = spark.sql("SELECT * FROM default.weekly")

df = df.withColumn("time", col("time").cast("date"))

min_date = df.selectExpr("min(time)").collect()[0][0]
max_date = df.selectExpr("max(time)").collect()[0][0]

# Create a list of all the Sundays in the date range
all_sundays = [d for d in pd.date_range(start='2022-10-30', end='2023-05-07') if d.weekday() == 6]

# Convert the DataFrame column to a pandas Series and access the values
df_dates = df.select("time").toPandas()["time"].tolist()

missing_sundays = [d for d in all_sundays if d.date() not in df_dates]

morocco_holidays = holidays.Morocco()
for sunday in all_sundays:
    if sunday in df["time"].dt.date.tolist():
        if sunday in morocco_holidays:
            print(f" the flow of {sunday.strftime('%Y-%m-%d')} was ingested in holiday ({morocco_holidays[sunday]}).")

for sunday in missing_sundays:
    if sunday in morocco_holidays:
        print(f"{sunday.strftime('%Y-%m-%d')} is a holiday ({morocco_holidays[sunday]}) , and it is missing from the table.")
    else:
        print(f"{sunday.strftime('%Y-%m-%d')} ({sunday.strftime('%A')}) is missing from the table.")