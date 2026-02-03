# Energy Consumption Forecasting on AWS

End-to-end time-series forecasting project that predicts hourly electricity demand using historical PJME energy consumption dataset.
The project demonstrates a production-oriented ML pipeline built on AWS, covering data ingestion, feature engineering, model training, evaluation, and business-facing visualization.

---

## Problem statement
Accurate energy demand forecasting is critical for grid reliability, cost optimization, and resource planning. This project focuses on forecasting hourly energy consumption (MW) for the PJME region using historical load data and machine learning models.

---

## Dataset
- **Source:** PJM Interconnection (via kaggle)
- **Granularity:** Hourly
- **Target Variable:** Energy Consumption in megawatts (MW)
- **Region:** PJME

Raw and processed datasets are stored in **Amazon S3** and are intentionally not committed to GitHub.

---

## Architecture Overview
**Pipeline Flow:**
1. **S3 (Raw Data)**
   PJME hourly CSV data stored in S3.
2. **AWS Glue (Pandas ETL)**
   - cleans and standardizes data
   - Engineers lag, rollling, and calendar features
   - Writes Parquet output back to S3
3. **Amazon Athena**
   - Queries processed features and model predictions
   - Creates analytical views for error analysis
4. **Amazon SageMaker Studio**
   - Trains and tunes forecasting models
   - Saves model artifacts and predictions to S3
5. **Amazon QuickSight**
   - Visualizes actual vs predicted demand
   - Monitors error trends over time

---

## Feature Engineering

The following features were engineered to capture temporal patterns:
