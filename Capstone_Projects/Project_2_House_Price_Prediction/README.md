# Capstone Project 2: House Price Prediction

## Objective

Build an end-to-end machine learning pipeline that predicts residential house prices from
structured tabular features. You will practice the full workflow -- exploratory data analysis,
feature engineering, model selection, hyperparameter tuning, and evaluation -- using
Scikit-learn's regression toolkit.

---

## Skills Practiced

| Skill | Details |
|---|---|
| Exploratory Data Analysis | Distribution plots, correlation matrices, outlier detection |
| Feature Engineering | Encoding categoricals, creating interaction features, handling missing values |
| Regression Modeling | Linear Regression, Ridge, Lasso, Random Forest, Gradient Boosting |
| Model Evaluation | RMSE, MAE, R-squared, cross-validation |
| Pipeline Construction | Scikit-learn Pipeline and ColumnTransformer |

---

## Dataset

**Recommended: Ames Housing Dataset**

The Ames Housing dataset contains 2,930 observations and 80 features describing residential
homes in Ames, Iowa. It is a modern, richer replacement for the classic Boston Housing dataset.

| Source | URL |
|---|---|
| Kaggle competition | https://www.kaggle.com/c/house-prices-advanced-regression-techniques |
| Direct CSV (train) | `https://raw.githubusercontent.com/jbrownlee/Datasets/master/housing.csv` (Boston -- simpler alternative) |
| OpenML Ames | `from sklearn.datasets import fetch_openml; data = fetch_openml(name="house_prices", as_frame=True)` |

> **Note:** The Boston Housing dataset (`sklearn.datasets.load_boston`) has been deprecated
> due to ethical concerns about the data. We recommend the Ames dataset instead. For a
> quick start you can also fetch it via OpenML as shown above.

---

## Step-by-Step Instructions

### Step 1 -- Load and Explore
- Load the dataset into a Pandas DataFrame.
- Print shape, dtypes, and summary statistics.
- Identify numerical vs. categorical columns.
- Check the distribution of the target variable (`SalePrice`). Apply a log transform if it
  is heavily skewed.

### Step 2 -- Data Cleaning
- Quantify missing values per column. Decide on a strategy for each:
  - Drop columns with more than 40 % missing.
  - Impute numerical columns with the median.
  - Impute categorical columns with the mode or a placeholder like `"None"`.
- Detect and optionally remove extreme outliers (e.g., houses with `GrLivArea > 4000`
  and low sale price).

### Step 3 -- Feature Engineering
- Encode ordinal features (e.g., quality ratings) with ordinal encoding.
- One-hot encode nominal categorical features.
- Create new features:
  - `TotalSF = TotalBsmtSF + 1stFlrSF + 2ndFlrSF`
  - `HouseAge = YrSold - YearBuilt`
  - `RemodAge = YrSold - YearRemodAdd`
- Scale numerical features using StandardScaler or RobustScaler.

### Step 4 -- Modeling
Train and compare at least three models:

1. **Linear Regression** (baseline)
2. **Ridge / Lasso Regression** (regularized)
3. **Random Forest Regressor**
4. **Gradient Boosting Regressor** (e.g., `GradientBoostingRegressor` or XGBoost)

Use `sklearn.pipeline.Pipeline` and `ColumnTransformer` to bundle preprocessing and modeling.

### Step 5 -- Hyperparameter Tuning
- Use `GridSearchCV` or `RandomizedSearchCV` on your best model.
- Tune at least 3 hyperparameters (e.g., `n_estimators`, `max_depth`, `learning_rate`).
- Use 5-fold cross-validation.

### Step 6 -- Evaluation
Report the following metrics on the held-out test set:

| Metric | Formula |
|---|---|
| RMSE | `sqrt(mean((y_true - y_pred)^2))` |
| MAE | `mean(abs(y_true - y_pred))` |
| R-squared | `1 - SS_res / SS_tot` |
| RMSLE | `sqrt(mean((log(y_true+1) - log(y_pred+1))^2))` -- Kaggle's metric |

Create a residual plot and a predicted-vs-actual scatter plot.

### Step 7 -- Feature Importance
- Extract and visualize the top 15 most important features from your best tree-based model.
- Discuss which features matter most and whether that aligns with domain knowledge.

---

## Expected Deliverables

1. `starter.py` (or Jupyter notebook) with the full pipeline.
2. Model comparison table printed to the console.
3. At least 3 saved figures: residual plot, feature importance bar chart, predicted vs. actual.
4. A brief interpretation of results in code comments.

---

## Evaluation Metrics Summary

| Model | RMSE | MAE | R-squared |
|---|---|---|---|
| Linear Regression | _fill in_ | _fill in_ | _fill in_ |
| Ridge | _fill in_ | _fill in_ | _fill in_ |
| Random Forest | _fill in_ | _fill in_ | _fill in_ |
| Gradient Boosting | _fill in_ | _fill in_ | _fill in_ |

---

## Bonus Challenges

- Submit your predictions to the **Kaggle House Prices** leaderboard and report your score.
- Implement a **stacking ensemble** that combines multiple base models with a meta-learner.
- Use **SHAP** (SHapley Additive exPlanations) to produce per-prediction explanations.
- Build a simple **Flask** or **FastAPI** web app that accepts house features via a form and returns a predicted price.
- Experiment with **target encoding** for high-cardinality categorical features (e.g., `Neighborhood`).
