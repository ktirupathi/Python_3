# Day 14: Decorators, Context Managers, and Regular Expressions

## Introduction

Today covers three distinct but important intermediate topics. **Decorators** add
behavior to functions without modifying them. **Context managers** ensure proper
resource cleanup. **Regular expressions** are the power tool for text pattern matching.
Together, these skills round out your intermediate Python toolkit.

---

## 1. Decorators

A **decorator** is a function that takes another function and extends its behavior
without modifying the original function's code.

### Functions Are First-Class Objects

In Python, functions can be assigned to variables, passed as arguments, and returned
from other functions.

```python
def greet(name):
    return f"Hello, {name}!"

say_hello = greet           # assign function to variable
print(say_hello("Alice"))   # Hello, Alice!

def apply(func, value):
    return func(value)

print(apply(greet, "Bob"))  # Hello, Bob!
```

### Closures -- Functions That Remember

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor   # 'factor' is remembered from enclosing scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))  # 10
print(triple(5))  # 15
```

### Your First Decorator

```python
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

add(3, 5)
# Calling add with args=(3, 5), kwargs={}
# add returned 8
```

The `@log_calls` syntax is equivalent to `add = log_calls(add)`.

### Preserving Function Metadata with functools.wraps

```python
from functools import wraps

def log_calls(func):
    @wraps(func)  # preserves __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_calls
def add(a, b):
    """Add two numbers."""
    return a + b

print(add.__name__)  # add (not 'wrapper')
print(add.__doc__)   # Add two numbers.
```

### Practical Decorators

#### Timing Decorator

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

slow_sum(10_000_000)  # slow_sum took 0.2134s
```

#### Retry Decorator

```python
import time
from functools import wraps

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"Attempt {attempt} failed: {e}. Retrying...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def fetch_data(url):
    # simulate unreliable network
    import random
    if random.random() < 0.7:
        raise ConnectionError("Network timeout")
    return {"data": "success"}
```

#### Cache / Memoize Decorator

```python
from functools import wraps

def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))  # instant, without memoize this would take forever
```

> Python provides `@functools.lru_cache` and `@functools.cache` as built-in
> memoization decorators.

### Stacking Decorators

```python
@timer
@log_calls
def multiply(a, b):
    return a * b

# Equivalent to: multiply = timer(log_calls(multiply))
```

### Class-Based Decorators

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} called {self.count} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")

say_hello()  # say_hello called 1 times \n Hello!
say_hello()  # say_hello called 2 times \n Hello!
```

---

## 2. Context Managers

Context managers ensure that resources are properly acquired and released. The `with`
statement is the interface.

### Built-in Context Managers

```python
# File handling
with open("data.txt") as f:
    content = f.read()

# Thread locks
import threading
lock = threading.Lock()
with lock:
    # critical section
    pass
```

### Creating Context Managers with a Class

Implement `__enter__` and `__exit__`:

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # Return False (or None) to propagate exceptions
        # Return True to suppress exceptions
        return False

with FileManager("test.txt", "w") as f:
    f.write("Hello, context manager!")
```

### Creating Context Managers with contextlib

The `@contextmanager` decorator is simpler for most use cases:

```python
from contextlib import contextmanager

@contextmanager
def timer_context(label):
    import time
    start = time.perf_counter()
    try:
        yield  # code inside 'with' block runs here
    finally:
        elapsed = time.perf_counter() - start
        print(f"{label}: {elapsed:.4f}s")

with timer_context("Data processing"):
    total = sum(range(10_000_000))
# Data processing: 0.2145s
```

### Practical Context Managers

#### Temporary Directory

```python
from contextlib import contextmanager
import tempfile
import shutil

@contextmanager
def temp_directory():
    dirpath = tempfile.mkdtemp()
    try:
        yield dirpath
    finally:
        shutil.rmtree(dirpath)

with temp_directory() as tmpdir:
    # work with temporary files in tmpdir
    pass
# directory automatically deleted
```

#### Database Connection

```python
@contextmanager
def db_connection(db_url):
    conn = create_connection(db_url)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
```

#### Redirect stdout

```python
from contextlib import redirect_stdout
import io

buffer = io.StringIO()
with redirect_stdout(buffer):
    print("This goes to the buffer")

captured = buffer.getvalue()
print(f"Captured: {captured!r}")
```

---

## 3. Regular Expressions

Regular expressions (regex) are patterns for matching, searching, and manipulating
text. Python's `re` module provides full regex support.

### Basic Patterns

| Pattern | Matches |
|---------|---------|
| `.` | Any character except newline |
| `\d` | Digit (0-9) |
| `\D` | Non-digit |
| `\w` | Word character (a-z, A-Z, 0-9, _) |
| `\W` | Non-word character |
| `\s` | Whitespace (space, tab, newline) |
| `\S` | Non-whitespace |
| `^` | Start of string |
| `$` | End of string |
| `\b` | Word boundary |

### Quantifiers

