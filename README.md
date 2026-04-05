<div align="center">

# 🐍 Python in 30 Days

### From Zero to Data Science, ML & Deep Learning

**A complete, structured, hands-on Python curriculum designed for aspiring data professionals.**

[![GitHub stars](https://img.shields.io/github/stars/ktirupathi/Python_3?style=social)](https://github.com/ktirupathi/Python_3/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ktirupathi/Python_3?style=social)](https://github.com/ktirupathi/Python_3/network/members)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Level](https://img.shields.io/badge/Level-Beginner_to_Advanced-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)

---

**4 Weeks** · **30 Days** · **120+ Examples** · **80+ Assignments** · **5 Capstone Projects**

[🚀 Get Started](#-how-to-use-this-repo) · [📋 Roadmap](#-30-day-roadmap-overview) · [💡 Capstones](#-capstone-projects) · [🤝 Contribute](#-contributing)

</div>

---

## 📖 What is This?

This is a **30-day, project-based Python curriculum** that takes you from absolute beginner to building real data science, machine learning, and deep learning projects. Every day has theory, code examples, and practice problems — organized into 4 weekly sprints with increasing difficulty.

**Who is this for?**
- Complete beginners starting their Python journey
- Analysts transitioning into data science
- Anyone preparing for data science / ML interviews
- Self-learners who want a structured path with real projects

**What you'll build by Day 30:**
- Clean, Pythonic code with best practices
- Data analysis pipelines with Pandas & NumPy
- Interactive visualizations with Matplotlib, Seaborn & Plotly
- Machine learning models with Scikit-Learn
- Deep learning networks with TensorFlow/Keras
- 5 portfolio-ready capstone projects

---

## 🚀 How to Use This Repo

### Option 1: Clone & Run Locally

```bash
# Clone the repository
git clone https://github.com/ktirupathi/Python_3.git
cd Python_3

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

### Option 2: Run in Google Colab (No Setup!)

Each notebook includes a **"Open in Colab"** badge at the top. Just click and start coding — no installation required.

### Repo Structure

```
Python_3/
├── week_1/                     # Python Fundamentals
│   ├── day_01_setup.ipynb
│   ├── day_02_variables.ipynb
│   ├── ...
│   └── assignments/
│       ├── assignment_1.ipynb
│       └── solutions/
├── week_2/                     # Data Analysis & Visualization
│   ├── day_08_numpy.ipynb
│   ├── ...
│   └── assignments/
├── week_3/                     # Machine Learning
│   ├── day_15_intro_ml.ipynb
│   ├── ...
│   └── assignments/
├── week_4/                     # Deep Learning & Advanced Topics
│   ├── day_22_intro_dl.ipynb
│   ├── ...
│   └── assignments/
├── capstones/                  # 5 Capstone Projects
│   ├── capstone_1_eda/
│   ├── capstone_2_dashboard/
│   ├── capstone_3_ml_pipeline/
│   ├── capstone_4_nlp/
│   └── capstone_5_dl_image/
├── datasets/                   # Sample datasets
├── cheatsheets/                # Quick reference PDFs
├── requirements.txt
└── README.md
```

### Daily Workflow

1. **Read** the day's notebook (theory + examples)
2. **Code along** — run every cell, experiment with changes
3. **Solve** the practice questions at the end of each notebook
4. **Submit** the weekly assignment before moving to the next week
5. **Build** the capstone project at the end

---

## 📋 30-Day Roadmap Overview

| Week | Theme | Days | What You'll Learn |
|------|-------|------|-------------------|
| **1** | 🐍 Python Fundamentals | Day 1–7 | Core syntax, data structures, functions, OOP, file I/O |
| **2** | 📊 Data Analysis & Viz | Day 8–14 | NumPy, Pandas, Matplotlib, Seaborn, EDA |
| **3** | 🤖 Machine Learning | Day 15–21 | Scikit-Learn, regression, classification, clustering, evaluation |
| **4** | 🧠 Deep Learning & Advanced | Day 22–30 | TensorFlow/Keras, CNNs, NLP, time series, deployment |

---

## 📅 WEEK 1: Python Fundamentals (Day 1–7)

> **Goal:** Master Python syntax, data structures, functions, and OOP — the foundation everything else builds on.

---

### Day 1: Setup & Your First Program

**Topics:** Installing Python, IDE setup (VS Code / Jupyter), running your first script, `print()`, comments, Python interpreter

**Example:**
```python
# Your very first Python program
name = "VenkataKiran"
age = 30
print(f"Hello, my name is {name} and I am {age} years old.")
print(f"In 5 years, I will be {age + 5} years old.")

# Understanding types
print(type(name))   # <class 'str'>
print(type(age))    # <class 'int'>
```

---

### Day 2: Variables, Data Types & Operators

**Topics:** int, float, str, bool, type casting, arithmetic operators, comparison operators, logical operators, assignment operators

**Example:**
```python
# Type casting
price = "49.99"
quantity = 3
total = float(price) * quantity
print(f"Total: ₹{total}")  # Total: ₹149.97

# Logical operators
age = 25
has_license = True
can_drive = age >= 18 and has_license
print(f"Can drive: {can_drive}")  # True

# Floor division vs regular division
print(17 / 5)   # 3.4
print(17 // 5)  # 3
print(17 % 5)   # 2 (modulus - remainder)
```

---

### Day 3: Strings & String Methods

**Topics:** String indexing, slicing, methods (`upper`, `lower`, `strip`, `split`, `join`, `replace`, `find`), f-strings, escape characters, multiline strings

**Example:**
```python
text = "  Data Science is Amazing!  "

# Chaining string methods
cleaned = text.strip().lower().replace("amazing", "powerful")
print(cleaned)  # "data science is powerful!"

# String slicing
email = "venkat@example.com"
username = email[:email.index("@")]
domain = email[email.index("@")+1:]
print(f"User: {username}, Domain: {domain}")

# f-string formatting
revenue = 1500000
print(f"Revenue: ₹{revenue:,.2f}")  # Revenue: ₹1,500,000.00
```

---

### Day 4: Lists, Tuples & Sets

**Topics:** Creating, indexing, slicing, list methods (`append`, `extend`, `pop`, `sort`, `reverse`), list comprehensions, tuples (immutable), sets (unique values, set operations), when to use which

**Example:**
```python
# List comprehension — powerful one-liner
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]

# Set operations — finding common skills
team_a_skills = {"Python", "SQL", "Tableau", "Excel"}
team_b_skills = {"Python", "R", "Power BI", "SQL"}

common = team_a_skills & team_b_skills       # {'Python', 'SQL'}
all_skills = team_a_skills | team_b_skills    # Union of both
unique_to_a = team_a_skills - team_b_skills   # {'Tableau', 'Excel'}

# Tuple unpacking
coordinates = (12.9716, 77.5946)  # Bangalore
lat, lng = coordinates
print(f"Bangalore: {lat}°N, {lng}°E")
```

---

### Day 5: Dictionaries & Control Flow

**Topics:** Dictionaries (CRUD, nesting, `get`, `keys`, `values`, `items`), if/elif/else, for loops, while loops, `break`, `continue`, `enumerate`, `zip`

**Example:**
```python
# Nested dictionary — employee records
employees = {
    "E001": {"name": "Kiran", "dept": "Data Science", "salary": 120000},
    "E002": {"name": "Priya", "dept": "Marketing", "salary": 95000},
    "E003": {"name": "Rahul", "dept": "Data Science", "salary": 110000},
}

# Filter data scientists earning above 100k
ds_team = {
    eid: info for eid, info in employees.items()
    if info["dept"] == "Data Science" and info["salary"] > 100000
}
print(ds_team)

# zip — combining two lists into a dictionary
cities = ["Bangalore", "Mumbai", "Delhi"]
populations = [12_000_000, 20_000_000, 19_000_000]
city_pop = dict(zip(cities, populations))

for city, pop in city_pop.items():
    print(f"{city}: {pop:,}")
```

---

### Day 6: Functions, Lambda & Error Handling

**Topics:** Defining functions, `*args`, `**kwargs`, return values, lambda functions, `map`, `filter`, `reduce`, try/except/finally, custom exceptions, decorators (intro)

**Example:**
```python
# Function with default args and **kwargs
def create_report(title, author="Unknown", **metadata):
    report = f"📊 {title}\nBy: {author}"
    for key, value in metadata.items():
        report += f"\n{key}: {value}"
    return report

print(create_report("Q4 Sales", author="Kiran", department="Marketing", year=2025))

# Lambda + map + filter chain
salaries = [45000, 72000, 58000, 120000, 95000, 34000]

# Get salaries above 50k and apply 10% raise
updated = list(map(lambda s: s * 1.10, filter(lambda s: s > 50000, salaries)))
print(updated)  # [79200.0, 63800.0, 132000.0, 104500.0]

# Error handling in data processing
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid input types"
    else:
        return round(result, 2)

print(safe_divide(100, 3))   # 33.33
print(safe_divide(100, 0))   # Cannot divide by zero
```

---

### Day 7: OOP & File I/O

**Topics:** Classes, objects, `__init__`, instance/class methods, inheritance, polymorphism, reading/writing files (text, CSV, JSON), `with` statement, `os` and `pathlib`

**Example:**
```python
import json
from datetime import datetime

class DataPipeline:
    """A simple data pipeline that reads, transforms, and saves data."""

    def __init__(self, source_file):
        self.source_file = source_file
        self.data = []
        self.processed = False

    def extract(self):
        with open(self.source_file, 'r') as f:
            self.data = json.load(f)
        print(f"✅ Extracted {len(self.data)} records")
        return self

    def transform(self, filter_fn=None):
        if filter_fn:
            self.data = [row for row in self.data if filter_fn(row)]
        self.processed = True
        print(f"✅ Transformed → {len(self.data)} records remaining")
        return self

    def load(self, output_file):
        with open(output_file, 'w') as f:
            json.dump(self.data, f, indent=2)
        print(f"✅ Saved to {output_file}")

# Usage (method chaining)
# pipeline = DataPipeline("raw_data.json")
# pipeline.extract().transform(lambda r: r["age"] > 25).load("cleaned.json")
```

---

### 📝 Week 1 Assignments

| # | Assignment | Difficulty | Topics Covered |
|---|-----------|------------|----------------|
| 1 | **Calculator Pro:** Build a CLI calculator that supports +, -, ×, ÷, power, square root, and maintains a history of calculations | ⭐ Basic | Variables, operators, loops, functions |
| 2 | **Student Grade Analyzer:** Read a list of students with marks in 5 subjects, compute average, grade (A/B/C/D/F), rank, and find topper per subject | ⭐⭐ Medium | Lists, dicts, loops, functions, sorting |
| 3 | **Contact Book App:** Build a contact book using OOP — add, search, update, delete contacts. Save/load from JSON file. Support search by name or phone | ⭐⭐ Medium | OOP, file I/O, dictionaries, error handling |
| 4 | **Text File Analyzer:** Read any `.txt` file and report: word count, character count, sentence count, top 10 most frequent words, average word length, longest word | ⭐⭐⭐ Hard | File I/O, strings, dicts, sorting, functions |
| 5 | **Mini Data Pipeline:** Build a class that reads a CSV file, cleans missing values (fill or drop), filters rows by a condition, and saves the result — all using only built-in Python (no Pandas!) | ⭐⭐⭐ Hard | OOP, file I/O, CSV, error handling, list comprehensions |

---

## 📅 WEEK 2: Data Analysis & Visualization (Day 8–14)

> **Goal:** Master NumPy, Pandas, and data visualization — the core toolkit every data scientist uses daily.

---

### Day 8: NumPy Fundamentals

**Topics:** Arrays vs lists, creating arrays (`arange`, `linspace`, `zeros`, `ones`, `random`), indexing, slicing, reshaping, broadcasting, vectorized operations, performance comparison

**Example:**
```python
import numpy as np

# Performance: NumPy vs Python lists
import time

size = 1_000_000
python_list = list(range(size))
numpy_array = np.arange(size)

# Python list — slow
start = time.time()
result_list = [x ** 2 for x in python_list]
print(f"Python list: {time.time() - start:.4f}s")

# NumPy — fast (vectorized)
start = time.time()
result_np = numpy_array ** 2
print(f"NumPy array: {time.time() - start:.4f}s")  # ~50-100x faster!

# Broadcasting — adding a bonus to each department's salaries
salaries = np.array([[50000, 60000, 55000],   # Dept A
                     [70000, 80000, 75000],   # Dept B
                     [45000, 50000, 48000]])   # Dept C

bonus_pct = np.array([0.10, 0.15, 0.12])  # Different bonus per dept
bonuses = salaries * bonus_pct.reshape(3, 1)
print("Bonuses:\n", bonuses)
```

---

### Day 9: NumPy Advanced & Linear Algebra

**Topics:** Boolean masking, fancy indexing, `np.where`, stacking/splitting, statistical functions, matrix operations, dot product, eigenvalues, solving linear equations

**Example:**
```python
import numpy as np

# Boolean masking — filter outliers
data = np.array([12, 45, 67, 234, 23, 56, 890, 34, 78, 1200])
mean, std = data.mean(), data.std()
mask = np.abs(data - mean) <= 2 * std
cleaned = data[mask]
outliers = data[~mask]
print(f"Cleaned: {cleaned}")
print(f"Outliers removed: {outliers}")

# Solving linear equations: 2x + 3y = 8, x - y = 1
A = np.array([[2, 3], [1, -1]])
b = np.array([8, 1])
solution = np.linalg.solve(A, b)
print(f"x = {solution[0]}, y = {solution[1]}")  # x = 2.2, y = 1.2
```

---

### Day 10: Pandas — Series & DataFrames

**Topics:** Creating Series/DataFrames, reading data (`read_csv`, `read_excel`, `read_json`), `head`, `tail`, `info`, `describe`, `shape`, `dtypes`, selecting columns, `loc` vs `iloc`, conditional filtering

**Example:**
```python
import pandas as pd

# Creating a DataFrame from a dictionary
sales_data = {
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "revenue": [120000, 135000, 128000, 142000, 155000, 148000],
    "expenses": [95000, 88000, 102000, 91000, 99000, 94000],
    "region": ["North", "South", "North", "East", "South", "East"]
}
df = pd.DataFrame(sales_data)

# Add profit column
df["profit"] = df["revenue"] - df["expenses"]
df["margin_%"] = (df["profit"] / df["revenue"] * 100).round(1)

# Filter: months where margin > 30%
high_margin = df[df["margin_%"] > 30]
print(high_margin)

# loc vs iloc
print(df.loc[0:2, ["month", "revenue"]])   # Label-based (inclusive)
print(df.iloc[0:2, [0, 1]])                 # Position-based (exclusive end)
```

---

### Day 11: Pandas — Data Wrangling

**Topics:** Handling missing data (`isnull`, `fillna`, `dropna`), duplicates, `apply`, `map`, string methods, `merge`/`join`, `concat`, `melt`/`pivot`, data type conversion

**Example:**
```python
import pandas as pd
import numpy as np

# Handling messy real-world data
df = pd.DataFrame({
    "name": ["Kiran", "Priya", None, "Rahul", "Kiran"],
    "salary": [120000, np.nan, 95000, 110000, 120000],
    "join_date": ["2020-01-15", "2019-06-20", "2021-03-10", "invalid", "2020-01-15"],
    "department": ["data science", "MARKETING", "Data Science", "engineering", "data science"]
})

# Clean pipeline
cleaned = (df
    .drop_duplicates()
    .dropna(subset=["name"])
    .assign(
        salary=lambda x: x["salary"].fillna(x["salary"].median()),
        department=lambda x: x["department"].str.strip().str.title(),
        join_date=lambda x: pd.to_datetime(x["join_date"], errors="coerce")
    )
)
print(cleaned)

# Merging two DataFrames
orders = pd.DataFrame({"customer_id": [1, 2, 3], "amount": [500, 300, 800]})
customers = pd.DataFrame({"customer_id": [1, 2, 4], "name": ["Alice", "Bob", "Dave"]})

result = orders.merge(customers, on="customer_id", how="left")
print(result)
```

---

### Day 12: Pandas — GroupBy & Aggregation

**Topics:** `groupby`, `agg`, `transform`, `pivot_table`, `crosstab`, window functions (`rolling`, `expanding`, `shift`), `resample` for time series

**Example:**
```python
import pandas as pd

# Sales dataset
df = pd.DataFrame({
    "date": pd.date_range("2025-01-01", periods=12, freq="M"),
    "region": ["North", "South"] * 6,
    "product": ["A", "B", "A", "B"] * 3,
    "revenue": [100, 150, 120, 180, 90, 200, 130, 170, 110, 190, 140, 160]
})

# Multi-level aggregation
summary = df.groupby(["region", "product"]).agg(
    total_revenue=("revenue", "sum"),
    avg_revenue=("revenue", "mean"),
    max_revenue=("revenue", "max"),
    count=("revenue", "count")
).round(2)
print(summary)

# Pivot table
pivot = df.pivot_table(values="revenue", index="region", columns="product", aggfunc=["sum", "mean"])
print(pivot)

# Rolling average (3-month window)
df["rolling_avg"] = df.groupby("region")["revenue"].transform(lambda x: x.rolling(3).mean())
```

---

### Day 13: Data Visualization — Matplotlib & Seaborn

**Topics:** Line plots, bar charts, scatter plots, histograms, box plots, heatmaps, subplots, customization (labels, legends, colors, styles), Seaborn categorical & distribution plots

**Example:**
```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Professional-looking multi-panel figure
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 1. Distribution plot
np.random.seed(42)
salaries = np.random.normal(85000, 15000, 500)
sns.histplot(salaries, bins=30, kde=True, ax=axes[0], color="#2563eb")
axes[0].set_title("Salary Distribution", fontweight="bold")
axes[0].set_xlabel("Annual Salary (₹)")

# 2. Bar chart with values
departments = ["Data Science", "Marketing", "Engineering", "Sales"]
headcount = [45, 30, 60, 35]
bars = axes[1].bar(departments, headcount, color=["#2563eb", "#f59e0b", "#10b981", "#ef4444"])
axes[1].set_title("Headcount by Department", fontweight="bold")
for bar, count in zip(bars, headcount):
    axes[1].text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
                 str(count), ha='center', fontweight='bold')

# 3. Correlation heatmap
data = np.random.randn(100, 4)
corr = np.corrcoef(data.T)
sns.heatmap(corr, annot=True, cmap="RdBu_r", center=0, ax=axes[2],
            xticklabels=["Revenue", "Traffic", "Spend", "Conversions"],
            yticklabels=["Revenue", "Traffic", "Spend", "Conversions"])
axes[2].set_title("Correlation Heatmap", fontweight="bold")

plt.tight_layout()
plt.savefig("visualization_demo.png", dpi=150, bbox_inches="tight")
plt.show()
```

---

### Day 14: EDA — Putting It All Together

**Topics:** End-to-end EDA workflow: load → inspect → clean → analyze → visualize → summarize. Profiling with `ydata-profiling`, interactive plots with Plotly

**Example:**
```python
import pandas as pd
import plotly.express as px

# Complete EDA mini-project
df = pd.read_csv("datasets/ecommerce_sales.csv")

# Step 1: Quick inspection
print(f"Shape: {df.shape}")
print(f"Missing values:\n{df.isnull().sum()}")
print(f"Duplicates: {df.duplicated().sum()}")

# Step 2: Statistical summary
print(df.describe())

# Step 3: Interactive visualization with Plotly
fig = px.scatter(df, x="marketing_spend", y="revenue",
                 color="region", size="customer_count",
                 hover_data=["product_category"],
                 title="Marketing Spend vs Revenue by Region",
                 trendline="ols")
fig.show()

# Step 4: Automated profiling (generates full HTML report)
# from ydata_profiling import ProfileReport
# profile = ProfileReport(df, title="E-commerce Sales EDA")
# profile.to_file("eda_report.html")
```

---

### 📝 Week 2 Assignments

| # | Assignment | Difficulty | Topics Covered |
|---|-----------|------------|----------------|
| 1 | **NumPy Matrix Operations:** Create a 10×10 random matrix, find row/column means, normalize it (0-1), extract the diagonal, and compute the determinant | ⭐ Basic | NumPy arrays, math, linear algebra |
| 2 | **Pandas Data Cleaning Challenge:** Given a messy CSV with mixed types, missing values, duplicates, inconsistent formatting, and outliers — clean it into analysis-ready form in 10 steps | ⭐⭐ Medium | Pandas, data wrangling, method chaining |
| 3 | **Sales Dashboard Dataset:** Using a sales dataset, compute monthly trends, top products, regional performance, YoY growth, and create a 6-panel visualization figure | ⭐⭐ Medium | Pandas groupby, Matplotlib, Seaborn |
| 4 | **Web Scraping + EDA:** Scrape a table from Wikipedia (using `pd.read_html`), clean the data, perform EDA, and generate 5 key insights with supporting charts | ⭐⭐⭐ Hard | Pandas, web scraping, EDA, visualization |
| 5 | **Time Series EDA:** Analyze a stock price or weather dataset — compute rolling averages, detect seasonality, identify anomalies, and create an interactive Plotly dashboard | ⭐⭐⭐ Hard | Pandas time series, Plotly, statistical analysis |

---

## 📅 WEEK 3: Machine Learning (Day 15–21)

> **Goal:** Build, evaluate, and tune ML models for real-world classification, regression, and clustering problems.

---

### Day 15: Introduction to Machine Learning

**Topics:** What is ML, supervised vs unsupervised vs reinforcement learning, train/test split, overfitting vs underfitting, bias-variance tradeoff, ML workflow, Scikit-Learn introduction

**Example:**
```python
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# Load and split data — the first step in every ML project
data = load_iris()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Training samples: {X_train.shape[0]}")
print(f"Test samples: {X_test.shape[0]}")
print(f"Features: {data.feature_names}")
print(f"Classes: {data.target_names}")
```

---

### Day 16: Linear Regression & Polynomial Regression

**Topics:** Simple & multiple linear regression, cost function (MSE), gradient descent intuition, polynomial features, regularization (Ridge, Lasso, ElasticNet), evaluation metrics (R², MAE, RMSE)

**Example:**
```python
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Predict house prices
np.random.seed(42)
area = np.random.uniform(500, 3000, 200).reshape(-1, 1)
price = 50 * area + np.random.normal(0, 15000, (200, 1)) + 100000

X_train, X_test = area[:160], area[160:]
y_train, y_test = price[:160], price[160:]

# Simple Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f"R² Score: {r2_score(y_test, y_pred):.4f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):,.0f}")
print(f"Price = {model.coef_[0][0]:.2f} × Area + {model.intercept_[0]:,.0f}")

# Ridge Regression (L2 regularization)
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)
print(f"Ridge R²: {r2_score(y_test, ridge.predict(X_test)):.4f}")
```

---

### Day 17: Logistic Regression & Classification Metrics

**Topics:** Binary & multi-class classification, sigmoid function, decision boundary, confusion matrix, accuracy, precision, recall, F1-score, ROC-AUC, classification report

**Example:**
```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

print(classification_report(y_test, y_pred, target_names=data.target_names))
print(f"ROC-AUC: {roc_auc_score(y_test, y_prob):.4f}")
print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")
```

---

### Day 18: Decision Trees & Random Forests

**Topics:** Decision tree algorithm, information gain, Gini impurity, pruning, Random Forest (bagging), feature importance, hyperparameter tuning

**Example:**
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import pandas as pd

# Train a Random Forest with hyperparameter tuning
rf = RandomForestClassifier(random_state=42)

param_grid = {
    "n_estimators": [100, 200, 300],
    "max_depth": [5, 10, 15, None],
    "min_samples_split": [2, 5, 10]
}

grid_search = GridSearchCV(rf, param_grid, cv=5, scoring="f1", n_jobs=-1)
grid_search.fit(X_train, y_train)

print(f"Best params: {grid_search.best_params_}")
print(f"Best F1: {grid_search.best_score_:.4f}")

# Feature importance
best_model = grid_search.best_estimator_
importance = pd.Series(best_model.feature_importances_, index=data.feature_names)
top_features = importance.nlargest(10)
print(f"Top 10 Features:\n{top_features}")
```

---

### Day 19: SVM, KNN & Naive Bayes

**Topics:** Support Vector Machines (kernel trick, margin), K-Nearest Neighbors (distance metrics, choosing K), Naive Bayes (Gaussian, Multinomial), when to use each algorithm

**Example:**
```python
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Compare 3 classifiers using pipelines
models = {
    "SVM": Pipeline([("scaler", StandardScaler()), ("clf", SVC(kernel="rbf"))]),
    "KNN": Pipeline([("scaler", StandardScaler()), ("clf", KNeighborsClassifier(n_neighbors=5))]),
    "Naive Bayes": Pipeline([("scaler", StandardScaler()), ("clf", GaussianNB())])
}

for name, model in models.items():
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print(f"{name}: Accuracy = {score:.4f}")
```

---

### Day 20: Clustering & Unsupervised Learning

**Topics:** K-Means, elbow method, silhouette score, DBSCAN, hierarchical clustering, PCA (dimensionality reduction), t-SNE for visualization

**Example:**
```python
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Customer segmentation with K-Means
# Assume X = customer features (spending, frequency, recency)

# Elbow method to find optimal K
inertias = []
K_range = range(2, 11)
for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_train)
    inertias.append(km.inertia_)

# Fit with optimal K
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
labels = kmeans.fit_predict(X_train)
print(f"Silhouette Score: {silhouette_score(X_train, labels):.4f}")

# Visualize with PCA
pca = PCA(n_components=2)
X_2d = pca.fit_transform(X_train)
plt.scatter(X_2d[:, 0], X_2d[:, 1], c=labels, cmap="viridis", alpha=0.6)
plt.title("Customer Segments (PCA)")
plt.show()
```

---

### Day 21: Feature Engineering & Model Pipelines

**Topics:** Feature scaling (Standard, MinMax, Robust), encoding (One-Hot, Label, Target), feature selection (`SelectKBest`, mutual info), Scikit-Learn pipelines, cross-validation, saving/loading models

**Example:**
```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score
import joblib

# Real-world pipeline with mixed data types
numeric_features = ["age", "income", "credit_score"]
categorical_features = ["education", "employment_type", "region"]

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
])

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", GradientBoostingClassifier(n_estimators=200, max_depth=5))
])

# Cross-validation
scores = cross_val_score(pipeline, X, y, cv=5, scoring="roc_auc")
print(f"CV ROC-AUC: {scores.mean():.4f} ± {scores.std():.4f}")

# Save model
# pipeline.fit(X_train, y_train)
# joblib.dump(pipeline, "model_pipeline.pkl")
```

---

### 📝 Week 3 Assignments

| # | Assignment | Difficulty | Topics Covered |
|---|-----------|------------|----------------|
| 1 | **House Price Predictor:** Build a regression model on the Boston/Ames housing dataset. Try Linear, Ridge, Lasso, and Random Forest. Compare R² and RMSE. Visualize actual vs predicted | ⭐⭐ Medium | Regression, evaluation, visualization |
| 2 | **Customer Churn Classifier:** Predict telecom customer churn using Logistic Regression, Random Forest, and XGBoost. Handle class imbalance with SMOTE. Report precision/recall/F1 for both classes | ⭐⭐ Medium | Classification, imbalanced data, metrics |
| 3 | **Customer Segmentation:** Perform RFM analysis on an e-commerce dataset, apply K-Means clustering, profile each segment, and visualize with PCA | ⭐⭐⭐ Hard | Clustering, PCA, feature engineering |
| 4 | **ML Pipeline Factory:** Build a reusable function that takes any dataset + target column and automatically: detects feature types, preprocesses, trains 5 models, compares them, and returns the best | ⭐⭐⭐ Hard | Pipelines, cross-validation, automation |
| 5 | **Kaggle Competition Entry:** Submit a prediction to any active Kaggle competition. Document your full approach: EDA → feature engineering → model selection → tuning → submission | ⭐⭐⭐⭐ Expert | End-to-end ML workflow |

---

## 📅 WEEK 4: Deep Learning & Advanced Topics (Day 22–30)

> **Goal:** Build neural networks for image classification, NLP, and time series — then learn to deploy your models.

---

### Day 22: Introduction to Deep Learning & Neural Networks

**Topics:** Perceptrons, activation functions (ReLU, Sigmoid, Softmax), backpropagation intuition, TensorFlow/Keras setup, building your first neural network

**Example:**
```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Build a simple neural network for classification
model = keras.Sequential([
    layers.Dense(128, activation="relu", input_shape=(30,)),
    layers.Dropout(0.3),
    layers.Dense(64, activation="relu"),
    layers.Dropout(0.2),
    layers.Dense(1, activation="sigmoid")
])

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
model.summary()

# Train
# history = model.fit(X_train, y_train, epochs=50, batch_size=32,
#                     validation_split=0.2, callbacks=[
#                         keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True)
#                     ])
```

---

### Day 23–24: Convolutional Neural Networks (CNNs)

**Topics:** Convolution operation, filters/kernels, pooling, CNN architectures (LeNet, VGG, ResNet), transfer learning, image augmentation, building an image classifier

**Example:**
```python
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2

# Transfer Learning — classify images using a pretrained model
base_model = MobileNetV2(weights="imagenet", include_top=False, input_shape=(224, 224, 3))
base_model.trainable = False  # Freeze pretrained weights

model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation="relu"),
    layers.Dropout(0.5),
    layers.Dense(10, activation="softmax")  # 10 classes
])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
print(f"Total params: {model.count_params():,}")
```

---

### Day 25–26: Natural Language Processing (NLP)

**Topics:** Text preprocessing (tokenization, stopwords, stemming, lemmatization), bag of words, TF-IDF, word embeddings, sentiment analysis, text classification with LSTMs and transformers (intro)

**Example:**
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Sentiment analysis pipeline
reviews = [
    "This product is absolutely amazing, love it!",
    "Terrible quality, broke after one day",
    "Good value for the price, recommended",
    "Waste of money, don't buy this",
    "Exceeded my expectations, five stars"
]
labels = [1, 0, 1, 0, 1]  # 1 = positive, 0 = negative

nlp_pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=5000, ngram_range=(1, 2), stop_words="english")),
    ("clf", MultinomialNB())
])

