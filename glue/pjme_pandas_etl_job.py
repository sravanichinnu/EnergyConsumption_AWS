"""
Glue Pandas ETL Job
------------------
Reads raw PJME hourly energy data from S3,
performs feature engineering for time-series forecasting,
and writes processed Parquet output back to S3.
"""

import pandas as pd

RAW_PATH = "s3://energy-consumption-forecasting-project/raw/kaggle/PJME_hourly.csv"
OUTPUT_PATH = "s3://energy-consumption-forecasting-project/processed/pandas/pjme_energy_features.parquet"

# read raw data
df = pd.read_csv(RAW_PATH)

# standardize columns
df.columns = ["timestamp", "energy_mw"]

# parse timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# add region
df["region"] = "PJME"

# sort for time-series correctness
df = df.sort_values("timestamp")

# feature engineering
df["lag_1"] = df["energy_mw"].shift(1)
df["lag_24"] = df["energy_mw"].shift(24)
df["lag_168"] = df["energy_mw"].shift(168)

df["rolling_mean_24"] = df["energy_mw"].rolling(24).mean()
df["rolling_std_24"] = df["energy_mw"].rolling(24).std()

df["hour"] = df["timestamp"].dt.hour
df["day_of_week"] = df["timestamp"].dt.dayofweek
df["month"] = df["timestamp"].dt.month

# drop rows with NaNs
df = df.dropna()

# write processed data
df.to_parquet(OUTPUT_PATH, engine = "pyarrow", index = False)

print("PJME Pandas ETL completed successfully")