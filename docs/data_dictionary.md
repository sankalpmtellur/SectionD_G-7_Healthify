# Data Dictionary

## Dataset Summary

| Item          | Details                                        |
| ------------- | ---------------------------------------------- |
| Dataset name  | Hospital Readmission Dataset                   |
| Source        | Simulated healthcare dataset (project dataset) |
| Raw file name | hospital_readmissions.csv                  |
| Last updated  | April 2026                                     |
| Granularity   | One row per patient admission                  |

---

## Column Definitions

| Column Name           | Data Type | Description                                              | Example Value | Used In       | Cleaning Notes                |
| --------------------- | --------- | -------------------------------------------------------- | ------------- | ------------- | ----------------------------- |
| patient_id            | string    | Unique identifier for each patient                       | P10234        | EDA / Tableau | No changes                    |
| age                   | int       | Patient age in years                                     | 56            | EDA           | Used to create age_group      |
| gender                | string    | Patient gender                                           | Male          | EDA / Tableau | Standardized labels           |
| cholesterol           | float     | Cholesterol level of patient                             | 210.5         | EDA           | Checked for outliers          |
| bmi                   | float     | Body Mass Index of patient                               | 27.3          | EDA           | No major changes              |
| diabetes              | string    | Indicates if patient has diabetes                        | Yes           | KPI / Tableau | Converted to categorical      |
| hypertension          | string    | Indicates if patient has hypertension                    | No            | KPI / Tableau | Standardized Yes/No           |
| medication_count      | int       | Number of medications prescribed                         | 5             | EDA           | No changes                    |
| length_of_stay        | int       | Number of days patient stayed in hospital                | 7             | KPI / Tableau | Used for stay_category        |
| discharge_destination | string    | Where patient goes after discharge                       | Home          | KPI / Tableau | Cleaned category names        |
| readmitted_30_days    | int       | Indicates if patient was readmitted within 30 days (0/1) | 1             | EDA           | Base column                   |
| systolic_bp           | int       | Systolic blood pressure                                  | 130           | EDA           | Derived from BP               |
| diastolic_bp          | int       | Diastolic blood pressure                                 | 85            | EDA           | Derived from BP               |
| is_readmitted         | int       | Binary flag for readmission (0/1)                        | 1             | KPI / Tableau | Used for KPI calculations     |
| age_group             | string    | Categorized age buckets                                  | 45–60         | KPI / Tableau | Derived column                |
| stay_category         | string    | Categorized length of stay                               | Long Stay     | KPI / Tableau | Derived column                |
| risk_tier             | string    | Risk classification of patient                           | High          | KPI / Tableau | Derived from multiple factors |

---

## Derived Columns

| Derived Column | Logic                                               | Business Meaning                               |
| -------------- | --------------------------------------------------- | ---------------------------------------------- |
| age_group      | Age bucketed into ranges (18–30, 30–45, 45–60, 60+) | Helps identify risk by age segment             |
| stay_category  | Length of stay grouped into Short, Medium, Long     | Helps analyze impact of stay duration          |
| risk_tier      | Based on conditions and patient attributes          | Identifies high-risk patients for intervention |
| is_readmitted  | Binary conversion of readmitted_30_days             | Used for KPI calculation (readmission rate)    |

---

## Data Quality Notes

* Dataset is simulated and may not reflect real-world hospital complexity
* No time-series/date column available for trend analysis
* Some categorical fields required standardization (Yes/No values)
* Outliers in cholesterol and BMI checked but retained for realism
* Risk tier is derived, not originally present in raw dataset