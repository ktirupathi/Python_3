# Day 15: NumPy — Arrays, Indexing, Broadcasting, Linear Algebra

## Introduction

NumPy (Numerical Python) is the foundational package for numerical computing in Python.
It provides a powerful N-dimensional array object, sophisticated broadcasting functions,
and tools for integrating C/C++ and Fortran code. Nearly every data science library in
Python (Pandas, Scikit-learn, TensorFlow) is built on top of NumPy.

---

## 1. Why NumPy?

Python lists are flexible but slow for numerical computation. NumPy arrays are:

- **Fast** — operations are implemented in C under the hood
- **Memory-efficient** — elements are stored in contiguous memory blocks
- **Vectorized** — you can operate on entire arrays without writing loops

```python
import numpy as np

# Python list vs NumPy array — squaring a million numbers
import time

py_list = list(range(1_000_000))
np_array = np.arange(1_000_000)

start = time.time()
result_list = [x ** 2 for x in py_list]
print(f"List comprehension: {time.time() - start:.4f}s")

start = time.time()
result_np = np_array ** 2
print(f"NumPy vectorized:   {time.time() - start:.4f}s")
# NumPy is typically 10-100x faster
```

---

## 2. Creating Arrays

### From Python Lists

```python
a = np.array([1, 2, 3])              # 1D array
b = np.array([[1, 2, 3], [4, 5, 6]]) # 2D array (matrix)
c = np.array([1, 2, 3], dtype=float) # specify data type
```

### Using Built-in Constructors

```python
np.zeros((3, 4))        # 3x4 matrix of zeros
np.ones((2, 3))         # 2x3 matrix of ones
np.full((2, 2), 7)      # 2x2 matrix filled with 7
np.eye(4)               # 4x4 identity matrix
np.empty((3, 3))        # uninitialized 3x3 (fast, random values)

np.arange(0, 10, 2)     # [0, 2, 4, 6, 8] — like range()
np.linspace(0, 1, 5)    # [0.0, 0.25, 0.5, 0.75, 1.0] — evenly spaced

np.random.rand(3, 3)    # 3x3 uniform random [0, 1)
np.random.randn(3, 3)   # 3x3 standard normal distribution
np.random.randint(0, 10, size=(3, 3))  # 3x3 random integers
```

### Array Attributes

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

arr.shape      # (2, 3) — rows, columns
arr.ndim       # 2 — number of dimensions
arr.size       # 6 — total number of elements
arr.dtype      # dtype('int64') — data type
arr.itemsize   # 8 — bytes per element
arr.nbytes     # 48 — total bytes consumed
```

---

## 3. Indexing and Slicing

### Basic Indexing (works like Python lists)

```python
a = np.array([10, 20, 30, 40, 50])

a[0]       # 10
a[-1]      # 50
a[1:4]     # array([20, 30, 40])
a[:3]      # array([10, 20, 30])
a[::2]     # array([10, 30, 50]) — every other element
```

### 2D Indexing

```python
m = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

m[0, 0]      # 1 — row 0, col 0
m[1, 2]      # 6 — row 1, col 2
m[0]         # array([1, 2, 3]) — entire first row
m[:, 1]      # array([2, 5, 8]) — entire second column
m[0:2, 1:3]  # sub-matrix: [[2, 3], [5, 6]]
```

### Boolean (Fancy) Indexing

This is one of NumPy's most powerful features.

```python
arr = np.array([10, 25, 30, 45, 50])

mask = arr > 25          # array([False, False, True, True, True])
arr[mask]                # array([30, 45, 50])
arr[arr > 25]            # same thing, inline

# Combining conditions (use & for AND, | for OR, ~ for NOT)
arr[(arr > 20) & (arr < 50)]  # array([25, 30, 45])
```

### Fancy Indexing with Integer Arrays

```python
arr = np.array([10, 20, 30, 40, 50])
indices = np.array([0, 2, 4])
arr[indices]  # array([10, 30, 50])
```

---

## 4. Reshaping and Manipulating Arrays

```python
a = np.arange(12)           # [0, 1, 2, ..., 11]

a.reshape(3, 4)             # 3 rows, 4 columns
a.reshape(4, -1)            # -1 means "infer this dimension" -> (4, 3)

a.flatten()                 # always returns a copy
a.ravel()                   # returns a view when possible (faster)

np.concatenate([a[:6], a[6:]])  # join arrays along existing axis
np.vstack([np.ones((2, 3)), np.zeros((2, 3))])  # vertical stack
np.hstack([np.ones((2, 2)), np.zeros((2, 3))])  # horizontal stack

arr = np.array([[1, 2], [3, 4]])
arr.T                       # transpose: [[1, 3], [2, 4]]
```

---

## 5. Vectorized Operations and Universal Functions

NumPy replaces explicit loops with vectorized operations.

```python
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

# Element-wise arithmetic
a + b       # array([11, 22, 33, 44])
a * b       # array([10, 40, 90, 160])
a ** 2      # array([1, 4, 9, 16])
1 / a       # array([1.0, 0.5, 0.333, 0.25])

