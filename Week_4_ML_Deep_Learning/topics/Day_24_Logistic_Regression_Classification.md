# Day 24: Logistic Regression & Classification Metrics

## From Regression to Classification

While linear regression predicts continuous values, **logistic regression** predicts the
probability that an input belongs to a particular class. Despite its name, logistic
regression is a **classification** algorithm.

---

## The Logistic (Sigmoid) Function

The sigmoid function maps any real number to the range (0, 1):

```
sigma(z) = 1 / (1 + e^(-z))
```

Properties:
- When z is very negative, sigma(z) approaches 0
- When z is very positive, sigma(z) approaches 1
- When z = 0, sigma(z) = 0.5

```python
import numpy as np
import matplotlib.pyplot as plt

z = np.linspace(-10, 10, 200)
sigmoid = 1 / (1 + np.exp(-z))

plt.plot(z, sigmoid)
plt.axhline(y=0.5, color='r', linestyle='--', label='Decision boundary')
plt.xlabel('z')
plt.ylabel('sigma(z)')
plt.title('Sigmoid Function')
plt.legend()
plt.grid(True)
plt.show()
```

---

## How Logistic Regression Works

1. Compute a linear combination: `z = w1*x1 + w2*x2 + ... + b`
2. Pass through the sigmoid: `P(y=1) = sigma(z)`
3. Classify using a threshold (default 0.5):
   - If P(y=1) >= 0.5, predict class 1
   - If P(y=1) < 0.5, predict class 0

### The Loss Function: Log Loss (Binary Cross-Entropy)

Unlike linear regression's MSE, logistic regression minimizes **log loss**:

```
Loss = -1/n * sum[ y*log(p) + (1-y)*log(1-p) ]
```

This penalizes confident wrong predictions heavily.

---

## Binary Classification with Scikit-learn

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load data
data = load_breast_cancer()
X, y = data.data, data.target

# Split and scale
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

# Train
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train_s, y_train)

# Predict
y_pred = model.predict(X_test_s)
y_prob = model.predict_proba(X_test_s)  # Probabilities for each class

print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Sample probabilities:\n{y_prob[:5]}")
```

---

## Multiclass Classification

Logistic regression extends to multiple classes via:

- **One-vs-Rest (OvR)**: Train one binary classifier per class.
- **Multinomial (Softmax)**: Generalize the sigmoid to multiple classes simultaneously.

```python
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42
)

# Multinomial logistic regression
model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000)
model.fit(X_train, y_train)
print(f"Accuracy: {model.score(X_test, y_test):.4f}")

# Predict probabilities for all 3 classes
probs = model.predict_proba(X_test[:3])
for i, p in enumerate(probs):
    print(f"Sample {i}: {dict(zip(iris.target_names, p.round(3)))}")
```

---

## Classification Metrics In Depth

Accuracy alone is often misleading, especially with **imbalanced datasets**. If 95% of
emails are not spam, a model that always predicts "not spam" gets 95% accuracy but
catches zero spam.

### The Confusion Matrix

```
                    Predicted
                 Positive  Negative
Actual Positive    TP         FN
Actual Negative    FP         TN
```

- **TP** (True Positive): Correctly predicted positive
- **TN** (True Negative): Correctly predicted negative
- **FP** (False Positive): Incorrectly predicted positive (Type I error)
- **FN** (False Negative): Incorrectly predicted negative (Type II error)

```python
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

cm = confusion_matrix(y_test, y_pred)
print(cm)

# Visual display
disp = ConfusionMatrixDisplay(cm, display_labels=data.target_names)
disp.plot(cmap='Blues')
plt.show()
```

### Precision, Recall, and F1

```
Precision = TP / (TP + FP)   -- "Of what I predicted positive, how many truly are?"
Recall    = TP / (TP + FN)   -- "Of all actual positives, how many did I catch?"
F1        = 2 * (Precision * Recall) / (Precision + Recall)
```

**When to prioritize which:**
- **Precision**: When false positives are costly (spam filter -- don't flag real emails)
- **Recall**: When false negatives are costly (cancer detection -- don't miss a case)
- **F1**: When you need a balance

```python
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import classification_report

