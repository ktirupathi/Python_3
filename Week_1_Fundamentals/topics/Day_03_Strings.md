# Day 3: Strings -- Slicing, Methods, and Formatting

## Table of Contents
1. [Creating Strings](#creating-strings)
2. [String Indexing](#string-indexing)
3. [String Slicing](#string-slicing)
4. [String Methods](#string-methods)
5. [String Formatting](#string-formatting)
6. [Escape Characters](#escape-characters)
7. [String Operations](#string-operations)
8. [Practical Applications](#practical-applications)
9. [Key Takeaways](#key-takeaways)

---

## Creating Strings

Strings are sequences of characters. In Python, they are **immutable** -- once created,
you cannot change individual characters. Think of a string like a printed page: you can
read any letter, copy sections, but to change a word, you need to print a new page.

```python
# Single or double quotes -- no difference
greeting = 'Hello'
name = "Alice"

# Triple quotes for multi-line strings
bio = """Alice is a data scientist
who loves Python and coffee.
She has 5 years of experience."""

# Raw strings -- backslashes are treated literally
path = r"C:\Users\new_folder\test"  # no escape interpretation
print(path)  # C:\Users\new_folder\test

# Empty string
empty = ""
print(len(empty))  # 0
print(bool(empty))  # False (empty strings are falsy)
```

---

## String Indexing

Every character in a string has a position (index). Python uses **zero-based indexing**
and supports **negative indexing** from the end.

```
 String:   P   y   t   h   o   n
 Index:    0   1   2   3   4   5
 Neg:     -6  -5  -4  -3  -2  -1
```

```python
text = "Python"

print(text[0])    # P (first character)
print(text[5])    # n (last character)
print(text[-1])   # n (last character, using negative index)
print(text[-2])   # o (second to last)

# IndexError if you go out of bounds
# print(text[10])  # IndexError: string index out of range
```

---

## String Slicing

Slicing extracts a **substring** using the syntax `string[start:stop:step]`.

- `start`: inclusive (defaults to 0)
- `stop`: exclusive (defaults to end of string)
- `step`: how many characters to skip (defaults to 1)

```python
text = "Hello, World!"

# Basic slicing
print(text[0:5])     # Hello
print(text[7:12])    # World
print(text[:5])      # Hello (start defaults to 0)
print(text[7:])      # World! (stop defaults to end)
print(text[:])       # Hello, World! (full copy)

# With step
print(text[::2])     # Hlo ol! (every other character)
print(text[1::2])    # el,Wrd

# Negative step -- reverses direction
print(text[::-1])    # !dlroW ,olleH (reversed string)
print(text[12:6:-1]) # !dlroW

# Practical: extract file extension
filename = "report_2024.csv"
extension = filename[filename.rfind('.'):]
print(extension)  # .csv
```

### Slicing Never Raises IndexError

```python
text = "Hello"
print(text[0:100])   # Hello (no error, just goes to end)
print(text[100:200]) # "" (empty string, no error)
```

This is a key difference from indexing -- slicing is forgiving.

---

## String Methods

Python strings come with dozens of built-in methods. Here are the most important ones.

### Case Methods

```python
text = "Hello, World!"

print(text.upper())       # HELLO, WORLD!
print(text.lower())       # hello, world!
print(text.title())       # Hello, World!
print(text.capitalize())  # Hello, world!
print(text.swapcase())    # hELLO, wORLD!

# Useful for case-insensitive comparison
user_input = "YES"
if user_input.lower() == "yes":
    print("User agreed")
```

### Search Methods

```python
text = "The quick brown fox jumps over the lazy dog"

# find() -- returns index of first occurrence, -1 if not found
print(text.find("fox"))      # 16
print(text.find("cat"))      # -1

# index() -- like find(), but raises ValueError if not found
print(text.index("fox"))     # 16
# text.index("cat")          # ValueError

# rfind() / rindex() -- search from the right
text2 = "banana"
print(text2.find("an"))      # 1 (first occurrence)
print(text2.rfind("an"))     # 3 (last occurrence)

# count() -- count occurrences
print(text2.count("an"))     # 2
print(text.count("the"))     # 1 (case-sensitive!)
print(text.lower().count("the"))  # 2

# startswith() / endswith()
filename = "report_2024.csv"
print(filename.startswith("report"))  # True
print(filename.endswith(".csv"))      # True
print(filename.endswith((".csv", ".xlsx", ".tsv")))  # True (tuple of suffixes)
```

### Modification Methods

Remember: these return **new strings** (strings are immutable).

```python
# strip() -- remove leading/trailing whitespace (or specified chars)
messy = "   hello   \n"
print(messy.strip())          # "hello"
print(messy.lstrip())         # "hello   \n"
print(messy.rstrip())         # "   hello"

data = "###price###"
print(data.strip("#"))        # "price"

# replace()
text = "Hello World"
print(text.replace("World", "Python"))  # Hello Python
print(text.replace("l", "L", 1))        # HeLlo World (replace first only)

# Chaining replacements for data cleaning
dirty = "  John   Doe  "
clean = dirty.strip().replace("   ", " ")
print(clean)  # "John Doe"
```

### Split and Join

These are workhorses for data processing.

```python
# split() -- break string into a list
csv_line = "Alice,30,Data Scientist,New York"
fields = csv_line.split(",")
print(fields)  # ['Alice', '30', 'Data Scientist', 'New York']

# Split with maxsplit
print("a.b.c.d".split(".", 2))  # ['a', 'b', 'c.d']

# splitlines() -- split by line breaks
multiline = "line1\nline2\nline3"
print(multiline.splitlines())  # ['line1', 'line2', 'line3']

# join() -- combine a list into a string
words = ["Python", "is", "awesome"]
print(" ".join(words))        # Python is awesome
print(", ".join(words))       # Python, is, awesome
print(" -> ".join(words))     # Python -> is -> awesome

# Practical: build a CSV line
row = ["Alice", "30", "NYC"]
csv_output = ",".join(row)
print(csv_output)  # Alice,30,NYC
```

### Validation Methods

```python
print("hello".isalpha())      # True (only letters)
print("hello123".isalnum())   # True (letters and numbers)
print("12345".isdigit())      # True (only digits)
print("12345".isnumeric())    # True (broader than isdigit)
print("   ".isspace())        # True (only whitespace)
print("Hello World".istitle()) # True (title case)
print("HELLO".isupper())      # True
print("hello".islower())      # True
```

### Padding and Alignment

```python
text = "hello"

# Center, left-justify, right-justify
print(text.center(20, "-"))   # -------hello--------
print(text.ljust(20, "."))    # hello...............
print(text.rjust(20, "."))    # ...............hello

# Zero-padding numbers
print("42".zfill(6))          # 000042
print("-42".zfill(6))         # -00042 (handles negative sign)
```

---

## String Formatting

Python offers three main ways to format strings. **f-strings** are the modern standard.

### f-strings (Python 3.6+) -- Recommended

```python
name = "Alice"
age = 30
salary = 75000.5

# Basic interpolation
print(f"Name: {name}, Age: {age}")

# Expressions inside braces
print(f"Next year: {age + 1}")
print(f"Name upper: {name.upper()}")

# Number formatting
print(f"Salary: ${salary:,.2f}")        # Salary: $75,000.50
print(f"Percentage: {0.856:.1%}")        # Percentage: 85.6%
print(f"Scientific: {1234567:.2e}")      # Scientific: 1.23e+06
print(f"Binary: {42:b}")                 # Binary: 101010
print(f"Hex: {255:x}")                   # Hex: ff

# Alignment in f-strings
print(f"{'left':<20}|")      # left                |
print(f"{'center':^20}|")    #        center        |
print(f"{'right':>20}|")     #                right|

# Padding with zeros
print(f"{42:06d}")            # 000042

# Debug mode (Python 3.8+)
x = 42
print(f"{x = }")              # x = 42
print(f"{x * 2 = }")          # x * 2 = 84
```

### .format() Method

```python
# Positional arguments
print("Hello, {}! You are {} years old.".format("Alice", 30))

# Named arguments
print("Hello, {name}! Age: {age}".format(name="Alice", age=30))

# Reuse arguments
print("{0} likes {1}. {0} also likes {2}.".format("Alice", "Python", "coffee"))

# Number formatting works the same way
print("Price: ${:,.2f}".format(1234.5))  # Price: $1,234.50
```

### % Operator (Old Style)

You will see this in older codebases. Know it, but prefer f-strings:

```python
name = "Alice"
age = 30
print("Hello, %s! Age: %d" % (name, age))   # Hello, Alice! Age: 30
print("Price: %.2f" % 19.99)                 # Price: 19.99
```

---

## Escape Characters

Special characters that start with a backslash:

| Escape | Meaning |
|--------|---------|
| `\n` | Newline |
| `\t` | Tab |
| `\\` | Literal backslash |
| `\'` | Single quote |
| `\"` | Double quote |
| `\r` | Carriage return |
| `\0` | Null character |

```python
print("Line 1\nLine 2")
# Line 1
# Line 2

print("Col1\tCol2\tCol3")
# Col1    Col2    Col3

print("She said \"hello\"")
# She said "hello"

# Raw strings disable escape processing
print(r"No \n newline here")
# No \n newline here
```

---

## String Operations

### Concatenation and Repetition

```python
# Concatenation with +
first = "Hello"
last = "World"
full = first + " " + last
print(full)  # Hello World

# Repetition with *
line = "-" * 40
print(line)  # ----------------------------------------

# Implicit concatenation (adjacent string literals)
message = ("This is a very long string that "
           "spans multiple lines in source code "
           "but is actually one string.")
```

### String Membership

```python
print("Python" in "I love Python")     # True
print("java" in "I love Python")       # False
print("java" not in "I love Python")   # True
```

### Iterating Over Strings

```python
for char in "Hello":
    print(char, end=" ")
# H e l l o

# With index using enumerate
for i, char in enumerate("Hello"):
    print(f"Index {i}: {char}")
```

---

## Practical Applications

### Data Cleaning

```python
# Clean a messy dataset value
raw = "  $1,234.56  USD  "
cleaned = raw.strip().replace("$", "").replace(",", "").replace("USD", "").strip()
price = float(cleaned)
print(price)  # 1234.56

# Normalize names
name = "  jOHN   dOE  "
normalized = " ".join(name.split()).title()
print(normalized)  # John Doe
```

### Parsing Log Lines

```python
log = "2024-01-15 14:30:22 ERROR Database connection timeout"
date = log[:10]
time = log[11:19]
level = log[20:25].strip()
message = log[26:]
print(f"Date: {date}, Level: {level}, Message: {message}")
```

### Building Reports

```python
headers = ["Name", "Age", "City"]
rows = [
    ["Alice", "30", "New York"],
    ["Bob", "25", "San Francisco"],
    ["Charlie", "35", "Chicago"],
]

# Print formatted table
header_line = " | ".join(h.ljust(15) for h in headers)
print(header_line)
print("-" * len(header_line))
for row in rows:
    print(" | ".join(val.ljust(15) for val in row))
```

---

## Key Takeaways

1. **Strings are immutable** -- all methods return new strings.
2. **Slicing syntax**: `s[start:stop:step]` -- stop is exclusive, slicing never errors.
3. **Reverse a string**: `s[::-1]`.
4. **`split()` and `join()`** are your best friends for text processing.
5. **Use f-strings** for formatting -- they are the most readable and performant.
6. **`strip()`** removes whitespace by default -- essential for cleaning data.
7. **Use `in` operator** for substring checks, not `find()`.
8. **Strings support chained method calls**: `text.strip().lower().replace(...)`.

---

## Next Up

Day 4 covers **Lists and Tuples** -- Python's ordered collection types that you will
use constantly in data science workflows.