# Universal functions (ufuncs)
np.sqrt(a)         # square root
np.exp(a)          # e^x
np.log(a)          # natural log
np.sin(a)          # sine
np.abs(np.array([-1, -2, 3]))  # absolute value
np.maximum(a, b)   # element-wise maximum
```

---

## 6. Aggregation Functions

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

arr.sum()          # 21 — sum of all elements
arr.sum(axis=0)    # [5, 7, 9] — column sums
arr.sum(axis=1)    # [6, 15] — row sums

arr.mean()         # 3.5
arr.std()          # standard deviation
arr.var()          # variance
arr.min()          # 1
arr.max()          # 6
arr.argmin()       # 0 — index of minimum
arr.argmax()       # 5 — index of maximum

np.median(arr)     # 3.5
np.percentile(arr, 75)  # 75th percentile
np.cumsum(arr.flatten())  # cumulative sum
```

**Axis convention:** `axis=0` operates down rows (collapses rows), `axis=1` operates
across columns (collapses columns).

---

## 7. Broadcasting

Broadcasting is the set of rules NumPy uses to perform operations on arrays of
different shapes.

### Rules

1. If arrays have different numbers of dimensions, the shape of the smaller array is
   padded with 1s on the left.
2. Arrays with size 1 along a dimension act as if they had the size of the larger
   array along that dimension.
3. If sizes disagree along any dimension (and neither is 1), an error is raised.

```python
# Scalar + array
a = np.array([1, 2, 3])
a + 5  # array([6, 7, 8]) — 5 is broadcast to [5, 5, 5]

# 2D + 1D
m = np.array([[1, 2, 3],
              [4, 5, 6]])   # shape (2, 3)
v = np.array([10, 20, 30])  # shape (3,) -> broadcast to (2, 3)
m + v  # [[11, 22, 33], [14, 25, 36]]

# Column vector + row vector
col = np.array([[1], [2], [3]])   # shape (3, 1)
row = np.array([10, 20, 30])     # shape (3,)
col + row  # shape (3, 3) — outer addition
# [[11, 21, 31],
#  [12, 22, 32],
#  [13, 23, 33]]
```

### Practical Example: Centering Data

```python
data = np.random.rand(100, 3)  # 100 samples, 3 features
means = data.mean(axis=0)      # shape (3,) — one mean per feature
centered = data - means        # broadcasting subtracts from each row
```

---

## 8. Linear Algebra with NumPy

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication (three equivalent ways)
A @ B
np.dot(A, B)
np.matmul(A, B)
# Result: [[19, 22], [43, 50]]

# Determinant
np.linalg.det(A)  # -2.0

# Inverse
np.linalg.inv(A)  # [[-2, 1], [1.5, -0.5]]

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Solving linear systems: Ax = b
b = np.array([5, 11])
x = np.linalg.solve(A, b)  # x such that A @ x = b

# Singular Value Decomposition
U, S, Vt = np.linalg.svd(A)

# Norm
np.linalg.norm(np.array([3, 4]))  # 5.0 — Euclidean norm
```

### Practical Example: Least Squares Regression

```python
# Fit y = mx + c using normal equation: x = (A^T A)^-1 A^T b
x_data = np.array([1, 2, 3, 4, 5], dtype=float)
y_data = np.array([2.1, 3.9, 6.2, 7.8, 10.1])

# Design matrix with bias column
A = np.vstack([x_data, np.ones(len(x_data))]).T  # shape (5, 2)

# Solve using lstsq (more numerically stable than the normal equation)
result = np.linalg.lstsq(A, y_data, rcond=None)
m, c = result[0]
print(f"Slope: {m:.2f}, Intercept: {c:.2f}")
```

---

## 9. Copying vs Views

Understanding when NumPy creates a copy vs a view is critical.

```python
a = np.array([1, 2, 3, 4, 5])

# Slicing creates a VIEW (shared memory)
b = a[1:4]
b[0] = 99
print(a)  # [1, 99, 3, 4, 5] — a is modified!

# .copy() creates an independent COPY
c = a[1:4].copy()
c[0] = -1
print(a)  # [1, 99, 3, 4, 5] — a is NOT modified
```

---

## 10. Performance Tips

1. **Avoid Python loops** — use vectorized operations whenever possible.
2. **Preallocate arrays** — use `np.empty()` or `np.zeros()` instead of growing arrays.
3. **Use appropriate dtypes** — `float32` instead of `float64` halves memory usage.
4. **Use in-place operations** — `a += 1` instead of `a = a + 1` avoids creating a new array.
5. **Use `np.where`** for conditional assignment:

```python
arr = np.array([1, -2, 3, -4, 5])
result = np.where(arr > 0, arr, 0)  # replace negatives with 0
# array([1, 0, 3, 0, 5])
```

---

## Key Takeaways

- NumPy arrays are faster and more memory-efficient than Python lists for numerical work.
- Indexing supports slices, boolean masks, and integer arrays.
- Broadcasting eliminates the need for explicit loops across many operations.
- The `np.linalg` module provides essential linear algebra operations.
- Always be aware of views vs copies to avoid unintended side effects.
- NumPy is the foundation — mastering it makes Pandas, Matplotlib, and ML libraries
  much easier to learn.

---

*Next: Day 16 — Introduction to Pandas Series and DataFrames.*
