# Day 6: Conditionals and Loops

## Table of Contents
1. [if Statements](#if-statements)
2. [if-elif-else Chains](#if-elif-else-chains)
3. [Ternary Operator](#ternary-operator)
4. [Match-Case (Python 3.10+)](#match-case)
5. [for Loops](#for-loops)
6. [while Loops](#while-loops)
7. [Loop Control: break, continue, pass](#loop-control)
8. [The else Clause on Loops](#the-else-clause-on-loops)
9. [Nested Loops](#nested-loops)
10. [Iterating Techniques](#iterating-techniques)
11. [Performance Considerations](#performance-considerations)
12. [Practical Applications](#practical-applications)
13. [Key Takeaways](#key-takeaways)

---

## if Statements

The `if` statement lets your program make decisions. Think of it as a fork in the road:
if a condition is true, take one path; otherwise, take another.

```python
age = 20

if age >= 18:
    print("You are an adult.")
```

The block under `if` runs **only** when the condition evaluates to `True`.

### if-else

```python
temperature = 35

if temperature > 30:
    print("It is hot outside.")
else:
    print("The weather is pleasant.")
```

---

## if-elif-else Chains

When you have multiple conditions to check, use `elif` (short for "else if"):

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")  # Score: 85, Grade: B
```

**Important:** Python evaluates conditions top to bottom and stops at the **first True**
condition. Order matters!

```python
# Wrong order -- everyone gets "positive"
x = 100
if x > 0:
    print("positive")      # this always wins for positive numbers
elif x > 50:
    print("above fifty")   # never reached for values > 0

# Correct order -- most specific first
if x > 50:
    print("above fifty")
elif x > 0:
    print("positive")
```

### Nested if Statements

```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive.")
    else:
        print("Get a license first.")
else:
    print("You are too young to drive.")

# Often cleaner with logical operators:
if age >= 18 and has_license:
    print("You can drive.")
elif age >= 18:
    print("Get a license first.")
else:
    print("You are too young to drive.")
```

---

## Ternary Operator

A one-line `if-else` expression:

```python
# Syntax: value_if_true if condition else value_if_false

age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # adult

# Useful for assignments
x = -5
abs_x = x if x >= 0 else -x
print(abs_x)  # 5

# Can be nested (but avoid for readability)
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(grade)  # B -- works but hard to read; prefer if-elif instead
```

---

## Match-Case (Python 3.10+)

Structural pattern matching -- Python's version of switch-case, but much more powerful:

```python
command = "quit"

match command:
    case "start":
        print("Starting the program...")
    case "stop" | "quit" | "exit":
        print("Shutting down...")
    case "pause":
        print("Pausing...")
    case _:
        print(f"Unknown command: {command}")
```

### Pattern Matching with Structure

```python
# Match on data structure
point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"On x-axis at {x}")
    case (0, y):
        print(f"On y-axis at {y}")
    case (x, y):
        print(f"Point at ({x}, {y})")

# Match with guards
match point:
    case (x, y) if x == y:
        print("On the diagonal")
    case (x, y):
        print(f"Not on diagonal: ({x}, {y})")
```

---

## for Loops

A `for` loop iterates over any **iterable** (list, string, range, dict, file, etc.).

### Basic for Loop

```python
# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterate over a string
for char in "Python":
    print(char, end=" ")  # P y t h o n

# Iterate over a dictionary
person = {"name": "Alice", "age": 30}
for key, value in person.items():
    print(f"{key}: {value}")
```

### The range() Function

`range(start, stop, step)` generates a sequence of numbers:

```python
# range(stop) -- 0 to stop-1
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4

# range(start, stop)
for i in range(2, 6):
    print(i, end=" ")  # 2 3 4 5

# range(start, stop, step)
for i in range(0, 20, 3):
    print(i, end=" ")  # 0 3 6 9 12 15 18

# Counting down
for i in range(10, 0, -1):
    print(i, end=" ")  # 10 9 8 7 6 5 4 3 2 1
```

### enumerate() -- Get Index and Value

```python
colors = ["red", "green", "blue"]

# Instead of this:
for i in range(len(colors)):
    print(f"{i}: {colors[i]}")

# Do this (Pythonic):
for i, color in enumerate(colors):
    print(f"{i}: {color}")

# Start from a different index
for i, color in enumerate(colors, start=1):
    print(f"{i}. {color}")
# 1. red
# 2. green
# 3. blue
```

### zip() -- Iterate Multiple Sequences

```python
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]
grades = ["A", "B+", "A-"]

for name, score, grade in zip(names, scores, grades):
    print(f"{name}: {score} ({grade})")

# zip stops at the shortest iterable
# Use itertools.zip_longest to go to the longest
```

---

## while Loops

A `while` loop repeats as long as a condition is `True`. Use it when you do not know
how many iterations you need.

```python
# Countdown
count = 5
while count > 0:
    print(count)
    count -= 1
print("Liftoff!")

# Input validation
while True:
    password = input("Enter password: ")
    if len(password) >= 8:
        print("Password accepted.")
        break
    print("Too short. Minimum 8 characters.")

# Converging calculation (e.g., Newton's method for square root)
number = 25
guess = number / 2
tolerance = 0.0001

while abs(guess * guess - number) > tolerance:
    guess = (guess + number / guess) / 2

print(f"Square root of {number} is approximately {guess:.6f}")
```

### Infinite Loops

```python
# Intentional infinite loop with break condition
while True:
    user_input = input("Type 'quit' to exit: ")
    if user_input.lower() == "quit":
        break
    print(f"You typed: {user_input}")

# Accidental infinite loop -- always ensure the condition can become False
# x = 1
# while x > 0:   # x is always > 0, this never ends!
#     x += 1
```

---

## Loop Control: break, continue, pass

### break -- Exit the Loop Immediately

```python
# Find the first negative number
numbers = [4, 7, 2, -1, 8, -3, 5]
for num in numbers:
    if num < 0:
        print(f"First negative: {num}")
        break
# Output: First negative: -1
```

### continue -- Skip to the Next Iteration

```python
# Print only positive numbers
numbers = [4, -2, 7, -1, 3, -5, 8]
for num in numbers:
    if num < 0:
        continue  # skip negative numbers
    print(num, end=" ")  # 4 7 3 8
```

### pass -- Do Nothing (Placeholder)

```python
# Placeholder for future code
for i in range(10):
    if i % 2 == 0:
        pass  # TODO: implement even number handling
    else:
        print(f"{i} is odd")
```

---

## The else Clause on Loops

Python has a unique feature: an `else` block on loops that runs **only if the loop
completed without hitting a `break`**.

```python
# Check if a number is prime
num = 17

for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        print(f"{num} is not prime (divisible by {i})")
        break
else:
    # This runs only if no break occurred
    print(f"{num} is prime!")
# Output: 17 is prime!

# Useful for search patterns
target = "grape"
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} not found in the list.")
# Output: grape not found in the list.
```

Think of the `else` as "no break" -- it runs when the loop finishes naturally.

---

## Nested Loops

A loop inside another loop. The inner loop runs completely for each iteration of the
outer loop.

```python
# Multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()  # new line after each row

# Output:
#    1   2   3   4   5
#    2   4   6   8  10
#    3   6   9  12  15
#    4   8  12  16  20
#    5  10  15  20  25
```

### Pattern Printing

```python
# Right triangle
n = 5
for i in range(1, n + 1):
    print("* " * i)
# *
# * *
# * * *
# * * * *
# * * * * *

# Pyramid
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "* " * i
    print(spaces + stars)
```

### Breaking Out of Nested Loops

```python
# break only exits the innermost loop
for i in range(3):
    for j in range(3):
        if j == 2:
            break  # only breaks inner loop
        print(f"({i}, {j})", end=" ")
    print()

# To break out of both, use a flag or a function
def find_in_matrix(matrix, target):
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == target:
                return (i, j)
    return None

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = find_in_matrix(matrix, 5)
print(f"Found at: {result}")  # Found at: (1, 1)
```

---

## Iterating Techniques

### Iterating in Reverse

```python
numbers = [1, 2, 3, 4, 5]

# reversed() -- does not create a new list
for num in reversed(numbers):
    print(num, end=" ")  # 5 4 3 2 1

# Slice
for num in numbers[::-1]:
    print(num, end=" ")  # 5 4 3 2 1 (creates a copy)
```

### Iterating Over Multiple Sequences

```python
# zip for parallel iteration
names = ["Alice", "Bob"]
ages = [30, 25]
for name, age in zip(names, ages):
    print(f"{name} is {age}")

# Combine with enumerate
for i, (name, age) in enumerate(zip(names, ages)):
    print(f"{i}: {name} is {age}")
```

### Iterating Over Dictionaries

```python
data = {"a": 1, "b": 2, "c": 3}

# Keys only
for key in data:
    print(key)

# Values only
for value in data.values():
    print(value)

# Both
for key, value in data.items():
    print(f"{key} = {value}")

# Sorted keys
for key in sorted(data.keys()):
    print(f"{key}: {data[key]}")
```

---

## Performance Considerations

```python
# Prefer list comprehension over append loop
# Slower:
result = []
for i in range(1000000):
    result.append(i ** 2)

# Faster:
result = [i ** 2 for i in range(1000000)]

# Use generators for memory efficiency (covered later)
# Instead of creating a huge list:
total = sum(i ** 2 for i in range(1000000))  # generator expression

# Avoid modifying a list while iterating over it
numbers = [1, 2, 3, 4, 5]
# WRONG: modifying during iteration
# for num in numbers:
#     if num % 2 == 0:
#         numbers.remove(num)  # skips elements!

# CORRECT: iterate over a copy, or build a new list
odds = [num for num in numbers if num % 2 != 0]
```

---

## Practical Applications

### Menu-Driven Program

```python
def show_menu():
    print("\n=== Task Manager ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

tasks = []

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print(f"Added: {task}")
    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"  {i}. {task}")
    elif choice == "3":
        idx = int(input("Task number to remove: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            print(f"Removed: {removed}")
    elif choice == "4":
        print("Goodbye!")
        break
```

### Data Validation Loop

```python
def get_valid_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if 0 < age < 150:
                return age
            print("Age must be between 1 and 149.")
        except ValueError:
            print("Please enter a valid number.")

# age = get_valid_age()
```

### FizzBuzz

```python
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

---

## Key Takeaways

1. **if-elif-else**: Order conditions from most specific to least specific.
2. **Ternary operator**: `x if condition else y` for simple one-line conditionals.
3. **for loops** iterate over iterables; **while loops** repeat until a condition is False.
4. **`range()`**: Use `range(start, stop, step)` -- stop is exclusive.
5. **`enumerate()`** gives you index and value -- never use `range(len(...))`.
6. **`zip()`** iterates over multiple sequences in parallel.
7. **`break`** exits the loop, **`continue`** skips to the next iteration.
8. **Loop `else`** runs only when the loop completes without `break`.
9. **Never modify a list** while iterating over it -- use a comprehension instead.
10. **List comprehensions** are faster and more Pythonic than append loops.

---

## Next Up

Day 7 covers **Functions** -- the building blocks for writing reusable, modular code
including parameters, `*args`, `**kwargs`, and lambda expressions.
