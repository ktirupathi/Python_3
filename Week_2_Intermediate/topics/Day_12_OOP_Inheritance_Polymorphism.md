# Day 12: OOP -- Inheritance, Polymorphism, Encapsulation, Abstraction

## Introduction

Day 11 introduced classes and objects. Today we explore the four pillars of OOP:
**Inheritance**, **Polymorphism**, **Encapsulation**, and **Abstraction**. These
principles help you write modular, reusable, and maintainable code -- qualities you
will appreciate when building complex data pipelines and ML systems.

---

## 1. Inheritance

Inheritance allows a class (child/sub) to acquire attributes and methods from another
class (parent/super). It models an **"is-a"** relationship.

### Basic Inheritance

```python
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}!"

class Dog(Animal):
    def fetch(self, item):
        return f"{self.name} fetches the {item}."

class Cat(Animal):
    def purr(self):
        return f"{self.name} is purring..."

dog = Dog("Rex", "Woof")
cat = Cat("Whiskers", "Meow")

print(dog.speak())   # Rex says Woof!
print(dog.fetch("ball"))  # Rex fetches the ball.
print(cat.speak())   # Whiskers says Meow!
```

### `super()` -- Calling the Parent

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # call parent __init__
        self.department = department

    def __repr__(self):
        return f"Manager({self.name!r}, dept={self.department!r})"

m = Manager("Alice", 95000, "Data Science")
print(m)  # Manager('Alice', dept='Data Science')
```

### Method Overriding

A child class can **override** a parent method to change its behavior.

```python
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # overrides Shape.area
        import math
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):  # overrides Shape.area
        return self.width * self.height

c = Circle(5)
r = Rectangle(4, 6)
print(f"Circle area: {c.area():.2f}")    # 78.54
print(f"Rectangle area: {r.area():.2f}") # 24.00
```

---

## 2. Polymorphism

Polymorphism means "many forms." Different classes can share the same method name and
be used interchangeably.

### Duck Typing

Python does not require formal interfaces. If an object has the right methods, it works.

> "If it walks like a duck and quacks like a duck, it is a duck."

```python
class CSVExporter:
    def export(self, data):
        return "Exporting as CSV..."

class JSONExporter:
    def export(self, data):
        return "Exporting as JSON..."

class ExcelExporter:
    def export(self, data):
        return "Exporting as Excel..."

def run_export(exporter, data):
    """Works with ANY object that has an export() method."""
    print(exporter.export(data))

run_export(CSVExporter(), [1, 2, 3])
run_export(JSONExporter(), [1, 2, 3])
```

### Polymorphism with Inheritance

```python
shapes = [Circle(3), Rectangle(4, 5), Circle(7)]

total_area = sum(s.area() for s in shapes)
print(f"Total area: {total_area:.2f}")
```

Each shape computes its own area, but the calling code does not need to know the
specific type.

### Operator Overloading as Polymorphism

The `+` operator works differently for integers, strings, and lists -- that is
polymorphism built into the language.

```python
print(1 + 2)           # 3 (int addition)
print("a" + "b")       # "ab" (string concatenation)
print([1] + [2])       # [1, 2] (list concatenation)
```

---

## 3. Encapsulation

Encapsulation bundles data and methods together and restricts direct access to internal
state, exposing only what is necessary.

### Access Conventions in Python

Python uses **naming conventions** rather than strict access modifiers.

| Convention | Meaning | Example |
|---|---|---|
| `name` | Public | `self.name` |
| `_name` | Protected (internal use) | `self._cache` |
| `__name` | Private (name-mangled) | `self.__secret` |

### Protected Attributes (Single Underscore)

```python
class Sensor:
    def __init__(self, name):
        self.name = name
        self._readings = []  # convention: internal use

    def record(self, value):
        self._readings.append(value)

    def average(self):
        if not self._readings:
            return 0
        return sum(self._readings) / len(self._readings)

s = Sensor("Temperature")
s.record(22.5)
s.record(23.1)
print(s.average())  # 22.8
# s._readings is accessible but signals "don't touch directly"
```

### Name Mangling (Double Underscore)

```python
class SecureAccount:
    def __init__(self, balance):
        self.__balance = balance  # name-mangled to _SecureAccount__balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

account = SecureAccount(1000)
# print(account.__balance)  # AttributeError!
print(account.get_balance())  # 1000
# Still accessible via mangled name (not truly private):
print(account._SecureAccount__balance)  # 1000
```

### Properties for Controlled Access

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

c = Circle(5)
print(c.area)      # 78.54
c.radius = 10
print(c.area)      # 314.16
```

---

## 4. Abstraction

