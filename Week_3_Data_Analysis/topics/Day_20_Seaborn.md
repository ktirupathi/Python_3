# Day 20: Seaborn — Statistical Plots, Heatmaps, Pair Plots

## Introduction

Seaborn is a statistical data visualization library built on top of Matplotlib. It
provides a high-level interface for creating attractive and informative plots with
minimal code. Seaborn is tightly integrated with Pandas DataFrames and automatically
handles many formatting details that require manual effort in Matplotlib.

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set the default style
sns.set_theme(style='whitegrid')
```

---

## 1. Seaborn vs Matplotlib

| Feature                | Matplotlib                    | Seaborn                        |
|------------------------|-------------------------------|--------------------------------|
| Level of abstraction   | Low (full control)            | High (smart defaults)          |
| Input format           | Arrays, lists                 | DataFrames (column names)      |
| Statistical features   | Manual                        | Built-in (CI, regression, KDE) |
| Styling                | Requires effort               | Beautiful by default           |
| Complex plots          | Many lines of code            | One function call              |

Seaborn does not replace Matplotlib; it builds on it. You can always use Matplotlib
commands to customize Seaborn plots.

---

## 2. Built-in Datasets

Seaborn comes with several classic datasets for learning.

```python
# Available datasets
print(sns.get_dataset_names())

# Load a dataset
tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')
penguins = sns.load_dataset('penguins')
titanic = sns.load_dataset('titanic')

print(tips.head())
# total_bill  tip  sex   smoker day  time   size
# 16.99      1.01  Female No   Sun  Dinner   2
# 10.34      1.66  Male   No   Sun  Dinner   3
# ...
```

---

## 3. Distribution Plots

### Histogram (histplot)

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Basic histogram
sns.histplot(data=tips, x='total_bill', bins=20, ax=axes[0])
axes[0].set_title('Basic Histogram')

# With KDE overlay
sns.histplot(data=tips, x='total_bill', kde=True, ax=axes[1])
axes[1].set_title('Histogram + KDE')

# Grouped by category
sns.histplot(data=tips, x='total_bill', hue='sex', multiple='dodge', ax=axes[2])
axes[2].set_title('Grouped Histogram')

plt.tight_layout()
plt.show()
```

### KDE Plot (Kernel Density Estimate)

```python
fig, ax = plt.subplots(figsize=(8, 5))
sns.kdeplot(data=tips, x='total_bill', hue='time', fill=True, alpha=0.4)
ax.set_title('KDE: Bill Distribution by Meal Time')
plt.show()
```

### Box Plot

Box plots show the median, quartiles, and outliers of a distribution.

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Basic box plot
sns.boxplot(data=tips, x='day', y='total_bill', ax=axes[0])
axes[0].set_title('Box Plot')

# Grouped box plot
sns.boxplot(data=tips, x='day', y='total_bill', hue='sex', ax=axes[1])
axes[1].set_title('Grouped Box Plot')

plt.tight_layout()
plt.show()
```

### Violin Plot

Combines a box plot with a KDE, showing the full distribution shape.

```python
fig, ax = plt.subplots(figsize=(10, 6))
sns.violinplot(data=tips, x='day', y='total_bill', hue='sex',
               split=True, inner='quartile')
ax.set_title('Violin Plot: Bill Distribution by Day and Gender')
plt.show()
```

### Strip and Swarm Plots

Show individual data points.

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Strip plot (jittered points)
sns.stripplot(data=tips, x='day', y='total_bill', alpha=0.5, ax=axes[0])
axes[0].set_title('Strip Plot')

# Swarm plot (non-overlapping points)
sns.swarmplot(data=tips, x='day', y='total_bill', size=4, ax=axes[1])
axes[1].set_title('Swarm Plot')

plt.tight_layout()
plt.show()
```

### Combining Box and Strip Plots

```python
fig, ax = plt.subplots(figsize=(8, 6))
sns.boxplot(data=tips, x='day', y='total_bill', color='lightblue')
sns.stripplot(data=tips, x='day', y='total_bill', color='black', alpha=0.3, size=3)
ax.set_title('Box + Strip Overlay')
plt.show()
```

---

## 4. Relational Plots

### Scatter Plot (scatterplot)

