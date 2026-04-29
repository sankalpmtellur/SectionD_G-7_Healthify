# 🏥 Healthify — Hospital Readmission Analytics

> **Newton School of Technology** | Data Visualization & Analytics
> Capstone project using Python and Tableau to identify the key drivers of 30-day hospital readmissions and translate patient data into actionable care improvements.

---

## 📋 Project Overview

| Field | Details |
|---|---|
| **Project Title** | Healthify |
| **Sector** | Healthcare |
| **Team ID** | Group-7 |
| **Section** | D |
| **Faculty Mentor** | Archit Raj |
| **Institute** | Newton School of Technology |
| **Submission Date** | 29-04-2026 |

---

## 👥 Team Members

| Role | Name | Dashboard Ownership |
|------|------|---------------------|
| Project Lead | Sankalp M Tellur | Overall coordination & narrative |
| Data Lead | Daksh Yadav | Data cleaning & preparation |
| Analysis Lead | Ansh | Dashboard 2 — Clinical Conditions |
| Visualization Lead | Balanagu Sesha Srikar | Dashboard 1 — Patient Demographics & Risk |
| PPT and Quality Lead | Jigyasu Kalyan | Presentation design & transitions |
| Strategy Lead | Vaishnavi Dhanai | Dashboard 3 — Hospital Operations |

---

## 🔍 Business Problem

Hospital readmissions within 30 days increase costs and indicate gaps in patient care. This project analyzes patient data to identify key factors driving 30-day readmissions, including health conditions, demographics, and treatment patterns.

### Core Questions This Project Answers

| # | Question | Addressed In |
|---|----------|-------------|
| 1 | **Who** is most at risk of readmission? | Dashboard 1 |
| 2 | **Why** are patients being readmitted? | Dashboard 2 |
| 3 | **Where** can hospital operations improve? | Dashboard 3 |

### Decision Supported
Allocate hospital resources efficiently by focusing on high-risk patient segments, chronic condition management, and optimizing discharge pathways.

---

## 📁 Dataset

| Attribute | Details |
|---|---|
| **Source** | Kaggle Healthcare Dataset |
| **Link** | https://www.kaggle.com/datasets/sankalpmtellur/healthify-raw-dataset |
| **Rows** | ~30,000 |
| **Columns** | 12 |
| **Format** | CSV |

### Data Files Used in This Project

| File | Used By | Purpose |
|------|---------|---------|
| `cleaned_data.csv` | All three dashboards | Primary patient dataset |
| `age_kpi.csv` | Dashboard 1 | Age-based KPI supplementary data |
| `risk_kpi.csv` | Dashboard 1 | Risk tier KPI supplementary data |
| `condition_kpi.csv` | Dashboard 2 | Condition-based KPI data |
| `stay_kpi.csv` | Dashboard 2 | Length-of-stay KPI data |
| `discharge_kpi.csv` | Dashboard 3 | Discharge destination KPI data |

### Key Columns

| Column | Description | Used In |
|--------|-------------|---------|
| `patient_id` | Unique patient identifier | All dashboards |
| `is_readmitted` | 1 = readmitted within 30 days, 0 = not | All dashboards |
| `age` / `age_group` | Patient age and age bracket | Dashboard 1 |
| `gender` | Patient gender | Dashboard 1 |
| `risk_tier` | Low / Medium / High risk classification | Dashboard 1 |
| `diabetes` | Whether patient has diabetes (yes/no) | Dashboard 2 |
| `hypertension` | Whether patient has hypertension (yes/no) | Dashboard 2 |
| `bmi` | Body Mass Index | Dashboard 2 |
| `cholesterol` | Cholesterol level | Dashboard 2 |
| `medication_count` | Number of medications at discharge | Dashboard 2 & 3 |
| `length_of_stay` | Total days admitted | Dashboard 2 & 3 |
| `stay_category` | Short / Medium / Long / Extended | Dashboard 3 |
| `discharge_destination` | Where patient was discharged to | Dashboard 3 |

---

## 📊 Dashboard Architecture

The three dashboards are designed as chapters of a single narrative:

```
Dashboard 1          Dashboard 2          Dashboard 3
─────────────   →    ─────────────   →    ─────────────
Patient Risk &       Clinical             Hospital
Demographics         Conditions           Operations

WHO is at risk?      WHY readmitted?      WHERE to improve?
```

---

### Dashboard 1 — Patient Demographics & Risk Analysis
**Owner:** Balanagu Sesha Srikar

#### KPIs
| KPI | Formula |
|-----|---------|
| Overall Readmission Rate | `SUM(is_readmitted) / COUNT(patient_id)` |
| Total Patients | `COUNT(patient_id)` |
| High-Risk Patient % | `COUNT(IF risk_tier='high' THEN patient_id END) / COUNT(patient_id)` |

#### Charts
| # | Title | Type |
|---|-------|------|
| 1 | Age Group vs Readmission Rate | Bar Chart |
| 2 | Gender vs Readmission Rate | Bar Chart |
| 3 | Risk Tier Distribution | Pie Chart |
| 4 | Risk Tier vs Readmission Rate | Bar Chart |
| 5 | Age vs Length of Stay | Scatter Plot |

