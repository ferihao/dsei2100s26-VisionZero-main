# Predicting Traffic Collision Injury Outcomes to Prioritize NYC Vision Zero Redesigns

---

## 1. Problem and Stakeholders

Traffic collisions remain a major public safety issue in New York City. Despite ongoing efforts from the NYC Vision Zero initiative, many collisions still result in injuries across the city. Current safety interventions are often **reactive** — infrastructure improvements are implemented only after severe crashes have already occurred, which can delay safety measures and lead to inefficient use of resources.

**Primary Stakeholder:** NYC Department of Transportation (NYC DOT) Vision Zero Task Force

Their goal is to identify high-risk locations and prioritize redesign efforts such as:

- Safer intersections
- Improved signal timing
- Pedestrian protection

This project aims to develop a machine learning model that predicts whether a traffic collision will result in **no injury**, **injury**, or **fatality** based on observable conditions such as time and location. By identifying patterns associated with higher-risk crashes, the model can support proactive decision-making and help reduce injuries across the city.

---

## 2. Dataset

**Source:** [Motor Vehicle Collisions – Crashes](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95) (NYC Open Data)

The dataset contains detailed records of police-reported traffic collisions in New York City. Each row represents a crash event with information about time, location, contributing factors, and injury counts.

**Key characteristics:**

| Property | Detail |
| --- | --- |
| Rows | ~2.2 million |
| Columns | 29 |
| Updated | Daily by NYPD |
| Access | Publicly available |

**Important features:**

- **Time:** `crash_date`, `crash_time`
- **Location:** `borough`, `zip_code`, `latitude`, `longitude`, street-level info
- **Crash details:** contributing factors, injury counts, fatality counts

> For efficiency, the dataset may be limited to a recent year (e.g., 2023) during model development.

---

## 3. Machine Learning Methods

The core task is a **multi-class classification** problem — predicting crash severity.

### Target Variable

Derived from `number_of_persons_injured` and `number_of_persons_killed`, then encoded as:

| Class | Label |
| --- | --- |
| `0` | No Injury |
| `1` | Injury |
| `2` | Fatality |

### Feature Design

Features available at the time of the crash:

| Category | Features |
| --- | --- |
| Time-based | Hour of day, day of week, weekend indicator, rush hour flag |
| Location-based | Borough, ZIP code, geographic coordinates |
| Contributing factors | Grouped and encoded |

> Features that directly reveal the outcome (e.g., injury counts) are **excluded** from predictors to avoid data leakage.

### Models

| # | Model | Role |
| --- | --- | --- |
| 1 | **Logistic Regression** | Baseline — simple and interpretable |
| 2 | **Random Forest** | Required — ensemble of decision trees, robust to noise and missing data |
| 3 | **XGBoost** | Primary model — captures nonlinear relationships and feature interactions |
| 4 | **SVM** | Comparison — evaluates performance in high-dimensional feature space |

### Train / Test Split Strategy

To avoid **temporal leakage**, the dataset will be split by time rather than randomly:

| Split | Years | Purpose |
| --- | --- | --- |
| **Train** | 2022 – 2024 | Fit all models |
| **Validation** | 2025 | Tune hyperparameters |
| **Test** | 2026 | Final evaluation (held out until end) |

A random split would allow the model to train on future crashes and test on past ones, which inflates performance metrics and does not reflect real-world deployment conditions. The time-based split ensures the model is always predicting forward in time.

### Evaluation Metrics

Because severe crashes are relatively rare, the dataset is **imbalanced**. Accuracy alone is not sufficient. Performance will be evaluated using:

- F1-score
- Precision & Recall
- ROC-AUC
- Confusion matrix

---

## 4. Team Work Distribution

The project is divided into parallel work streams to ensure equal contribution.

| Work Stream | Responsibilities |
| --- | --- |
| **Data Preparation & Feature Engineering** | Clean dataset, handle missing values, create time-based features |
| **Exploratory Data Analysis (EDA)** | Analyze crash distributions by location, time, and contributing factors |
| **Model Development** | Implement and train Logistic Regression, XGBoost, and SVM; evaluate performance |
| **Model Interpretation & Insights** | Analyze feature importance, translate findings into actionable recommendations |

All work will be coordinated through a shared GitHub repository, with each member contributing through version-controlled commits.