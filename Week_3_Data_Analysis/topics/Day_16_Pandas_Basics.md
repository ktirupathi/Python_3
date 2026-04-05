# Day 16: Pandas — Series, DataFrames, Indexing, Selection

## Introduction

Pandas is the most widely used Python library for data manipulation and analysis. It
provides two primary data structures — **Series** (1D) and **DataFrame** (2D) — that
make working with structured, tabular data intuitive and efficient. Pandas is built on
top of NumPy and integrates seamlessly with visualization libraries and machine
learning tools.

```python
import pandas as pd
import numpy as np
```

---

## 1. Pandas Series

A Series is a one-dimensional labeled array capable of holding any data type.

### Creating a Series

```python
# From a list
s = pd.Series([10, 20, 30, 40])
# 0    10
# 1    20
# 2    30
# 3    40

# With a custom index
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

# From a dictionary
d = {'apples': 3, 'bananas': 5, 'oranges': 2}
s = pd.Series(d)

# From a scalar (broadcasts to all indices)
s = pd.Series(5, index=['a', 'b', 'c'])
```

### Series Attributes and Methods

```python
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'], name='scores')

s.values        # array([10, 20, 30, 40])
s.index         # Index(['a', 'b', 'c', 'd'])
s.dtype         # dtype('int64')
s.name          # 'scores'
s.shape         # (4,)

s.sum()         # 100
s.mean()        # 25.0
s.describe()    # count, mean, std, min, 25%, 50%, 75%, max
```

### Series Indexing

```python
s['a']          # 10 — label-based
s[0]            # 10 — positional (if index is not integer-based)
s[['a', 'c']]   # select multiple labels
s['a':'c']      # slice by label (INCLUSIVE of endpoint!)
s[s > 20]       # boolean indexing
```

---

## 2. DataFrames

A DataFrame is a two-dimensional, size-mutable, tabular data structure with labeled
axes (rows and columns). Think of it as a spreadsheet or SQL table in Python.

### Creating DataFrames

```python
# From a dictionary of lists
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'age': [25, 30, 35, 28],
    'city': ['New York', 'London', 'Paris', 'Tokyo'],
    'salary': [70000, 80000, 90000, 75000]
}
df = pd.DataFrame(data)

# From a list of dictionaries
records = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
]
df = pd.DataFrame(records)

# From a NumPy array
arr = np.random.rand(4, 3)
df = pd.DataFrame(arr, columns=['A', 'B', 'C'])

# From a CSV file (most common in practice)
# df = pd.read_csv('data.csv')
# df = pd.read_csv('data.csv', index_col=0, parse_dates=['date'])
```

### DataFrame Attributes

```python
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'salary': [70000, 80000, 90000]
})

df.shape        # (3, 3) — rows, columns
df.columns      # Index(['name', 'age', 'salary'])
df.index        # RangeIndex(start=0, stop=3, step=1)
df.dtypes       # data type of each column
df.info()       # concise summary (types, non-null counts, memory)
df.describe()   # statistical summary of numeric columns
df.head(2)      # first 2 rows
df.tail(2)      # last 2 rows
df.sample(2)    # 2 random rows
```

---

## 3. Selecting Columns

```python
# Single column (returns a Series)
df['name']
df.name           # dot notation (does not work if column name has spaces)

# Multiple columns (returns a DataFrame)
df[['name', 'age']]
```

---

## 4. Selecting Rows — loc vs iloc

This is one of the most important concepts in Pandas.

### loc — Label-based selection

`loc` uses **labels** (index values, column names).

```python
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'salary': [70000, 80000, 90000]
}, index=['x', 'y', 'z'])

df.loc['x']                   # row with label 'x' (returns Series)
df.loc[['x', 'z']]            # rows with labels 'x' and 'z'
df.loc['x':'z']               # slice — INCLUSIVE of 'z'
df.loc['x', 'name']           # single value: 'Alice'
df.loc['x':'y', 'name':'age'] # sub-DataFrame
df.loc[df['age'] > 25]        # boolean selection
df.loc[df['age'] > 25, 'name']  # filtered column
```

### iloc — Integer position-based selection

`iloc` uses **integer positions** (0-indexed), like NumPy indexing.

```python
df.iloc[0]                    # first row
df.iloc[[0, 2]]               # first and third rows
df.iloc[0:2]                  # first two rows (EXCLUSIVE of end)
df.iloc[0, 1]                 # row 0, column 1
df.iloc[0:2, 0:2]             # sub-DataFrame
df.iloc[-1]                   # last row
```

