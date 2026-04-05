# Day 13: Modules, Packages, Virtual Environments, and pip

## Introduction

As projects grow beyond a single file, you need to organize code into **modules** and
**packages**, manage third-party libraries with **pip**, and isolate project
dependencies using **virtual environments**. These are foundational skills for any
professional Python developer or data scientist.

---

## 1. Modules

A **module** is simply a `.py` file containing Python code. Any Python file can be
imported as a module.

### Creating a Module

```python
# math_utils.py
PI = 3.14159

def circle_area(radius):
    return PI * radius ** 2

def rectangle_area(width, height):
    return width * height

def _internal_helper():
    """Underscore signals this is not part of the public API."""
    pass
```

### Importing a Module

```python
# main.py
import math_utils

print(math_utils.circle_area(5))   # 78.53975
print(math_utils.PI)               # 3.14159
```

### Import Variations

```python
# Import specific names
from math_utils import circle_area, PI

# Import with alias
import math_utils as mu
print(mu.circle_area(5))

# Import all public names (avoid in production code)
from math_utils import *
```

### The `__name__` Variable

Every module has a `__name__` attribute. When run directly, it equals `"__main__"`.

```python
# my_module.py
def greet():
    print("Hello from my_module!")

if __name__ == "__main__":
    # This block runs only when the file is executed directly,
    # not when it is imported.
    greet()
    print("Running as main script")
```

This pattern is essential for writing reusable modules that can also be run standalone.

---

## 2. Packages

A **package** is a directory containing modules and a special `__init__.py` file.

### Package Structure

```
my_project/
    my_package/
        __init__.py
        data_loading.py
        preprocessing.py
        models/
            __init__.py
            linear.py
            tree.py
    main.py
```

### `__init__.py`

This file makes a directory a package. It can be empty or define what gets exported.

```python
# my_package/__init__.py
from .data_loading import load_csv, load_json
from .preprocessing import normalize, standardize

__all__ = ["load_csv", "load_json", "normalize", "standardize"]
```

### Importing from Packages

```python
# Absolute imports
from my_package.data_loading import load_csv
from my_package.models.linear import LinearRegression

# Using __init__.py exports
from my_package import load_csv, normalize
```

### Relative Imports (Within a Package)

```python
# Inside my_package/preprocessing.py
from .data_loading import load_csv      # same-level module
from .models.linear import LinearRegression  # sub-package
from ..other_package import helper       # parent-level package
```

---

## 3. The Standard Library -- Useful Modules

Python comes with a rich standard library. Here are modules every data scientist
should know:

| Module | Purpose |
|--------|---------|
| `os` | Operating system interaction |
| `sys` | System-specific parameters |
| `pathlib` | Object-oriented file paths |
| `json` | JSON encoding/decoding |
| `csv` | CSV file reading/writing |
| `math` | Mathematical functions |
| `random` | Random number generation |
| `datetime` | Date and time handling |
| `collections` | Specialized containers |
| `itertools` | Iterator building blocks |
| `functools` | Higher-order functions |
| `logging` | Logging framework |
| `re` | Regular expressions |
| `typing` | Type hints |
| `unittest` | Testing framework |

### Quick Examples

```python
import os
print(os.getcwd())           # current working directory
print(os.listdir("."))        # directory contents

import sys
print(sys.version)            # Python version
print(sys.path)               # module search paths

from collections import Counter, defaultdict
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
print(Counter(words))         # Counter({'apple': 3, 'banana': 2, 'cherry': 1})

scores = defaultdict(list)
scores["Alice"].append(90)
scores["Alice"].append(85)
print(dict(scores))           # {'Alice': [90, 85]}

from datetime import datetime, timedelta
now = datetime.now()
one_week_later = now + timedelta(weeks=1)
print(now.strftime("%Y-%m-%d %H:%M"))
```

---

## 4. pip -- The Package Installer

`pip` installs packages from the **Python Package Index (PyPI)**.

### Basic Commands

```bash
# Install a package
pip install pandas

# Install a specific version
pip install pandas==2.1.0

# Install minimum version
pip install "pandas>=2.0"

# Upgrade a package
pip install --upgrade pandas

# Uninstall
pip uninstall pandas

# List installed packages
pip list

# Show package details
pip show pandas

# Search for packages (use PyPI website instead)
# pip search is disabled; browse https://pypi.org
```

### Requirements Files

A `requirements.txt` file lists all project dependencies.

```
# requirements.txt
pandas==2.1.0
numpy>=1.24
scikit-learn~=1.3.0
matplotlib
requests>=2.28,<3.0
```

