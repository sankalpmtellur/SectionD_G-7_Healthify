# Predicting and Reducing 30-Day Hospital Readmissions

## Slide 1 – Title
- Project Title: Predicting and Reducing 30-Day Hospital Readmissions
- Sector: Healthcare Analytics
- Team ID: [Add Team ID]
- Team Members: [Add Team Members]
- Faculty Mentor: [Add Faculty Mentor]

## Slide 2 – Context & Problem Statement
- Unplanned 30-day hospital readmissions drive massive financial penalties and reflect systemic gaps in care transition.
- **Stakeholders:** Hospital administrators, clinical management, and transitional care teams.
- **Core Business Question:** How can we proactively identify patients at the highest risk of returning within 30 days and intervene effectively?
- **Objective:** Develop a robust analytics methodology to isolate readmission risk factors and deliver a trackable KPI framework for operational deployment.

## Slide 3 – Data Engineering
- **Dataset Source:** Historical hospital patient discharge records.
- **Size:** 30,600 unique rows × 12 clinical and demographic columns.
- **Key Cleaning Steps:**
  - Mitigated missing values through robust clinical imputations (median for continuous inputs, mode for categorical).
  - Standardized categorical formats and mitigated noisy strings to ensure downstream metric consistency.
  - Parsed complex string variables (e.g., blood pressure) into actionable binary and continuous vectors.
- **Data Coverage:** Comprehensive view encompassing patient demographics, key clinical indicators, and longitudinal outcomes.

## Slide 4 – KPI Framework
- **30-Day Readmission Rate:** The primary benchmark metric reflecting overall transitional care efficacy.
- **Readmission by Discharge Destination:** Highlights structural breakdowns based on where the patient is released.
- **Length of Stay Comparison:** Evaluates the variance in baseline inpatient time against future readmission propensity.
- **High-Risk Patient Rate:** Monitors the proportion of patient volume meeting multi-variate high-risk criteria.
- **Medication Burden Index:** Evaluates the complexity of pharmaceutical regimens ordered at discharge.
- **Business Value:** Translating raw clinical events into trackable operational benchmarks guides strategic resource allocation and policy refinement.

## Slide 5 – Key EDA Insights
- **Polypharmacy Risk:** Patients with a medication burden exceeding 5 concurrent prescriptions show a 22% higher likelihood of readmission.
- **Length of Stay Correlation:** Extended initial stays (beyond 7 days) strongly predicate secondary complications, driving bounce-backs.
- **Comorbidity Amplifiers:** Co-presentation of clinical diabetes and hypertension drives a compounded risk significantly higher than the baseline average.
- **Discharge Structural Risks:** Discharges to non-home nursing facilities correspond directly with elevated readmission ratios, indicating gaps in facility hand-offs.
- **Metabolic Factors:** High BMI classifications coupled with advanced age cohorts correlate strongly with failure to thrive post-discharge.

## Slide 6 – Advanced Analysis
- **Model Framework:** Logistic Regression & Decision Tree Classifiers.
- **Purpose:** To transition from historical descriptive analytics to predictive risk targeting for impending discharges.
- **Key Findings:** Medication count, principal comorbidities (diabetes/hypertension), and prolonged initial stay length emerged as the strongest predictive risk signals.
- **Diagnostic Performance:** Achieved balanced evaluation metrics (Accuracy, Precision, Recall) optimized to minimize false negatives, ensuring high-risk profiles are flagged prior to release.

## Slide 7 – Dashboard Overview
- **Executive View:** Top-level metrics tracking the aggregate 30-day readmission rate and total patient operational volume.
- **Operational View:** Deep-dive drill-downs analyzing readmission velocity segmented by discharge destination and risk tiers.
- **Dynamic Filters:** Empowers end-users to isolate trends actively across Age Groups, Gender, BP Categories, and Specific Discharge Locations.

## Slide 8 – Top Insights
- **Targeted Vulnerability:** The cross-interaction between elevated age and the presence of diabetes serves as a massive amplifier for readmission likelihood.
- **Polypharmacy Danger Zone:** Quantifiable evidence indicates that post-discharge medication counts directly index against 30-day return risk, requiring immediate intervention strategies.
- **Destination Blind Spots:** Releasing patients to specific secondary care facilities without stringent baseline health requirements creates highly predictable bounce-back events.

## Slide 9 – Recommendations
- **Automated Risk Scoring:** Implement a predictive threshold flag in the EHR system prior to patient discharge to halt unsafe releases.
- **Transitional Follow-up:** Mandate a 48-hour tele-health check-in protocol for all patients crossing into the "High Risk" tier.
- **Medication Review Taskforce:** Require clinical pharmacist sign-off on discharge plans exceeding 5 concurrent medications.
- **Targeted Destination Vetting:** Enhance care coordination protocols and verify clinical capabilities for nursing facilities receiving complex cases.

## Slide 10 – Impact
- **Outcome Improvement:** Targeted 12-15% reduction in the baseline 30-Day Readmission Rate.
- **Cost Benefits:** Avoidance of substantial readmission penalty fines from regulatory bodies and insurers, optimizing bed turnover.
- **Feasibility:** High priority and highly actionable using existing clinical outreach personnel reallocated to focus purely on high-risk discharge planning.

## Slide 11 – Limitations
- **Data Constraints:** Absence of granular ICD-10 diagnostic coding prevents disease-specific modeling.
- **Temporal Blindness:** Lack of time-series event data limits understanding regarding exact symptom onset post-discharge.
- **Model Constraints:** Algorithmic approximations may under-represent deeply complex, unpredictable multi-morbidity interactions out-of-sample.

## Slide 12 – Next Steps
- **Data Enrichment:** Procure and integrate comprehensive ICD-10 diagnostic data streams.
- **System Integration:** Deploy the finalized algorithm as a live, real-time micro-service API interacting with hospital admission systems.
- **Longitudinal Tracking:** Extend tracking windows beyond 30 days to measure 60/90-day comprehensive care success.

## Closing Statement
"From 30,000 patient records to actionable readmission reduction — enabling data-driven healthcare decisions."
