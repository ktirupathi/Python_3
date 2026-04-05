# Day 27: Model Selection -- Cross Validation & Hyperparameter Tuning

## Why Model Selection Matters

Choosing the right model and its optimal hyperparameters is the difference between a
mediocre and a high-performing ML system. A single train-test split can be misleading --
the results depend heavily on which samples end up in which set.

---

## Cross-Validation

### K-Fold Cross-Validation

Instead of a single train-test split, K-Fold divides the data into K equal parts (folds).
The model is trained K times, each time using K-1 folds for training and 1 fold for
validation. The final score is the average across all K folds.

```
Fold 1: [VAL] [Train] [Train] [Train] [Train]
Fold 2: [Train] [VAL] [Train] [Train] [Train]
Fold 3: [Train] [Train] [VAL] [Train] [Train]
Fold 4: [Train] [Train] [Train] [VAL] [Train]
Fold 5: [Train] [Train] [Train] [Train] [VAL]
```

**Typical K values:** 5 or 10.

### Implementation

```python
from sklearn.model_selection import cross_val_score, cross_validate
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
X, y = data.data, data.target

model = RandomForestClassifier(n_estimators=100, random_state=42)

# Simple cross-validation
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print(f"Accuracy: {scores.mean():.4f} (+/- {scores.std():.4f})")
print(f"Individual folds: {scores}")

# Multiple metrics at once
results = cross_validate(model, X, y, cv=5,
                         scoring=['accuracy', 'f1', 'roc_auc'],
                         return_train_score=True)

for metric in ['accuracy', 'f1', 'roc_auc']:
    train = results[f'train_{metric}'].mean()
    test = results[f'test_{metric}'].mean()
    print(f"{metric:>10}: Train={train:.4f}, Test={test:.4f}")
```

### Stratified K-Fold

For classification, regular K-Fold might create folds with uneven class distributions.
**Stratified K-Fold** ensures each fold has roughly the same class proportions as the
full dataset. Scikit-learn uses this by default for classifiers.

```python
from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

for fold, (train_idx, val_idx) in enumerate(skf.split(X, y)):
    X_train, X_val = X[train_idx], X[val_idx]
    y_train, y_val = y[train_idx], y[val_idx]
    model.fit(X_train, y_train)
    score = model.score(X_val, y_val)
    print(f"Fold {fold+1}: {score:.4f} (val size: {len(val_idx)})")
```

### Other Cross-Validation Strategies

```python
from sklearn.model_selection import (
    LeaveOneOut, RepeatedKFold, TimeSeriesSplit
)

# Leave-One-Out: K = n_samples (expensive but thorough)
loo = LeaveOneOut()

# Repeated K-Fold: runs K-Fold multiple times with different splits
rkf = RepeatedKFold(n_splits=5, n_repeats=3, random_state=42)

# Time Series Split: respects temporal order (no future data leakage)
tscv = TimeSeriesSplit(n_splits=5)
```

**Time Series Split** is critical for time-ordered data. Standard K-Fold would leak
future information into training, giving unrealistically good results.

---

## Hyperparameter Tuning

**Parameters** are learned during training (weights, splits).
**Hyperparameters** are set before training (learning_rate, max_depth, n_estimators).

### Grid Search

Exhaustively tries every combination of hyperparameter values:

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 10, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,          # Use all CPU cores
    verbose=1
)

grid_search.fit(X, y)

print(f"Best score: {grid_search.best_score_:.4f}")
print(f"Best params: {grid_search.best_params_}")

# Access the best model directly
best_model = grid_search.best_estimator_
```

**Total combinations** = 3 x 4 x 3 x 3 = 108 models, each with 5-fold CV = 540 fits!

### Randomized Search

When the search space is large, try random combinations instead:

```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform

param_distributions = {
    'n_estimators': randint(50, 500),
    'max_depth': randint(3, 20),
    'min_samples_split': randint(2, 20),
    'min_samples_leaf': randint(1, 10),
    'max_features': uniform(0.1, 0.9)
}

random_search = RandomizedSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_distributions=param_distributions,
    n_iter=50,          # Try 50 random combinations
    cv=5,
    scoring='accuracy',
    random_state=42,
    n_jobs=-1
)

random_search.fit(X, y)

print(f"Best score: {random_search.best_score_:.4f}")
print(f"Best params: {random_search.best_params_}")
```

**Randomized search** is usually preferred because:
- Much faster for large search spaces
- Not all hyperparameters are equally important
- Often finds equally good or better results

### Analyzing Search Results

```python
import pandas as pd

