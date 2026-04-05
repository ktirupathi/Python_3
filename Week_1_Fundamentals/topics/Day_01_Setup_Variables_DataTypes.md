# Day 1: Python Setup, Syntax, Variables, and Data Types

## Table of Contents
1. [Why Python?](#why-python)
2. [Setting Up Python](#setting-up-python)
3. [Your First Python Program](#your-first-python-program)
4. [Python Syntax Basics](#python-syntax-basics)
5. [Variables](#variables)
6. [Data Types](#data-types)
7. [Type Checking](#type-checking)
8. [Key Takeaways](#key-takeaways)

---

## Why Python?

Python is one of the most popular programming languages in the world, especially in data
science, machine learning, web development, and automation. Here is why:

- **Readable syntax** -- Python reads almost like English, making it beginner-friendly.
- **Massive ecosystem** -- Libraries like pandas, NumPy, scikit-learn, and TensorFlow.
- **Versatile** -- From scripting small tasks to building production ML pipelines.
- **Community** -- One of the largest developer communities means answers are always a search away.

Think of Python as the Swiss Army knife of programming -- not always the fastest blade,
but almost always the most convenient one.

---

## Setting Up Python

### Installing Python

1. **Download** Python from [python.org](https://www.python.org/downloads/).
   - Choose Python 3.10 or later (Python 2 is obsolete).
   - On Windows, check "Add Python to PATH" during installation.

2. **Verify** the installation by opening a terminal/command prompt:

```bash
python --version
# or on some systems:
python3 --version
```

### Choosing an Editor / IDE

| Tool | Best For |
|------|----------|
| **VS Code** | General-purpose, lightweight, excellent extensions |
| **PyCharm** | Full-featured Python IDE, great debugger |
| **Jupyter Notebook** | Data science, exploration, visualization |
| **Google Colab** | Free cloud-based Jupyter with GPU access |

For this course, any of these will work. VS Code with the Python extension is a solid
all-around choice.

### Virtual Environments (Best Practice)

Always isolate your project dependencies:

```bash
# Create a virtual environment
python -m venv myenv

# Activate it
# On macOS/Linux:
source myenv/bin/activate
# On Windows:
myenv\Scripts\activate

# Install packages inside it
pip install numpy pandas
```

Think of a virtual environment like a separate toolbox for each project -- you would not
mix your plumbing tools with your electrical tools.

---

## Your First Python Program

```python
print("Hello, World!")
```

Run it:
```bash
python hello.py
```

Output:
```
Hello, World!
```

The `print()` function sends output to the console. It is one of the most-used functions
in Python. You can print numbers, strings, or even multiple values:

```python
print("Name:", "Alice", "Age:", 30)
# Output: Name: Alice Age: 30
```

---

## Python Syntax Basics

### Indentation Matters

Unlike most languages that use braces `{}` to define blocks, Python uses **indentation**.
This is not optional -- it is part of the language.

```python
# Correct
if True:
    print("This is indented correctly")

# Wrong -- will raise IndentationError
if True:
print("This will fail")
```

Use **4 spaces** per indentation level (the Python community standard). Most editors
handle this automatically.

### Comments

```python
# This is a single-line comment

"""
This is a multi-line comment (technically a docstring).
Often used to describe what a function or module does.
"""
```

### Semicolons and Line Continuation

Semicolons are allowed but discouraged. Use line continuation with `\` for long lines:

```python
total = 1 + 2 + 3 + \
        4 + 5 + 6

# Or use parentheses (preferred):
total = (1 + 2 + 3 +
         4 + 5 + 6)
```

---

## Variables

A variable is a **name that refers to a value** stored in memory. Think of it as a
labeled box where you can store data.

### Creating Variables

Python is **dynamically typed** -- you do not declare a type; Python figures it out:

```python
name = "Alice"          # string
age = 30                # integer
height = 5.6            # float
is_student = True       # boolean
```

### Variable Naming Rules

1. Must start with a letter or underscore: `_count`, `name` (valid); `2name` (invalid).
2. Can contain letters, numbers, and underscores: `my_var_2` (valid).
3. Case-sensitive: `Name` and `name` are different variables.
4. Cannot be a Python keyword: `for`, `if`, `class`, etc.

### Naming Conventions

```python
# snake_case for variables and functions (PEP 8 standard)
user_name = "alice"
total_score = 95

# UPPER_SNAKE_CASE for constants
MAX_RETRIES = 3
PI = 3.14159

# CamelCase for class names
class DataProcessor:
    pass
```

### Multiple Assignment

```python
# Assign multiple variables at once
x, y, z = 1, 2, 3

# Same value to multiple variables
a = b = c = 0
```

### Variable Reassignment

```python
x = 10
print(x)    # 10

x = "hello"
print(x)    # hello -- type changed! Python allows this.
```

---

## Data Types

Python has several built-in data types. Here are the fundamental ones:

### Numeric Types

#### int (Integer)
Whole numbers, positive or negative, with no decimal point.

```python
age = 25
population = 7_900_000_000   # underscores for readability
negative = -42

print(type(age))  # <class 'int'>
```

Python integers have **unlimited precision** -- they can be as large as your memory allows:

```python
big_number = 10 ** 100  # a googol -- no overflow!
```

#### float (Floating Point)
Numbers with a decimal point.

```python
pi = 3.14159
temperature = -40.0
scientific = 2.5e6      # 2,500,000.0 (scientific notation)

print(type(pi))  # <class 'float'>
```

**Caution -- floating point precision:**
```python
print(0.1 + 0.2)        # 0.30000000000000004 (not exactly 0.3)
print(0.1 + 0.2 == 0.3) # False!
```

This is not a Python bug -- it is how all computers store decimals. For exact decimal
arithmetic, use the `decimal` module.

#### complex (Complex Numbers)
Used in scientific computing:

```python
z = 3 + 4j
print(z.real)  # 3.0
print(z.imag)  # 4.0
```

### str (String)
A sequence of characters enclosed in quotes.

```python
single = 'Hello'
double = "Hello"
triple = """This is a
multi-line string"""

print(type(single))  # <class 'str'>
```

Strings are **immutable** -- once created, you cannot change individual characters.

### bool (Boolean)
Represents truth values: `True` or `False`.

```python
is_active = True
has_permission = False

print(type(is_active))  # <class 'bool'>
```

Booleans are actually a subclass of `int`: `True` equals `1`, `False` equals `0`.

```python
print(True + True)   # 2
print(False * 100)   # 0
```

### NoneType
The `None` keyword represents the absence of a value.

```python
result = None
print(type(result))  # <class 'NoneType'>
```

Think of `None` like an empty box -- the variable exists, but it holds nothing yet.

### Collection Types (Preview)

These will be covered in depth on Days 4-5:

```python
my_list = [1, 2, 3]            # list -- ordered, mutable
my_tuple = (1, 2, 3)           # tuple -- ordered, immutable
my_dict = {"key": "value"}     # dict -- key-value pairs
my_set = {1, 2, 3}             # set -- unordered, unique elements
```

---

## Type Checking

### The `type()` Function

```python
x = 42
print(type(x))         # <class 'int'>
print(type(x).__name__) # int
```

### The `isinstance()` Function

More flexible -- also works with inheritance:

```python
x = 42
print(isinstance(x, int))          # True
print(isinstance(x, (int, float))) # True (checks multiple types)
print(isinstance(True, int))       # True (bool is subclass of int)
```

In data science, you will often check types when cleaning data:

```python
value = "123"
if isinstance(value, str):
    value = int(value)  # convert string to integer
```

---

## Memory and Identity

Every object in Python has an **identity** (memory address), a **type**, and a **value**.

```python
x = 256
y = 256
print(id(x))       # memory address
print(x is y)      # True -- Python caches small integers (-5 to 256)

a = 257
b = 257
print(a is b)      # May be False -- outside the cache range
print(a == b)      # True -- values are equal
```

**Rule of thumb:** Use `==` to compare values, use `is` to compare identity (mostly
used for `None` checks: `if x is None`).

---

## Key Takeaways

1. **Python is dynamically typed** -- variables do not need type declarations.
2. **Indentation is syntax** -- use 4 spaces consistently.
3. **Fundamental types**: `int`, `float`, `str`, `bool`, `None`.
4. **Use `type()` and `isinstance()`** to inspect types at runtime.
5. **Floating point arithmetic** has precision limitations -- be aware.
6. **Use virtual environments** to isolate project dependencies.
7. **Follow PEP 8** naming conventions: `snake_case` for variables, `UPPER_CASE` for
   constants.
8. **`is` vs `==`**: Use `==` for value comparison, `is` for identity (especially `None`).

---

## Next Up

Day 2 covers **Operators, Type Casting, and User Input** -- the tools you need to start
building interactive programs.
