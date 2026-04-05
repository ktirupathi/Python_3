"""
Capstone Project 2: House Price Prediction
============================================
End-to-end regression pipeline using the Ames Housing dataset.

Usage:
    python starter.py
"""

import os
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

warnings.filterwarnings("ignore")

FIGURES_DIR = os.path.join(os.path.dirname(__file__), "figures")
os.makedirs(FIGURES_DIR, exist_ok=True)

RANDOM_STATE = 42
TEST_SIZE = 0.2


# ---------------------------------------------------------------------------
# Step 1: Load and Explore
# ---------------------------------------------------------------------------
def load_dataset():
    """Fetch the Ames Housing dataset from OpenML.

    Returns:
        pd.DataFrame: Full DataFrame with features and target (SalePrice).
    """
    # TODO: Use fetch_openml(name="house_prices", as_frame=True) to load data.
    # Combine features and target into a single DataFrame.
    pass


def explore_data(df):
    """Print summary statistics and plot target distribution.

    Args:
        df (pd.DataFrame): Full dataset.
    """
    # TODO: Print shape, dtypes, describe().
    # TODO: Plot histogram of SalePrice; check skewness.
    # TODO: Apply np.log1p transform if skew > 0.75.
    pass


# ---------------------------------------------------------------------------
# Step 2: Data Cleaning
# ---------------------------------------------------------------------------
def clean_data(df):
    """Handle missing values and remove outliers.

    Args:
        df (pd.DataFrame): Raw dataset.

    Returns:
        pd.DataFrame: Cleaned dataset.
    """
    # TODO: Drop columns with > 40% missing values.
    # TODO: Remove outlier rows (e.g., GrLivArea > 4000 with low SalePrice).
    # TODO: Separate numerical and categorical columns for later imputation.
    pass


# ---------------------------------------------------------------------------
# Step 3: Feature Engineering
# ---------------------------------------------------------------------------
def engineer_features(df):
    """Create new features and identify column types.

    Args:
        df (pd.DataFrame): Cleaned dataset.

    Returns:
        tuple: (df, numerical_cols, categorical_cols)
    """
    # TODO: Create TotalSF, HouseAge, RemodAge features.
    # TODO: Separate numerical and categorical column lists.
    pass


def build_preprocessor(numerical_cols, categorical_cols):
    """Build a ColumnTransformer for preprocessing.

    Args:
        numerical_cols (list[str]): Numerical feature names.
        categorical_cols (list[str]): Categorical feature names.

    Returns:
        ColumnTransformer: Fitted-ready preprocessor.
    """
    numerical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])

    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
    ])

    preprocessor = ColumnTransformer([
        ("num", numerical_pipeline, numerical_cols),
        ("cat", categorical_pipeline, categorical_cols),
    ])
    return preprocessor


# ---------------------------------------------------------------------------
# Step 4: Modeling
# ---------------------------------------------------------------------------
def build_models():
    """Return a dictionary of model name -> estimator.

    Returns:
        dict[str, object]: Models to train and compare.
    """
    models = {
        "Linear Regression": LinearRegression(),
        "Ridge": Ridge(alpha=10.0),
        "Lasso": Lasso(alpha=0.001),
        "Random Forest": RandomForestRegressor(
            n_estimators=200, max_depth=15, random_state=RANDOM_STATE
        ),
        "Gradient Boosting": GradientBoostingRegressor(
            n_estimators=300, max_depth=4, learning_rate=0.1,
            random_state=RANDOM_STATE
        ),
    }
    return models


def train_and_evaluate(models, preprocessor, X_train, X_test, y_train, y_test):
    """Train each model and collect evaluation metrics.

    Args:
        models (dict): Model name -> estimator.
        preprocessor (ColumnTransformer): Feature preprocessor.
        X_train, X_test, y_train, y_test: Train/test splits.

    Returns:
        pd.DataFrame: Comparison table with RMSE, MAE, R-squared per model.
    """
    results = []
    best_model = None
    best_rmse = float("inf")

    for name, model in models.items():
        pipe = Pipeline([
            ("preprocessor", preprocessor),
            ("model", model),
        ])

        # TODO: Fit the pipeline on training data.
        # TODO: Predict on test data.
        # TODO: Compute RMSE, MAE, R-squared.
        # TODO: Track the best model by RMSE.
        # TODO: Append results dict to the results list.
        pass

    results_df = pd.DataFrame(results)
    print("\n=== Model Comparison ===")
    print(results_df.to_string(index=False))
    return results_df, best_model