results = pd.DataFrame(random_search.cv_results_)
results = results.sort_values('rank_test_score')

print(results[['params', 'mean_test_score', 'std_test_score', 'rank_test_score']].head(10))
```

---

## Pipeline + GridSearch

Combine preprocessing and model tuning in a single search:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA()),
    ('svc', SVC())
])

param_grid = {
    'pca__n_components': [5, 10, 20, 30],
    'svc__C': [0.01, 0.1, 1, 10],
    'svc__kernel': ['rbf', 'linear'],
    'svc__gamma': ['scale', 'auto']
}

grid = GridSearchCV(pipe, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid.fit(X, y)

print(f"Best score: {grid.best_score_:.4f}")
print(f"Best params: {grid.best_params_}")
```

Note the double-underscore syntax: `step_name__parameter_name`.

---

## Learning Curves

Diagnose whether your model suffers from high bias or high variance:

```python
from sklearn.model_selection import learning_curve

train_sizes, train_scores, val_scores = learning_curve(
    RandomForestClassifier(n_estimators=100, random_state=42),
    X, y, cv=5,
    train_sizes=np.linspace(0.1, 1.0, 10),
    scoring='accuracy',
    n_jobs=-1
)

train_mean = train_scores.mean(axis=1)
val_mean = val_scores.mean(axis=1)
train_std = train_scores.std(axis=1)
val_std = val_scores.std(axis=1)

plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.1)
plt.fill_between(train_sizes, val_mean - val_std, val_mean + val_std, alpha=0.1)
plt.plot(train_sizes, train_mean, 'o-', label='Training')
plt.plot(train_sizes, val_mean, 'o-', label='Validation')
plt.xlabel('Training Set Size')
plt.ylabel('Accuracy')
plt.title('Learning Curves')
plt.legend()
plt.show()
```

**Interpretation:**
- Large gap between train and val = **overfitting** (more data or simpler model)
- Both curves plateau at low score = **underfitting** (more complex model or features)
- Curves converge at high score = **good fit**

---

## Validation Curves

See how a single hyperparameter affects performance:

```python
from sklearn.model_selection import validation_curve

param_range = [1, 2, 5, 10, 20, 50, None]
train_scores, val_scores = validation_curve(
    DecisionTreeClassifier(random_state=42),
    X, y,
    param_name='max_depth',
    param_range=param_range,
    cv=5,
    scoring='accuracy'
)

plt.plot(range(len(param_range)), train_scores.mean(axis=1), 'o-', label='Training')
plt.plot(range(len(param_range)), val_scores.mean(axis=1), 'o-', label='Validation')
plt.xticks(range(len(param_range)), param_range)
plt.xlabel('max_depth')
plt.ylabel('Accuracy')
plt.title('Validation Curve')
plt.legend()
plt.show()
```

---

## Model Comparison Best Practices

```python
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import (RandomForestClassifier,
                               GradientBoostingClassifier)
from sklearn.neighbors import KNeighborsClassifier

models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'KNN': KNeighborsClassifier(),
    'SVM': SVC(),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'Gradient Boosting': GradientBoostingClassifier(random_state=42),
}

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

for name, model in models.items():
    pipe = make_pipeline(StandardScaler(), model)
    scores = cross_val_score(pipe, X, y, cv=5, scoring='accuracy')
    print(f"{name:>22}: {scores.mean():.4f} (+/- {scores.std():.4f})")
```

---

## Nested Cross-Validation

For an **unbiased estimate** of model performance when tuning hyperparameters:

```python
from sklearn.model_selection import cross_val_score, GridSearchCV

# Inner loop: tune hyperparameters
inner_cv = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid={'n_estimators': [50, 100], 'max_depth': [5, 10]},
    cv=3, scoring='accuracy', n_jobs=-1
)

# Outer loop: estimate performance
outer_scores = cross_val_score(inner_cv, X, y, cv=5, scoring='accuracy')
print(f"Nested CV: {outer_scores.mean():.4f} (+/- {outer_scores.std():.4f})")
```

---

## Key Takeaways

1. **Never evaluate on training data.** Use cross-validation for reliable estimates.
2. Stratified K-Fold preserves class proportions; use TimeSeriesSplit for temporal data.
3. **Grid Search** is exhaustive; **Randomized Search** is faster and often equally effective.
4. Use Pipelines with GridSearch to tune preprocessing and model together.
5. Learning curves diagnose overfitting vs underfitting.
6. Validation curves show how one hyperparameter affects performance.
7. Nested cross-validation gives an unbiased performance estimate when tuning.
