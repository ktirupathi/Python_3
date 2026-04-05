# Day 25: Decision Trees, Random Forest, and Ensemble Methods

## Decision Trees

A decision tree learns a series of if-then rules to split data into groups. It is one
of the most intuitive ML algorithms -- you can literally visualize and explain each
decision.

### How a Decision Tree Works

1. Start with the entire dataset at the root node.
2. Find the feature and threshold that best splits the data.
3. Create two child nodes based on the split.
4. Repeat recursively for each child until a stopping condition is met.

### Splitting Criteria

**For Classification:**
- **Gini Impurity**: Measures how often a randomly chosen element would be misclassified.
  `Gini = 1 - sum(p_i^2)` where p_i is the probability of class i.
- **Entropy / Information Gain**: Measures the reduction in uncertainty.
  `Entropy = -sum(p_i * log2(p_i))`

**For Regression:**
- **MSE**: Splits that minimize the mean squared error in each child node.

### Implementation

```python
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42
)

# Train
tree = DecisionTreeClassifier(max_depth=3, random_state=42)
tree.fit(X_train, y_train)

# View the rules
print(export_text(tree, feature_names=iris.feature_names))

# Evaluate
print(f"Train accuracy: {tree.score(X_train, y_train):.4f}")
print(f"Test accuracy:  {tree.score(X_test, y_test):.4f}")
```

### Visualizing a Decision Tree

```python
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(15, 8))
plot_tree(tree, feature_names=iris.feature_names,
          class_names=iris.target_names, filled=True, rounded=True)
plt.tight_layout()
plt.show()
```

### Controlling Tree Complexity

| Parameter | Description | Effect |
|-----------|-------------|--------|
| `max_depth` | Maximum depth of tree | Lower = simpler |
| `min_samples_split` | Min samples to split a node | Higher = simpler |
| `min_samples_leaf` | Min samples in a leaf | Higher = simpler |
| `max_features` | Max features per split | Lower = more random |
| `max_leaf_nodes` | Max number of leaves | Lower = simpler |

```python
# An unrestricted tree will overfit
tree_full = DecisionTreeClassifier(random_state=42)
tree_full.fit(X_train, y_train)
print(f"Unrestricted - Train: {tree_full.score(X_train, y_train):.4f}, "
      f"Test: {tree_full.score(X_test, y_test):.4f}")

# A pruned tree generalizes better
tree_pruned = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=42)
tree_pruned.fit(X_train, y_train)
print(f"Pruned       - Train: {tree_pruned.score(X_train, y_train):.4f}, "
      f"Test: {tree_pruned.score(X_test, y_test):.4f}")
```

### Feature Importance

Decision trees naturally rank features by how much they reduce impurity:

```python
import numpy as np

importances = tree.feature_importances_
indices = np.argsort(importances)[::-1]

for i in indices:
    print(f"{iris.feature_names[i]:>20}: {importances[i]:.4f}")
```

---

## Ensemble Methods: Why Combine Models?

A single decision tree is prone to overfitting and high variance. Ensemble methods
combine multiple models to produce a stronger, more stable predictor.

**Key insight:** A committee of diverse "weak" models often outperforms a single "strong" model.

### Types of Ensembles

1. **Bagging** (Bootstrap Aggregating): Train many models on random subsets, average results.
2. **Boosting**: Train models sequentially, each correcting the previous one's errors.
3. **Stacking**: Train different types of models, then train a meta-model on their outputs.

---

## Random Forest

Random Forest = Bagging + Random Feature Selection applied to decision trees.

**How it works:**
1. Create N bootstrap samples (random subsets with replacement) from the training data.
2. Train a decision tree on each sample, but at each split consider only a random
   subset of features (typically sqrt(total_features) for classification).
3. For classification: each tree votes, majority wins.
4. For regression: average the predictions.

### Implementation

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42
)

rf = RandomForestClassifier(
    n_estimators=100,      # Number of trees
    max_depth=10,          # Max depth per tree
    random_state=42,
    n_jobs=-1              # Use all CPU cores
)
rf.fit(X_train, y_train)

