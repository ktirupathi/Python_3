# Day 18: Data Cleaning — Missing Values, Duplicates, Outliers

## Introduction

Real-world data is messy. Before any analysis or modeling, you must clean your data.
Data cleaning typically consumes 60-80% of a data scientist's time. This lesson covers
the three most common data quality issues: missing values, duplicates, and outliers,
along with systematic strategies to handle each.

```python
import pandas as pd
import numpy as np
```

---

## 1. Understanding Your Data First

Before cleaning, always start with an exploratory check.

```python
df = pd.read_csv('data.csv')

# Shape and types
df.shape                    # (rows, columns)
df.dtypes                   # column data types
df.info()                   # types + non-null counts + memory

# Quick look
df.head()
df.tail()
df.sample(5)

# Missing value summary
df.isnull().sum()           # count of NaN per column
df.isnull().mean() * 100    # percentage missing per column

# Unique values
df.nunique()                # unique value count per column
df.describe()               # statistics for numeric columns
df.describe(include='object')  # statistics for string columns
```

---

## 2. Missing Values

Missing values appear as `NaN` (Not a Number) in Pandas and can arise from data
collection errors, sensor failures, optional survey fields, or merge operations.

### Detecting Missing Values

```python
df = pd.DataFrame({
    'name': ['Alice', 'Bob', None, 'Diana', 'Eve'],
    'age': [25, np.nan, 35, 28, np.nan],
    'salary': [70000, 80000, np.nan, 75000, 65000],
    'dept': ['Eng', 'Mkt', 'Eng', None, 'HR']
})

df.isnull()             # boolean DataFrame of NaN locations
df.notnull()            # inverse of isnull
df.isnull().sum()       # count per column
df.isnull().any()       # True if column has any NaN
df.isnull().sum().sum() # total NaN count across entire DataFrame

# Rows with any missing value
df[df.isnull().any(axis=1)]

# Columns with missing values
cols_with_missing = df.columns[df.isnull().any()].tolist()
```

### Strategy 1: Drop Missing Values

Use when the percentage of missing data is small (< 5%) or when the rows/columns
are not important.

```python
# Drop rows with ANY NaN
df.dropna()

# Drop rows where ALL values are NaN
df.dropna(how='all')

# Drop rows with NaN in specific columns
df.dropna(subset=['name', 'salary'])

# Drop columns with any NaN
df.dropna(axis=1)

# Drop columns where more than 50% of values are missing
threshold = len(df) * 0.5
df.dropna(axis=1, thresh=threshold)
```

### Strategy 2: Fill Missing Values (Imputation)

```python
# Fill with a constant
df['age'].fillna(0)
df['dept'].fillna('Unknown')

# Fill with the mean/median (for numeric columns)
df['age'].fillna(df['age'].mean())
df['salary'].fillna(df['salary'].median())

# Fill with the mode (for categorical columns)
df['dept'].fillna(df['dept'].mode()[0])

# Forward fill (use previous value)
df['age'].fillna(method='ffill')

# Backward fill (use next value)
df['age'].fillna(method='bfill')

# Interpolation (for time series or ordered data)
df['age'].interpolate(method='linear')

# Group-based imputation (more accurate)
df['salary'] = df.groupby('dept')['salary'].transform(
    lambda x: x.fillna(x.median())
)
```

### Strategy 3: Flag Missing Values

Sometimes the fact that a value is missing is itself informative.

```python
df['age_missing'] = df['age'].isnull().astype(int)
df['age'].fillna(df['age'].median(), inplace=True)
```

### Choosing the Right Strategy

| Situation                        | Recommended Approach               |
|----------------------------------|------------------------------------|
| < 5% missing, random            | Drop the rows                      |
| Numeric, roughly symmetric      | Fill with mean                     |
| Numeric, skewed                 | Fill with median                   |
| Categorical                     | Fill with mode or "Unknown"        |
| Time series                     | Forward fill or interpolation      |
| Feature is > 50% missing        | Drop the column                    |
| Missingness is informative      | Create a flag column, then impute  |

