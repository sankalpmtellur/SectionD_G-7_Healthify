# Healthify - Healthcare Analytics Dashboard

> Newton School of Technology | Data Visualization & Analytics  
> Capstone project using Python and Tableau to transform healthcare data into actionable insights.

---

## Project Overview

| Field | Details |
|---|---|
| Project Title | Healthify |
| Sector | Healthcare |
| Team ID | Group-7 |
| Section | D |
| Faculty Mentor | Archit Raj |
| Institute | Newton School of Technology |
| Submission Date | To be updated |

---

## Team Members

| Role | Name |
|------|------|
| Project Lead | Sankalp M Tellur |
| Data Lead | Daksh Yadav |
| Analysis Lead | Ansh |
| Visualization Lead | Balanagu sesha srikar |
| PPT and Quality Lead | Jigyasu Kalyan |
| Strategy Lead | Vaishnavi dhanai |

---

## Business Problem

Healthcare organizations generate large volumes of patient and hospital data, but decision-makers often lack clear insights into admission trends, treatment costs, and patient demographics. This project analyzes healthcare data to identify patterns in admissions, billing, and medical conditions to support data-driven hospital management.

### Core Business Question
Which medical conditions, hospitals, and patient groups drive the highest admissions and billing costs?

### Decision Supported
Allocate hospital resources efficiently by focusing on high-demand conditions and high-cost patient segments.

---

## Dataset

| Attribute | Details |
|---|---|
| Source Name | Kaggle Healthcare Dataset |
| Direct Access Link | https://www.kaggle.com/code/basantabdelmwla/healthcare |
| Row Count | ~55,000 |
| Column Count | 15 |
| Format | CSV |

### Key Columns Used

| Column Name | Description | Role in Analysis |
|-------------|-------------|-----------------|
| Medical Condition | Patient diagnosis | Segmentation |
| Billing Amount | Treatment cost | KPI |
| Admission Type | Emergency / Urgent / Elective | Filter |
| Hospital | Hospital name | Comparison |
| Age | Patient age | Demographics |
| Gender | Patient gender | Segmentation |
| Insurance Provider | Insurance company | Analysis |
| Test Results | Medical test outcome | Outcome analysis |

---

## KPI Framework

| KPI | Definition | Formula |
|-----|------------|--------|
| Average Billing Amount per Patient | Tracks treatment cost trend | Total Billing Amount / Total Patients |
| Average Length of Stay | Measures hospital stay duration | Discharge Date - Admission Date |

---

## Tableau Dashboard

| Item | Details |
|------|--------|
| Executive View | KPI summary of billing, admissions, and conditions |
| Operational View | Hospital-wise and condition-wise drill down |
| Main Filters | Gender, Age, Admission Type, Hospital, Condition |

---

## Expected Insights

1. High-cost medical conditions driving overall billing  
2. Hospitals with highest patient admissions  
3. Age groups with frequent hospital visits  
4. Emergency vs elective admission trends  
5. Insurance providers covering highest billing  
6. Gender-wise condition distribution  
7. Average stay duration by condition  
8. Test results vs treatment cost relationship  

---

## Recommendations

| # | Insight | Recommendation | Expected Impact |
|---|---|---|---|
| 1 | High cost conditions | Allocate more resources | Reduce delays |
| 2 | Peak admissions | Optimize staffing | Improve efficiency |
| 3 | Long stays | Improve discharge planning | Reduce costs |

---

## Tech Stack

- Python (Pandas, NumPy, Matplotlib, Seaborn)  
- Jupyter Notebook  
- Tableau Public  
- GitHub  

---

## Project Goal

Build an interactive healthcare dashboard that helps stakeholders analyze patient trends, treatment costs, and hospital performance for better decision-making.