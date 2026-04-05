# Day 9: File Handling -- Read, Write, CSV, JSON

## Introduction

Almost every data-science workflow starts and ends with files: reading raw data,
writing cleaned output, saving model parameters, and logging results. Python provides
powerful built-in tools for text files and standard-library modules for CSV and JSON --
the two most common interchange formats.

---

## 1. Opening and Closing Files

### The `open()` Built-in

```python
f = open("data.txt", "r")   # open for reading
content = f.read()
f.close()                    # always close!
```

**Problem:** If an error occurs between `open()` and `close()`, the file stays open and
resources leak.

### The `with` Statement (Context Manager)

```python
with open("data.txt", "r") as f:
    content = f.read()
# file is automatically closed here, even if an exception occurs
```

> **Best practice:** Always use `with` for file operations.

---

## 2. File Modes

| Mode | Description |
|------|-------------|
| `"r"` | Read (default). File must exist. |
| `"w"` | Write. Creates file or **truncates** existing. |
| `"a"` | Append. Creates file or adds to end. |
| `"x"` | Exclusive create. Fails if file exists. |
| `"b"` | Binary mode (e.g., `"rb"`, `"wb"`). |
| `"t"` | Text mode (default). |
| `"r+"` | Read and write. |

---

## 3. Reading Text Files

### Read Entire File

```python
with open("poem.txt") as f:
    text = f.read()          # single string with newlines
```

### Read Line by Line

```python
with open("poem.txt") as f:
    for line in f:           # memory-efficient: one line at a time
        print(line.strip())
```

### Read All Lines into a List

```python
with open("poem.txt") as f:
    lines = f.readlines()    # list of strings, each ending with '\n'
```

### Read a Fixed Number of Characters

```python
with open("poem.txt") as f:
    chunk = f.read(100)      # first 100 characters
```

---

## 4. Writing Text Files

### Write (Overwrites)

```python
with open("output.txt", "w") as f:
    f.write("First line\n")
    f.write("Second line\n")
```

### Write Multiple Lines

```python
lines = ["alpha\n", "beta\n", "gamma\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)      # does NOT add newlines automatically
```

### Append

```python
with open("log.txt", "a") as f:
    f.write("New log entry\n")
```

### Using print() to Write

```python
with open("output.txt", "w") as f:
    print("Hello, file!", file=f)
    print(42, "items", sep=", ", file=f)
```

---

## 5. Working with File Paths (pathlib)

The `pathlib` module provides an object-oriented interface to file paths -- preferred
over `os.path` in modern Python.

```python
from pathlib import Path

# Build paths
data_dir = Path("data")
file_path = data_dir / "sales" / "2025.csv"

# Check existence
file_path.exists()
file_path.is_file()
data_dir.is_dir()

# Read and write shortcuts
text = file_path.read_text(encoding="utf-8")
file_path.write_text("new content", encoding="utf-8")

# Iterate over directory
for p in data_dir.glob("*.csv"):
    print(p.name)

# Recursive glob
for p in data_dir.rglob("*.json"):
    print(p)
```

---

## 6. CSV Files

CSV (Comma-Separated Values) is the workhorse format for tabular data.

### Reading CSV with the csv Module

```python
import csv

with open("employees.csv", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        print(row)           # row is a list of strings
```

### Reading CSV as Dictionaries

```python
import csv

with open("employees.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["salary"])
```

### Writing CSV

```python
import csv

data = [
    ["name", "age", "city"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "London"],
]

with open("people.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
```

### Writing CSV from Dictionaries

```python
import csv

records = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "London"},
]

with open("people.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
    writer.writeheader()
    writer.writerows(records)
```

### Handling Different Delimiters

```python
# Tab-separated file
with open("data.tsv", newline="") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        print(row)
```

---

## 7. JSON Files

JSON (JavaScript Object Notation) is the standard for web APIs and configuration
files. Python's `json` module maps JSON objects to dicts and JSON arrays to lists.

### JSON <-> Python Type Mapping

| JSON | Python |
|------|--------|
| object `{}` | `dict` |
| array `[]` | `list` |
| string | `str` |
| number (int) | `int` |
| number (float) | `float` |
| true/false | `True`/`False` |
| null | `None` |

### Reading JSON

```python
import json

with open("config.json") as f:
    config = json.load(f)    # parse file -> Python object

print(config["database"]["host"])
```

### Parsing a JSON String

```python
import json

text = '{"name": "Alice", "scores": [90, 85, 92]}'
data = json.loads(text)      # parse string -> Python object
```

### Writing JSON

```python
import json

data = {
    "name": "Alice",
    "age": 30,
    "courses": ["Python", "Statistics", "ML"],
}

with open("student.json", "w") as f:
    json.dump(data, f, indent=4)
```

### Converting Python Object to JSON String

```python
json_str = json.dumps(data, indent=2, sort_keys=True)
print(json_str)
```

### Handling Non-serializable Types

```python
import json
from datetime import datetime

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data = {"event": "launch", "timestamp": datetime.now()}
print(json.dumps(data, cls=DateEncoder, indent=2))
```

---

## 8. Binary Files

For images, audio, or any non-text data, use binary mode.

```python
# Copy a binary file
with open("image.png", "rb") as src:
    data = src.read()

with open("copy.png", "wb") as dst:
    dst.write(data)
```

---

## 9. Encoding and Unicode

Always be explicit about encoding, especially for international data.

```python
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()

with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Cafe\u0301 au lait")
```

Common encodings: `utf-8` (recommended default), `latin-1`, `cp1252`, `ascii`.

---

## 10. Practical Patterns for Data Science

### Pattern 1: Process a Large File Line by Line

```python
def count_lines(filepath):
    count = 0
    with open(filepath) as f:
        for _ in f:
            count += 1
    return count
```

### Pattern 2: Merge Multiple CSV Files

```python
import csv
from pathlib import Path

all_rows = []
for csv_file in Path("data").glob("*.csv"):
    with open(csv_file, newline="") as f:
        reader = csv.DictReader(f)
        all_rows.extend(reader)

print(f"Total records: {len(all_rows)}")
```

### Pattern 3: Read JSON API Response and Save as CSV

```python
import json
import csv

with open("api_response.json") as f:
    records = json.load(f)

with open("output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=records[0].keys())
    writer.writeheader()
    writer.writerows(records)
```

---

## Key Takeaways

1. Always use `with` statements to ensure files are properly closed.
2. Use `csv.DictReader`/`DictWriter` for readable, maintainable CSV code.
3. Use `json.load()`/`json.dump()` for files, `json.loads()`/`json.dumps()` for strings.
4. Use `pathlib.Path` for modern, cross-platform path handling.
5. Always specify `encoding="utf-8"` when working with text files to avoid surprises.
6. For large files, iterate line by line instead of loading everything into memory.
