# Day 5: Dictionaries and Sets

## Table of Contents
1. [Dictionaries -- Overview](#dictionaries-overview)
2. [Creating Dictionaries](#creating-dictionaries)
3. [Accessing Dictionary Values](#accessing-dictionary-values)
4. [Modifying Dictionaries (CRUD)](#modifying-dictionaries-crud)
5. [Dictionary Methods](#dictionary-methods)
6. [Dictionary Comprehensions](#dictionary-comprehensions)
7. [Nested Dictionaries](#nested-dictionaries)
8. [Sets -- Overview](#sets-overview)
9. [Creating Sets](#creating-sets)
10. [Set Operations](#set-operations)
11. [Set Methods](#set-methods)
12. [Frozen Sets](#frozen-sets)
13. [Practical Applications](#practical-applications)
14. [Key Takeaways](#key-takeaways)

---

## Dictionaries -- Overview

A dictionary is an **unordered (insertion-ordered since Python 3.7), mutable collection
of key-value pairs**. Think of it like a real dictionary: you look up a word (key) to
find its definition (value).

Key characteristics:
- **Key-value pairs**: Every entry has a unique key mapped to a value.
- **Fast lookup**: O(1) average time to access by key (uses hash tables internally).
- **Keys must be immutable**: Strings, numbers, tuples (not lists or dicts).
- **Values can be anything**: Strings, lists, other dicts, functions, etc.

---

## Creating Dictionaries

```python
# Curly braces
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# dict() constructor
person2 = dict(name="Bob", age=25, city="Chicago")

# From list of tuples
pairs = [("name", "Charlie"), ("age", 35)]
person3 = dict(pairs)

# From two parallel lists using zip
keys = ["name", "age", "city"]
values = ["Diana", 28, "Boston"]
person4 = dict(zip(keys, values))

# Empty dictionary
empty = {}
also_empty = dict()

# dict.fromkeys() -- same value for all keys
defaults = dict.fromkeys(["host", "port", "debug"], None)
print(defaults)  # {'host': None, 'port': None, 'debug': None}

scores = dict.fromkeys(["Alice", "Bob", "Charlie"], 0)
print(scores)  # {'Alice': 0, 'Bob': 0, 'Charlie': 0}
```

---

## Accessing Dictionary Values

```python
person = {"name": "Alice", "age": 30, "city": "New York"}

# Bracket notation
print(person["name"])   # Alice
# print(person["email"]) # KeyError! Key does not exist.

# get() -- safe access with optional default
print(person.get("name"))          # Alice
print(person.get("email"))         # None (no error)
print(person.get("email", "N/A")) # N/A (custom default)

# Check if key exists
print("name" in person)       # True
print("email" in person)      # False
print("email" not in person)  # True

# Get all keys, values, or items
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 30, 'New York'])
print(person.items())   # dict_items([('name', 'Alice'), ('age', 30), ...])

# Iterate over a dictionary
for key in person:
    print(f"{key}: {person[key]}")

# Better: iterate with items()
for key, value in person.items():
    print(f"{key}: {value}")
```

---

## Modifying Dictionaries (CRUD)

### Create / Update

```python
person = {"name": "Alice", "age": 30}

# Add or update a single key
person["email"] = "alice@example.com"  # adds new key
person["age"] = 31                      # updates existing key

# update() -- merge another dict or keyword arguments
person.update({"city": "NYC", "age": 32})
person.update(phone="555-1234")
print(person)

# setdefault() -- set only if key does not exist
person.setdefault("name", "Unknown")   # does nothing, "name" exists
person.setdefault("country", "USA")    # adds "country": "USA"
print(person["country"])  # USA
```

### Read

Covered above: bracket notation, `get()`, `keys()`, `values()`, `items()`.

### Delete

```python
person = {"name": "Alice", "age": 30, "city": "NYC", "email": "a@b.com"}

# pop() -- remove by key, return the value
email = person.pop("email")
print(email)   # a@b.com

# pop() with default -- no error if missing
result = person.pop("phone", "not found")
print(result)  # not found

# popitem() -- remove and return the last inserted pair
last = person.popitem()
print(last)  # ('city', 'NYC')

# del -- remove by key
del person["age"]
print(person)  # {'name': 'Alice'}

# clear() -- empty the dictionary
person.clear()
print(person)  # {}
```

---

## Dictionary Methods

```python
# copy() -- shallow copy
original = {"a": 1, "b": [2, 3]}
copied = original.copy()
copied["a"] = 99
print(original["a"])  # 1 (safe for immutable values)
copied["b"].append(4)
print(original["b"])  # [2, 3, 4] (shallow copy -- nested list is shared!)

# Merge dictionaries (Python 3.9+)
defaults = {"color": "blue", "size": "medium", "debug": False}
user_prefs = {"color": "red", "debug": True}

# | operator creates a new merged dict (right side wins on conflicts)
merged = defaults | user_prefs
print(merged)  # {'color': 'red', 'size': 'medium', 'debug': True}

# |= updates in place
defaults |= user_prefs

# For Python < 3.9, use unpacking
merged = {**defaults, **user_prefs}
```

---

## Dictionary Comprehensions

Same idea as list comprehensions, but produce key-value pairs.

```python
# Basic: square numbers
squares = {x: x**2 for x in range(6)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}

# From a list, create a frequency map
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
freq = {w: words.count(w) for w in set(words)}
print(freq)  # {'cherry': 1, 'banana': 2, 'apple': 3}

# Transform values
prices_usd = {"apple": 1.20, "banana": 0.50, "cherry": 2.00}
prices_eur = {k: round(v * 0.85, 2) for k, v in prices_usd.items()}
print(prices_eur)  # {'apple': 1.02, 'banana': 0.42, 'cherry': 1.7}

# Filter a dictionary
scores = {"Alice": 92, "Bob": 67, "Charlie": 85, "Diana": 45}
passed = {name: score for name, score in scores.items() if score >= 70}
print(passed)  # {'Alice': 92, 'Charlie': 85}
```

---

## Nested Dictionaries

Dictionaries can hold other dictionaries, forming tree-like structures common in
JSON data and configuration files.

```python
company = {
    "engineering": {
        "Alice": {"role": "Lead", "salary": 120000},
        "Bob": {"role": "Senior", "salary": 100000},
    },
    "marketing": {
        "Charlie": {"role": "Manager", "salary": 95000},
    }
}

# Access nested values
print(company["engineering"]["Alice"]["salary"])  # 120000

# Safe nested access
eng = company.get("engineering", {})
alice = eng.get("Alice", {})
salary = alice.get("salary", 0)
print(salary)  # 120000

# Iterate over nested structure
for dept, employees in company.items():
    print(f"\n{dept.upper()}")
    for name, info in employees.items():
        print(f"  {name}: {info['role']} (${info['salary']:,})")
```

---

## Sets -- Overview

A set is an **unordered collection of unique elements**. Think of it as a bag of
distinct items -- no duplicates, no defined order.

Key characteristics:
- **Unique elements**: Duplicates are automatically removed.
- **Unordered**: No indexing, no slicing.
- **Mutable**: You can add/remove elements (but elements must be immutable).
- **Fast membership testing**: O(1) average for `in` operator.

---

## Creating Sets

```python
# Curly braces
fruits = {"apple", "banana", "cherry"}

# From a list (removes duplicates)
numbers = set([1, 2, 2, 3, 3, 3])
print(numbers)  # {1, 2, 3}

# From a string (each character is an element)
letters = set("hello")
print(letters)  # {'h', 'e', 'l', 'o'} (note: only one 'l')

# Empty set -- MUST use set(), not {}
empty_set = set()    # correct
empty_dict = {}      # this is a dict, not a set!

# Set of tuples (tuples are hashable)
points = {(0, 0), (1, 1), (2, 2)}

# Cannot contain mutable elements
# bad = {[1, 2], [3, 4]}  # TypeError: unhashable type: 'list'
```

---

## Set Operations

Sets support mathematical set operations. These are extremely useful for data analysis.

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Union -- elements in either set
print(a | b)            # {1, 2, 3, 4, 5, 6, 7, 8}
print(a.union(b))       # same

# Intersection -- elements in both sets
print(a & b)            # {4, 5}
print(a.intersection(b))

# Difference -- elements in a but not in b
print(a - b)            # {1, 2, 3}
print(a.difference(b))

# Symmetric Difference -- elements in either but not both
print(a ^ b)            # {1, 2, 3, 6, 7, 8}
print(a.symmetric_difference(b))
```

### Subset and Superset

```python
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

print(a.issubset(b))     # True (a <= b)
print(b.issuperset(a))   # True (b >= a)
print(a < b)             # True (proper subset)

c = {1, 2, 3}
print(a <= c)            # True (subset, can be equal)
print(a < c)             # False (not a proper subset)

# Check if two sets have no common elements
d = {6, 7, 8}
print(a.isdisjoint(d))   # True (no overlap)
```

---

## Set Methods

### Adding and Removing

```python
colors = {"red", "green", "blue"}

# add() -- add a single element
colors.add("yellow")
colors.add("red")       # no error, no effect (already exists)
print(colors)

# update() -- add multiple elements from an iterable
colors.update(["purple", "orange"])
colors.update({"black", "white"})
print(colors)

# remove() -- remove an element (raises KeyError if missing)
colors.remove("red")
# colors.remove("pink")  # KeyError!

# discard() -- remove if present (no error if missing)
colors.discard("pink")   # no error

# pop() -- remove and return an arbitrary element
random_color = colors.pop()
print(f"Removed: {random_color}")

# clear() -- remove all elements
colors.clear()
```

### Set Comprehensions

```python
# Create a set with comprehension
squares = {x**2 for x in range(-5, 6)}
print(squares)  # {0, 1, 4, 9, 16, 25}

# Extract unique first letters
names = ["Alice", "Bob", "Anna", "Charlie", "Adam"]
first_letters = {name[0] for name in names}
print(first_letters)  # {'A', 'B', 'C'}
```

---

## Frozen Sets

An immutable version of a set. Can be used as dictionary keys or elements of other sets.

```python
fs = frozenset([1, 2, 3, 4])
# fs.add(5)  # AttributeError: 'frozenset' has no attribute 'add'

# Use as a dictionary key
permissions = {
    frozenset({"read", "write"}): "editor",
    frozenset({"read"}): "viewer",
    frozenset({"read", "write", "admin"}): "admin"
}

user_perms = frozenset({"read", "write"})
print(permissions[user_perms])  # editor
```

---

## Practical Applications

### Removing Duplicates While Preserving Order

```python
# set() removes order, but we can use dict.fromkeys() to preserve it
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
unique_ordered = list(dict.fromkeys(data))
print(unique_ordered)  # [3, 1, 4, 5, 9, 2, 6]
```

### Finding Common and Missing Data

```python
# Students enrolled in different courses
python_students = {"Alice", "Bob", "Charlie", "Diana"}
sql_students = {"Bob", "Diana", "Eve", "Frank"}

# Who is in both courses?
both = python_students & sql_students
print(f"In both: {both}")  # {'Bob', 'Diana'}

# Who is only in Python?
only_python = python_students - sql_students
print(f"Only Python: {only_python}")  # {'Alice', 'Charlie'}

# All unique students
all_students = python_students | sql_students
print(f"Total unique: {len(all_students)}")
```

### Counting with Dictionaries

```python
# Manual frequency counting
text = "the quick brown fox jumps over the lazy brown dog"
word_counts = {}
for word in text.split():
    word_counts[word] = word_counts.get(word, 0) + 1
print(word_counts)

# Better: use collections.Counter
from collections import Counter
word_counts = Counter(text.split())
print(word_counts.most_common(3))
# [('the', 2), ('brown', 2), ('quick', 1)]
```

### Grouping Data

```python
# Group employees by department
employees = [
    {"name": "Alice", "dept": "Engineering"},
    {"name": "Bob", "dept": "Marketing"},
    {"name": "Charlie", "dept": "Engineering"},
    {"name": "Diana", "dept": "Marketing"},
    {"name": "Eve", "dept": "Engineering"},
]

from collections import defaultdict
by_dept = defaultdict(list)
for emp in employees:
    by_dept[emp["dept"]].append(emp["name"])

for dept, names in by_dept.items():
    print(f"{dept}: {', '.join(names)}")
```

### Caching with Dictionaries

```python
# Simple memoization
cache = {}

def fibonacci(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    result = fibonacci(n - 1) + fibonacci(n - 2)
    cache[n] = result
    return result

print(fibonacci(50))  # 12586269025 (fast with caching!)
```

### Configuration Management

```python
# Default config merged with user config
default_config = {
    "host": "localhost",
    "port": 5432,
    "database": "mydb",
    "debug": False,
    "log_level": "WARNING",
}

user_config = {
    "host": "production.server.com",
    "debug": True,
    "log_level": "INFO",
}

# Merge: user settings override defaults
config = {**default_config, **user_config}
print(config)
# host is production.server.com, debug is True, etc.
```

---

## Key Takeaways

1. **Dictionaries** are the go-to for key-value mappings -- O(1) lookups.
2. **Use `get()`** instead of bracket notation to avoid KeyError.
3. **Dictionary comprehensions** are powerful for transforming and filtering data.
4. **Sets** guarantee uniqueness and provide fast membership testing.
5. **Set operations** (`|`, `&`, `-`, `^`) are invaluable for comparing datasets.
6. **`collections.Counter`** and `defaultdict` extend dictionary capabilities.
7. **Keys must be hashable** -- use strings, numbers, or tuples (not lists).
8. **Empty set** must be `set()`, not `{}` (that creates a dict).
9. **Use `frozenset`** when you need an immutable set (e.g., as a dict key).
10. **`dict.fromkeys()`** preserves order when removing duplicates from a list.

---

## Next Up

Day 6 covers **Conditionals and Loops** -- the control flow structures that let you
make decisions and repeat actions in your programs.