Abstraction hides implementation details and exposes only the relevant interface.
Python supports this via **Abstract Base Classes (ABCs)**.

### Abstract Base Classes

```python
from abc import ABC, abstractmethod

class DataLoader(ABC):
    @abstractmethod
    def load(self, source):
        """Load data from the source. Must be implemented."""
        pass

    @abstractmethod
    def validate(self, data):
        """Validate the loaded data. Must be implemented."""
        pass

    def process(self, source):
        """Template method -- uses abstract methods."""
        data = self.load(source)
        if self.validate(data):
            return data
        raise ValueError("Data validation failed")
```

```python
class CSVLoader(DataLoader):
    def load(self, source):
        print(f"Loading CSV from {source}")
        return [{"col1": 1, "col2": 2}]

    def validate(self, data):
        return len(data) > 0

class JSONLoader(DataLoader):
    def load(self, source):
        print(f"Loading JSON from {source}")
        return {"key": "value"}

    def validate(self, data):
        return isinstance(data, dict)

# loader = DataLoader()  # TypeError: Can't instantiate abstract class
csv_loader = CSVLoader()
result = csv_loader.process("data.csv")
```

---

## 5. Multiple Inheritance

Python supports inheriting from multiple classes.

```python
class Flyable:
    def fly(self):
        return f"{self.__class__.__name__} is flying!"

class Swimmable:
    def swim(self):
        return f"{self.__class__.__name__} is swimming!"

class Duck(Flyable, Swimmable):
    pass

donald = Duck()
print(donald.fly())   # Duck is flying!
print(donald.swim())  # Duck is swimming!
```

### Method Resolution Order (MRO)

Python uses the **C3 linearization** algorithm to determine which method to call.

```python
print(Duck.__mro__)
# (<class 'Duck'>, <class 'Flyable'>, <class 'Swimmable'>, <class 'object'>)
```

### The Diamond Problem

```python
class A:
    def greet(self):
        return "Hello from A"

class B(A):
    def greet(self):
        return "Hello from B"

class C(A):
    def greet(self):
        return "Hello from C"

class D(B, C):
    pass

d = D()
print(d.greet())     # Hello from B (follows MRO: D -> B -> C -> A)
print(D.__mro__)
```

---

## 6. Mixins

A **mixin** is a class designed to add specific functionality without being a
standalone entity.

```python
import json

class JSONMixin:
    def to_json(self):
        return json.dumps(self.__dict__, indent=2)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(**data)

class LogMixin:
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")

class User(JSONMixin, LogMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email

user = User("Alice", "alice@example.com")
print(user.to_json())
user.log("User created")
```

---

## 7. isinstance() and issubclass()

```python
print(isinstance(dog, Dog))      # True
print(isinstance(dog, Animal))   # True (Dog inherits from Animal)
print(issubclass(Dog, Animal))   # True
print(issubclass(Animal, Dog))   # False
```

---

## 8. Practical Example: ML Pipeline with OOP

```python
from abc import ABC, abstractmethod

class Transformer(ABC):
    @abstractmethod
    def fit(self, data):
        pass

    @abstractmethod
    def transform(self, data):
        pass

    def fit_transform(self, data):
        self.fit(data)
        return self.transform(data)

class Normalizer(Transformer):
    def fit(self, data):
        self.min_val = min(data)
        self.max_val = max(data)

    def transform(self, data):
        rng = self.max_val - self.min_val
        if rng == 0:
            return [0.0] * len(data)
        return [(x - self.min_val) / rng for x in data]

class StandardScaler(Transformer):
    def fit(self, data):
        n = len(data)
        self.mean = sum(data) / n
        self.std = (sum((x - self.mean) ** 2 for x in data) / n) ** 0.5

    def transform(self, data):
        if self.std == 0:
            return [0.0] * len(data)
        return [(x - self.mean) / self.std for x in data]

data = [10, 20, 30, 40, 50]
norm = Normalizer()
print(norm.fit_transform(data))  # [0.0, 0.25, 0.5, 0.75, 1.0]

scaler = StandardScaler()
print(scaler.fit_transform(data))  # [-1.41, -0.71, 0.0, 0.71, 1.41]
```

---

## Key Takeaways

1. **Inheritance** promotes code reuse: child classes inherit parent functionality
   and can override or extend it.
2. **Polymorphism** lets you write generic code that works with any object having
   the right interface.
3. **Encapsulation** protects internal state -- use `_` and `__` conventions, and
   `@property` for controlled access.
4. **Abstraction** via ABCs defines contracts that subclasses must fulfill.
5. Prefer **composition over inheritance** for complex systems; use mixins for
   cross-cutting concerns.
6. Understand **MRO** when working with multiple inheritance to predict method
   resolution.
