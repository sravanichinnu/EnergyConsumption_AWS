# Energy Consumption Forecasting on AWS

End-to-end time-series forecasting project that predicts hourly electricity demand using historical PJME energy consumption dataset.
The project demonstrates a production-oriented ML pipeline built on AWS, covering data ingestion, feature engineering, model training, evaluation, and business-facing visualization.

## Problem statement
Accurate energy demand forecasting is critical for grid reliability, cost optimization, and resource planning. This project focuses on forecasting hourly energy consumption (MW) for the PJME region using historical load data and machine learning models.

## Dataset
- **Source:** PJM Interconnection (via kaggle)
- **Granularity:** Hourly
- **Target Variable:** Energy Consumption in megawatts (MW)
- **Region:** PJME

Raw and processed datasets are stored in **Amazon S3** and are intentionally not committed to GitHub.

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

## Feature Engineering

The following features were engineered to capture temporal patterns:
- **Lag features:** "lag_1", "lag_24", "lag_168"
- **Rolling statistics:** 24-hour rolling mean and standard deviation
- **Calendar features:** hour of day, day of week, month
Feature importance analysis showed that **short-term and seasonal lags dominated**, confirming strong temporal autocorrelation in energy demand.

## Modeling Approach

### Baseline Model
- **Algorithm:** XGBoost Regressor
- **Evaluation Metrics:** MAE, RMSE
- **Train/Test Split:** Time-based (no shuffling)

### Hyperparameter tuning
- **Method:** GridSearchCV
- **Optimized Parameters:**
  - "max_depth"
  - "learning_rate"
  - "subsample"
  - colsample_bytree"
  - "n_estimators"

**Result:**
Hyperparameter tuning reduced RMSE from **470.66 -> 429.36**, an improvement of approximately **8.8%**.

### Model Comparison
- **XGBoost:** RMSE ≈ 470 (baseline), 429 (tuned)
- **LSTM:** Significantly higher RMSE due to limited sequence modeling and data scaling sensitivity.

**Final Model Selected:** Tuned XGBoost Regressor

## Evaluation & Error Analysis
Model evaluation included:
- Actual vs predicted energy demand plots
- Absolute error trends over time
- Error distribution analysis

Error trends remained stable with no visible drift, indicating strong generalization on unseen data.

## Notebooks Walkthrough

| Notebook | Description |
|-------|------------|
| `01_data_ingestion_glue.ipynb` | Explains Glue-based ingestion and validates processed data |
| `02_feature_engineering.ipynb` | Details feature engineering strategy |
| `03_xgboost_training_tuning.ipynb` | Model training and hyperparameter tuning |
| `04_model_evaluation_visualization.ipynb` | Metrics and visual diagnostics |

## Key Takeaways

- Demonstrates **end-to-end ML system design**, not just modeling
- Uses AWS-native services for scalability and analytics integration
- Shows practical decision-making (model selection, feature reduction, tuning)
- Designed for both **technical and business stakeholders**

## Future Enhancements

- Add automated Glue job scheduling
- Implement model versioning and registry
- Explore probabilistic forecasting
- Deploy model for real-time inference

## Author

**Sravani Namburu**  
Data Engineer / Data Analyst  
GitHub: https://github.com/sravanichinnu  
LinkedIn: https://www.linkedin.com/in/sravani-namburu/















