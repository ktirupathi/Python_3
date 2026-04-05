"""
Day 8: Comprehensions, Generators, and Iterators -- Runnable Examples
"""

# ============================================================
# 1. LIST COMPREHENSIONS
# ============================================================

# Basic: squares of 0-9
squares = [x ** 2 for x in range(10)]
print("Squares:", squares)

# With filter: only even numbers
evens = [x for x in range(20) if x % 2 == 0]
print("Evens:", evens)

# Ternary expression: label each number
labels = ["even" if x % 2 == 0 else "odd" for x in range(6)]
print("Labels:", labels)

# Nested: flatten a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print("Flattened:", flat)

# String processing: extract uppercase words
sentence = "Python IS a GREAT language FOR data SCIENCE"
upper_words = [w for w in sentence.split() if w.isupper()]
print("Uppercase words:", upper_words)

# ============================================================
# 2. DICTIONARY COMPREHENSIONS
# ============================================================

# Word lengths
words = ["Python", "data", "science", "machine", "learning"]
word_lengths = {w: len(w) for w in words}
print("\nWord lengths:", word_lengths)

# Invert a dictionary
grades = {"Alice": "A", "Bob": "B", "Charlie": "A"}
inverted = {}
for k, v in grades.items():
    inverted.setdefault(v, []).append(k)
print("Inverted grades:", inverted)

# Filter: students who passed
scores = {"Alice": 85, "Bob": 42, "Charlie": 91, "Diana": 55}
passed = {name: score for name, score in scores.items() if score >= 60}
print("Passed:", passed)

# ============================================================
# 3. SET COMPREHENSIONS
# ============================================================

# Unique first letters
names = ["Alice", "Anna", "Bob", "Bella", "Charlie", "Carol"]
initials = {name[0] for name in names}
print("\nInitials:", initials)

# Unique lengths
lengths = {len(w) for w in words}
print("Unique word lengths:", lengths)

# ============================================================
# 4. ITERATORS
# ============================================================

# Manual iteration with iter/next
print("\n--- Manual Iterator ---")
colors = ["red", "green", "blue"]
it = iter(colors)
print(next(it))  # red
print(next(it))  # green
print(next(it))  # blue

# Custom iterator: Fibonacci sequence
class FibIterator:
    """Produces Fibonacci numbers up to a maximum value."""
    def __init__(self, max_val):
        self.max_val = max_val
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.max_val:
            raise StopIteration
        current = self.a
        self.a, self.b = self.b, self.a + self.b
        return current

print("\nFibonacci up to 50:")
print(list(FibIterator(50)))

# ============================================================
# 5. GENERATOR FUNCTIONS
# ============================================================

def countdown(n):
    """Generator that counts down from n to 1."""
    while n > 0:
        yield n
        n -= 1

print("\nCountdown from 5:")
print(list(countdown(5)))

# Generator for even numbers
def even_numbers(limit):
    """Yield even numbers up to limit."""
    n = 0
    while n <= limit:
        yield n
        n += 2

print("Even numbers up to 10:", list(even_numbers(10)))

# ============================================================
# 6. GENERATOR EXPRESSIONS
# ============================================================

# Generator expression -- lazy evaluation
gen = (x ** 2 for x in range(10))
print("\nGenerator object:", gen)
print("Sum via generator:", sum(x ** 2 for x in range(10)))

# Memory comparison
import sys
list_comp = [x ** 2 for x in range(10000)]
gen_expr = (x ** 2 for x in range(10000))
print(f"List size: {sys.getsizeof(list_comp):,} bytes")
print(f"Generator size: {sys.getsizeof(gen_expr):,} bytes")

# ============================================================
# 7. GENERATOR PIPELINE
# ============================================================

def integers(start=1):
    """Infinite sequence of integers."""
    n = start
    while True:
        yield n
        n += 1

def square(seq):
    """Square each value in the sequence."""
    for n in seq:
        yield n ** 2

def take(n, seq):
    """Take the first n items from a sequence."""
    for i, val in enumerate(seq):
        if i >= n:
            return
        yield val

# Pipeline: first 5 squares of odd numbers
odd_nums = (x for x in integers() if x % 2 != 0)
result = list(take(5, square(odd_nums)))
print("\nFirst 5 squares of odd numbers:", result)

# ============================================================
# 8. ITERTOOLS EXAMPLES
# ============================================================

import itertools

# chain: merge multiple iterables
merged = list(itertools.chain([1, 2], [3, 4], [5, 6]))
print("\nChained:", merged)

# islice: slice an iterator
first_five_squares = list(itertools.islice(square(integers()), 5))
print("First 5 squares:", first_five_squares)

# groupby: group sorted data
data = [("fruit", "apple"), ("fruit", "banana"), ("veggie", "carrot"), ("veggie", "pea")]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(f"  {key}: {[item[1] for item in group]}")

# combinations
combos = list(itertools.combinations("ABCD", 2))
print("Combinations of ABCD (2):", combos)

# product: cartesian product
suits = ["H", "D"]
ranks = ["A", "K"]
cards = list(itertools.product(suits, ranks))
print("Cards:", cards)

# ============================================================
# 9. PRACTICAL: WORD FREQUENCY WITH COMPREHENSIONS
# ============================================================

text = "the cat sat on the mat the cat ate the rat"
word_list = text.split()
freq = {word: word_list.count(word) for word in set(word_list)}
top_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print("\nWord frequencies:", top_words)

print("\n--- All examples complete! ---")
