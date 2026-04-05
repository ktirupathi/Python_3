# Day 22: Machine Learning Fundamentals

## What is Machine Learning?

Machine Learning (ML) is a subset of artificial intelligence that enables computers to learn
patterns from data and make predictions or decisions without being explicitly programmed
for every scenario. Instead of writing rules, you feed the algorithm data and let it
discover the rules on its own.

### The ML Workflow

1. **Define the problem** -- What are you trying to predict or discover?
2. **Collect and prepare data** -- Gather relevant data and clean it.
3. **Choose a model** -- Select an algorithm suited to your problem.
4. **Train the model** -- Feed the data to the algorithm.
5. **Evaluate the model** -- Test it on unseen data.
6. **Tune and improve** -- Adjust hyperparameters and iterate.
7. **Deploy** -- Put the model into production.

---

## Types of Machine Learning

### 1. Supervised Learning

The algorithm learns from **labeled data** -- each training example has an input and a
known correct output (label).

**Use cases:**
- Spam detection (email -> spam or not spam)
- House price prediction (features -> price)
- Medical diagnosis (symptoms -> disease)

**Two main categories:**
- **Classification**: Predict a discrete category (e.g., cat vs dog)
- **Regression**: Predict a continuous value (e.g., temperature, price)

```python
# Supervised learning example: predicting house prices
# X = features (square footage, bedrooms, etc.)
# y = labels (actual prices)
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)        # Learn from labeled data
predictions = model.predict(X_test) # Predict on new data
```

### 2. Unsupervised Learning

The algorithm finds patterns in **unlabeled data** -- there are no known correct outputs.

**Use cases:**
- Customer segmentation (group similar customers)
- Anomaly detection (find unusual transactions)
- Dimensionality reduction (compress features)

**Main categories:**
- **Clustering**: Group similar data points (K-Means, DBSCAN)
- **Dimensionality Reduction**: Reduce feature count (PCA, t-SNE)
- **Association**: Find rules in data (Apriori algorithm)

```python
# Unsupervised learning example: customer segmentation
from sklearn.cluster import KMeans

model = KMeans(n_clusters=3)
model.fit(X)                   # No labels needed
clusters = model.predict(X)    # Assign each point to a cluster
```

### 3. Reinforcement Learning

The algorithm learns by **interacting with an environment**, receiving rewards or penalties
for its actions. Think of it like training a dog -- good behavior gets a treat.

**Use cases:** Game AI, robotics, recommendation systems, autonomous driving.

---

## Introduction to Scikit-learn

Scikit-learn (sklearn) is the most popular Python library for traditional machine learning.
It provides a consistent, clean API for dozens of algorithms.

### Installation

```bash
pip install scikit-learn
```

### The Scikit-learn API Pattern

Every estimator in scikit-learn follows the same pattern:

```python
from sklearn.some_module import SomeEstimator

# 1. Instantiate
model = SomeEstimator(hyperparameter1=value1)

# 2. Fit (train)
model.fit(X_train, y_train)

# 3. Predict
predictions = model.predict(X_test)

# 4. Evaluate
score = model.score(X_test, y_test)
```

This consistency is one of sklearn's greatest strengths -- once you learn one algorithm,
switching to another is trivial.

### Key Modules

| Module | Purpose |
|--------|---------|
| `sklearn.datasets` | Built-in datasets for practice |
| `sklearn.model_selection` | Train/test split, cross-validation |
| `sklearn.preprocessing` | Feature scaling, encoding |
| `sklearn.linear_model` | Linear/logistic regression |
| `sklearn.tree` | Decision trees |
| `sklearn.ensemble` | Random forests, boosting |
| `sklearn.cluster` | Clustering algorithms |
| `sklearn.metrics` | Evaluation metrics |
| `sklearn.pipeline` | Chain preprocessing + model |

---

## Preparing Data for ML

### Train-Test Split

Never evaluate a model on data it was trained on. Always split your data:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,       # 20% for testing
    random_state=42      # Reproducibility
)
```

### Feature Scaling

Many algorithms are sensitive to feature scales. A feature ranging from 0-1000 will
dominate one ranging from 0-1.

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# StandardScaler: mean=0, std=1
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Use same scaling!

# MinMaxScaler: scales to [0, 1]
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

**Important:** Always `fit_transform` on training data, then only `transform` on test data.
This prevents data leakage.

### Handling Categorical Features

ML models need numeric input. Encode categorical variables:

```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# LabelEncoder: converts categories to integers
le = LabelEncoder()
y_encoded = le.fit_transform(['cat', 'dog', 'cat', 'bird'])
# Result: [0, 1, 0, 2]

# OneHotEncoder: creates binary columns (preferred for features)
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse_output=False)
X_encoded = ohe.fit_transform(X_categorical)
```

---

## Your First ML Model: End to End

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Load data
iris = load_iris()
X, y = iris.data, iris.target

# 2. Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Train
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)

# 5. Predict and evaluate
y_pred = model.predict(X_test_scaled)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
```

---

## Common Evaluation Metrics

### For Regression
- **MAE** (Mean Absolute Error): Average absolute difference
- **MSE** (Mean Squared Error): Average squared difference (penalizes large errors)
- **RMSE**: Square root of MSE (same units as target)
- **R-squared**: Proportion of variance explained (0 to 1, higher is better)

### For Classification
- **Accuracy**: Fraction of correct predictions
- **Precision**: Of predicted positives, how many are actually positive
- **Recall**: Of actual positives, how many were correctly predicted
- **F1 Score**: Harmonic mean of precision and recall

```python
from sklearn.metrics import (mean_squared_error, r2_score,
                             accuracy_score, f1_score)

# Regression metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Classification metrics
acc = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')
```

---

## Overfitting vs Underfitting

| Concept | Training Score | Test Score | Cause | Fix |
|---------|---------------|------------|-------|-----|
| **Underfitting** | Low | Low | Model too simple | More features, complex model |
| **Good Fit** | High | High | Balanced | Keep it |
| **Overfitting** | Very High | Low | Model memorizes noise | Regularization, more data |

### Bias-Variance Tradeoff
- **High bias** = underfitting (model is too simple)
- **High variance** = overfitting (model is too sensitive to training data)
- The goal is to find the sweet spot between the two.

---

## Key Takeaways

1. ML automates pattern discovery from data instead of manual rule writing.
2. **Supervised learning** uses labeled data; **unsupervised** finds structure in unlabeled data.
3. Scikit-learn provides a uniform `fit/predict/score` API across all algorithms.
4. Always split data into training and test sets to avoid misleading results.
5. Feature scaling is critical for distance-based and gradient-based algorithms.
6. Understand the bias-variance tradeoff to diagnose model performance.
7. Choose metrics appropriate to your problem type (regression vs classification).