---

## 3. Duplicates

Duplicate rows inflate your dataset and can skew analysis results.

### Detecting Duplicates

```python
df = pd.DataFrame({
    'id': [1, 2, 3, 2, 4, 3],
    'name': ['Alice', 'Bob', 'Charlie', 'Bob', 'Diana', 'Charlie'],
    'score': [90, 85, 92, 85, 88, 92]
})

# Check for exact duplicate rows
df.duplicated()              # boolean Series (True for duplicate rows)
df.duplicated().sum()        # count of duplicates
df[df.duplicated()]          # view duplicated rows

# Keep first or last occurrence
df.duplicated(keep='first')  # marks all but first occurrence
df.duplicated(keep='last')   # marks all but last occurrence
df.duplicated(keep=False)    # marks ALL duplicate rows

# Check duplicates on specific columns
df.duplicated(subset=['name'])
df.duplicated(subset=['id', 'name'])
```

### Removing Duplicates

```python
# Remove exact duplicates (keep first occurrence)
df.drop_duplicates()

# Remove duplicates based on specific columns
df.drop_duplicates(subset=['id'])
df.drop_duplicates(subset=['name'], keep='last')

# Reset index after dropping
df.drop_duplicates().reset_index(drop=True)
```

### Handling Near-Duplicates

Sometimes duplicates are not exact but fuzzy (e.g., "New York" vs "new york").

```python
# Standardize text before checking
df['name_clean'] = df['name'].str.lower().str.strip()
df.drop_duplicates(subset=['name_clean'])

# For numeric near-duplicates, round before checking
df['score_rounded'] = df['score'].round(-1)  # round to nearest 10
```

---

## 4. Data Type Issues

Incorrect data types cause subtle bugs and prevent operations.

```python
# Check types
df.dtypes

# Common conversions
df['age'] = df['age'].astype(int)
df['price'] = df['price'].astype(float)
df['date'] = pd.to_datetime(df['date'])
df['category'] = df['category'].astype('category')  # saves memory

# Handle errors in conversion
df['price'] = pd.to_numeric(df['price'], errors='coerce')  # invalid -> NaN
df['date'] = pd.to_datetime(df['date'], errors='coerce')
```

---

## 5. Outliers

Outliers are data points that are significantly different from the rest. They can be
legitimate extreme values or errors. Detecting and handling them depends on context.

### Detection Method 1: Z-Score

A Z-score measures how many standard deviations a point is from the mean.
Typically, |Z| > 3 is considered an outlier.

```python
from scipy import stats

df = pd.DataFrame({
    'salary': [50000, 52000, 48000, 51000, 49000, 500000, 47000]
})

# Calculate Z-scores
z_scores = np.abs(stats.zscore(df['salary']))
outlier_mask = z_scores > 3
print(df[outlier_mask])  # salary of 500000

# Or without scipy
mean = df['salary'].mean()
std = df['salary'].std()
z_scores = np.abs((df['salary'] - mean) / std)
```

### Detection Method 2: IQR (Interquartile Range)

More robust than Z-scores because it is not affected by extreme values.

```python
Q1 = df['salary'].quantile(0.25)
Q3 = df['salary'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['salary'] < lower_bound) | (df['salary'] > upper_bound)]
print(f"Found {len(outliers)} outliers")
print(f"Bounds: [{lower_bound:.0f}, {upper_bound:.0f}]")
```

### Detection Method 3: Domain Knowledge

Sometimes outliers are best identified by domain rules.

```python
# Age cannot be negative or > 120
df = df[(df['age'] >= 0) & (df['age'] <= 120)]

# Temperature outlier for a city in degrees Celsius
df = df[(df['temp'] >= -50) & (df['temp'] <= 60)]
```

### Handling Outliers

