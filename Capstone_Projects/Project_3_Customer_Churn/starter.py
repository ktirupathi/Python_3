"""
Capstone Project 3: Customer Churn Prediction
===============================================
Binary classification pipeline for telecom customer churn.

Usage:
    python starter.py
"""

import os
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, roc_curve, confusion_matrix, classification_report,
    precision_recall_curve,
)

warnings.filterwarnings("ignore")

DATA_URL = (
    "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/"
    "master/data/Telco-Customer-Churn.csv"
)

FIGURES_DIR = os.path.join(os.path.dirname(__file__), "figures")
os.makedirs(FIGURES_DIR, exist_ok=True)

RANDOM_STATE = 42
TEST_SIZE = 0.2


# ---------------------------------------------------------------------------
# Step 1: Load and Inspect
# ---------------------------------------------------------------------------
def load_data():
    """Load the Telco Customer Churn dataset.

    Returns:
        pd.DataFrame: Raw dataset.
    """
    # TODO: Read CSV from DATA_URL.
    # TODO: Convert TotalCharges to numeric (handle empty strings with pd.to_numeric, errors='coerce').
    # TODO: Drop customerID column.
    # TODO: Drop rows with NaN in TotalCharges.
    pass


def inspect_data(df):
    """Print summary information about the dataset.

    Args:
        df (pd.DataFrame): Dataset to inspect.
    """
    # TODO: Print shape, dtypes, describe(), value_counts for Churn.
    pass


# ---------------------------------------------------------------------------
# Step 2: Exploratory Data Analysis
# ---------------------------------------------------------------------------
def plot_churn_distribution(df, save=True):
    """Bar chart showing the overall churn rate."""
    fig, ax = plt.subplots(figsize=(6, 4))
    # TODO: Plot value counts of Churn column.
    ax.set_title("Customer Churn Distribution")
    plt.tight_layout()
    if save:
        fig.savefig(os.path.join(FIGURES_DIR, "churn_distribution.png"), dpi=150)
    plt.show()


def plot_churn_by_contract(df, save=True):
    """Grouped bar chart: churn rate by contract type."""
    fig, ax = plt.subplots(figsize=(8, 5))
    # TODO: Group by Contract and Churn, plot grouped bar chart.
    ax.set_title("Churn Rate by Contract Type")
    plt.tight_layout()
    if save:
        fig.savefig(os.path.join(FIGURES_DIR, "churn_by_contract.png"), dpi=150)
    plt.show()


def plot_tenure_distribution(df, save=True):
    """Overlapping KDE plots of tenure for churned vs. retained."""
    fig, ax = plt.subplots(figsize=(8, 5))
    # TODO: Plot KDE of tenure for Churn=Yes and Churn=No.
    ax.set_title("Tenure Distribution by Churn Status")
    ax.set_xlabel("Tenure (months)")
    ax.legend()
    plt.tight_layout()
    if save:
        fig.savefig(os.path.join(FIGURES_DIR, "tenure_distribution.png"), dpi=150)
    plt.show()


def plot_correlation_heatmap(df, save=True):
    """Heatmap of correlations among numerical features."""
    fig, ax = plt.subplots(figsize=(10, 8))
    # TODO: Select numeric columns, compute correlation matrix, plot with sns.heatmap.
    ax.set_title("Feature Correlation Heatmap")
    plt.tight_layout()
    if save:
        fig.savefig(os.path.join(FIGURES_DIR, "correlation_heatmap.png"), dpi=150)
    plt.show()


# ---------------------------------------------------------------------------
# Step 3: Data Preprocessing
# ---------------------------------------------------------------------------
def preprocess(df):
    """Encode categorical variables and prepare feature/target arrays.

    Args:
        df (pd.DataFrame): Cleaned dataset.

    Returns:
        tuple: (X, y, numerical_cols, categorical_cols)
    """
    # TODO: Encode target: Churn Yes=1, No=0.
    # TODO: Identify binary columns and encode as 0/1.
    # TODO: Identify multi-class categoricals for one-hot encoding.
    # TODO: Separate X and y.
    # TODO: Return X, y, and column lists.
    pass


def build_preprocessor(numerical_cols, categorical_cols):
    """Construct a ColumnTransformer for the pipeline.

    Returns:
        ColumnTransformer
    """
    numerical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])

    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
    ])

    return ColumnTransformer([
        ("num", numerical_pipeline, numerical_cols),
        ("cat", categorical_pipeline, categorical_cols),
    ])


# ---------------------------------------------------------------------------
# Step 4: Modeling
# ---------------------------------------------------------------------------
def build_models():
    """Return a dictionary of classifiers to compare.

    Returns:
        dict[str, object]
    """
    return {
        "Logistic Regression": LogisticRegression(
            max_iter=1000, class_weight="balanced", random_state=RANDOM_STATE
        ),
        "Random Forest": RandomForestClassifier(
            n_estimators=200, class_weight="balanced", random_state=RANDOM_STATE
        ),
        "Gradient Boosting": GradientBoostingClassifier(
            n_estimators=200, learning_rate=0.1, random_state=RANDOM_STATE
        ),
        "SVM": SVC(
            kernel="rbf", class_weight="balanced", probability=True,
            random_state=RANDOM_STATE
        ),
    }


