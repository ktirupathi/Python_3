# Capstone Project 3: Customer Churn Prediction

## Objective

Build a binary classification system that predicts whether a telecom customer will churn
(cancel their service). This project walks you through the complete machine learning
lifecycle -- from exploratory data analysis through model deployment -- with a strong
emphasis on handling class imbalance and selecting appropriate evaluation metrics for
business decision-making.

---

## Skills Practiced

| Skill | Details |
|---|---|
| Exploratory Data Analysis | Distribution analysis, group comparisons, correlation |
| Data Preprocessing | Encoding, scaling, handling imbalanced classes |
| Classification Modeling | Logistic Regression, Random Forest, XGBoost, SVM |
| Model Evaluation | Accuracy, Precision, Recall, F1-Score, AUC-ROC, Confusion Matrix |
| Business Interpretation | Translating model outputs into actionable retention strategies |

---

## Dataset

**Telco Customer Churn Dataset**

This classic dataset from IBM contains 7,043 customer records with 21 features covering
demographics, account information, and subscribed services.

| Source | URL |
|---|---|
| Kaggle | https://www.kaggle.com/datasets/blastchar/telco-customer-churn |
| Direct CSV | `https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv` |

**Key columns:**

| Column | Description |
|---|---|
| `customerID` | Unique identifier |
| `gender`, `SeniorCitizen`, `Partner`, `Dependents` | Demographics |
| `tenure` | Months with the company |
| `PhoneService`, `InternetService`, `Contract` | Service details |
| `MonthlyCharges`, `TotalCharges` | Billing |
| `Churn` | Target variable (Yes / No) |

---

## Step-by-Step Instructions

### Step 1 -- Load and Inspect
- Load the CSV into a Pandas DataFrame.
- Check shape, data types, and missing values.
- Convert `TotalCharges` from string to numeric (watch for empty strings).
- Drop `customerID` as it carries no predictive signal.

### Step 2 -- Exploratory Data Analysis
Create visualizations that answer these questions:

1. What is the overall churn rate? (bar chart)
2. How does churn vary by `Contract` type? (grouped bar chart)
3. How does `tenure` distribution differ between churned and retained customers? (overlapping histograms or KDE plot)
4. What is the correlation between numerical features and churn? (heatmap)
5. Which services are most associated with churn? (stacked bar chart)

### Step 3 -- Data Preprocessing
- Encode binary categorical columns (Yes/No) as 0/1.
- One-hot encode multi-class categorical columns (`InternetService`, `Contract`, `PaymentMethod`).
- Scale numerical features (`tenure`, `MonthlyCharges`, `TotalCharges`).
- Address class imbalance using one or more of:
  - SMOTE (from `imblearn`)
  - Class weights (`class_weight="balanced"`)
  - Undersampling the majority class

### Step 4 -- Modeling
Train and compare at least four classifiers:

1. **Logistic Regression** (baseline, interpretable)
2. **Random Forest Classifier**
3. **Gradient Boosting / XGBoost**
4. **Support Vector Machine** (optional)

Use `sklearn.pipeline.Pipeline` to chain preprocessing and modeling.

### Step 5 -- Evaluation
For each model, report:

| Metric | Why It Matters |
|---|---|
| **Accuracy** | Overall correctness (but misleading with imbalanced data) |
| **Precision** | Of predicted churners, how many actually churned? |
| **Recall (Sensitivity)** | Of actual churners, how many did we catch? |
| **F1-Score** | Harmonic mean of precision and recall |
| **AUC-ROC** | Ability to discriminate between classes across all thresholds |

Generate and save:
- Confusion matrix heatmap for each model.
- ROC curves for all models on the same plot.
- Precision-Recall curve.

### Step 6 -- Feature Importance and Interpretation
- Extract the top 15 most important features from the best tree-based model.
- Discuss: Which factors most strongly predict churn? Do these align with business intuition?

### Step 7 -- Threshold Optimization
- The default classification threshold is 0.5, but the optimal threshold depends on
  business costs (cost of losing a customer vs. cost of a retention offer).
- Plot F1-score and profit as a function of the decision threshold.
- Select the threshold that maximizes the chosen business metric.

---

## Expected Deliverables

1. `starter.py` (or Jupyter notebook) with complete, well-commented code.
2. Model comparison table printed to console.
3. At least 4 saved figures: churn distribution, ROC curves, confusion matrix, feature importance.
4. A brief written interpretation of which customers are most at risk and why.

---

## Bonus Challenges

- Implement **SHAP** values to explain individual predictions (e.g., "Why is this specific customer predicted to churn?").
- Build a **customer segmentation** layer using K-Means clustering before classification.
- Create a **Streamlit dashboard** where a user enters customer details and receives a churn probability.
- Calculate the expected **financial impact** of deploying this model assuming a retention offer cost and a customer lifetime value.
- Train a **neural network** classifier using TensorFlow/Keras and compare with traditional ML models.
