# Day 8: List/Dict/Set Comprehensions, Generators, and Iterators

## Introduction

Comprehensions and generators are among Python's most powerful features. They let you
write concise, readable code for transforming and producing data -- skills you will use
constantly in data science when cleaning datasets, building feature pipelines, and
processing large files.

---

## 1. List Comprehensions

A list comprehension builds a new list by applying an expression to each item in an
iterable, optionally filtering items with a condition.

### Basic Syntax

```python
new_list = [expression for item in iterable]
```

### Simple Example

```python
squares = [x ** 2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### With a Condition (Filtering)

```python
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]
```

### With an if/else (Ternary in the Expression)

```python
labels = ["even" if x % 2 == 0 else "odd" for x in range(6)]
# ['even', 'odd', 'even', 'odd', 'even', 'odd']
```

> **Key distinction:** `if` after `for` is a *filter*. `if/else` before `for` is a
> *ternary expression* applied to every item.

### Nested Loops

```python
pairs = [(x, y) for x in range(3) for y in range(3)]
# [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
```

### Flattening a Matrix

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## 2. Dictionary Comprehensions

Dictionary comprehensions follow the same idea but produce `{key: value}` pairs.

### Syntax

```python
new_dict = {key_expr: value_expr for item in iterable}
```

### Examples

```python
# Square mapping
sq_map = {x: x ** 2 for x in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Invert a dictionary
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}

# Filter while building
scores = {"Alice": 85, "Bob": 42, "Charlie": 91, "Diana": 67}
passed = {name: score for name, score in scores.items() if score >= 60}
# {'Alice': 85, 'Charlie': 91, 'Diana': 67}
```

### Counting Word Lengths

```python
words = ["Python", "is", "great", "for", "data"]
lengths = {w: len(w) for w in words}
# {'Python': 6, 'is': 2, 'great': 5, 'for': 3, 'data': 4}
```

---

## 3. Set Comprehensions

Set comprehensions produce a set (unique, unordered values).

```python
nums = [1, 2, 2, 3, 3, 3, 4]
unique_squares = {x ** 2 for x in nums}
# {1, 4, 9, 16}
```

### Practical Example -- Unique First Letters

```python
names = ["Alice", "Anna", "Bob", "Bella", "Charlie"]
initials = {name[0] for name in names}
# {'A', 'B', 'C'}
```

---

## 4. When to Use Comprehensions vs. Loops

| Comprehension | Traditional Loop |
|---|---|
| One-liner transformations | Complex multi-step logic |
| Filtering + mapping | Side effects (printing, writing files) |
| Building a new collection | Mutating existing data |

**Rule of thumb:** If the comprehension is hard to read on one line, use a regular loop.

---

## 5. Iterators

An **iterator** is any object that implements the **iterator protocol**:

- `__iter__()` -- returns the iterator object itself.
- `__next__()` -- returns the next value or raises `StopIteration`.

Every `for` loop in Python works by obtaining an iterator behind the scenes.

```python
nums = [10, 20, 30]
it = iter(nums)       # calls nums.__iter__()

print(next(it))       # 10
print(next(it))       # 20
print(next(it))       # 30
# next(it) would raise StopIteration
```

### Building a Custom Iterator

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

for num in Countdown(5):
    print(num)  # 5 4 3 2 1
```

---

## 6. Generators

A **generator** is a simpler way to create an iterator. Instead of a class with
`__iter__` and `__next__`, you write a function that uses `yield`.

### Generator Function

```python
def countdown(start):
    while start > 0:
        yield start
        start -= 1

for num in countdown(5):
    print(num)  # 5 4 3 2 1
```

Each time `yield` is hit, the function's state is *frozen* and the yielded value is
returned. On the next call to `next()`, execution resumes right after the `yield`.

### Generator Expression

Just like a list comprehension but with parentheses instead of brackets.

```python
squares_gen = (x ** 2 for x in range(1_000_000))
# No list in memory -- values produced one at a time
```

### Why Generators Matter for Data Science

When you process a 10 GB CSV, you cannot load it all into a list. Generators let you
stream rows one at a time:

```python
def read_large_csv(filepath):
    with open(filepath) as f:
        header = f.readline().strip().split(",")
        for line in f:
            values = line.strip().split(",")
            yield dict(zip(header, values))

for row in read_large_csv("huge_dataset.csv"):
    process(row)  # only one row in memory at a time
```

### Chaining Generators (Pipeline Pattern)

```python
def integers():
    n = 1
    while True:
        yield n
        n += 1

def squares(seq):
    for n in seq:
        yield n ** 2

def take(n, seq):
    for i, val in enumerate(seq):
        if i >= n:
            return
        yield val

print(list(take(5, squares(integers()))))
# [1, 4, 9, 16, 25]
```

---

## 7. Generator Methods: send, throw, close

Generators support advanced control:

```python
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

gen = accumulator()
next(gen)          # prime the generator -> 0
print(gen.send(10))  # 10
print(gen.send(20))  # 30
print(gen.send(5))   # 35
gen.close()
```

---

## 8. yield from (Delegating to Sub-generators)

`yield from` delegates iteration to another iterable or generator:

```python
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

print(list(flatten([1, [2, [3, 4], 5], 6])))
# [1, 2, 3, 4, 5, 6]
```

---

## 9. itertools -- The Standard Library Powerhouse

The `itertools` module provides high-performance iterator building blocks.

```python
import itertools

# chain -- concatenate iterables
list(itertools.chain([1, 2], [3, 4]))  # [1, 2, 3, 4]

# islice -- slice an iterator
list(itertools.islice(range(100), 5, 10))  # [5, 6, 7, 8, 9]

# groupby -- group consecutive elements
data = sorted(["apple", "avocado", "banana", "blueberry"], key=lambda x: x[0])
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(key, list(group))
# a ['apple', 'avocado']
# b ['banana', 'blueberry']

# product -- cartesian product
list(itertools.product("AB", "12"))
# [('A','1'), ('A','2'), ('B','1'), ('B','2')]

# combinations and permutations
list(itertools.combinations([1, 2, 3], 2))  # [(1,2), (1,3), (2,3)]
list(itertools.permutations([1, 2, 3], 2))  # all ordered pairs
```

---

## 10. Memory Comparison: List vs. Generator

```python
import sys

list_comp = [x ** 2 for x in range(1_000_000)]
gen_expr  = (x ** 2 for x in range(1_000_000))

print(sys.getsizeof(list_comp))  # ~8 MB
print(sys.getsizeof(gen_expr))   # ~200 bytes  (constant!)
```

---

## Key Takeaways

1. **List/dict/set comprehensions** replace simple for-loops with concise, readable
   one-liners.
2. **Generators** produce values lazily, saving memory -- essential for big-data work.
3. **Iterators** are the protocol that powers `for` loops; generators are the easiest
   way to create them.
4. **`itertools`** provides battle-tested building blocks for iterator pipelines.
5. Choose comprehensions for clarity, generators for memory efficiency, and regular
   loops for complex logic.