**Filters:** `gender`, `age_group`, `risk_tier`

---

### Dashboard 2 — Clinical Condition Impact Analysis
**Owner:** Ansh

#### KPIs
| KPI | Formula |
|-----|---------|
| Diabetes Patient Readmission % | `AVG(IF diabetes='yes' THEN is_readmitted END)` |
| Hypertension Patient Readmission % | `AVG(IF hypertension='yes' THEN is_readmitted END)` |
| Average Length of Stay | `AVG(length_of_stay)` |

#### Charts
| # | Title | Type |
|---|-------|------|
| 1 | Diabetes vs Readmission Rate | Bar Chart |
| 2 | Hypertension vs Readmission Rate | Bar Chart |
| 3 | Condition Combination Heatmap (Diabetes × Hypertension) | Heatmap |
| 4 | BMI Distribution | Histogram |
| 5 | Cholesterol vs Readmission | Scatter Plot |

**Filters:** `diabetes`, `hypertension`

---

### Dashboard 3 — Hospital Operations Optimization
**Owner:** Vaishnavi Dhanai

#### KPIs
| KPI | Formula |
|-----|---------|
| Average Length of Stay | `AVG(length_of_stay)` |
| Average Medication Count | `AVG(medication_count)` |
| Highest-Risk Discharge Type | `MAX readmission rate by discharge_destination` |

#### Charts
| # | Title | Type |
|---|-------|------|
| 1 | Discharge Destination vs Readmission Rate | Bar Chart |
| 2 | Discharge Destination — Patient Volume | Bar Chart |
| 3 | Average Stay by Discharge Destination | Bar Chart |
| 4 | Medication Count by Risk Tier | Box Plot |
| 5 | Stay Category vs Readmission Rate | Bar Chart |

**Filters:** `discharge_destination`, `stay_category`

---

## 💡 Key Insights

1. Elderly patients (60+) show disproportionately higher readmission rates
2. Patients with both diabetes and hypertension represent the highest-risk clinical segment
3. High-risk tier patients are significantly more likely to be readmitted than low/medium risk patients
4. Certain discharge destinations are consistently associated with worse 30-day outcomes
5. Patients managing a high number of medications at discharge face greater readmission risk
6. Short-stay patients in some categories show unexpectedly high readmission rates, suggesting premature discharge

---

## ✅ Recommendations

| # | Recommendation | Evidence From | Expected Impact |
|---|----------------|---------------|-----------------|
| 1 | Strengthen discharge planning for High-risk tier patients | Dashboard 1 — Risk Tier vs Readmission | Reduces readmissions in the most critical segment |
| 2 | Increase post-discharge monitoring for patients with both diabetes and hypertension | Dashboard 2 — Condition Heatmap | Targets highest compounded clinical risk |
| 3 | Create age-specific post-discharge care plans for patients 60+ | Dashboard 1 — Age Group vs Readmission | Reduces readmissions in the most vulnerable age group |
| 4 | Improve follow-up for long-stay patients managing complex medication regimens | Dashboard 3 — Medication Count & Stay Category | Reduces compliance-related re-entries |
| 5 | Audit and redesign the highest-risk discharge pathway identified in Dashboard 3 | Dashboard 3 — Discharge Destination vs Readmission | Directly targets the weakest care transition |

---

## 🛠 Tech Stack

| Tool | Purpose |
|------|---------|
| Python (Pandas, NumPy) | Data cleaning & preparation |
| Matplotlib / Seaborn | Exploratory data analysis |
| Jupyter Notebook | Data pipeline documentation |
| Tableau Public | Interactive dashboard creation |
| GitHub | Version control & collaboration |

---

## 📂 Repository Structure

```
healthify/
│
├── data/
│   ├── cleaned_data.csv
│   ├── age_kpi.csv
│   ├── risk_kpi.csv
│   ├── condition_kpi.csv
│   ├── stay_kpi.csv
│   └── discharge_kpi.csv
│
├── notebooks/
│   └── data_cleaning.ipynb
│
├── dashboards/
│   ├── dashboard1_demographics.twbx
│   ├── dashboard2_conditions.twbx
│   └── dashboard3_operations.twbx
│
├── presentation/
│   └── healthify_final_presentation.pptx
│
└── README.md
```

---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/sankalpmtellur/SectionD_G-7_Healthify
   cd SectionD_G-7_Healthify
   ```

2. **Install Python dependencies**
   ```bash
   pip install pandas numpy matplotlib seaborn jupyter
   ```

3. **Run the data cleaning notebook**
   ```bash
   jupyter notebook notebooks/data_cleaning.ipynb
   ```

4. **Open dashboards in Tableau**
   - Open Tableau Desktop or Tableau Public
   - Open the `.twbx` files from the `dashboards/` folder
   - Connect to the data files in the `data/` folder if prompted

---

## 📌 Project Goal

Build a three-part interactive healthcare dashboard that helps hospital administrators and clinical staff identify which patients are at risk of 30-day readmission, understand the clinical conditions driving that risk, and take targeted operational action to improve care outcomes and reduce costs.

---

> *Newton School of Technology — Group 7, Section D*
> *Faculty Mentor: Archit Raj*