```python
# Option 1: Remove them
df_clean = df[(df['salary'] >= lower_bound) & (df['salary'] <= upper_bound)]

# Option 2: Cap/clip them (Winsorization)
df['salary'] = df['salary'].clip(lower=lower_bound, upper=upper_bound)

# Option 3: Log transformation (reduces the impact of extreme values)
df['salary_log'] = np.log1p(df['salary'])  # log1p handles zero values

# Option 4: Replace with NaN, then impute
df.loc[z_scores > 3, 'salary'] = np.nan
df['salary'].fillna(df['salary'].median(), inplace=True)

# Option 5: Binning (discretization)
df['salary_bin'] = pd.cut(df['salary'], bins=5, labels=False)
```

---

## 6. String Cleaning

Text data often requires extensive cleaning.

```python
df = pd.DataFrame({
    'name': ['  Alice ', 'BOB', 'charlie', ' Diana  '],
    'email': ['alice@test.com', 'BOB@TEST.COM', 'invalid', 'diana@test.com'],
    'phone': ['123-456-7890', '(123) 456-7890', '1234567890', 'N/A']
})

# Strip whitespace
df['name'] = df['name'].str.strip()

# Standardize case
df['name'] = df['name'].str.title()  # 'Alice', 'Bob', 'Charlie', 'Diana'
df['email'] = df['email'].str.lower()

# Replace patterns
df['phone'] = df['phone'].str.replace(r'[^\d]', '', regex=True)  # keep digits only

# Validate patterns
email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
df['valid_email'] = df['email'].str.match(email_pattern)

# Replace invalid values
df.loc[~df['valid_email'], 'email'] = np.nan
```

---

## 7. Putting It All Together — A Cleaning Pipeline

```python
def clean_dataframe(df):
    """Standard data cleaning pipeline."""
    # 1. Make a copy
    df = df.copy()

    # 2. Standardize column names
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # 3. Remove exact duplicates
    initial_rows = len(df)
    df = df.drop_duplicates()
    print(f"Removed {initial_rows - len(df)} duplicate rows")

    # 4. Fix data types
    for col in df.select_dtypes(include='object'):
        df[col] = df[col].str.strip()
        # Try to convert to numeric
        converted = pd.to_numeric(df[col], errors='coerce')
        if converted.notna().sum() > len(df) * 0.5:
            df[col] = converted

    # 5. Handle missing values
    missing_pct = df.isnull().mean() * 100
    # Drop columns with > 50% missing
    cols_to_drop = missing_pct[missing_pct > 50].index
    df = df.drop(columns=cols_to_drop)
    print(f"Dropped columns: {list(cols_to_drop)}")

    # Fill numeric with median, categorical with mode
    for col in df.select_dtypes(include=[np.number]):
        df[col] = df[col].fillna(df[col].median())
    for col in df.select_dtypes(include='object'):
        df[col] = df[col].fillna(df[col].mode()[0])

    # 6. Handle outliers (IQR method for numeric columns)
    for col in df.select_dtypes(include=[np.number]):
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        df[col] = df[col].clip(lower, upper)

    return df

# Usage
# df_clean = clean_dataframe(df_raw)
```

---

## 8. Data Validation After Cleaning

Always verify your cleaning steps did not introduce new problems.

```python
def validate_cleaned_data(df):
    """Run basic checks on cleaned data."""
    assert df.isnull().sum().sum() == 0, "Still has missing values!"
    assert df.duplicated().sum() == 0, "Still has duplicates!"
    print(f"Shape: {df.shape}")
    print(f"Data types:\n{df.dtypes}")
    print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024:.1f} KB")
    print("Validation passed!")
```

---

## Key Takeaways

- Always explore data with `info()`, `describe()`, `isnull().sum()` before cleaning.
- Missing values: drop, fill (mean/median/mode), interpolate, or flag depending on
  the situation.
- Duplicates: detect with `duplicated()`, remove with `drop_duplicates()`.
- Outliers: use IQR or Z-scores for detection; remove, cap, transform, or bin.
- String data needs whitespace trimming, case standardization, and validation.
- Build a reusable cleaning pipeline and always validate after cleaning.
- Document your cleaning decisions — they affect downstream analysis.

---

*Next: Day 19 — Matplotlib: Creating Publication-Quality Visualizations.*
