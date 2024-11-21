-- Add new schema named "public"
CREATE SCHEMA IF NOT EXISTS "public";
-- Set comment to schema: "public"
COMMENT ON SCHEMA "public" IS 'standard public schema';

-- Add new table named "stocks_daily"
CREATE TABLE IF NOT EXISTS "stocks_daily" (
    id BIGINT NOT NULL GENERATED ALWAYS AS IDENTITY,
    ticker TEXT NOT NULL,
    volume BIGINT,
    open FLOAT,
    close FLOAT,
    high FLOAT,
    low FLOAT,
    window_start timestamptz NOT NULL,
    transactions INT
);