print(f"Precision: {precision_score(y_test, y_pred):.4f}")
print(f"Recall:    {recall_score(y_test, y_pred):.4f}")
print(f"F1 Score:  {f1_score(y_test, y_pred):.4f}")

# Full report
print(classification_report(y_test, y_pred, target_names=data.target_names))
```

### ROC Curve and AUC

The **Receiver Operating Characteristic** curve plots True Positive Rate vs False Positive
Rate at every classification threshold.

- **AUC** (Area Under Curve): Ranges from 0.5 (random) to 1.0 (perfect).

```python
from sklearn.metrics import roc_curve, roc_auc_score

y_scores = model.predict_proba(X_test_s)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_scores)
auc = roc_auc_score(y_test, y_scores)

plt.plot(fpr, tpr, label=f'AUC = {auc:.3f}')
plt.plot([0, 1], [0, 1], 'k--', label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()
```

### Precision-Recall Curve

More informative than ROC for imbalanced datasets:

```python
from sklearn.metrics import precision_recall_curve, average_precision_score

precision, recall, thresholds = precision_recall_curve(y_test, y_scores)
ap = average_precision_score(y_test, y_scores)

plt.plot(recall, precision, label=f'AP = {ap:.3f}')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend()
plt.show()
```

---

## Handling Imbalanced Datasets

When one class vastly outnumbers the other:

### 1. Class Weights

```python
model = LogisticRegression(class_weight='balanced', max_iter=1000)
model.fit(X_train_s, y_train)
```

### 2. Resampling

```python
# Oversampling the minority class (conceptual)
from sklearn.utils import resample

X_minority_upsampled = resample(
    X_train[y_train == 1],
    replace=True,
    n_samples=sum(y_train == 0),
    random_state=42
)
```

### 3. Threshold Tuning

Instead of the default 0.5 threshold, choose one that maximizes your target metric:

```python
# Find optimal threshold for F1
from sklearn.metrics import f1_score

best_f1, best_thresh = 0, 0
for thresh in np.arange(0.1, 0.9, 0.01):
    y_pred_t = (y_scores >= thresh).astype(int)
    f1 = f1_score(y_test, y_pred_t)
    if f1 > best_f1:
        best_f1, best_thresh = f1, thresh

print(f"Best threshold: {best_thresh:.2f}, F1: {best_f1:.4f}")
```

---

## Regularization in Logistic Regression

Logistic regression in sklearn includes regularization by default via the `C` parameter:

- **C** = inverse of regularization strength (smaller C = stronger regularization)
- `penalty='l2'` (default): Ridge-style
- `penalty='l1'`: Lasso-style (requires solver='liblinear' or 'saga')

```python
for C in [0.001, 0.01, 0.1, 1, 10, 100]:
    model = LogisticRegression(C=C, max_iter=1000, random_state=42)
    model.fit(X_train_s, y_train)
    train_acc = model.score(X_train_s, y_train)
    test_acc = model.score(X_test_s, y_test)
    print(f"C={C:<6} Train: {train_acc:.4f}  Test: {test_acc:.4f}")
```

---

## Key Takeaways

1. Logistic regression predicts class probabilities using the sigmoid function.
2. It minimizes log loss (binary cross-entropy), not MSE.
3. Accuracy is insufficient for imbalanced datasets -- use precision, recall, F1, and AUC.
4. The confusion matrix is the foundation for understanding classification errors.
5. ROC-AUC evaluates performance across all thresholds; precision-recall curve is better
   for imbalanced problems.
6. Class weights, resampling, and threshold tuning address class imbalance.
7. The `C` parameter controls regularization strength in sklearn's LogisticRegression.
