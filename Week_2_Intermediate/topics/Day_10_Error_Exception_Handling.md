# Day 10: Error and Exception Handling, Custom Exceptions

## Introduction

Errors are inevitable: files go missing, APIs return unexpected data, users provide bad
input. Robust exception handling is what separates a script that crashes mysteriously
from one that fails gracefully, logs the problem, and recovers. This is especially
important in data pipelines where one corrupted row should not bring down an entire
ETL job.

---

## 1. Errors vs. Exceptions

- **Syntax errors** are caught by the parser before your code runs.
- **Exceptions** occur at runtime when something goes wrong.

```python
# Syntax error -- caught before execution
# if True print("hello")  # SyntaxError

# Exception -- happens at runtime
result = 10 / 0  # ZeroDivisionError
```

---

## 2. Common Built-in Exceptions

| Exception | When It Occurs |
|-----------|----------------|
| `ZeroDivisionError` | Division by zero |
| `TypeError` | Wrong type in an operation |
| `ValueError` | Right type, wrong value |
| `KeyError` | Missing dictionary key |
| `IndexError` | List index out of range |
| `FileNotFoundError` | File does not exist |
| `AttributeError` | Object lacks the attribute |
| `ImportError` | Module cannot be imported |
| `StopIteration` | Iterator exhausted |
| `OSError` | Operating system error |

---

## 3. The try/except Block

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### Catching the Exception Object

```python
try:
    num = int("abc")
except ValueError as e:
    print(f"Conversion failed: {e}")
```

### Catching Multiple Exceptions

```python
try:
    data = {"key": "value"}
    print(data["missing"])
except (KeyError, TypeError) as e:
    print(f"Data access error: {e}")
```

### Multiple except Blocks

```python
try:
    value = int(input("Enter a number: "))
    result = 100 / value
except ValueError:
    print("That is not a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
```

---

## 4. else and finally

### else -- Runs Only If No Exception Occurred

```python
try:
    number = int("42")
except ValueError:
    print("Invalid number")
else:
    print(f"Successfully parsed: {number}")
```

### finally -- Always Runs

```python
try:
    f = open("data.txt")
    content = f.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("This always executes -- good for cleanup.")
```

### Complete Pattern

```python
try:
    # risky operation
    result = perform_calculation(data)
except SpecificError as e:
    # handle known error
    log_error(e)
    result = default_value
else:
    # success path
    save_result(result)
finally:
    # cleanup regardless of outcome
    close_resources()
```

---

## 5. Raising Exceptions

Use `raise` to signal that something went wrong.

```python
def set_age(age):
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    if age > 150:
        raise ValueError(f"Age seems unrealistic: {age}")
    return age
```

### Re-raising an Exception

```python
try:
    process_data(raw_data)
except ValueError as e:
    log_error(e)
    raise  # re-raise the same exception
```

### Chaining Exceptions

```python
try:
    value = int("abc")
except ValueError as original:
    raise RuntimeError("Data processing failed") from original
```

This preserves the original traceback, making debugging easier.

---

## 6. The Exception Hierarchy

All exceptions inherit from `BaseException`. Most user-relevant exceptions inherit
from `Exception`.

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   └── OverflowError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── OSError
    │   └── FileNotFoundError
    ├── TypeError
    ├── ValueError
    └── ...