# ---------------------------------------------------------------------------
# Step 5: Hyperparameter Tuning
# ---------------------------------------------------------------------------
def tune_best_model(best_pipeline, X_train, y_train):
    """Run GridSearchCV on the best model.

    Args:
        best_pipeline (Pipeline): Pipeline with preprocessor + best model.
        X_train, y_train: Training data.

    Returns:
        Pipeline: Refitted pipeline with best hyperparameters.
    """
    # TODO: Define a param_grid targeting model__ prefixed parameters.
    # TODO: Run GridSearchCV with cv=5 and scoring="neg_root_mean_squared_error".
    # TODO: Print best params and best score.
    # TODO: Return the best estimator.
    pass


# ---------------------------------------------------------------------------
# Step 6: Evaluation Visualizations
# ---------------------------------------------------------------------------
def plot_residuals(y_test, y_pred, save=True):
    """Create a residual plot."""
    residuals = y_test - y_pred
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(y_pred, residuals, alpha=0.5, edgecolors="k", linewidths=0.5)
    ax.axhline(y=0, color="red", linestyle="--")
    ax.set_xlabel("Predicted Price")
    ax.set_ylabel("Residual")
    ax.set_title("Residual Plot")
    plt.tight_layout()
    if save:
        fig.savefig(os.path.join(FIGURES_DIR, "residuals.png"), dpi=150)
    plt.show()


def plot_predicted_vs_actual(y_test, y_pred, save=True):
    """Scatter plot of predicted vs. actual values."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(y_test, y_pred, alpha=0.5, edgecolors="k", linewidths=0.5)
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()],
            "r--", label="Perfect prediction")
    ax.set_xlabel("Actual Price")
    ax.set_ylabel("Predicted Price")
    ax.set_title("Predicted vs. Actual")
    ax.legend()
    plt.tight_layout()
    if save:
        fig.savefig(os.path.join(FIGURES_DIR, "predicted_vs_actual.png"), dpi=150)
    plt.show()


def plot_feature_importance(model, feature_names, top_n=15, save=True):
    """Bar chart of top feature importances from a tree-based model.

    Args:
        model: Fitted model with a feature_importances_ attribute.
        feature_names (list[str]): Names corresponding to each feature.
        top_n (int): Number of top features to display.
        save (bool): Save figure to disk.
    """
    # TODO: Extract feature_importances_, sort, and plot top_n as a horizontal bar chart.
    pass


# ---------------------------------------------------------------------------
# Step 7: Main Pipeline
# ---------------------------------------------------------------------------
def main():
    """Run the complete house price prediction pipeline."""
    print("Step 1: Loading dataset...")
    df = load_dataset()

    print("Step 2: Exploring data...")
    explore_data(df)

    print("Step 3: Cleaning data...")
    df = clean_data(df)

    print("Step 4: Engineering features...")
    df, numerical_cols, categorical_cols = engineer_features(df)

    # Separate features and target
    target = "SalePrice"
    X = df.drop(columns=[target])
    y = df[target]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
    )

    print("Step 5: Building preprocessor...")
    preprocessor = build_preprocessor(numerical_cols, categorical_cols)

    print("Step 6: Training models...")
    models = build_models()
    results_df, best_pipeline = train_and_evaluate(
        models, preprocessor, X_train, X_test, y_train, y_test
    )

    print("Step 7: Tuning best model...")
    # TODO: Call tune_best_model.

    print("Step 8: Final evaluation and plots...")
    # TODO: Generate predictions with best model.
    # TODO: Call plot_residuals, plot_predicted_vs_actual, plot_feature_importance.

    print("Pipeline complete. Figures saved to:", FIGURES_DIR)


if __name__ == "__main__":
    main()
