import json
import datetime as dt

# import boto3
import requests
import boto3
import polars as pl


# read sample data
sample_date = "2023-03-28"
y, m, d = map(int, sample_date.split("-"))
sample_data = "stocks_day_candlesticks_example.csv"
df = pl.read_csv(sample_data)


# convert window_start from unix to datetime & create year/month/day cols
df = df.with_columns(
    pl.from_epoch("window_start", time_unit="ms"),
    year=y,
    month=m,
    day=d,
)
print(df)
# TODO: write data to database