```python
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(data=tips, x='total_bill', y='tip',
                hue='time', size='size', style='sex',
                sizes=(20, 200), alpha=0.7)
ax.set_title('Tips vs Total Bill')
plt.show()
```

### Line Plot (lineplot)

```python
# Simulate time series data
fmri = sns.load_dataset('fmri')

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=fmri, x='timepoint', y='signal',
             hue='region', style='event',
             markers=True, dashes=True)
ax.set_title('FMRI Signal Over Time')
plt.show()
```

Seaborn automatically computes the mean and 95% confidence interval when there are
multiple observations per x-value.

### Regression Plot (regplot / lmplot)

```python
# Simple regression
fig, ax = plt.subplots(figsize=(8, 6))
sns.regplot(data=tips, x='total_bill', y='tip', scatter_kws={'alpha': 0.5})
ax.set_title('Linear Regression: Tip vs Bill')
plt.show()

# lmplot — supports faceting by category
g = sns.lmplot(data=tips, x='total_bill', y='tip',
               col='time', hue='sex', height=5, aspect=1.2)
g.fig.suptitle('Regression by Time and Gender', y=1.02)
plt.show()
```

---

## 5. Categorical Plots

### Count Plot (bar chart of frequencies)

```python
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(data=tips, x='day', hue='sex', order=['Thur', 'Fri', 'Sat', 'Sun'])
ax.set_title('Visit Count by Day and Gender')
plt.show()
```

### Bar Plot (mean + confidence interval)

```python
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=tips, x='day', y='total_bill', hue='sex',
            estimator=np.mean, errorbar='ci')
ax.set_title('Average Bill by Day and Gender (with 95% CI)')
plt.show()
```

### Point Plot

Like a bar plot but uses points and lines, making it easy to compare across groups.

```python
fig, ax = plt.subplots(figsize=(8, 5))
sns.pointplot(data=tips, x='day', y='total_bill', hue='sex',
              markers=['o', 's'], linestyles=['-', '--'])
ax.set_title('Average Bill by Day and Gender')
plt.show()
```

---

## 6. Heatmaps

Heatmaps are used to visualize matrices (correlation matrices, pivot tables,
confusion matrices).

### Correlation Heatmap

```python
# Compute correlation matrix
numeric_tips = tips.select_dtypes(include=[np.number])
corr = numeric_tips.corr()

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm',
            center=0, square=True, linewidths=0.5,
            vmin=-1, vmax=1,
            cbar_kws={'shrink': 0.8})
ax.set_title('Correlation Heatmap')
plt.tight_layout()
plt.show()
```

### Pivot Table Heatmap

```python
# Create a pivot table first
pivot = tips.pivot_table(values='total_bill', index='day', columns='time',
                         aggfunc='mean')

fig, ax = plt.subplots(figsize=(6, 4))
sns.heatmap(pivot, annot=True, fmt='.1f', cmap='YlOrRd', linewidths=1)
ax.set_title('Average Bill: Day vs Time')
plt.show()
```

### Custom Heatmap (Confusion Matrix)

```python
confusion = np.array([[50, 5, 2],
                       [3, 45, 8],
                       [1, 6, 40]])
labels = ['Cat', 'Dog', 'Bird']

fig, ax = plt.subplots(figsize=(6, 5))
sns.heatmap(confusion, annot=True, fmt='d', cmap='Blues',
            xticklabels=labels, yticklabels=labels)
ax.set_xlabel('Predicted')
ax.set_ylabel('Actual')
ax.set_title('Confusion Matrix')
plt.tight_layout()
plt.show()
```

---

## 7. Pair Plots

Pair plots create a grid of scatter plots for every pair of numeric variables,
with histograms (or KDEs) on the diagonal. They are extremely useful for initial
data exploration.

```python
# Basic pair plot
sns.pairplot(iris, hue='species', diag_kind='kde', height=2.5)
plt.suptitle('Iris Dataset — Pairwise Relationships', y=1.02)
plt.show()
```

### Customized Pair Plot

```python
g = sns.pairplot(iris, hue='species',
                 vars=['sepal_length', 'sepal_width', 'petal_length'],
                 diag_kind='hist',
                 plot_kws={'alpha': 0.6, 's': 30},
                 diag_kws={'bins': 15})
plt.show()
```