nlp_pipeline.fit(reviews, labels)

# Predict on new reviews
new_reviews = ["Great product, highly recommend!", "Not worth the price at all"]
predictions = nlp_pipeline.predict(new_reviews)
for review, pred in zip(new_reviews, predictions):
    sentiment = "Positive ✅" if pred == 1 else "Negative ❌"
    print(f"{sentiment}: {review}")
```

---

### Day 27: Time Series Forecasting

**Topics:** Time series components (trend, seasonality, noise), stationarity (ADF test), ARIMA/SARIMA, Prophet, LSTM for time series, evaluation (MAPE, RMSE)

**Example:**
```python
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

# Decompose a time series
df = pd.read_csv("datasets/monthly_sales.csv", parse_dates=["date"], index_col="date")

decomposition = seasonal_decompose(df["sales"], model="multiplicative", period=12)
decomposition.plot()

# Simple forecast with rolling statistics
df["rolling_mean_12"] = df["sales"].rolling(window=12).mean()
df["rolling_std_12"] = df["sales"].rolling(window=12).std()

# ARIMA (conceptual)
# from statsmodels.tsa.arima.model import ARIMA
# model = ARIMA(df["sales"], order=(1, 1, 1))
# fitted = model.fit()
# forecast = fitted.forecast(steps=12)
```

---

### Day 28: Model Deployment Basics

**Topics:** Saving models (joblib, pickle, SavedModel), building a Flask/FastAPI REST API, Docker basics, deploying to cloud (Heroku/Railway), Streamlit for quick demos

**Example:**
```python
from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model_pipeline.pkl")

