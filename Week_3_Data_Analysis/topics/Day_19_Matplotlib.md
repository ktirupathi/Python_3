# Day 19: Matplotlib — Line, Bar, Scatter, Histogram, Subplots

## Introduction

Matplotlib is the foundational plotting library in Python. While higher-level libraries
like Seaborn and Plotly build on top of it, understanding Matplotlib gives you full
control over every element of your visualizations. It is the go-to tool for creating
publication-quality figures.

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
```

---

## 1. The Two Interfaces

Matplotlib offers two ways to create plots:

### Pyplot Interface (State-based, quick plots)

```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Quick Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
```

### Object-Oriented Interface (Recommended for complex plots)

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 9, 16])
ax.set_title('OO Plot')
ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.show()
```

The object-oriented interface gives you explicit control over figures and axes,
making it easier to create multi-panel plots and customize every detail.

---

## 2. Line Plots

Line plots are ideal for showing trends over time or continuous data.

```python
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x, y1, label='sin(x)', color='blue', linewidth=2, linestyle='-')
ax.plot(x, y2, label='cos(x)', color='red', linewidth=2, linestyle='--')

ax.set_title('Trigonometric Functions', fontsize=16, fontweight='bold')
ax.set_xlabel('x (radians)', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.legend(fontsize=12)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)

plt.tight_layout()
plt.savefig('trig_functions.png', dpi=300, bbox_inches='tight')
plt.show()
```

### Line Styles and Markers

```python
# Common line styles: '-', '--', '-.', ':'
# Common markers: 'o', 's', '^', 'D', 'v', '*', '+', 'x'

fig, ax = plt.subplots(figsize=(8, 5))
x = np.arange(1, 6)

ax.plot(x, x, 'o-', label='linear', markersize=8)
ax.plot(x, x**2, 's--', label='quadratic', markersize=8)
ax.plot(x, x**3, '^-.', label='cubic', markersize=8)

ax.legend()
plt.show()
```

---

## 3. Bar Charts

Bar charts are used for comparing quantities across categories.

### Vertical Bar Chart

```python
categories = ['Python', 'JavaScript', 'Java', 'C++', 'Rust']
popularity = [30, 25, 20, 15, 10]
colors = ['#3776ab', '#f7df1e', '#ed8b00', '#00599c', '#dea584']

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(categories, popularity, color=colors, edgecolor='black',
              linewidth=0.5)

# Add value labels on top of bars
for bar, val in zip(bars, popularity):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
            f'{val}%', ha='center', va='bottom', fontsize=11)

ax.set_title('Programming Language Popularity', fontsize=14)
ax.set_ylabel('Popularity (%)')
ax.set_ylim(0, 35)
plt.tight_layout()
plt.show()
```

### Horizontal Bar Chart

```python
fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(categories, popularity, color=colors)
ax.set_xlabel('Popularity (%)')
ax.invert_yaxis()  # highest value on top
plt.tight_layout()
plt.show()
```

### Grouped Bar Chart

```python
x = np.arange(4)
width = 0.35

q1 = [20, 35, 30, 25]
q2 = [25, 32, 34, 20]

fig, ax = plt.subplots(figsize=(8, 5))
bars1 = ax.bar(x - width/2, q1, width, label='Q1', color='steelblue')
bars2 = ax.bar(x + width/2, q2, width, label='Q2', color='coral')

ax.set_xticks(x)
ax.set_xticklabels(['Product A', 'Product B', 'Product C', 'Product D'])
ax.legend()
ax.set_ylabel('Sales ($K)')
ax.set_title('Quarterly Sales Comparison')
plt.tight_layout()
plt.show()
```

### Stacked Bar Chart

```python
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(x, q1, width=0.6, label='Q1', color='steelblue')
ax.bar(x, q2, width=0.6, bottom=q1, label='Q2', color='coral')
ax.set_xticks(x)
ax.set_xticklabels(['A', 'B', 'C', 'D'])
ax.legend()
plt.show()
```

---

## 4. Scatter Plots

Scatter plots show relationships between two continuous variables.

