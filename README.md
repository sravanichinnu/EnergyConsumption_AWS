# EnergyConsumption_AWS
Based on the Forecasting Energy Consumption I have already worked on before, I am currently working on streaming real-time energy data form publicly available data sources and create an end-to-end AWS energy consumption forecasting system.
From raw data -> processed -> model -> predictions -> visualization

I use service-linked IAM roles for Glue jobs and user-assumable roles for console access, ensuring proper separation of duties.
I configured explicit iam:PassRole permissions to allow Glue jobs to assume a service role, following AWS least-privilege and separation-of-duties best practices.”