@app.post("/predict")
def predict(features: dict):
    """Predict from input features."""
    X = np.array([list(features.values())])
    prediction = model.predict(X)[0]
    probability = model.predict_proba(X)[0].tolist()
    return {
        "prediction": int(prediction),
        "probability": probability,
        "status": "success"
    }

# Run: uvicorn app:app --reload
# Test: curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"age": 35, "income": 85000}'
```

---

### Day 29: Advanced Python for Data Science

**Topics:** Generators & iterators for large datasets, decorators, context managers, multiprocessing, `functools` (`lru_cache`, `partial`), type hints, writing clean Pythonic code

**Example:**
```python
import functools
import time

# Decorator for timing functions
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"⏱️ {func.__name__}: {elapsed:.4f}s")
        return result
    return wrapper

# Generator for processing large files line by line (memory efficient)
def read_large_csv(filepath: str, chunk_size: int = 1000):
    """Yield rows from a large CSV without loading entire file into memory."""
    import csv
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        chunk = []
        for row in reader:
            chunk.append(row)
            if len(chunk) >= chunk_size:
                yield chunk
                chunk = []
        if chunk:
            yield chunk

# Cache expensive computations
@functools.lru_cache(maxsize=128)
def expensive_feature(x: float) -> float:
    """Simulate an expensive feature computation."""
    time.sleep(0.01)  # Simulate work
    return x ** 2 + 2 * x + 1
