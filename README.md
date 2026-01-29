# EnergyConsumption_AWS
Based on the Forecasting Energy Consumption I have already worked on before, I am currently working on streaming real-time energy data form publicly available data sources and create an end-to-end AWS energy consumption forecasting system.
From raw data -> processed -> model -> predictions -> visualization

I use service-linked IAM roles for Glue jobs and user-assumable roles for console access, ensuring proper separation of duties.
I configured explicit iam:PassRole permissions to allow Glue jobs to assume a service role, following AWS least-privilege and separation-of-duties best practices.

1. schema normalization
2. converting timestamps to datetime - as this enables: without this time-series features break
   a. sorting datetime
   b. extracting day/hour/month
   c. rolling windows

Time-series data must be sortable by a reliable timestamp - not necessarily pre-sorted.
As long as:
- each record has a correct timestamp
- you order it when querying/processing

## Time-series data is logically ordered by time, but it does not need to be strictly ordered in storage or ingestion as long as it contains a reliable timestamp and is ordered during processing or analysis.

When we are dealing with time-series data, make sure the data is ordered atleast for querying or processing. Because of the below reasons:
1. lag features assume previous rows = earlier time
   - in general, a lag feature means "use a value from the past to help predict the present". This only makes sense if "row before the current row actually represents an earlier time".
   EXAMPLE:
time  value  lag_1
10:00  100     -       Here, "previous row" = earlier timestamp. so, lag feature is meaningful.
10:01  110   100
10:02  105   110

when the data isn't ordered like below:
time  value  lag_1
10:02  105     -       Here, "previous row" might actually be from the future. your model learns future information. This causes data leakage.
10:00  100   105
10:01  110   100

# Interview Takeaway:
Lag features assume row order matches time order. If not sorted, lag features leak future information and break model validity.

2. Rolling windows assume ordered data.
   - in general, A rolling window "captures statistics over a continuous time range"
Example: rolling average (window size = 3)
correct order:
time  value  rolling_avg_3
10:00  10         -
10:01  20         -                 Here in this example, each window represents past -> present
10:02  30     (10+20+30)/3
10:03  40     (20+30+40)/3
If the data isn't ordered, last 3 rows not equals to last 3 time points and window jumps across time. Result is mathematically wrong, even if code runs.

Summary: Lag features and rolling windows rely on ordered time because they assume earlier rows represent past observtions; without ordering, they can introduce data leakage or compute incorrect aggregates.

# Glue Job and storing processed data in S3
Create a Glue job, work on the Glue script to read the data from S3 bucket, process it and store the resultant dataset in processed folder in S3 bucket in Parquet format.
After the data is processed, it is stored in the S3 bucket.
file path: "s3://energy-consumption-forecasting-project/processed/pandas/pjme_energy_features.parquet"

# Querying a data lake using SQL (without moving data)
For this, I leveraged Glue Data Catalog + Athena
At this point, the data is in S3 bucket in Parquet format. To query this wtih SQL, AWS needs metadata like column names, data types, S3 location. This metadata lives in the Glue Data Catalog. Then,
Athenae = SQL Engine
Glue Catalog = table definitions
S3 = actual data

1. Create a Glue database (logical container). In this case, its named as, "energy_forcasting_db"
2. Create a Glue Table. In this case, the table is named as, "pjme_energy_features"
3. Athena (SQL time)
   - came across error, "Error fetching workgroup
You are not authorized to perform: athena:GetWorkGroup on the resource. After your AWS administrator or you have updated your permissions, please try again."
Have to add the permission to "athena:GetWorkGroup"
4. Once I have some SQL queries results, I am now trying to visualize the data to answer some probable business question like,
   "What does energy consumption look like over time, and what patterns exist?"
5. For visualization, I am using Amazon QuickSight. Performed exploratory data analysis using Athena-backed QuickSight dashboards before training forecasting models.

# AWS SageMaker
SageMaker Unified Studio is built on top of AWS DataZone.
So for the first time, when I click "Set up Unified Studio", AWS internally does:
- create a DataZone domain
- create Projects
- Set up governance resources
That is admin-level infrastructure creation, not day-to-day ML work.





















