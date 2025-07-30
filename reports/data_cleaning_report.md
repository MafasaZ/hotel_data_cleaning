# Data Cleaning Report

## Executive Summary
- Cleaned the Hotel Booking Demand dataset
- Removed 40+ duplicates, treated 4 columns with missing values

## Data Quality Assessment
- 4 columns had missing values
- Found outliers in adr, lead_time
- Guest rows with 0 people were dropped

## Cleaning Methods
- Imputation (mode and 0)
- Outlier removal (IQR method)
- Duplicates dropped

## Final Stats
- Cleaned rows: 118,000+
- Columns: 32
- No missing values

## Recommendations
- Validate country codes on input
- Ensure agent/company data are recorded correctly