```bash
# Install all dependencies
pip install -r requirements.txt

# Generate from current environment
pip freeze > requirements.txt
```

### Version Specifiers

| Specifier | Meaning |
|-----------|---------|
| `==2.1.0` | Exact version |
| `>=2.0` | Minimum version |
| `<=3.0` | Maximum version |
| `~=2.1` | Compatible release (>=2.1, <3.0) |
| `!=2.0.1` | Exclude a version |

---

## 5. Virtual Environments

A **virtual environment** is an isolated Python installation. Each project gets its
own set of packages, avoiding version conflicts.

### Why Virtual Environments?

- Project A needs `pandas 1.5`, Project B needs `pandas 2.1`.
- Without isolation, installing one version breaks the other.
- Virtual environments solve this completely.

### Creating and Using venv

```bash
# Create a virtual environment
python -m venv myenv

# Activate it
# Linux/Mac:
source myenv/bin/activate
# Windows:
myenv\Scripts\activate

# Your prompt changes to show (myenv)
# Now pip install goes into this environment only

pip install pandas numpy

# Deactivate when done
deactivate
```

### Project Workflow

```bash
# 1. Create project directory
mkdir my_project && cd my_project

# 2. Create virtual environment
python -m venv .venv

# 3. Activate
source .venv/bin/activate

# 4. Install dependencies
pip install pandas scikit-learn matplotlib

# 5. Save dependencies
pip freeze > requirements.txt

# 6. Work on your project...

# 7. Deactivate when done
deactivate
```

### Recreating an Environment

```bash
# On a new machine or after cloning
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### .gitignore for Virtual Environments

```
# .gitignore
.venv/
__pycache__/
*.pyc
```

> **Never commit virtual environments to git.** They are large and platform-specific.
> Commit `requirements.txt` instead.

---

## 6. Alternative Tools

### conda (Popular in Data Science)

```bash
# Create environment
conda create -n myenv python=3.11

# Activate
conda activate myenv

# Install packages (from conda-forge or defaults)
conda install pandas numpy scikit-learn

# Export environment
conda env export > environment.yml

# Recreate
conda env create -f environment.yml
```

### Poetry (Modern Dependency Management)

```bash
# Initialize project
poetry init

# Add dependencies
poetry add pandas numpy

# Install from lock file
poetry install

# Run scripts in the environment
poetry run python main.py
```

### pyenv (Manage Python Versions)

```bash
# Install a Python version
pyenv install 3.11.5

# Set local version for project
pyenv local 3.11.5
```

---

## 7. Module Search Path

When you `import something`, Python searches in this order:

1. **Built-in modules** (sys, os, etc.)
2. **sys.path** directories:
   - Directory of the script being run
   - `PYTHONPATH` environment variable
   - Standard library directories
   - Site-packages (installed third-party)

```python
import sys
for path in sys.path:
    print(path)
```

---

## 8. Organizing a Real Project

### Recommended Structure

```
my_data_project/
    .venv/                  # virtual environment (git-ignored)
    .gitignore
    README.md
    requirements.txt
    setup.py                # or pyproject.toml
    src/
        my_package/
            __init__.py
            config.py
            data/
                __init__.py
                loader.py
                cleaner.py
            models/
                __init__.py
                trainer.py
                evaluator.py
            utils/
                __init__.py
                logger.py
                validators.py
    tests/
        __init__.py
        test_loader.py
        test_trainer.py
    notebooks/
        exploration.ipynb
    data/
        raw/
        processed/
```

### pyproject.toml (Modern Standard)

```toml
[build-system]
requires = ["setuptools>=68.0"]
build-backend = "setuptools.backends._legacy:_Backend"

[project]
name = "my-data-project"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = [
    "pandas>=2.0",
    "scikit-learn>=1.3",
    "matplotlib>=3.7",
]

[project.optional-dependencies]
dev = ["pytest", "black", "ruff"]
```

---

## 9. Distributing Your Package

### Installing Your Package in Development Mode

```bash
pip install -e .
```

This creates a link so that changes to your source code are immediately available
without reinstalling.

### Building and Publishing to PyPI

```bash
pip install build twine
python -m build
twine upload dist/*
```

---

## Key Takeaways

1. **Modules** are `.py` files; **packages** are directories with `__init__.py`.
2. Use `if __name__ == "__main__":` to make modules both importable and runnable.
3. **pip** installs packages; always pin versions in `requirements.txt`.
4. **Virtual environments** isolate project dependencies -- create one for every project.
5. Follow a consistent **project structure** to keep code organized as it grows.
6. Explore **conda** for data-science-heavy environments and **poetry** for modern
   dependency management.
