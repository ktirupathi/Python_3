# Day 17: Pandas — Merging, Groupby, Pivot Tables, Time Series

## Introduction

Building on the fundamentals from Day 16, today we explore the powerful data
transformation capabilities that make Pandas indispensable for data analysis:
combining datasets, aggregating data by groups, reshaping tables, and working with
time-series data.

```python
import pandas as pd
import numpy as np
```

---

## 1. Combining DataFrames — concat

`pd.concat` stacks DataFrames vertically or horizontally.

```python
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

# Vertical stacking (row-wise) — default axis=0
combined = pd.concat([df1, df2], ignore_index=True)
#    A  B
# 0  1  3
# 1  2  4
# 2  5  7
# 3  6  8

# Horizontal stacking (column-wise)
pd.concat([df1, df2], axis=1)

# Handling mismatched columns
df3 = pd.DataFrame({'A': [9], 'C': [10]})
pd.concat([df1, df3], ignore_index=True)
# Columns A, B, C — missing values filled with NaN
```

---

## 2. Merging DataFrames — merge

`pd.merge` performs SQL-style joins between two DataFrames.

### Merge Types

```python
orders = pd.DataFrame({
    'order_id': [1, 2, 3, 4],
    'customer_id': [101, 102, 103, 104],
    'amount': [250, 150, 300, 200]
})

customers = pd.DataFrame({
    'customer_id': [101, 102, 103, 105],
    'name': ['Alice', 'Bob', 'Charlie', 'Eve']
})

# Inner join (default) — only matching rows
pd.merge(orders, customers, on='customer_id', how='inner')
# 3 rows (customer 104 and 105 excluded)

# Left join — keep all rows from the left DataFrame
pd.merge(orders, customers, on='customer_id', how='left')
# 4 rows — customer 104 has NaN for name

# Right join — keep all rows from the right DataFrame
pd.merge(orders, customers, on='customer_id', how='right')
# 4 rows — customer 105 has NaN for order fields

# Outer join — keep all rows from both
pd.merge(orders, customers, on='customer_id', how='outer')
# 5 rows — all customers and orders
```

### Merging on Different Column Names

```python
# When key columns have different names
pd.merge(orders, customers,
         left_on='customer_id', right_on='cust_id')
```

### Merging on Index

```python
pd.merge(df1, df2, left_index=True, right_index=True)
# Or use join()
df1.join(df2, how='inner')
```

### Handling Duplicate Column Names

```python
# Suffixes for overlapping column names (other than the key)
pd.merge(df1, df2, on='id', suffixes=('_left', '_right'))
```

### Merge Validation

```python
# Verify merge assumptions
pd.merge(orders, customers, on='customer_id', validate='many_to_one')
# Options: 'one_to_one', 'one_to_many', 'many_to_one', 'many_to_many'
```

---

## 3. Groupby — Split-Apply-Combine

`groupby()` is one of the most powerful tools in Pandas. It follows a three-step
process: split the data into groups, apply a function to each group, and combine
the results.

### Basic Groupby

```python
df = pd.DataFrame({
    'department': ['Sales', 'Sales', 'Engineering', 'Engineering', 'HR'],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'salary': [60000, 65000, 90000, 85000, 55000],
    'years': [3, 5, 7, 4, 2]
})

# Group by department, compute mean salary
df.groupby('department')['salary'].mean()
# department
# Engineering    87500
# HR             55000
# Sales          62500

# Multiple aggregations
df.groupby('department')['salary'].agg(['mean', 'min', 'max', 'count'])

# Group by multiple columns
df.groupby(['department', 'years'])['salary'].mean()
```

### Named Aggregations (clean output)

```python
result = df.groupby('department').agg(
    avg_salary=('salary', 'mean'),
    max_salary=('salary', 'max'),
    headcount=('name', 'count'),
    avg_years=('years', 'mean')
)
```

### Custom Aggregation Functions

```python
# Using a lambda
df.groupby('department')['salary'].agg(lambda x: x.max() - x.min())

# Using a named function
def salary_range(series):
    return series.max() - series.min()

df.groupby('department')['salary'].agg(salary_range)
```

### Transform — Apply and Broadcast Back

`transform` returns a result that has the same shape as the input, making it
useful for adding group-level computations back to the original DataFrame.

```python
# Z-score within each department
df['salary_zscore'] = df.groupby('department')['salary'].transform(
    lambda x: (x - x.mean()) / x.std()
)

# Percentage of department total
df['pct_of_dept'] = df.groupby('department')['salary'].transform(
    lambda x: x / x.sum() * 100
)
```

### Filter — Keep or Discard Entire Groups

```python
# Keep only departments with average salary > 60000
df.groupby('department').filter(lambda g: g['salary'].mean() > 60000)
```

---

## 4. Pivot Tables

Pivot tables reshape data from long to wide format, summarizing values.

```python
sales = pd.DataFrame({
    'date': ['2024-01', '2024-01', '2024-02', '2024-02', '2024-01', '2024-02'],
    'product': ['A', 'B', 'A', 'B', 'A', 'B'],
    'region': ['East', 'East', 'East', 'East', 'West', 'West'],
    'revenue': [100, 200, 150, 250, 120, 180]
})

# Basic pivot table
pd.pivot_table(sales,
               values='revenue',
               index='product',
               columns='region',
               aggfunc='sum')
# region    East  West
# product
# A          250   120
# B          450   180

# Multiple aggregation functions
pd.pivot_table(sales,
               values='revenue',
               index='product',
               columns='region',
               aggfunc=['sum', 'mean', 'count'],
               fill_value=0,
               margins=True)  # adds row/column totals
```

