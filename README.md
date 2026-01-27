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
