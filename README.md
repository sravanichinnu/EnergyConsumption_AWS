# Energy Consumption Forecasting – End-to-End ML Pipeline on AWS

### Project Overview
This project implements an end-to-end energy consumption forecasting system using real-world PJM Interconnection data.
It demonstrates the full lifecycle of a production-grade ML solution — from raw data ingestion to model training, evaluation, visualization, and monitoring — all built on AWS cloud services.

The goal is to accurately forecast hourly electricity demand and analyze prediction errors over time to assess model reliability.

### Architecture Overview
#### Tech stack & flow:
Kaggle Dataset (PJM Hourly Load) -> Amazon S3 (Raw Layer) -> AWS Glue (Pandas ETL → Parquet) -> Amazon Athena (SQL + Views) -> Amazon QuickSight (Visual Analytics) -> Amazon SageMaker (Model Training & Tuning) -> S3 (Predictions + Model Artifacts)

### Data pipelines
- Raw PJM hourly CSV data ingested into Amazon S3
- ETL performed using AWS Glue (Pandas-based job)
- Feature engineering:
  - Lag features (1, 24, 168 hours)
  - Rolling statistics
  - Calendar features (hour, weekday, month)
- Processed data stored in Parquet format for analysis

🤖 Machine Learning Models
✅ XGBoost (Final Model)

Tree-based regression model optimized for time-series features

Hyperparameter tuning via GridSearchCV

Best parameters selected based on RMSE

Final performance:

RMSE ≈ 470

MAE ≈ 354

❌ LSTM (Comparison Model)

Sequence-based neural network

Significantly underperformed due to scaling and data volume constraints

RMSE ≈ 31,000

Highlighted why tree-based models are often better for structured time-series tabular data