### Key Difference

| Feature     | `loc`                      | `iloc`                 |
|-------------|----------------------------|------------------------|
| Uses        | Labels                     | Integer positions      |
| Slice end   | Inclusive                  | Exclusive              |
| Boolean     | Yes                        | Yes (via arrays)       |

---

## 5. Filtering Rows

```python
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'age': [25, 30, 35, 28],
    'dept': ['Engineering', 'Marketing', 'Engineering', 'Marketing']
})

# Single condition
df[df['age'] > 28]

# Multiple conditions (must use & | ~ and parentheses)
df[(df['age'] > 25) & (df['dept'] == 'Engineering')]

# Using isin()
df[df['dept'].isin(['Engineering', 'Sales'])]

# Using query() — cleaner syntax for complex filters
df.query('age > 25 and dept == "Engineering"')

# String methods
df[df['name'].str.startswith('A')]
df[df['name'].str.contains('li')]
```

---

## 6. Adding and Modifying Columns

```python
# Add a new column
df['bonus'] = df['salary'] * 0.1

# Conditional column with np.where
df['senior'] = np.where(df['age'] >= 30, True, False)

# Using apply() for custom transformations
df['name_upper'] = df['name'].apply(str.upper)

# Using assign() — returns a new DataFrame (does not modify in place)
df2 = df.assign(
    tax=df['salary'] * 0.2,
    net=df['salary'] * 0.8
)

# Rename columns
df.rename(columns={'name': 'full_name', 'age': 'years'}, inplace=True)

# Drop columns
df.drop(columns=['bonus'], inplace=True)
```

---

## 7. Sorting

```python
# Sort by one column
df.sort_values('age')                    # ascending (default)
df.sort_values('age', ascending=False)   # descending

# Sort by multiple columns
df.sort_values(['dept', 'age'], ascending=[True, False])

# Sort by index
df.sort_index()

# Get top N
df.nlargest(3, 'salary')
df.nsmallest(3, 'age')
```

---

## 8. Handling the Index

```python
# Set a column as the index
df.set_index('name', inplace=True)

# Reset the index back to a column
df.reset_index(inplace=True)

# Multi-level index
df.set_index(['dept', 'name'], inplace=True)
df.loc[('Engineering', 'Alice')]  # access with tuple

# Rename the index
df.index.name = 'employee_id'
```

---

## 9. Basic Statistics

```python
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
})

df.describe()              # summary statistics
df.mean()                  # mean of each column
df.median()                # median of each column
df.std()                   # standard deviation
df.corr()                  # correlation matrix
df['A'].value_counts()     # frequency count (for categorical data)
df['A'].nunique()          # number of unique values
```

---

## 10. Reading and Writing Data

```python
# CSV
df = pd.read_csv('data.csv')
df.to_csv('output.csv', index=False)

# Excel
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
df.to_excel('output.xlsx', index=False)

# JSON
df = pd.read_json('data.json')
df.to_json('output.json', orient='records')

# SQL (requires sqlalchemy)
# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///database.db')
# df = pd.read_sql('SELECT * FROM table', engine)
# df.to_sql('table_name', engine, if_exists='replace', index=False)

# Parquet (efficient columnar format)
# df = pd.read_parquet('data.parquet')
# df.to_parquet('output.parquet')
```

---

## 11. Common Pitfalls

### SettingWithCopyWarning

```python
# BAD — may not work as expected
subset = df[df['age'] > 25]
subset['new_col'] = 1  # Warning!

# GOOD — use .loc on the original DataFrame
df.loc[df['age'] > 25, 'new_col'] = 1

# Or make an explicit copy
subset = df[df['age'] > 25].copy()
subset['new_col'] = 1
```

### Chained Indexing

```python
# BAD — unpredictable behavior
df['age'][0] = 99

# GOOD
df.loc[df.index[0], 'age'] = 99
```

---

## Key Takeaways

- **Series** is a 1D labeled array; **DataFrame** is a 2D labeled table.
- Use `loc` for label-based access and `iloc` for position-based access.
- Pandas makes filtering intuitive with boolean indexing and `query()`.
- Always be mindful of the `SettingWithCopyWarning` — use `.loc` or `.copy()`.
- `read_csv` and `to_csv` are the workhorses for data I/O.
- `describe()`, `info()`, and `dtypes` are your first tools for understanding any dataset.

---

*Next: Day 17 — Pandas Advanced: Merging, Groupby, Pivot Tables, and Time Series.*