```

---

### Day 30: Putting It All Together — Review & Next Steps

**Topics:** Full ML project checklist, common mistakes to avoid, where to go next (MLOps, LLMs, Kaggle competitions, specializations), building your portfolio, interview preparation tips

---

### 📝 Week 4 Assignments

| # | Assignment | Difficulty | Topics Covered |
|---|-----------|------------|----------------|
| 1 | **Neural Network from Scratch:** Implement a 2-layer neural network using only NumPy (no TensorFlow). Train it on a simple classification task. Implement forward pass, backprop, and gradient descent | ⭐⭐⭐ Hard | NumPy, math, deep learning fundamentals |
| 2 | **Image Classifier:** Build a CNN to classify Fashion-MNIST (10 clothing categories). Use data augmentation and achieve >90% accuracy. Visualize misclassified samples | ⭐⭐ Medium | CNNs, TensorFlow/Keras, image processing |
| 3 | **Sentiment Analyzer:** Build a movie review sentiment classifier using TF-IDF + Logistic Regression AND an LSTM. Compare performance. Deploy as a Streamlit app | ⭐⭐⭐ Hard | NLP, deep learning, deployment |
| 4 | **Stock Price Forecaster:** Use ARIMA and LSTM to forecast stock prices for a chosen company. Compare both approaches. Create interactive Plotly charts with actual vs predicted | ⭐⭐⭐ Hard | Time series, LSTM, visualization |
| 5 | **Full ML API:** Take any model you've built, wrap it in FastAPI with input validation (Pydantic), add a `/health` endpoint, Dockerize it, and write a README with usage instructions | ⭐⭐⭐⭐ Expert | Deployment, Docker, API design |

---

## 🏆 Capstone Projects

These are portfolio-worthy projects that combine everything you've learned. Pick at least 2.

---

### Capstone 1: Exploratory Data Analysis — Indian Startup Funding

**Objective:** Analyze the Indian startup ecosystem using real funding data.

**Requirements:**
- Clean and preprocess a messy dataset (100k+ rows)
- Analyze trends: funding by year, top sectors, top cities, funding stages
- Identify patterns: which investors are most active? What's the average funding amount by stage?
- Create a comprehensive visualization report (15+ charts)
- Write a narrative summary with 10 actionable insights

**Skills tested:** Pandas, Matplotlib, Seaborn, EDA, storytelling with data

---

### Capstone 2: Interactive Dashboard — Sales Performance Tracker

**Objective:** Build a Streamlit dashboard for a retail company's sales data.

**Requirements:**
- Multi-page dashboard with filters (date range, region, product category)
- KPI cards: revenue, profit, growth rate, top products
- Interactive charts: time series trends, geographic heat map, product comparison
- Automated anomaly detection (flag unusual sales days)
- Export functionality (download filtered data as CSV)

**Skills tested:** Streamlit, Pandas, Plotly, data pipeline design, UX

---

### Capstone 3: End-to-End ML Pipeline — Loan Default Prediction

**Objective:** Build a production-ready ML system to predict loan defaults.

**Requirements:**
- EDA + feature engineering (20+ engineered features)
- Handle class imbalance (SMOTE, class weights, threshold tuning)
- Train and compare 5+ models with cross-validation
- Hyperparameter tuning with Optuna or GridSearchCV
- Build a Scikit-Learn pipeline with preprocessing + model
- Evaluate with business metrics (cost of false negatives vs false positives)
- Save and serve with FastAPI

**Skills tested:** Full ML workflow, feature engineering, model evaluation, deployment

---

### Capstone 4: NLP Project — News Article Classifier

**Objective:** Build a system that classifies news articles into categories (sports, politics, tech, entertainment, business).

**Requirements:**
- Scrape or use a news dataset (10k+ articles)
- Text preprocessing pipeline (cleaning, tokenization, TF-IDF)
- Compare Naive Bayes, SVM, and LSTM classifiers
- Build a confusion matrix dashboard showing per-category performance
- Deploy as a web app where users can paste an article and get a prediction

**Skills tested:** NLP, text preprocessing, classification, deep learning, deployment

---

### Capstone 5: Deep Learning — Medical Image Classification

**Objective:** Build a CNN to classify medical images (e.g., X-ray normal vs pneumonia).

**Requirements:**
- Use a public medical imaging dataset (e.g., Chest X-ray from Kaggle)
- Implement data augmentation to handle limited data
- Build a custom CNN and compare with transfer learning (ResNet50, VGG16)
- Achieve >90% accuracy with detailed error analysis
- Visualize what the CNN "sees" using Grad-CAM
- Create a Streamlit app for uploading and classifying images

**Skills tested:** CNNs, transfer learning, image processing, model interpretability, deployment

---

## 📊 Progress Tracker

Use this checklist to track your progress:

```
Week 1: Python Fundamentals
├── [ ] Day 1:  Setup & First Program
├── [ ] Day 2:  Variables, Types & Operators
├── [ ] Day 3:  Strings & String Methods
├── [ ] Day 4:  Lists, Tuples & Sets
├── [ ] Day 5:  Dictionaries & Control Flow
├── [ ] Day 6:  Functions, Lambda & Error Handling
├── [ ] Day 7:  OOP & File I/O
└── [ ] Week 1 Assignment ✅

