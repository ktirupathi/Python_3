# Day 23: Linear Regression & Polynomial Regression

## What is Regression?

Regression is a supervised learning technique for predicting a **continuous numerical value**
from input features. Examples: predicting house prices, stock returns, temperature, or
a student's exam score.

---

## Simple Linear Regression

Models the relationship between one feature (X) and one target (y) as a straight line:

```
y = w * x + b
```

- **w** (weight/slope): how much y changes per unit change in x
- **b** (bias/intercept): the value of y when x = 0

### How It Learns: Ordinary Least Squares (OLS)

The algorithm finds w and b that **minimize the sum of squared residuals**:

```
Loss = sum( (y_actual - y_predicted)^2 ) / n
```

This is called Mean Squared Error (MSE). The "least squares" solution has a closed-form
formula, so training is instantaneous for reasonable dataset sizes.

### Implementation with Scikit-learn

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Generate sample data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X.flatten() + np.random.randn(100)

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model = LinearRegression()
model.fit(X_train, y_train)

# Results
print(f"Slope (w): {model.coef_[0]:.4f}")
print(f"Intercept (b): {model.intercept_:.4f}")

# Evaluate
y_pred = model.predict(X_test)
print(f"MSE: {mean_squared_error(y_test, y_pred):.4f}")
print(f"R-squared: {r2_score(y_test, y_pred):.4f}")
```

### Interpreting R-squared

- **R-squared = 1.0**: Model explains all variance (perfect fit)
- **R-squared = 0.0**: Model explains none of the variance (predicts the mean)
- **R-squared < 0**: Model is worse than predicting the mean

---

## Multiple Linear Regression

Extends simple regression to **multiple features**:

```
y = w1*x1 + w2*x2 + ... + wn*xn + b
```

```python
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
data = fetch_california_housing()
X, y = data.data, data.target

# Split and scale
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

# Train
model = LinearRegression()
model.fit(X_train_s, y_train)

# Feature importance
for name, coef in zip(data.feature_names, model.coef_):
    print(f"{name:>15}: {coef:+.4f}")

y_pred = model.predict(X_test_s)
print(f"\nR-squared: {r2_score(y_test, y_pred):.4f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")
```

### Assumptions of Linear Regression

1. **Linearity**: Relationship between X and y is linear
2. **Independence**: Observations are independent of each other
3. **Homoscedasticity**: Constant variance of residuals
4. **Normality**: Residuals are normally distributed
5. **No multicollinearity**: Features are not highly correlated with each other

---

## Regularized Linear Models

When you have many features, plain linear regression can overfit. Regularization adds a
penalty term to the loss function to keep weights small.

### Ridge Regression (L2)

Adds the sum of squared weights as a penalty:

```
Loss = MSE + alpha * sum(w_i^2)
```

```python
from sklearn.linear_model import Ridge

ridge = Ridge(alpha=1.0)
ridge.fit(X_train_s, y_train)
print(f"Ridge R2: {ridge.score(X_test_s, y_test):.4f}")
```

### Lasso Regression (L1)

Adds the sum of absolute weights. Can drive coefficients to exactly zero (feature selection):

```
Loss = MSE + alpha * sum(|w_i|)
```

```python
from sklearn.linear_model import Lasso

lasso = Lasso(alpha=0.01)
lasso.fit(X_train_s, y_train)
print(f"Lasso R2: {lasso.score(X_test_s, y_test):.4f}")

# Features with non-zero coefficients
for name, coef in zip(data.feature_names, lasso.coef_):
    if coef != 0:
        print(f"  {name}: {coef:+.4f}")
```

### Elastic Net

Combines L1 and L2 penalties:

```python
from sklearn.linear_model import ElasticNet

en = ElasticNet(alpha=0.01, l1_ratio=0.5)
en.fit(X_train_s, y_train)
print(f"ElasticNet R2: {en.score(X_test_s, y_test):.4f}")
```

---

## Polynomial Regression

When the relationship between X and y is **nonlinear**, we can create polynomial features
and still use linear regression.

The idea: transform `x` into `[x, x^2, x^3, ...]` and fit a linear model on the
expanded features.

```
y = w0 + w1*x + w2*x^2 + w3*x^3 + ...
```

This is still "linear" regression because it is linear in the **weights** (w).

### Implementation

```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
import numpy as np

# Generate nonlinear data
np.random.seed(42)
X = np.sort(5 * np.random.rand(80, 1), axis=0)
y = np.sin(X).ravel() + np.random.randn(80) * 0.1

# Compare different polynomial degrees
for degree in [1, 2, 4, 10]:
    model = Pipeline([
        ('poly', PolynomialFeatures(degree=degree)),
        ('linear', LinearRegression())
    ])
    model.fit(X, y)
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    print(f"Degree {degree:>2}: MSE = {mse:.4f}")
```

### The Danger of High-Degree Polynomials

- **Degree too low**: Underfitting -- the curve cannot capture the data's shape.
- **Degree just right**: Good fit -- captures the real pattern.
- **Degree too high**: Overfitting -- the curve passes through every training point but
  performs poorly on new data. The model has memorized noise.

**Rule of thumb**: Use cross-validation to pick the best degree, and prefer lower degrees.

### Using a Pipeline

Pipelines chain preprocessing steps with a model so everything is applied consistently:

```python
from sklearn.pipeline import make_pipeline

model = make_pipeline(
    PolynomialFeatures(degree=3, include_bias=False),
    StandardScaler(),
    Ridge(alpha=0.1)
)
model.fit(X_train, y_train)
score = model.score(X_test, y_test)
```

---

## Gradient Descent (Conceptual)

For very large datasets, the closed-form OLS solution is too slow. Gradient descent
is an iterative optimization algorithm:

1. Initialize weights randomly.
2. Compute the gradient (direction of steepest increase in loss).
3. Update weights in the opposite direction: `w = w - learning_rate * gradient`.
4. Repeat until convergence.

```python
from sklearn.linear_model import SGDRegressor

# Stochastic Gradient Descent regressor
sgd = SGDRegressor(max_iter=1000, tol=1e-3, learning_rate='invscaling', random_state=42)
sgd.fit(X_train_s, y_train)
print(f"SGD R2: {sgd.score(X_test_s, y_test):.4f}")
```

**Variants:**
- **Batch GD**: Uses all data per step (slow but stable)
- **Stochastic GD**: Uses one sample per step (fast but noisy)
- **Mini-batch GD**: Uses a small batch (best of both worlds)

---

## Practical Tips

1. **Always visualize** the data before choosing a model.
2. **Scale features** when using regularization or gradient descent.
3. **Check residuals** -- they should be randomly scattered around zero.
4. **Use pipelines** to prevent data leakage and keep code clean.
5. **Start simple** with linear regression, then add complexity only if needed.

---

## Key Takeaways

1. Linear regression fits `y = wX + b` by minimizing squared errors.
2. Multiple regression extends this to many features simultaneously.
3. Regularization (Ridge, Lasso, ElasticNet) prevents overfitting by penalizing large weights.
4. Polynomial regression captures nonlinear patterns by engineering polynomial features.
5. Cross-validation is essential for choosing the right polynomial degree or alpha value.
6. Scikit-learn Pipelines chain preprocessing and modeling into a single reproducible object.
