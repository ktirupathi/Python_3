# Day 2: Operators, Type Casting, and User Input

## Table of Contents
1. [Arithmetic Operators](#arithmetic-operators)
2. [Comparison Operators](#comparison-operators)
3. [Logical Operators](#logical-operators)
4. [Assignment Operators](#assignment-operators)
5. [Bitwise Operators](#bitwise-operators)
6. [Membership and Identity Operators](#membership-and-identity-operators)
7. [Operator Precedence](#operator-precedence)
8. [Type Casting](#type-casting)
9. [User Input](#user-input)
10. [Key Takeaways](#key-takeaways)

---

## Arithmetic Operators

These perform mathematical calculations -- the bread and butter of any program.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `7 / 2` | `3.5` |
| `//` | Floor Division | `7 // 2` | `3` |
| `%` | Modulus | `7 % 2` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

### Division Details

```python
# Regular division always returns a float
print(10 / 3)    # 3.3333333333333335
print(10 / 2)    # 5.0 (still a float!)

# Floor division truncates toward negative infinity
print(10 // 3)   # 3
print(-10 // 3)  # -4 (not -3! It floors, not truncates)

# Modulus gives the remainder
print(10 % 3)    # 1
print(-10 % 3)   # 2 (follows the floor division rule)
```

### Practical Uses

```python
# Check if a number is even or odd
number = 42
if number % 2 == 0:
    print("Even")

# Convert total minutes to hours and minutes
total_minutes = 150
hours = total_minutes // 60     # 2
minutes = total_minutes % 60    # 30
print(f"{hours}h {minutes}m")   # 2h 30m

# Compound interest: A = P * (1 + r) ** t
principal = 1000
rate = 0.05
years = 10
amount = principal * (1 + rate) ** years
print(f"${amount:.2f}")  # $1628.89
```

---

## Comparison Operators

These compare two values and return a boolean (`True` or `False`).

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater or equal | `5 >= 5` | `True` |
| `<=` | Less or equal | `5 <= 3` | `False` |

### Chained Comparisons

Python allows chaining -- a feature many languages lack:

```python
x = 15
print(10 < x < 20)       # True -- reads like math!
print(1 < 2 < 3 < 4)     # True

# Equivalent to:
print(10 < x and x < 20) # True
```

### Comparing Different Types

```python
print(1 == 1.0)    # True -- int and float compared by value
print(1 == True)   # True -- bool is a subclass of int
print(0 == False)  # True
print("1" == 1)    # False -- string and int are never equal
```

---

## Logical Operators

Used to combine boolean expressions. Think of them as the glue for conditions.

| Operator | Description | Example |
|----------|-------------|---------|
| `and` | Both must be True | `True and False` -> `False` |
| `or` | At least one True | `True or False` -> `True` |
| `not` | Inverts the value | `not True` -> `False` |

### Truth Tables

```python
# and -- both must be True
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False

# or -- at least one must be True
print(True or False)    # True
print(False or False)   # False

# not -- flips the value
print(not True)         # False
print(not False)        # True
```

### Short-Circuit Evaluation

Python is lazy -- it stops evaluating as soon as the result is determined:

```python
# 'and' stops at the first False
print(False and (1/0))  # False -- never evaluates 1/0

# 'or' stops at the first True
print(True or (1/0))    # True -- never evaluates 1/0
```

### Truthy and Falsy Values

In Python, every value has a boolean interpretation:

**Falsy values** (evaluate to `False`):
- `False`, `None`
- `0`, `0.0`, `0j`
- `""` (empty string)
- `[]`, `()`, `{}`, `set()` (empty collections)

**Everything else is truthy.**

```python
# Practical use: check if a list has elements
data = [1, 2, 3]
if data:  # truthy because it is not empty
    print("Data has elements")

name = ""
if not name:  # falsy because empty string
    print("Name is missing")
```

### Logical Operators Return Values (Not Just Booleans)

```python
# 'and' returns the first falsy value, or the last value
print("hello" and "world")  # "world"
print("" and "world")       # ""
print(0 and 42)             # 0

# 'or' returns the first truthy value, or the last value
print("" or "default")      # "default"
print(None or 0 or "found") # "found"

# Common pattern: default values
username = None
display_name = username or "Anonymous"
print(display_name)  # "Anonymous"
```

---

## Assignment Operators

Shortcuts for updating a variable's value.

| Operator | Example | Equivalent |
|----------|---------|------------|
| `=` | `x = 5` | -- |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `//=` | `x //= 3` | `x = x // 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 3` | `x = x ** 3` |

```python
count = 0
count += 1    # increment
count += 1
print(count)  # 2

price = 100
price *= 0.9  # apply 10% discount
print(price)  # 90.0
```

### Walrus Operator `:=` (Python 3.8+)

Assigns a value as part of an expression:

```python
# Without walrus operator
data = input("Enter data: ")
if len(data) > 10:
    print(f"Too long: {len(data)} chars")

# With walrus operator -- avoids calling len() twice
if (n := len(data)) > 10:
    print(f"Too long: {n} chars")
```

---

## Bitwise Operators

These operate on the binary representation of integers. Less common in data science,
but useful to know.

| Operator | Name | Example |
|----------|------|---------|
| `&` | AND | `5 & 3` -> `1` |
| `\|` | OR | `5 \| 3` -> `7` |
| `^` | XOR | `5 ^ 3` -> `6` |
| `~` | NOT | `~5` -> `-6` |
| `<<` | Left Shift | `5 << 1` -> `10` |
| `>>` | Right Shift | `5 >> 1` -> `2` |

```python
# Practical: checking flags/permissions
READ = 0b100    # 4
WRITE = 0b010   # 2
EXEC = 0b001    # 1

user_perms = READ | WRITE  # 6 (binary: 110)
print(user_perms & READ)   # 4 (truthy -- user can read)
print(user_perms & EXEC)   # 0 (falsy -- user cannot execute)
```

---

## Membership and Identity Operators

### Membership: `in` and `not in`

Check if a value exists in a sequence:

```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)      # True
print("grape" not in fruits)   # True

# Works with strings too
print("py" in "python")        # True

# Works with dictionaries (checks keys)
config = {"host": "localhost", "port": 8080}
print("host" in config)        # True
print("localhost" in config)   # False (checks keys, not values)
```

### Identity: `is` and `is not`

Check if two variables point to the same object in memory:

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)     # True -- same values
print(a is b)     # False -- different objects
print(a is c)     # True -- same object

# Always use 'is' for None checks
x = None
print(x is None)      # True (correct way)
print(x == None)      # True (works but discouraged)
```

---

## Operator Precedence

From highest to lowest priority:

| Priority | Operator |
|----------|----------|
| 1 | `**` (exponentiation) |
| 2 | `~`, `+x`, `-x` (unary) |
| 3 | `*`, `/`, `//`, `%` |
| 4 | `+`, `-` |
| 5 | `<<`, `>>` |
| 6 | `&` |
| 7 | `^` |
| 8 | `\|` |
| 9 | `==`, `!=`, `<`, `>`, `<=`, `>=`, `is`, `in` |
| 10 | `not` |
| 11 | `and` |
| 12 | `or` |

**Best practice:** Use parentheses to make intent clear, even when precedence rules
would give you the right answer:

```python
# Hard to read
result = 2 + 3 * 4 ** 2

# Clear
result = 2 + (3 * (4 ** 2))   # 50
```

---

## Type Casting

Converting one data type to another. Think of it as pouring water from a bottle into
a glass -- same water, different container.

### Implicit Casting (Automatic)

Python automatically converts types in mixed operations:

```python
x = 5       # int
y = 2.0     # float
result = x + y
print(result)        # 7.0
print(type(result))  # <class 'float'> -- int was promoted to float
```

### Explicit Casting (Manual)

Use built-in functions to convert types:

```python
# String to Integer
age_str = "25"
age = int(age_str)
print(age + 5)  # 30

# String to Float
price = float("19.99")
print(price)  # 19.99

# Number to String
score = 95
message = "Score: " + str(score)
print(message)  # Score: 95

# Float to Integer (truncates, does not round)
print(int(3.7))    # 3
print(int(-3.7))   # -3

# To round properly, use round()
print(round(3.7))  # 4
print(round(3.5))  # 4 (banker's rounding in Python 3)
print(round(2.5))  # 2 (rounds to nearest even!)

# Boolean casting
print(bool(0))      # False
print(bool(42))     # True
print(bool(""))     # False
print(bool("hi"))   # True

# Integer to Boolean
print(int(True))    # 1
print(int(False))   # 0
```

### Common Casting Errors

```python
# Cannot convert non-numeric strings to numbers
# int("hello")   # ValueError: invalid literal for int()
# float("abc")   # ValueError: could not convert string to float

# Safe conversion pattern
def safe_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

print(safe_int("42"))      # 42
print(safe_int("hello"))   # 0
print(safe_int(None))      # 0
```

---

## User Input

The `input()` function pauses the program and waits for the user to type something.

### Basic Input

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

**Important:** `input()` always returns a **string**, even if the user types a number:

```python
age = input("Enter your age: ")
print(type(age))  # <class 'str'>

# You must cast it to use it as a number
age = int(input("Enter your age: "))
next_year = age + 1
print(f"Next year you will be {next_year}")
```

### Handling Bad Input

```python
while True:
    try:
        age = int(input("Enter your age: "))
        if 0 < age < 150:
            break
        print("Please enter a realistic age.")
    except ValueError:
        print("That is not a valid number. Try again.")

print(f"Your age is {age}")
```

### Reading Multiple Values

```python
# Split input into multiple values
x, y = input("Enter two numbers separated by space: ").split()
x, y = int(x), int(y)
print(f"Sum: {x + y}")

# Using map for cleaner conversion
a, b, c = map(int, input("Enter three numbers: ").split())
print(f"Average: {(a + b + c) / 3}")
```

### Practical Example: Simple Calculator

```python
num1 = float(input("First number: "))
operator = input("Operator (+, -, *, /): ")
num2 = float(input("Second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2 if num2 != 0 else "undefined"
else:
    result = "Invalid operator"

print(f"Result: {result}")
```

---

## Key Takeaways

1. **Arithmetic operators**: `/` always returns float; `//` floors; `%` gives remainder.
2. **Chained comparisons** like `10 < x < 20` are Pythonic and readable.
3. **Short-circuit evaluation**: `and`/`or` stop early, and they return values, not just booleans.
4. **Truthy/falsy**: Empty collections and zero are falsy; nearly everything else is truthy.
5. **Type casting**: Use `int()`, `float()`, `str()`, `bool()` for explicit conversions.
6. **`input()` always returns a string** -- always cast to the type you need.
7. **Use parentheses** for clarity when mixing operators.
8. **Use `is` for `None` checks**, `==` for value comparisons.

---

## Next Up

Day 3 dives into **Strings** -- slicing, methods, and formatting techniques that are
essential for data cleaning and text processing.