Week 2: Data Analysis & Visualization
├── [ ] Day 8:  NumPy Fundamentals
├── [ ] Day 9:  NumPy Advanced & Linear Algebra
├── [ ] Day 10: Pandas — Series & DataFrames
├── [ ] Day 11: Pandas — Data Wrangling
├── [ ] Day 12: Pandas — GroupBy & Aggregation
├── [ ] Day 13: Matplotlib & Seaborn
├── [ ] Day 14: EDA — Putting It All Together
└── [ ] Week 2 Assignment ✅

Week 3: Machine Learning
├── [ ] Day 15: Intro to Machine Learning
├── [ ] Day 16: Linear & Polynomial Regression
├── [ ] Day 17: Logistic Regression & Classification
├── [ ] Day 18: Decision Trees & Random Forests
├── [ ] Day 19: SVM, KNN & Naive Bayes
├── [ ] Day 20: Clustering & Unsupervised Learning
├── [ ] Day 21: Feature Engineering & Pipelines
└── [ ] Week 3 Assignment ✅

Week 4: Deep Learning & Advanced
├── [ ] Day 22: Intro to Deep Learning
├── [ ] Day 23-24: CNNs & Image Classification
├── [ ] Day 25-26: NLP & Text Classification
├── [ ] Day 27: Time Series Forecasting
├── [ ] Day 28: Model Deployment
├── [ ] Day 29: Advanced Python
├── [ ] Day 30: Review & Next Steps
└── [ ] Week 4 Assignment ✅