```python
np.random.seed(42)
n = 200
x = np.random.randn(n)
y = 2 * x + np.random.randn(n) * 0.5
sizes = np.random.randint(20, 200, n)
colors = np.random.rand(n)

fig, ax = plt.subplots(figsize=(8, 6))
scatter = ax.scatter(x, y, c=colors, s=sizes, alpha=0.6,
                     cmap='viridis', edgecolors='black', linewidth=0.5)

# Colorbar
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Color Value')

ax.set_title('Scatter Plot with Size and Color Encoding')
ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.tight_layout()
plt.show()
```

### Adding a Trend Line

```python
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(x, y, alpha=0.5, s=30)

# Linear fit
m, b = np.polyfit(x, y, 1)
ax.plot(x, m * x + b, color='red', linewidth=2, label=f'y = {m:.2f}x + {b:.2f}')

ax.legend()
ax.set_title('Scatter with Trend Line')
plt.show()
```

---

## 5. Histograms

Histograms show the distribution of a single continuous variable.

```python
data = np.random.randn(1000)

fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(data, bins=30, color='steelblue', edgecolor='black',
        alpha=0.7, density=True)

# Overlay a KDE-like curve
from scipy import stats
x_range = np.linspace(-4, 4, 100)
ax.plot(x_range, stats.norm.pdf(x_range), 'r-', linewidth=2,
        label='Normal PDF')

ax.set_title('Distribution of Random Data')
ax.set_xlabel('Value')
ax.set_ylabel('Density')
ax.legend()
plt.tight_layout()
plt.show()
```

### Comparing Distributions

```python
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(2, 1.5, 1000)

fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(data1, bins=30, alpha=0.5, label='Group A', color='blue')
ax.hist(data2, bins=30, alpha=0.5, label='Group B', color='orange')
ax.legend()
ax.set_title('Comparing Two Distributions')
plt.show()
```

---

## 6. Subplots — Multiple Plots in One Figure

### Basic Grid

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Top-left: line plot
axes[0, 0].plot(np.random.randn(50).cumsum())
axes[0, 0].set_title('Line Plot')

# Top-right: bar plot
axes[0, 1].bar(['A', 'B', 'C'], [3, 7, 5], color='coral')
axes[0, 1].set_title('Bar Chart')

# Bottom-left: scatter
axes[1, 0].scatter(np.random.rand(50), np.random.rand(50), alpha=0.6)
axes[1, 0].set_title('Scatter Plot')

# Bottom-right: histogram
axes[1, 1].hist(np.random.randn(500), bins=25, color='green', alpha=0.7)
axes[1, 1].set_title('Histogram')

fig.suptitle('Four Plot Types', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

### Unequal Subplot Sizes with GridSpec

```python
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(12, 8))
gs = GridSpec(2, 3, figure=fig)

ax1 = fig.add_subplot(gs[0, :])     # top row, spans all 3 columns
ax2 = fig.add_subplot(gs[1, 0:2])   # bottom-left, spans 2 columns
ax3 = fig.add_subplot(gs[1, 2])     # bottom-right, 1 column

ax1.plot(np.random.randn(100).cumsum())
ax1.set_title('Wide Plot')

ax2.bar(['X', 'Y', 'Z'], [4, 7, 2])
ax2.set_title('Medium Plot')

ax3.hist(np.random.randn(200), bins=15)
ax3.set_title('Small Plot')

plt.tight_layout()
plt.show()
```

---

## 7. Customization

### Colors

```python
# Named colors: 'red', 'steelblue', 'coral', 'seagreen'
# Hex: '#FF5733'
# RGB tuple: (0.2, 0.4, 0.6)
# Colormaps: 'viridis', 'plasma', 'inferno', 'magma', 'cividis'
#            'coolwarm', 'RdBu', 'Set1', 'tab10'
```

### Annotations and Text

```python
fig, ax = plt.subplots(figsize=(8, 5))
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax.plot(x, y)

# Annotate a specific point
ax.annotate('Peak', xy=(np.pi/2, 1), xytext=(3, 1.3),
            fontsize=12, arrowprops=dict(arrowstyle='->', color='red'),
            color='red')

# Add text
ax.text(7, -0.5, 'Note: this is a sine wave', fontsize=10,
        style='italic', bbox=dict(boxstyle='round', facecolor='wheat'))

plt.show()
```

### Axis Formatting

```python
fig, ax = plt.subplots()
ax.plot(range(10), np.random.rand(10) * 1000000)

# Format tick labels
from matplotlib.ticker import FuncFormatter
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, p: f'${x/1e6:.1f}M'))

# Rotate tick labels
ax.tick_params(axis='x', rotation=45)

# Log scale
ax.set_yscale('log')
```

### Styles

```python
# Available styles
print(plt.style.available)

# Use a style
plt.style.use('seaborn-v0_8-whitegrid')

# Temporary style
with plt.style.context('dark_background'):
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.show()
```

---

## 8. Saving Figures

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])

