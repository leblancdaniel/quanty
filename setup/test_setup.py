import os

from dotenv import load_dotenv
import psycopg2 as pg
import polars as pl

""" Connect to Postgres DB and get some metrics from the stocks_daily table
"""
# establish connection to Postgres DB
load_dotenv()
pw = os.getenv("aws_db_password")
host = os.getenv("aws_db_host")
port = os.getenv("aws_db_port")
db_uri = f"postgresql://postgres:{pw}@{host}:{port}"

# Fetch all data from stocks_daily table
query = "SELECT * FROM stocks_daily"
df = pl.read_database_uri(query, db_uri)
print(df)

# get Volume-Weighted Average Price (VWAP)
vwap_query = """
    WITH daily_vwap AS (
        SELECT 
            window_start, 
            ticker, 
            SUM(volume * close) / SUM(volume) AS vwap
        FROM stocks_daily
        GROUP BY window_start, ticker
    ),
    rolling_vwap AS (
        SELECT 
            window_start,
            ticker, 
            AVG(vwap) OVER (
                PARTITION BY ticker 
                ORDER BY window_start
                ROWS BETWEEN 29 PRECEDING AND CURRENT ROW
            ) AS rolling_30_day_vwap
        FROM daily_vwap
    )
    SELECT * FROM rolling_vwap
    ORDER BY ticker, window_start
    """
df = pl.read_database_uri(vwap_query, db_uri)
print(df)
