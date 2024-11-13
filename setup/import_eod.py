import json
import datetime as dt

# import boto3
import requests
import boto3
import polars as pl


# read sample data
sample_date = "2023-10-31"
sample_data = "stocks_day_candlesticks_example.csv"
df = pl.read_csv(sample_data)
# convert window_start from unix to datetime & create year/month/day cols
df = df.with_columns(pl.from_epoch("window_start", time_unit="ms")).with_columns(
    year=pl.col("window_start").dt.year(),
    month=pl.col("window_start").dt.month(),
    day=pl.col("window_start").dt.day(),
)
print(df)