### Melt — Unpivot (Wide to Long)

```python
wide_df = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'math': [90, 85],
    'science': [88, 92],
    'english': [95, 78]
})

long_df = pd.melt(wide_df,
                   id_vars=['name'],
                   value_vars=['math', 'science', 'english'],
                   var_name='subject',
                   value_name='score')
#     name  subject  score
# 0  Alice     math     90
# 1    Bob     math     85
# 2  Alice  science     88
# ...
```

### Stack and Unstack

```python
# stack: columns -> index level (wide -> long)
# unstack: index level -> columns (long -> wide)
grouped = df.groupby(['department', 'name'])['salary'].sum()
grouped.unstack(fill_value=0)  # pivot 'name' to columns
```

---

## 5. Time Series in Pandas

Pandas has excellent support for time series data.

### Creating DateTime Objects

```python
# Parse strings to datetime
pd.to_datetime('2024-01-15')
pd.to_datetime(['2024-01-15', '2024-02-20', '2024-03-25'])

# Date ranges
dates = pd.date_range('2024-01-01', periods=365, freq='D')   # daily
months = pd.date_range('2024-01-01', periods=12, freq='MS')  # month start
business = pd.date_range('2024-01-01', periods=20, freq='B') # business days
```

### DatetimeIndex

```python
ts = pd.Series(np.random.randn(365),
               index=pd.date_range('2024-01-01', periods=365))

# Access components
ts.index.year
ts.index.month
ts.index.day_of_week   # Monday=0, Sunday=6
ts.index.quarter

# Slicing by date strings
ts['2024-03']            # all of March 2024
ts['2024-01':'2024-03']  # January through March
```

### Resampling — Changing Frequency

```python
# Daily to monthly
ts.resample('M').mean()         # monthly average
ts.resample('M').sum()          # monthly sum
ts.resample('M').agg(['mean', 'std', 'min', 'max'])

# Upsample (monthly to daily) with forward fill
monthly = ts.resample('M').mean()
monthly.resample('D').ffill()
```

### Rolling Windows

```python
# 7-day moving average
ts.rolling(window=7).mean()

# 30-day rolling standard deviation
ts.rolling(window=30).std()

# Exponential moving average (gives more weight to recent data)
ts.ewm(span=7).mean()
```

### Shifting and Differencing

```python
# Shift values forward or backward
ts.shift(1)        # shift values forward by 1 period (lag)
ts.shift(-1)       # shift values backward by 1 period (lead)

# Percentage change
ts.pct_change()    # (current - previous) / previous

# Differencing
ts.diff()          # current - previous
ts.diff(7)         # current - 7 periods ago (weekly diff for daily data)
```

### Practical Example: Stock Analysis

```python
# Simulating stock data
dates = pd.date_range('2023-01-01', periods=252, freq='B')
stock = pd.DataFrame({
    'close': 100 + np.random.randn(252).cumsum(),
    'volume': np.random.randint(1000, 10000, 252)
}, index=dates)

# 20-day and 50-day moving averages
stock['ma_20'] = stock['close'].rolling(20).mean()
stock['ma_50'] = stock['close'].rolling(50).mean()

# Daily returns
stock['returns'] = stock['close'].pct_change()

# Monthly average volume
stock['volume'].resample('M').mean()
```

---

## 6. apply, map, and applymap

```python
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# apply — works on a Series or along an axis of a DataFrame
df['A'].apply(lambda x: x ** 2)            # element-wise on Series
df.apply(lambda col: col.max() - col.min()) # column-wise on DataFrame
df.apply(lambda row: row.sum(), axis=1)     # row-wise on DataFrame

# map — element-wise on a Series (also accepts a dict for mapping)
df['A'].map({1: 'one', 2: 'two', 3: 'three'})

# applymap (renamed to map in Pandas 2.1+) — element-wise on DataFrame
df.map(lambda x: f"${x}")
```

---

## 7. Combining Operations — Method Chaining

Pandas supports method chaining for cleaner code.

```python
result = (
    df
    .query('salary > 50000')
    .groupby('department')
    .agg(avg_salary=('salary', 'mean'))
    .sort_values('avg_salary', ascending=False)
    .reset_index()
    .rename(columns={'avg_salary': 'Average Salary'})
)
```

---

## Key Takeaways

- Use `pd.merge` for SQL-style joins; choose the right join type for your use case.
- `groupby` + `agg` is the primary tool for summarizing data by categories.
- `transform` broadcasts group results back to the original shape.
- Pivot tables reshape data for cross-tabulation analysis.
- Pandas datetime support (parsing, resampling, rolling windows) makes time-series
  analysis straightforward.
- Method chaining leads to clean, readable data pipelines.
- `melt` converts wide data to long format; `pivot_table` does the reverse.

---

*Next: Day 18 — Data Cleaning: Missing Values, Duplicates, and Outliers.*
