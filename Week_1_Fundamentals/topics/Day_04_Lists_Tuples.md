# Day 4: Lists and Tuples -- CRUD, Slicing, and Comprehensions

## Table of Contents
1. [Lists -- Overview](#lists-overview)
2. [Creating Lists](#creating-lists)
3. [Accessing Elements](#accessing-elements)
4. [List Slicing](#list-slicing)
5. [Modifying Lists (CRUD)](#modifying-lists-crud)
6. [List Methods](#list-methods)
7. [List Comprehensions](#list-comprehensions)
8. [Tuples](#tuples)
9. [Lists vs Tuples](#lists-vs-tuples)
10. [Nested Lists](#nested-lists)
11. [Practical Applications](#practical-applications)
12. [Key Takeaways](#key-takeaways)

---

## Lists -- Overview

A list is an **ordered, mutable collection** that can hold items of any type. Think of
it as a numbered shopping list -- you can read any item by its position, add new items,
remove items, and rearrange them.

Key characteristics:
- **Ordered**: Items maintain their insertion order.
- **Mutable**: You can add, remove, or change items after creation.
- **Heterogeneous**: A single list can hold integers, strings, other lists, etc.
- **Duplicates allowed**: The same value can appear multiple times.

---

## Creating Lists

```python
# Empty list
empty = []
also_empty = list()

# List with values
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]

# Mixed types (legal but usually avoided)
mixed = [1, "hello", 3.14, True, None]

# From other iterables
from_string = list("hello")           # ['h', 'e', 'l', 'l', 'o']
from_range = list(range(1, 6))        # [1, 2, 3, 4, 5]
from_tuple = list((10, 20, 30))       # [10, 20, 30]

# Repeated values
zeros = [0] * 5                       # [0, 0, 0, 0, 0]
pattern = [1, 2] * 3                  # [1, 2, 1, 2, 1, 2]
```

---

## Accessing Elements

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# By index (zero-based)
print(fruits[0])    # apple
print(fruits[2])    # cherry
print(fruits[-1])   # elderberry (last item)
print(fruits[-2])   # date

# Check length
print(len(fruits))  # 5

# Check membership
print("banana" in fruits)      # True
print("grape" not in fruits)   # True

# Get index of a value
print(fruits.index("cherry"))  # 2
# fruits.index("grape")        # ValueError if not found
```

---

## List Slicing

Same syntax as string slicing: `list[start:stop:step]`.

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[2:6])      # [2, 3, 4, 5]
print(nums[:4])        # [0, 1, 2, 3]
print(nums[6:])        # [6, 7, 8, 9]
print(nums[::2])       # [0, 2, 4, 6, 8] (every other)
print(nums[::-1])      # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reversed)
print(nums[1:8:3])     # [1, 4, 7]

# Slice assignment (unique to lists -- strings cannot do this)
nums[2:5] = [20, 30, 40]
print(nums)  # [0, 1, 20, 30, 40, 5, 6, 7, 8, 9]

# Insert multiple elements via slice
nums[2:2] = [99, 98, 97]  # insert at index 2 without removing
print(nums)

# Delete via slice
nums[2:5] = []  # removes indices 2, 3, 4
print(nums)

# Copy a list (shallow copy)
original = [1, 2, 3]
copy1 = original[:]       # slice copy
copy2 = original.copy()   # method copy
copy3 = list(original)    # constructor copy
```

---

## Modifying Lists (CRUD)

### Create (Add Elements)

```python
fruits = ["apple", "banana"]

# append() -- add to the end
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']

# insert() -- add at a specific position
fruits.insert(1, "avocado")
print(fruits)  # ['apple', 'avocado', 'banana', 'cherry']

# extend() -- add multiple items from another iterable
fruits.extend(["date", "elderberry"])
print(fruits)  # ['apple', 'avocado', 'banana', 'cherry', 'date', 'elderberry']

# Concatenation (creates a new list)
more_fruits = fruits + ["fig", "grape"]
```

**Common mistake**: `append` vs `extend`:
```python
a = [1, 2, 3]
a.append([4, 5])   # [1, 2, 3, [4, 5]] -- nested list!
b = [1, 2, 3]
b.extend([4, 5])   # [1, 2, 3, 4, 5] -- flat list
```

### Read (Access Elements)

Covered above: indexing, slicing, `in` operator, `index()` method.

### Update (Modify Elements)

```python
colors = ["red", "green", "blue"]

# By index
colors[1] = "yellow"
print(colors)  # ['red', 'yellow', 'blue']

# By slice (replace a range)
colors[0:2] = ["black", "white"]
print(colors)  # ['black', 'white', 'blue']
```

### Delete (Remove Elements)

```python
items = ["a", "b", "c", "d", "e"]

# remove() -- by value (first occurrence)
items.remove("c")
print(items)  # ['a', 'b', 'd', 'e']

# pop() -- by index, returns the removed item
last = items.pop()       # removes and returns 'e'
second = items.pop(1)    # removes and returns 'b'
print(items)             # ['a', 'd']

# del -- by index or slice
del items[0]
print(items)  # ['d']

# clear() -- remove all items
items.clear()
print(items)  # []
```

---

## List Methods

### Sorting

```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]

# sort() -- in place, returns None
nums.sort()
print(nums)  # [1, 1, 2, 3, 4, 5, 6, 9]

nums.sort(reverse=True)
print(nums)  # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() -- returns a new sorted list (original unchanged)
original = [3, 1, 4, 1, 5]
sorted_copy = sorted(original)
print(original)     # [3, 1, 4, 1, 5] (unchanged)
print(sorted_copy)  # [1, 1, 3, 4, 5]

# Sort by custom key
words = ["banana", "apple", "cherry", "date"]
words.sort(key=len)
print(words)  # ['date', 'apple', 'banana', 'cherry']

# Sort strings case-insensitively
names = ["alice", "Bob", "Charlie"]
names.sort(key=str.lower)
print(names)  # ['alice', 'Bob', 'Charlie']
```

### Other Useful Methods

```python
nums = [3, 1, 4, 1, 5, 9]

print(nums.count(1))     # 2 (how many times 1 appears)
print(nums.index(4))     # 2 (index of first occurrence of 4)

nums.reverse()            # reverse in place
print(nums)              # [9, 5, 1, 4, 1, 3]
```

### Built-in Functions That Work with Lists

```python
nums = [3, 1, 4, 1, 5, 9]

print(len(nums))      # 6
print(min(nums))      # 1
print(max(nums))      # 9
print(sum(nums))      # 23
print(any(nums))      # True (at least one truthy value)
print(all(nums))      # True (all values are truthy)

# enumerate -- get index and value together
for i, val in enumerate(nums):
    print(f"Index {i}: {val}")

# zip -- iterate over multiple lists in parallel
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

---

## List Comprehensions

A concise way to create lists. Think of it as a one-liner `for` loop that builds a list.

### Basic Syntax

```python
# [expression for item in iterable]

# Traditional way
squares = []
for x in range(10):
    squares.append(x ** 2)

# Comprehension (same result, one line)
squares = [x ** 2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### With Condition (Filtering)

```python
# [expression for item in iterable if condition]

# Only even numbers
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Words longer than 3 characters
words = ["hi", "hello", "hey", "howdy", "yo"]
long_words = [w for w in words if len(w) > 3]
print(long_words)  # ['hello', 'howdy']
```

### With if-else (Transformation)

```python
# [expr_if_true if condition else expr_if_false for item in iterable]

labels = ["even" if x % 2 == 0 else "odd" for x in range(6)]
print(labels)  # ['even', 'odd', 'even', 'odd', 'even', 'odd']
```

### Nested Comprehensions

```python
# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a multiplication table
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
for row in table:
    print(row)
```

### Data Science Example

```python
# Clean and filter data
raw_prices = ["$10.50", "$20.00", "N/A", "$5.75", "", "$15.25"]
clean_prices = [
    float(p.replace("$", ""))
    for p in raw_prices
    if p and p != "N/A"
]
print(clean_prices)  # [10.5, 20.0, 5.75, 15.25]
print(f"Average: ${sum(clean_prices) / len(clean_prices):.2f}")
```

---

## Tuples

A tuple is an **ordered, immutable collection**. Think of it as a list that cannot be
changed after creation -- like a record in a database row.

### Creating Tuples

```python
# With parentheses
point = (3, 4)
rgb = (255, 128, 0)

# Without parentheses (tuple packing)
coordinates = 10, 20, 30

# Single-element tuple NEEDS a trailing comma
single = (42,)       # this is a tuple
not_tuple = (42)     # this is just the integer 42!

# Empty tuple
empty = ()
also_empty = tuple()

# From other iterables
from_list = tuple([1, 2, 3])
from_string = tuple("hello")  # ('h', 'e', 'l', 'l', 'o')
```

### Accessing Tuple Elements

```python
point = (10, 20, 30)

# Indexing and slicing work exactly like lists
print(point[0])      # 10
print(point[-1])     # 30
print(point[1:])     # (20, 30)

# Tuple unpacking
x, y, z = point
print(x, y, z)  # 10 20 30

# Extended unpacking with *
first, *rest = (1, 2, 3, 4, 5)
print(first)  # 1
print(rest)   # [2, 3, 4, 5] (note: this is a list!)

# Swap variables using tuple unpacking
a, b = 5, 10
a, b = b, a
print(a, b)  # 10 5
```

### Tuple Methods

Tuples have only two methods (because they are immutable):

```python
t = (1, 2, 3, 2, 2, 4)
print(t.count(2))   # 3
print(t.index(3))   # 2
```

### Named Tuples

For more readable tuple-like objects:

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)    # 3 4
print(p[0], p[1])  # 3 4 (still works like a tuple)

# Common in data science: representing records
Student = namedtuple("Student", ["name", "age", "gpa"])
alice = Student("Alice", 22, 3.8)
print(f"{alice.name} has a GPA of {alice.gpa}")
```

---

## Lists vs Tuples

| Feature | List | Tuple |
|---------|------|-------|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Mutable | Yes | No |
| Speed | Slower | Faster |
| Memory | More | Less |
| Hashable | No | Yes (if elements are hashable) |
| Use as dict key | No | Yes |

**When to use tuples:**
- Data that should not change (coordinates, RGB values, database records).
- Dictionary keys or set elements.
- Returning multiple values from a function.
- When you want to signal "this data is fixed."

**When to use lists:**
- Data that needs to grow, shrink, or be modified.
- When you need sorting, appending, or other mutations.

---

## Nested Lists

Lists can contain other lists, forming matrices or tree-like structures.

```python
# 2D matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access element at row 1, column 2
print(matrix[1][2])  # 6

# Iterate over a matrix
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()

# Transpose a matrix using comprehension
transposed = [[row[i] for row in matrix] for i in range(3)]
print(transposed)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

### Deep Copy Warning

```python
import copy

# Shallow copy -- nested objects are shared
original = [[1, 2], [3, 4]]
shallow = original[:]
shallow[0][0] = 99
print(original)  # [[99, 2], [3, 4]] -- original was affected!

# Deep copy -- fully independent
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 99
print(original)  # [[1, 2], [3, 4]] -- original is safe
```

---

## Practical Applications

### Data Processing Pipeline

```python
# Simulate processing sensor readings
raw_readings = [22.5, -999, 23.1, 22.8, -999, 23.5, 22.9]
INVALID = -999

# Clean, filter, and summarize
valid = [r for r in raw_readings if r != INVALID]
avg_temp = sum(valid) / len(valid)
print(f"Valid readings: {len(valid)}")
print(f"Average temperature: {avg_temp:.1f}")
```

### Frequency Counter

```python
words = "the quick brown fox jumps over the lazy brown dog".split()
unique_words = list(set(words))
word_counts = [(w, words.count(w)) for w in unique_words]
word_counts.sort(key=lambda x: x[1], reverse=True)
for word, count in word_counts[:5]:
    print(f"{word}: {count}")
```

---

## Key Takeaways

1. **Lists are mutable**, tuples are not -- choose based on whether data should change.
2. **List comprehensions** are Pythonic and often faster than manual loops.
3. **`append()` adds one item**, `extend()` adds multiple -- do not confuse them.
4. **Slicing creates copies** (shallow), indexing returns references.
5. **`sort()` modifies in place** (returns None), `sorted()` returns a new list.
6. **Tuple unpacking** is powerful: `a, b = b, a` swaps variables.
7. **Use `enumerate()`** instead of manual index tracking.
8. **Beware shallow copies** with nested lists -- use `copy.deepcopy()` when needed.

---

## Next Up

Day 5 covers **Dictionaries and Sets** -- the key-value and unique-element collections
that are essential for fast lookups and data aggregation.