```

> **Never catch `BaseException`** unless you have a very specific reason. Catching it
> will swallow `KeyboardInterrupt` and `SystemExit`.

---

## 7. Custom Exceptions

Create your own exception classes by inheriting from `Exception`.

### Basic Custom Exception

```python
class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the account balance."""
    pass
```

### Custom Exception with Extra Data

```python
class ValidationError(Exception):
    def __init__(self, field, message, value=None):
        self.field = field
        self.value = value
        super().__init__(message)

    def __str__(self):
        return f"ValidationError on '{self.field}': {self.args[0]} (got {self.value!r})"
```

### Using Custom Exceptions

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Cannot withdraw ${amount:.2f}. Balance is ${balance:.2f}."
        )

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

# Usage
account = BankAccount(100)
try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(e)  # Cannot withdraw $150.00. Balance is $100.00.
    print(f"Short by: ${e.amount - e.balance:.2f}")
```

### Exception Hierarchies for Applications

```python
class AppError(Exception):
    """Base exception for our application."""
    pass

class DatabaseError(AppError):
    """Database-related errors."""
    pass

class ConnectionError(DatabaseError):
    """Cannot connect to database."""
    pass

class QueryError(DatabaseError):
    """Invalid or failed query."""
    pass

class AuthenticationError(AppError):
    """Authentication failures."""
    pass
```

This lets callers catch broad or narrow exceptions:

```python
try:
    run_query(sql)
except ConnectionError:
    retry_connection()
except DatabaseError:
    log_db_error()
except AppError:
    log_generic_error()
```

---

## 8. Best Practices

### 1. Be Specific with Exceptions

```python
# BAD -- catches everything, hides bugs
try:
    result = compute(data)
except Exception:
    pass

# GOOD -- catches only what you expect
try:
    result = compute(data)
except (ValueError, TypeError) as e:
    handle_error(e)
```

### 2. Use EAFP (Easier to Ask Forgiveness than Permission)

```python
# LBYL style (Look Before You Leap) -- less Pythonic
if "key" in my_dict:
    value = my_dict["key"]
else:
    value = default

# EAFP style -- Pythonic
try:
    value = my_dict["key"]
except KeyError:
    value = default
```

### 3. Log Before Re-raising

```python
import logging

try:
    process(data)
except ValueError as e:
    logging.error(f"Processing failed: {e}")
    raise
```

### 4. Clean Up with finally or Context Managers

```python
# Prefer context managers when possible
with open("data.txt") as f:
    data = f.read()

# Use finally when context managers are not available
resource = acquire_resource()
try:
    use(resource)
finally:
    release(resource)
```

### 5. Do Not Use Exceptions for Flow Control

```python
# BAD -- using exception as a loop exit
try:
    while True:
        item = get_next_item()
except StopIteration:
    pass

# GOOD -- use a proper condition
for item in items:
    process(item)
```

---

## 9. Data-Science Patterns

### Robust Row Processing

```python
errors = []
results = []

for i, row in enumerate(raw_data):
    try:
        cleaned = clean_row(row)
        results.append(cleaned)
    except (ValueError, KeyError) as e:
        errors.append({"row": i, "error": str(e), "data": row})

print(f"Processed {len(results)} rows, {len(errors)} errors")
```

### Retry Pattern

```python
import time

def fetch_with_retry(url, max_retries=3, delay=1):
    for attempt in range(max_retries):
        try:
            return fetch(url)
        except ConnectionError:
            if attempt == max_retries - 1:
                raise
            time.sleep(delay * (2 ** attempt))  # exponential backoff
```

### Assertions for Data Validation

```python
def train_model(X, y):
    assert X.shape[0] == y.shape[0], \
        f"Feature rows ({X.shape[0]}) != label count ({y.shape[0]})"
    assert X.shape[0] > 0, "Training data is empty"
    # ... training logic
```

> Assertions can be disabled with `python -O`, so never use them for input validation
> in production code. Use `raise ValueError(...)` instead.

---

## 10. Debugging Tips

1. **Read the traceback bottom-up** -- the last line is the error, working up shows the
   call stack.
2. **Use `traceback` module** for programmatic access to exception info.
3. **Use `logging.exception()`** inside except blocks to capture the full traceback.

```python
import traceback

try:
    risky_operation()
except Exception:
    tb = traceback.format_exc()
    print(tb)
```

---

## Key Takeaways

1. Use `try/except` for known failure points; be specific about which exceptions
   to catch.
2. `else` runs on success; `finally` always runs -- use them for clean control flow.
3. Raise exceptions early to fail fast; catch them at the level where you can
   meaningfully respond.
4. Create custom exceptions for domain-specific errors in larger applications.
5. In data pipelines, log errors and continue processing rather than crashing on the
   first bad row.
