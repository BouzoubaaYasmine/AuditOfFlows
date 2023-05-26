from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from datetime import datetime, timedelta
import holidays

spark = SparkSession.builder.appName("MissingDays").getOrCreate()
df = spark.read.csv("daily.csv", header=True, inferSchema=True)

df = df.withColumn("time", col("time").cast("date"))

min_date = df.selectExpr("min(time)").collect()[0][0]
max_date = df.selectExpr("max(time)").collect()[0][0]

all_dates = [min_date + timedelta(days=x) for x in range((max_date - min_date).days + 1)]

all_weekdays = [[d for d in all_dates if d.weekday() == i] for i in range(1, 6)]

all_days = sorted(list(set([d for d in all_dates])))

df_days = sorted(list(set([d for d in df.select("time").distinct().collect()[0]])))

# the missing ingestions days
missing_days = set(all_days) - set(df_days)

morocco_holidays = holidays.Morocco()

# Check if the missing ingestion was a holiday or not
for day in missing_days:
    if day.weekday() in range(1, 6):
        if day not in [row[0] for row in df.select("time").collect()]:
            if day in morocco_holidays:
                print(f"Missing {day.strftime('%A')} {day} was a holiday: {morocco_holidays[day]}")
            else:
                print(f"Missing {day.strftime('%A')} {day} the flow was not ingested")
