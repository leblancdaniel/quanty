import sys, os
import time
import json
import datetime as dt

import requests
import boto3
import polars as pl

api_key = os.environ("polygon_api_key")

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

# pull single stock EOD data
start_date = dt.datetime(2023, 3, 28)
end_date = dt.datetime(2024, 11, 18)
d = start_date
diff = 0
ticker = "AAPL"
while d <= end_date:
    if d.weekday() < 5:  # exclude weekends
        date = dt.datetime.strftime("%Y-%m-%d")
        url = f"https://api.polygon.io/v1/open-close/{ticker}/{date}?adjusted=true&apiKey={api_key}"
        diff += 1
        resp = requests.get(url)
        resp_content = json.loads(resp.content)
        if resp_content["status"] == "OK":
            rec = {
                "ticker": ticker,
                "volume": resp_content["volume"],
                "open": resp_content["open"],
                "close": resp_content["close"],
                "high": resp_content["high"],
                "low": resp_content["low"],
                "window_start": d.timestamp(),
                "transactions": None,
            }

    d += dt.timedelta(days=1)
    time.sleep(12.5)  # polygon.io free tier limits 5 API calls/min