Capstone Projects (pick 2+)
├── [ ] Capstone 1: EDA — Indian Startup Funding
├── [ ] Capstone 2: Interactive Dashboard
├── [ ] Capstone 3: ML Pipeline — Loan Default
├── [ ] Capstone 4: NLP — News Classifier
└── [ ] Capstone 5: Deep Learning — Medical Images
```

---

## 🛠️ Tech Stack & Prerequisites

| Tool | Purpose | Install |
|------|---------|---------|
| Python 3.10+ | Core language | [python.org](https://python.org) |
| Jupyter Notebook | Interactive coding | `pip install notebook` |
| NumPy | Numerical computing | `pip install numpy` |
| Pandas | Data manipulation | `pip install pandas` |
| Matplotlib | Static visualization | `pip install matplotlib` |
| Seaborn | Statistical visualization | `pip install seaborn` |
| Plotly | Interactive visualization | `pip install plotly` |
| Scikit-Learn | Machine learning | `pip install scikit-learn` |
| TensorFlow | Deep learning | `pip install tensorflow` |
| Streamlit | Web app deployment | `pip install streamlit` |
| FastAPI | API deployment | `pip install fastapi uvicorn` |

**Quick install everything:**
```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Found a bug? Have a better example? Want to add a new assignment?

1. Fork this repository
2. Create a branch (`git checkout -b improvement/your-idea`)
3. Commit your changes (`git commit -m 'Add: better Day 5 example'`)
4. Push and open a Pull Request

All contributions are welcome — from fixing typos to adding entire new sections!

---

## ⭐ Support This Project

If this curriculum helped you, please **give it a star** ⭐ — it helps others discover it!

---

<div align="center">

**Built with ❤️ by [VenkataKiran Tirupathi](https://github.com/ktirupathi)**

*Senior Data Scientist · 10+ Years · Follow me for more: [@datamavericks](https://instagram.com/datamavericks) · [@Venkatabuilds](https://x.com/Venkatabuilds)*

</div>
