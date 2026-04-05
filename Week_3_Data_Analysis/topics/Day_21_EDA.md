# Day 21: Exploratory Data Analysis (EDA) — Full Walkthrough

## Introduction

Exploratory Data Analysis (EDA) is the process of analyzing datasets to summarize
their main characteristics, often using visual methods. It is the critical first step
in any data science project. EDA helps you understand the data, discover patterns,
spot anomalies, test hypotheses, and guide feature engineering.

This lesson walks through a complete EDA workflow using everything from Week 3.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style='whitegrid')
```

---

## 1. The EDA Framework

A systematic EDA follows these stages:

1. **Load and Inspect** — understand the structure
2. **Univariate Analysis** — examine each variable individually
3. **Bivariate Analysis** — examine relationships between pairs of variables
4. **Multivariate Analysis** — examine interactions among multiple variables
5. **Data Quality Assessment** — identify and handle issues
6. **Summary and Hypotheses** — document findings

---

## 2. Stage 1: Load and Inspect

```python
# Load the dataset
df = pd.read_csv('housing.csv')

# Basic shape and types
print(f"Shape: {df.shape}")
print(f"\nColumn types:\n{df.dtypes}")

# First look
df.head()
df.tail()
df.sample(5)

# Comprehensive summary
df.info()

# Statistical summary
df.describe()                       # numeric columns
df.describe(include='object')       # categorical columns
df.describe(include='all')          # everything
```

### Understanding Each Column

```python
# Identify column types
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

print(f"Numeric columns ({len(numeric_cols)}): {numeric_cols}")
print(f"Categorical columns ({len(categorical_cols)}): {categorical_cols}")

# Unique values per column
for col in df.columns:
    n_unique = df[col].nunique()
    print(f"{col}: {n_unique} unique values")
```

### Missing Value Overview

```python
def missing_value_report(df):
    """Generate a comprehensive missing value report."""
    missing = df.isnull().sum()
    missing_pct = df.isnull().mean() * 100
    report = pd.DataFrame({
        'Missing Count': missing,
        'Missing %': missing_pct.round(2),
        'Dtype': df.dtypes
    })
    report = report[report['Missing Count'] > 0].sort_values(
        'Missing %', ascending=False
    )
    return report

print(missing_value_report(df))
```

### Visualize Missing Patterns

```python
fig, ax = plt.subplots(figsize=(12, 6))
missing_pct = df.isnull().mean() * 100
missing_pct = missing_pct[missing_pct > 0].sort_values(ascending=False)

if len(missing_pct) > 0:
    missing_pct.plot(kind='bar', color='salmon', ax=ax)
    ax.set_title('Missing Value Percentage by Column')
    ax.set_ylabel('Percentage Missing')
    ax.axhline(y=50, color='red', linestyle='--', label='50% threshold')
    ax.legend()
plt.tight_layout()
plt.show()
```

---

## 3. Stage 2: Univariate Analysis

Examine each variable individually to understand its distribution and characteristics.

### Numeric Variables

```python
def plot_numeric_distributions(df, numeric_cols, cols_per_row=3):
    """Plot histograms and box plots for all numeric columns."""
    n_cols = len(numeric_cols)
    n_rows = (n_cols + cols_per_row - 1) // cols_per_row

    # Histograms
    fig, axes = plt.subplots(n_rows, cols_per_row, figsize=(5 * cols_per_row, 4 * n_rows))
    axes = axes.flatten() if n_cols > 1 else [axes]

    for i, col in enumerate(numeric_cols):
        sns.histplot(df[col].dropna(), kde=True, ax=axes[i], color='steelblue')
        axes[i].set_title(f'{col}')
        # Add mean and median lines
        axes[i].axvline(df[col].mean(), color='red', linestyle='--', label='Mean')
        axes[i].axvline(df[col].median(), color='green', linestyle='-', label='Median')
        axes[i].legend(fontsize=8)

    # Hide unused axes
    for j in range(i + 1, len(axes)):
        axes[j].set_visible(False)

    fig.suptitle('Numeric Variable Distributions', fontsize=14)
    plt.tight_layout()
    plt.show()