def train_and_evaluate(models, preprocessor, X_train, X_test, y_train, y_test):
    """Train models and collect classification metrics.

    Args:
        models (dict): Name -> estimator.
        preprocessor (ColumnTransformer): Feature preprocessor.
        X_train, X_test, y_train, y_test: Data splits.

    Returns:
        tuple: (results_df, best_pipeline, all_pipelines)
    """
    results = []
    pipelines = {}
    best_pipeline = None
    best_f1 = 0.0

    for name, model in models.items():
        pipe = Pipeline([
            ("preprocessor", preprocessor),
            ("model", model),
        ])

        # TODO: Fit the pipeline.
        # TODO: Generate predictions and predicted probabilities.
        # TODO: Compute accuracy, precision, recall, f1, auc_roc.
        # TODO: Store the pipeline in pipelines dict.
        # TODO: Track the best model by F1 score.
        # TODO: Append results to the list.
        pass

    results_df = pd.DataFrame(results)
    print("\n=== Model Comparison ===")
    print(results_df.to_string(index=False))
    return results_df, best_pipeline, pipelines


# ---------------------------------------------------------------------------
# Step 5: Evaluation Visualizations
# ---------------------------------------------------------------------------
def plot_confusion_matrix(y_test, y_pred, model_name="Model", save=True):
    """Heatmap of the confusion matrix."""
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax,
                xticklabels=["Retained", "Churned"],
                yticklabels=["Retained", "Churned"])
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    ax.set_title(f"Confusion Matrix -- {model_name}")
    plt.tight_layout()
    if save:
        fig.savefig(os.path.join(FIGURES_DIR, f"confusion_matrix_{model_name}.png"), dpi=150)
    plt.show()


def plot_roc_curves(pipelines, X_test, y_test, save=True):
    """Plot ROC curves for all models on the same axes."""
    fig, ax = plt.subplots(figsize=(8, 6))

    for name, pipe in pipelines.items():
        # TODO: Get predicted probabilities, compute FPR/TPR, plot ROC curve.
        pass

    ax.plot([0, 1], [0, 1], "k--", label="Random (AUC = 0.50)")
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.set_title("ROC Curves -- Model Comparison")
    ax.legend(loc="lower right")
    plt.tight_layout()
    if save:
        fig.savefig(os.path.join(FIGURES_DIR, "roc_curves.png"), dpi=150)
    plt.show()


def plot_precision_recall(pipeline, X_test, y_test, model_name="Model", save=True):
    """Precision-Recall curve for the best model."""
    fig, ax = plt.subplots(figsize=(8, 6))
    # TODO: Get predicted probabilities, compute precision/recall, plot.
    ax.set_xlabel("Recall")
    ax.set_ylabel("Precision")
    ax.set_title(f"Precision-Recall Curve -- {model_name}")
    plt.tight_layout()
    if save:
        fig.savefig(os.path.join(FIGURES_DIR, "precision_recall.png"), dpi=150)
    plt.show()


# ---------------------------------------------------------------------------
# Step 6: Feature Importance
# ---------------------------------------------------------------------------
def plot_feature_importance(pipeline, feature_names, top_n=15, save=True):
    """Bar chart of top feature importances.

    Args:
        pipeline (Pipeline): Fitted pipeline with a tree-based model.
        feature_names (list[str]): Feature names after preprocessing.
        top_n (int): Number of top features to show.
    """
    # TODO: Extract feature_importances_ from the model step.
    # TODO: Sort and plot as horizontal bar chart.
    pass


# ---------------------------------------------------------------------------
# Step 7: Threshold Optimization
# ---------------------------------------------------------------------------
def optimize_threshold(pipeline, X_test, y_test, save=True):
    """Find the decision threshold that maximizes F1-score.

    Args:
        pipeline: Fitted pipeline.
        X_test, y_test: Test data.

    Returns:
        float: Optimal threshold.
    """
    # TODO: Get predicted probabilities.
    # TODO: Loop over thresholds from 0.1 to 0.9 in steps of 0.01.
    # TODO: Compute F1-score at each threshold.
    # TODO: Plot threshold vs. F1.
    # TODO: Return the threshold with the highest F1.
    pass


# ---------------------------------------------------------------------------
# Main Pipeline
# ---------------------------------------------------------------------------
def main():
    """Run the full churn prediction pipeline."""
    print("Step 1: Loading data...")
    df = load_data()
    inspect_data(df)

    print("Step 2: Exploratory Data Analysis...")
    plot_churn_distribution(df)
    plot_churn_by_contract(df)
    plot_tenure_distribution(df)
    plot_correlation_heatmap(df)

    print("Step 3: Preprocessing...")
    X, y, numerical_cols, categorical_cols = preprocess(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )

    preprocessor = build_preprocessor(numerical_cols, categorical_cols)

    print("Step 4: Training models...")
    models = build_models()
    results_df, best_pipeline, all_pipelines = train_and_evaluate(
        models, preprocessor, X_train, X_test, y_train, y_test
    )

    print("Step 5: Evaluation visualizations...")
    plot_roc_curves(all_pipelines, X_test, y_test)
    # TODO: Call plot_confusion_matrix and plot_precision_recall for the best model.

    print("Step 6: Feature importance...")
    # TODO: Call plot_feature_importance.

    print("Step 7: Threshold optimization...")
    # TODO: Call optimize_threshold.

    print("Pipeline complete. Figures saved to:", FIGURES_DIR)


if __name__ == "__main__":
    main()