# Save as PNG (raster)
fig.savefig('plot.png', dpi=300, bbox_inches='tight',
            facecolor='white', transparent=False)

# Save as SVG (vector — ideal for publications)
fig.savefig('plot.svg', bbox_inches='tight')

# Save as PDF
fig.savefig('plot.pdf', bbox_inches='tight')
```

---

## 9. Plotting with Pandas Integration

Pandas DataFrames have built-in Matplotlib integration.

```python
df = pd.DataFrame({
    'month': pd.date_range('2024-01', periods=12, freq='MS'),
    'sales': np.random.randint(100, 500, 12),
    'returns': np.random.randint(10, 50, 12)
})
df.set_index('month', inplace=True)

# Quick line plot
df.plot(figsize=(10, 5), title='Monthly Sales and Returns')
plt.show()

# Bar plot
df.plot(kind='bar', figsize=(10, 5))
plt.show()

# Individual column histogram
df['sales'].plot(kind='hist', bins=10, title='Sales Distribution')
plt.show()
```

---

## 10. Practical Example — Dashboard

```python
np.random.seed(42)
months = pd.date_range('2024-01', periods=12, freq='MS')
revenue = [45, 52, 48, 61, 55, 67, 72, 68, 75, 80, 77, 85]
costs = [30, 35, 33, 40, 38, 42, 45, 43, 48, 50, 47, 52]
categories = ['Electronics', 'Clothing', 'Food', 'Books']
cat_sales = [35, 25, 22, 18]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Revenue trend
axes[0, 0].plot(months, revenue, 'b-o', label='Revenue')
axes[0, 0].plot(months, costs, 'r--s', label='Costs')
axes[0, 0].fill_between(months, costs, revenue, alpha=0.2, color='green')
axes[0, 0].set_title('Revenue vs Costs')
axes[0, 0].legend()
axes[0, 0].tick_params(axis='x', rotation=45)

# Category breakdown
axes[0, 1].pie(cat_sales, labels=categories, autopct='%1.1f%%',
               startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
axes[0, 1].set_title('Sales by Category')

# Monthly profit
profit = [r - c for r, c in zip(revenue, costs)]
colors = ['green' if p > 20 else 'orange' for p in profit]
axes[1, 0].bar(range(12), profit, color=colors)
axes[1, 0].set_title('Monthly Profit')
axes[1, 0].set_xticks(range(12))
axes[1, 0].set_xticklabels([m.strftime('%b') for m in months])
axes[1, 0].axhline(y=20, color='gray', linestyle='--', alpha=0.5)

# Cumulative revenue
axes[1, 1].fill_between(range(12), np.cumsum(revenue), alpha=0.4)
axes[1, 1].plot(range(12), np.cumsum(revenue), 'b-o')
axes[1, 1].set_title('Cumulative Revenue')
axes[1, 1].set_xticks(range(12))
axes[1, 1].set_xticklabels([m.strftime('%b') for m in months])

fig.suptitle('2024 Business Dashboard', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

---

## Key Takeaways

- Use the object-oriented interface (`fig, ax = plt.subplots()`) for all but the
  simplest plots.
- Line, bar, scatter, and histogram cover most common visualization needs.
- `subplots()` and `GridSpec` allow flexible multi-panel figures.
- Always label axes, add titles, and include legends for clarity.
- Save figures with `dpi=300` and `bbox_inches='tight'` for publication quality.
- Matplotlib integrates directly with Pandas DataFrames for quick plotting.
- Master the basics here before moving to higher-level libraries like Seaborn.

---

*Next: Day 20 — Seaborn: Statistical Plots, Heatmaps, and Pair Plots.*