plot_numeric_distributions(df, numeric_cols)
```

### Skewness Check

```python
skewness = df[numeric_cols].skew().sort_values(ascending=False)
print("Skewness:\n", skewness)
# |skew| > 1  => highly skewed, consider transformation
# |skew| > 0.5 => moderately skewed

# Visualize highly skewed columns with and without log transform
highly_skewed = skewness[abs(skewness) > 1].index.tolist()

if highly_skewed:
    fig, axes = plt.subplots(len(highly_skewed), 2,
                             figsize=(12, 4 * len(highly_skewed)))
    if len(highly_skewed) == 1:
        axes = axes.reshape(1, -1)

    for i, col in enumerate(highly_skewed):
        # Original
        sns.histplot(df[col].dropna(), kde=True, ax=axes[i, 0])
        axes[i, 0].set_title(f'{col} (Original, skew={df[col].skew():.2f})')

        # Log-transformed
        log_vals = np.log1p(df[col].dropna())
        sns.histplot(log_vals, kde=True, ax=axes[i, 1], color='orange')
        axes[i, 1].set_title(f'{col} (Log-transformed, skew={log_vals.skew():.2f})')

    plt.tight_layout()
    plt.show()
```

### Categorical Variables

```python
def plot_categorical_distributions(df, categorical_cols, max_categories=15):
    """Plot bar charts for all categorical columns."""
    for col in categorical_cols:
        n_unique = df[col].nunique()
        if n_unique > max_categories:
            print(f"Skipping {col} ({n_unique} categories — too many to plot)")
            continue

        fig, ax = plt.subplots(figsize=(8, 4))
        order = df[col].value_counts().index
        sns.countplot(data=df, x=col, order=order, ax=ax, color='steelblue')
        ax.set_title(f'{col} — Value Counts')
        ax.tick_params(axis='x', rotation=45)

        # Add count labels
        for p in ax.patches:
            ax.annotate(f'{int(p.get_height())}',
                       (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='bottom', fontsize=9)
        plt.tight_layout()
        plt.show()

plot_categorical_distributions(df, categorical_cols)
```

---

## 4. Stage 3: Bivariate Analysis

Examine relationships between pairs of variables.

### Numeric vs Numeric — Correlation

```python
# Correlation matrix
corr = df[numeric_cols].corr()

# Heatmap
fig, ax = plt.subplots(figsize=(10, 8))
mask = np.triu(np.ones_like(corr, dtype=bool))  # upper triangle mask
sns.heatmap(corr, mask=mask, annot=True, fmt='.2f', cmap='coolwarm',
            center=0, square=True, linewidths=0.5)
ax.set_title('Correlation Matrix (Lower Triangle)')
plt.tight_layout()
plt.show()

# Find highly correlated pairs
def find_high_correlations(corr_matrix, threshold=0.7):
    """Find pairs of variables with correlation above threshold."""
    pairs = []
    cols = corr_matrix.columns
    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            if abs(corr_matrix.iloc[i, j]) >= threshold:
                pairs.append((cols[i], cols[j], corr_matrix.iloc[i, j]))
    return sorted(pairs, key=lambda x: abs(x[2]), reverse=True)

high_corr = find_high_correlations(corr, threshold=0.7)
for c1, c2, r in high_corr:
    print(f"{c1} <-> {c2}: r = {r:.3f}")
```

### Scatter Plots for Key Relationships

```python
# If there is a target variable (e.g., 'price')
target = 'price'  # adjust to your dataset

if target in numeric_cols:
    features = [c for c in numeric_cols if c != target]
    n = len(features)
    cols_per_row = 3
    rows = (n + cols_per_row - 1) // cols_per_row

    fig, axes = plt.subplots(rows, cols_per_row, figsize=(5 * cols_per_row, 4 * rows))
    axes = axes.flatten()

    for i, feat in enumerate(features):
        sns.scatterplot(data=df, x=feat, y=target, alpha=0.4, ax=axes[i], s=15)
        axes[i].set_title(f'{target} vs {feat}')

    for j in range(i + 1, len(axes)):
        axes[j].set_visible(False)

    plt.tight_layout()
    plt.show()
```

### Numeric vs Categorical

```python
def plot_numeric_by_category(df, numeric_col, categorical_cols):
    """Box plots of a numeric variable split by each categorical variable."""
    for cat_col in categorical_cols:
        if df[cat_col].nunique() > 10:
            continue
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.boxplot(data=df, x=cat_col, y=numeric_col, ax=ax)
        ax.set_title(f'{numeric_col} by {cat_col}')
        ax.tick_params(axis='x', rotation=45)
        plt.tight_layout()
        plt.show()

# Example usage:
# plot_numeric_by_category(df, 'price', categorical_cols)
```

---

## 5. Stage 4: Multivariate Analysis

### Pair Plot

```python
# Select a subset of key variables to avoid overwhelming the plot
key_vars = numeric_cols[:5]  # adjust based on your dataset

if len(categorical_cols) > 0:
    sns.pairplot(df[key_vars + [categorical_cols[0]]].dropna(),
                 hue=categorical_cols[0], diag_kind='kde', height=2.5)
else:
    sns.pairplot(df[key_vars].dropna(), diag_kind='kde', height=2.5)

plt.suptitle('Pairwise Relationships', y=1.02)
plt.show()
```

### Grouped Aggregations

```python
if len(categorical_cols) >= 2:
    pivot = df.pivot_table(
        values=numeric_cols[0],
        index=categorical_cols[0],
        columns=categorical_cols[1],
        aggfunc='mean'
    )

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(pivot, annot=True, fmt='.1f', cmap='YlOrRd')
    ax.set_title(f'Mean {numeric_cols[0]} by {categorical_cols[0]} and {categorical_cols[1]}')
    plt.tight_layout()
    plt.show()
```

---

## 6. Stage 5: Data Quality Assessment

### Outlier Detection Summary

```python
def outlier_report(df, numeric_cols):
    """IQR-based outlier report for all numeric columns."""
    report = []
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        n_outliers = ((df[col] < lower) | (df[col] > upper)).sum()
        pct = n_outliers / len(df) * 100
        report.append({
            'Column': col,
            'Lower Bound': round(lower, 2),
            'Upper Bound': round(upper, 2),
            'Outlier Count': n_outliers,
            'Outlier %': round(pct, 2)
        })
    return pd.DataFrame(report).sort_values('Outlier %', ascending=False)

print(outlier_report(df, numeric_cols))
```

### Duplicate Check

```python
n_duplicates = df.duplicated().sum()
print(f"Exact duplicate rows: {n_duplicates} ({n_duplicates/len(df)*100:.1f}%)")
```

---

## 7. Stage 6: Summary and Hypotheses

After completing the analysis, document your findings.

```python
def eda_summary(df):
    """Print a concise EDA summary."""
    print("=" * 60)
    print("EDA SUMMARY")
    print("=" * 60)
    print(f"Dataset shape: {df.shape[0]} rows x {df.shape[1]} columns")
    print(f"Numeric columns: {len(df.select_dtypes(include=[np.number]).columns)}")
    print(f"Categorical columns: {len(df.select_dtypes(include=['object']).columns)}")
    print(f"Total missing values: {df.isnull().sum().sum()}")
    print(f"Duplicate rows: {df.duplicated().sum()}")
    print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    print("=" * 60)

eda_summary(df)
```

### Typical Findings to Document

- **Data shape**: How many rows and columns? Is the dataset large enough?
- **Missing values**: Which columns? How much? Random or systematic?
- **Distributions**: Which variables are skewed? Any need for transformation?
- **Outliers**: How many? In which columns? Errors or legitimate extremes?
- **Correlations**: Which features are strongly correlated? Any multicollinearity?
- **Key relationships**: Which features are most related to the target variable?
- **Data quality issues**: Incorrect types, invalid values, inconsistent categories?

---

## 8. Complete EDA Template Function

```python
def full_eda(df, target=None):
    """
    Run a complete EDA on a DataFrame.

    Parameters:
        df: pandas DataFrame
        target: str, optional target variable name
    """
    print("=" * 60)
    print("STEP 1: DATA OVERVIEW")
    print("=" * 60)
    print(f"Shape: {df.shape}")
    print(f"\nData types:\n{df.dtypes}\n")
    print(f"First 5 rows:\n{df.head()}\n")

    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

    # Missing values
    print("=" * 60)
    print("STEP 2: MISSING VALUES")
    print("=" * 60)
    missing = df.isnull().sum()
    if missing.sum() > 0:
        print(missing[missing > 0].sort_values(ascending=False))
    else:
        print("No missing values!")

    # Duplicates
    print(f"\nDuplicate rows: {df.duplicated().sum()}")

    # Statistics
    print("\n" + "=" * 60)
    print("STEP 3: DESCRIPTIVE STATISTICS")
    print("=" * 60)
    print(df.describe())

    # Distributions
    print("\n" + "=" * 60)
    print("STEP 4: DISTRIBUTIONS")
    print("=" * 60)

    # Numeric distributions
    if numeric_cols:
        n = len(numeric_cols)
        rows = (n + 2) // 3
        fig, axes = plt.subplots(rows, 3, figsize=(15, 4 * rows))
        axes = axes.flatten() if n > 1 else [axes]
        for i, col in enumerate(numeric_cols):
            sns.histplot(df[col].dropna(), kde=True, ax=axes[i])
            axes[i].set_title(col)
        for j in range(i + 1, len(axes)):
            axes[j].set_visible(False)
        plt.suptitle('Numeric Distributions', fontsize=14)
        plt.tight_layout()
        plt.show()

    # Correlation
    if len(numeric_cols) >= 2:
        print("\n" + "=" * 60)
        print("STEP 5: CORRELATIONS")
        print("=" * 60)
        fig, ax = plt.subplots(figsize=(10, 8))
        corr = df[numeric_cols].corr()
        mask = np.triu(np.ones_like(corr, dtype=bool))
        sns.heatmap(corr, mask=mask, annot=True, fmt='.2f', cmap='coolwarm',
                    center=0, ax=ax)
        ax.set_title('Correlation Matrix')
        plt.tight_layout()
        plt.show()

    # Target analysis
    if target and target in df.columns:
        print("\n" + "=" * 60)
        print(f"STEP 6: TARGET VARIABLE — {target}")
        print("=" * 60)
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.histplot(df[target].dropna(), kde=True, ax=ax)
        ax.set_title(f'Distribution of {target}')
        plt.show()

        # Top correlations with target
        if target in numeric_cols:
            target_corr = corr[target].drop(target).abs().sort_values(ascending=False)
            print(f"\nTop correlations with {target}:")
            print(target_corr)

    print("\n" + "=" * 60)
    print("EDA COMPLETE")
    print("=" * 60)

# Usage:
# full_eda(df, target='price')
```

---

## 9. EDA Best Practices

1. **Start broad, then narrow down.** Overview first, details later.
2. **Visualize everything.** Numbers alone can be misleading (Anscombe's quartet).
3. **Ask questions.** EDA is hypothesis-driven exploration.
4. **Document findings.** Write notes as you go, not after.
5. **Iterate.** EDA is not linear — you will revisit earlier steps.
6. **Know your domain.** Statistical outliers may be domain-specific normal values.
7. **Do not over-clean.** Understand patterns before removing data.
8. **Check for data leakage.** Features that perfectly predict the target may
   encode future information.

---

## 10. Common EDA Mistakes

- **Skipping EDA entirely** and jumping to modeling.
- **Only looking at summary statistics** without visualizing.
- **Ignoring missing value patterns** (they may be informative).
- **Treating all outliers as errors** (some are genuine extreme values).
- **Not checking for duplicates** (they inflate model performance).
- **Applying the same cleaning to train and test sets independently** (should
  fit on train, transform on test).

---

## Key Takeaways

- EDA is the most important step in any data science project.
- Follow a structured framework: inspect, univariate, bivariate, multivariate,
  quality check, summary.
- Combine statistical summaries with visualizations for a complete picture.
- Build reusable EDA functions to speed up your workflow.
- Document findings and hypotheses to guide feature engineering and modeling.
- The tools from Days 15-20 (NumPy, Pandas, Matplotlib, Seaborn) all come together
  during EDA.

---

*Congratulations! You have completed Week 3: Data Analysis and Visualization.*
