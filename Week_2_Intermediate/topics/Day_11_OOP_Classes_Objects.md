# Day 11: Object-Oriented Programming -- Classes, Objects, and self

## Introduction

Object-Oriented Programming (OOP) lets you model real-world entities as objects that
bundle data (attributes) and behavior (methods). In data science, OOP appears
everywhere: scikit-learn estimators are classes with `.fit()` and `.predict()`,
DataFrames are objects, and custom transformers are classes you write yourself.

---

## 1. What Is a Class?

A **class** is a blueprint for creating objects. An **object** (or **instance**) is a
concrete realization of that blueprint.

```python
class Dog:
    species = "Canis familiaris"  # class attribute (shared)

    def __init__(self, name, age):
        self.name = name          # instance attribute (unique)
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"
```

### Creating Objects (Instantiation)

```python
rex = Dog("Rex", 5)
bella = Dog("Bella", 3)

print(rex.name)     # Rex
print(bella.bark())  # Bella says Woof!
print(rex.species)   # Canis familiaris
```

---

## 2. The `__init__` Method (Constructor)

`__init__` is called automatically when you create a new object. It initializes the
instance's attributes.

```python
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(("deposit", amount))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
            return
        self.balance -= amount
        self.transactions.append(("withdrawal", amount))

    def summary(self):
        return f"{self.owner}'s account: ${self.balance:.2f}"
```

---

## 3. Understanding `self`

`self` is a reference to the **current instance**. When you call `rex.bark()`, Python
translates it to `Dog.bark(rex)` -- the instance is passed as the first argument.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

p1 = Point(0, 0)
p2 = Point(3, 4)
print(p1.distance_to(p2))  # 5.0
```

> `self` is a convention, not a keyword. You could name it anything, but always
> use `self` -- it is a universal Python convention.

---

## 4. Class Attributes vs. Instance Attributes

```python
class Student:
    school = "Data Science Academy"  # class attribute

    def __init__(self, name, grade):
        self.name = name             # instance attribute
        self.grade = grade

s1 = Student("Alice", "A")
s2 = Student("Bob", "B")

# Both share the class attribute
print(s1.school)  # Data Science Academy
print(s2.school)  # Data Science Academy

# Instance attributes are unique
print(s1.name)    # Alice
print(s2.name)    # Bob

# Changing class attribute affects all instances (if not overridden)
Student.school = "AI Academy"
print(s1.school)  # AI Academy
```

> **Caution with mutable class attributes:** If a class attribute is a list or dict,
> all instances share the *same* object.

```python
# WRONG -- shared mutable default
class Bad:
    items = []  # all instances share this list!

# RIGHT -- use __init__
class Good:
    def __init__(self):
        self.items = []  # each instance gets its own list
```

---

## 5. Methods

### Instance Methods

Operate on a specific instance via `self`.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
```

### Class Methods

Operate on the class itself. Decorated with `@classmethod`, first parameter is `cls`.

```python
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "tomato", "basil"])

    @classmethod
    def pepperoni(cls):
        return cls(["mozzarella", "tomato", "pepperoni"])

p = Pizza.margherita()
print(p.ingredients)  # ['mozzarella', 'tomato', 'basil']
```

### Static Methods

Do not access instance or class state. Decorated with `@staticmethod`.

```python
class MathUtils:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def factorial(n):
        if n <= 1:
            return 1
        return n * MathUtils.factorial(n - 1)

print(MathUtils.is_even(4))    # True
print(MathUtils.factorial(5))  # 120
```

---

## 6. Dunder (Magic) Methods

"Dunder" means **d**ouble **under**score. These special methods let your objects
interact with Python's built-in operations.

### `__str__` and `__repr__`

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        """Human-friendly string (for print, str())."""
        return f"{self.name}: ${self.price:.2f}"

    def __repr__(self):
        """Developer-friendly string (for debugging, repr())."""
        return f"Product({self.name!r}, {self.price!r})"

p = Product("Widget", 9.99)
print(p)        # Widget: $9.99
print(repr(p))  # Product('Widget', 9.99)
```

### `__len__`, `__getitem__`, `__contains__`

```python
class Playlist:
    def __init__(self, name, songs=None):
        self.name = name
        self.songs = songs or []

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]

    def __contains__(self, song):
        return song in self.songs

    def add(self, song):
        self.songs.append(song)

pl = Playlist("Road Trip")
pl.add("Bohemian Rhapsody")
pl.add("Hotel California")

print(len(pl))                      # 2
print(pl[0])                        # Bohemian Rhapsody
print("Hotel California" in pl)     # True
```

### Arithmetic Dunder Methods

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)      # Vector(4, 6)
print(v1 * 3)       # Vector(3, 6)
print(v1 == v2)     # False
```

---

## 7. Properties (Managed Attributes)

Use `@property` to define getter/setter logic while keeping attribute-style access.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

t = Temperature(25)
print(t.celsius)      # 25
print(t.fahrenheit)   # 77.0
t.celsius = 100
print(t.fahrenheit)   # 212.0
```

---

## 8. Data Classes (Python 3.7+)

When a class is mainly a container for data, `@dataclass` eliminates boilerplate.

```python
from dataclasses import dataclass, field

@dataclass
class Employee:
    name: str
    department: str
    salary: float
    skills: list = field(default_factory=list)

    def annual_salary(self):
        return self.salary * 12

e = Employee("Alice", "Data Science", 8000)
print(e)           # Employee(name='Alice', department='Data Science', salary=8000, skills=[])
print(e == Employee("Alice", "Data Science", 8000))  # True (auto __eq__)
```

Data classes automatically generate `__init__`, `__repr__`, and `__eq__`.

---

## 9. Composition -- "Has-a" Relationships

Composition models objects that *contain* other objects.

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return f"Engine ({self.horsepower}hp) started."

class Car:
    def __init__(self, make, model, horsepower):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower)  # Car HAS-A Engine

    def start(self):
        return f"{self.make} {self.model}: {self.engine.start()}"

car = Car("Toyota", "Camry", 200)
print(car.start())  # Toyota Camry: Engine (200hp) started.
```

---

## 10. A Data-Science Example: Dataset Class

```python
class Dataset:
    def __init__(self, features, labels):
        assert len(features) == len(labels), "Length mismatch"
        self.features = features
        self.labels = labels

    def __len__(self):
        return len(self.features)

    def __getitem__(self, index):
        return self.features[index], self.labels[index]

    def split(self, ratio=0.8):
        split_idx = int(len(self) * ratio)
        train = Dataset(self.features[:split_idx], self.labels[:split_idx])
        test = Dataset(self.features[split_idx:], self.labels[split_idx:])
        return train, test

    def __repr__(self):
        return f"Dataset(samples={len(self)})"

ds = Dataset([[1], [2], [3], [4], [5]], [0, 1, 0, 1, 0])
train, test = ds.split(0.6)
print(train)  # Dataset(samples=3)
print(test)   # Dataset(samples=2)
```

---

## Key Takeaways

1. A **class** is a blueprint; an **object** is an instance of that blueprint.
2. `__init__` sets up initial state; `self` refers to the current instance.
3. Use **class methods** for alternative constructors, **static methods** for utility
   functions.
4. **Dunder methods** let your objects work with `+`, `len()`, `print()`, `[]`, `in`,
   and more.
5. Use `@property` for computed attributes and validation.
6. Use `@dataclass` for simple data containers to reduce boilerplate.
7. Prefer **composition** ("has-a") over inheritance when modeling parts/components.