print(f"Train accuracy: {rf.score(X_train, y_train):.4f}")
print(f"Test accuracy:  {rf.score(X_test, y_test):.4f}")
print(classification_report(y_test, rf.predict(X_test), target_names=data.target_names))
```

### Feature Importance in Random Forest

```python
importances = rf.feature_importances_
indices = np.argsort(importances)[::-1][:10]

plt.figure(figsize=(10, 5))
plt.bar(range(10), importances[indices])
plt.xticks(range(10), [data.feature_names[i] for i in indices], rotation=45, ha='right')
plt.title('Top 10 Feature Importances')
plt.tight_layout()
plt.show()
```

---

## Gradient Boosting

Instead of training trees in parallel (bagging), boosting trains them **sequentially**.
Each new tree focuses on the errors of the combined previous trees.

### Gradient Boosted Trees

```python
from sklearn.ensemble import GradientBoostingClassifier

gb = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,     # Shrinkage: how much each tree contributes
    max_depth=3,
    random_state=42
)
gb.fit(X_train, y_train)

print(f"Train accuracy: {gb.score(X_train, y_train):.4f}")
print(f"Test accuracy:  {gb.score(X_test, y_test):.4f}")
```

### Key Hyperparameters for Gradient Boosting

- `n_estimators`: Number of boosting stages (trees)
- `learning_rate`: Shrinks contribution of each tree. Lower values need more trees.
- `max_depth`: Depth of each tree (usually 3-8 for boosting)
- `subsample`: Fraction of samples used per tree (stochastic boosting)

### XGBoost and LightGBM (Industry Standards)

```python
# XGBoost (install: pip install xgboost)
# from xgboost import XGBClassifier
# xgb = XGBClassifier(n_estimators=100, learning_rate=0.1, max_depth=3)
# xgb.fit(X_train, y_train)

# LightGBM (install: pip install lightgbm)
# from lightgbm import LGBMClassifier
# lgbm = LGBMClassifier(n_estimators=100, learning_rate=0.1, max_depth=3)
# lgbm.fit(X_train, y_train)
```

---

## AdaBoost

Adaptive Boosting assigns **weights to samples**. Misclassified samples get higher
weights so the next model pays more attention to them.

```python
from sklearn.ensemble import AdaBoostClassifier

ada = AdaBoostClassifier(
    n_estimators=100,
    learning_rate=0.5,
    random_state=42
)
ada.fit(X_train, y_train)
print(f"AdaBoost accuracy: {ada.score(X_test, y_test):.4f}")
```

---

## Voting Classifier (Stacking Lite)

Combine different model types:

```python
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

voting = VotingClassifier(
    estimators=[
        ('lr', LogisticRegression(max_iter=1000)),
        ('rf', RandomForestClassifier(n_estimators=50, random_state=42)),
        ('svc', SVC(probability=True))
    ],
    voting='soft'  # Use predicted probabilities
)
voting.fit(X_train, y_train)
print(f"Voting accuracy: {voting.score(X_test, y_test):.4f}")
```

---

## Comparing Models

```python
from sklearn.model_selection import cross_val_score

models = {
    'Decision Tree': DecisionTreeClassifier(max_depth=5, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'Gradient Boost': GradientBoostingClassifier(n_estimators=100, random_state=42),
    'AdaBoost': AdaBoostClassifier(n_estimators=100, random_state=42),
}

for name, model in models.items():
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
    print(f"{name:>16}: {scores.mean():.4f} (+/- {scores.std():.4f})")
```

---

## When to Use What

| Algorithm | Strengths | Weaknesses |
|-----------|-----------|------------|
| Decision Tree | Interpretable, fast | Overfits easily |
| Random Forest | Robust, handles noise | Slower, less interpretable |
| Gradient Boost | Often best accuracy | Slow training, sensitive to tuning |
| AdaBoost | Simple, effective | Sensitive to outliers |

---

## Key Takeaways

1. Decision trees split data using impurity measures (Gini, entropy) and are fully interpretable.
2. Control overfitting with max_depth, min_samples_leaf, and other pruning parameters.
3. Random Forest reduces variance by averaging many decorrelated trees (bagging + feature randomness).
4. Gradient Boosting reduces bias by sequentially correcting errors (boosting).
5. Ensemble methods almost always outperform single models.
6. Feature importance from tree-based models helps with feature selection and interpretation.
7. XGBoost and LightGBM are industry-standard boosting libraries for competitions and production.
