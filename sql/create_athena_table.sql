CREATE EXTERNAL TABLE IF NOT EXISTS pjme_xgboost_final_predictions (
    timestamp TIMESTAMP,
    energy_mw DOUBLE,
    predicted_energy_mw DOUBLE
)
STORED AS PARQUET
LOCATION 's3://energy-consumption-forecasting-project/models/predictions/';