| Pattern | Meaning |
|---------|---------|
| `*` | 0 or more |
| `+` | 1 or more |
| `?` | 0 or 1 |
| `{n}` | Exactly n |
| `{n,m}` | Between n and m |
| `{n,}` | n or more |

### Core re Functions

```python
import re

text = "My phone is 123-456-7890 and email is alice@example.com"

# re.search -- find first match
match = re.search(r"\d{3}-\d{3}-\d{4}", text)
if match:
    print(match.group())  # 123-456-7890

# re.findall -- find all matches
emails = re.findall(r"\w+@\w+\.\w+", text)
print(emails)  # ['alice@example.com']

# re.match -- match at the START of string only
result = re.match(r"My", text)
print(result.group())  # My

# re.sub -- search and replace
cleaned = re.sub(r"\d{3}-\d{3}-\d{4}", "[REDACTED]", text)
print(cleaned)  # My phone is [REDACTED] and email is alice@example.com

# re.split -- split by pattern
parts = re.split(r"[,;]\s*", "apple, banana; cherry,  date")
print(parts)  # ['apple', 'banana', 'cherry', 'date']
```

### Groups -- Capturing Parts of a Match

```python
import re

pattern = r"(\d{4})-(\d{2})-(\d{2})"
match = re.search(pattern, "Date: 2025-03-15")

print(match.group())   # 2025-03-15 (full match)
print(match.group(1))  # 2025 (year)
print(match.group(2))  # 03 (month)
print(match.group(3))  # 15 (day)
print(match.groups())  # ('2025', '03', '15')
```

### Named Groups

```python
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
match = re.search(pattern, "Date: 2025-03-15")

print(match.group("year"))   # 2025
print(match.group("month"))  # 03
print(match.groupdict())     # {'year': '2025', 'month': '03', 'day': '15'}
```

### Compiled Patterns

For patterns used repeatedly, compile them for better performance:

```python
email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

texts = ["Contact alice@example.com", "Or bob@company.org", "No email here"]
for text in texts:
    match = email_pattern.search(text)
    if match:
        print(f"Found: {match.group()}")
```

### Flags

```python
# Case-insensitive matching
re.findall(r"python", "Python PYTHON python", re.IGNORECASE)
# ['Python', 'PYTHON', 'python']

# Multiline: ^ and $ match line boundaries
text = "line1\nline2\nline3"
re.findall(r"^\w+", text, re.MULTILINE)
# ['line1', 'line2', 'line3']

# Verbose: allows comments and whitespace in pattern
pattern = re.compile(r"""
    (?P<area>\d{3})    # area code
    [-.\s]?            # optional separator
    (?P<prefix>\d{3})  # prefix
    [-.\s]?            # optional separator
    (?P<line>\d{4})    # line number
""", re.VERBOSE)
```

### Common Patterns for Data Science

```python
import re

# Extract numbers from text
numbers = re.findall(r"-?\d+\.?\d*", "Temperature: -3.5C, Humidity: 82%")
print(numbers)  # ['-3.5', '82']

# Clean whitespace
text = "  too   many    spaces  "
cleaned = re.sub(r"\s+", " ", text).strip()
print(cleaned)  # "too many spaces"

# Validate email
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

# Parse log lines
log = "2025-03-15 14:30:22 ERROR Database connection timeout"
pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)"
match = re.match(pattern, log)
date, time, level, message = match.groups()

# Extract key-value pairs
config = "host=localhost port=5432 dbname=mydb"
pairs = re.findall(r"(\w+)=(\S+)", config)
config_dict = dict(pairs)
print(config_dict)  # {'host': 'localhost', 'port': '5432', 'dbname': 'mydb'}
```

### Lookahead and Lookbehind

```python
import re

# Positive lookahead: match 'foo' followed by 'bar'
re.findall(r"foo(?=bar)", "foobar foobaz")  # ['foo']

# Negative lookahead: match 'foo' NOT followed by 'bar'
re.findall(r"foo(?!bar)", "foobar foobaz")  # ['foo'] (the foobaz one)

# Positive lookbehind: match digits preceded by '$'
re.findall(r"(?<=\$)\d+", "Price: $100, Cost: $50")  # ['100', '50']

# Negative lookbehind: match digits NOT preceded by '$'
re.findall(r"(?<!\$)\d+", "Price: $100, Count: 5")  # ['00', '5']
```

---

## Key Takeaways

1. **Decorators** wrap functions to add behavior (logging, timing, caching, retrying)
   without modifying the original function.
2. Always use `@functools.wraps` in decorators to preserve function metadata.
3. **Context managers** (`with` statement) guarantee cleanup -- use them for files,
   locks, connections, and temporary resources.
4. Use `@contextmanager` from contextlib for simple context managers.
5. **Regular expressions** are powerful for text parsing -- learn the core patterns
   (`\d`, `\w`, `\s`, `+`, `*`, `?`) and functions (`search`, `findall`, `sub`).
6. Compile regex patterns that are used repeatedly for better performance.
7. Use named groups and verbose mode for readability in complex patterns.
