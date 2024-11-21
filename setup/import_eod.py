import os
from dotenv import load_dotenv
import time
import json
import datetime as dt

import requests
import boto3
import polars as pl
import psycopg2 as pg


load_dotenv()
api_key = os.getenv("polygon_api_key")
conn = pg.connect(
    database="postgres",
    user="postgres",
    host=os.getenv("aws_db_host"),
    port=os.getenv("aws_db_port"),
    password=os.getenv("aws_db_password"),
)
cur = conn.cursor()


# read sample data
sample_date = "2023-03-28"
y, m, d = map(int, sample_date.split("-"))
sample_data = "stocks_day_candlesticks_example.csv"

# convert window_start from unix to datetime & create year/month/day cols
df = pl.read_csv(sample_data)
df = df.with_columns(
    pl.from_epoch("window_start", time_unit="ms"),
    year=y,
    month=m,
    day=d,
)
print(df)
# TODO: try the processing with fireducks.pandas once available on MacOS


# pull single stock EOD data
start_date = dt.datetime(2023, 3, 28)
end_date = dt.datetime(2024, 11, 20)
d = start_date
diff = 0
ticker = "AAPL"
while d <= end_date:
    if d.weekday() < 5:  # exclude weekends
        date = d.strftime("%Y-%m-%d")
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
                "window_start": d.isoformat(),
                "transactions": None,
            }
            # TODO: insert record to Postgres
            cols = ", ".join(rec.keys())
            vals = ", ".join(["%s"] * len(rec))
            query = f"INSERT INTO stocks_daily ({cols}) VALUES ({vals})"
            cur.execute(query, tuple(rec.values()))
            conn.commit()
            print(f"Inserted {rec}")
    d += dt.timedelta(days=1)
    time.sleep(12.5)  # polygon.io free tier limits 5 API calls/min
# close Postgres connection
conn.close()