### PairGrid for Full Control

```python
g = sns.PairGrid(iris, hue='species', diag_sharey=False)
g.map_upper(sns.scatterplot, alpha=0.5)
g.map_lower(sns.kdeplot, fill=True, alpha=0.3)
g.map_diag(sns.histplot, kde=True)
g.add_legend()
plt.show()
```

---

## 8. Joint Plot

Combines a scatter plot (or other bivariate plot) with marginal distributions.

```python
g = sns.jointplot(data=tips, x='total_bill', y='tip',
                  kind='reg', height=7,
                  marginal_kws={'bins': 20})
g.fig.suptitle('Joint Distribution: Bill vs Tip', y=1.02)
plt.show()

# Other kinds: 'scatter', 'kde', 'hex', 'hist', 'reg'
```

---

## 9. FacetGrid — Small Multiples

FacetGrid creates a grid of plots based on categorical variables.

```python
g = sns.FacetGrid(tips, col='time', row='sex', hue='smoker',
                  height=4, aspect=1.2, margin_titles=True)
g.map(sns.scatterplot, 'total_bill', 'tip', alpha=0.7)
g.add_legend()
g.fig.suptitle('Tips Faceted by Time, Gender, and Smoking Status', y=1.02)
plt.show()
```

### catplot — Built-in Faceting for Categorical Plots

```python
g = sns.catplot(data=tips, x='day', y='total_bill',
                col='time', kind='box', height=5, aspect=0.8)
g.fig.suptitle('Bill Distribution by Day and Meal Time', y=1.02)
plt.show()

# kind options: 'strip', 'swarm', 'box', 'violin', 'boxen', 'point', 'bar', 'count'
```

---

## 10. Styling and Themes

```python
# Built-in themes
sns.set_theme(style='whitegrid')   # white background with grid
sns.set_theme(style='darkgrid')    # gray background with grid
sns.set_theme(style='white')       # white, no grid
sns.set_theme(style='dark')        # gray, no grid
sns.set_theme(style='ticks')       # white with tick marks

# Color palettes
sns.set_palette('Set2')            # qualitative
sns.set_palette('Blues')           # sequential
sns.set_palette('coolwarm')        # diverging

# Custom palette
custom = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12']
sns.set_palette(custom)

# View a palette
sns.palplot(sns.color_palette('Set2', 8))
plt.show()

# Context scaling (controls element sizes)
sns.set_context('paper')           # small elements
sns.set_context('notebook')        # default
sns.set_context('talk')            # larger (for presentations)
sns.set_context('poster')          # largest
```

### Removing Spines

```python
fig, ax = plt.subplots()
sns.boxplot(data=tips, x='day', y='total_bill')
sns.despine()  # remove top and right spines
# sns.despine(left=True, bottom=True)  # remove more spines
plt.show()
```

---

## 11. When to Use Which Plot

| Goal                                  | Plot Type                     |
|---------------------------------------|-------------------------------|
| Distribution of one variable          | histplot, kdeplot             |
| Compare distributions across groups   | boxplot, violinplot           |
| Show individual points by category    | stripplot, swarmplot          |
| Relationship between two variables    | scatterplot, regplot          |
| Trend over time                       | lineplot                      |
| Frequency of categories              | countplot                     |
| Aggregate by category                | barplot, pointplot            |
| Correlation matrix                   | heatmap                       |
| All pairwise relationships           | pairplot, PairGrid            |
| Bivariate + marginals                | jointplot                     |
| Small multiples                      | FacetGrid, catplot            |

---

## Key Takeaways

- Seaborn produces attractive statistical plots with minimal code.
- It works natively with Pandas DataFrames and column names.
- Distribution plots (histplot, boxplot, violinplot) reveal spread and outliers.
- Relational plots (scatterplot, regplot, lineplot) show variable relationships.
- Heatmaps excel at displaying matrices (correlations, confusion, pivot tables).
- Pair plots give an instant overview of all pairwise relationships in a dataset.
- FacetGrid and catplot create small multiples for multi-dimensional exploration.
- Seaborn is for exploration and presentation; fall back to Matplotlib for pixel-level
  customization.

---

*Next: Day 21 — Exploratory Data Analysis: A Complete Walkthrough.*
