# Python Interview Question Bank for ML & AI Engineers (250+ Real Questions)

## Learning Flow
1. **Concept**: Build the core idea and constraint model.
2. **Examples**: Walk through easy → medium → hard samples.
3. **Weekly Assignments**: Practice mixed conceptual/coding tasks.
4. **Interview Questions**: Solve under time pressure with trade-off discussion.

## Python Basics

### Q001: Normalize and tokenize a sentence into lowercase words
1. **Problem statement**: Normalize and tokenize a sentence into lowercase words.
2. **Explanation**: Useful for text preprocessing before feature extraction.
3. **Working Python code**:
```python
import re

def normalize_tokens(text):
    return re.findall(r"[a-z0-9]+", text.lower())
```
4. **Alternate solution**:
```python
def normalize_tokens(text):
    cleaned = ''.join(ch.lower() if ch.isalnum() else ' ' for ch in text)
    return [w for w in cleaned.split() if w]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Clarify punctuation, unicode, and numeric token rules.

### Q002: Count frequency of each character while preserving insertion order
1. **Problem statement**: Count frequency of each character while preserving insertion order.
2. **Explanation**: Demonstrates dictionaries and deterministic iteration.
3. **Working Python code**:
```python
def ordered_char_count(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    return counts
```
4. **Alternate solution**:
```python
from collections import Counter

def ordered_char_count(s):
    c = Counter(s)
    return {ch: c[ch] for ch in dict.fromkeys(s)}
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(k).
7. **Interview tip**: Mention that Python 3.7+ dictionaries preserve insertion order.

### Q003: Return indices of all vowels in a string
1. **Problem statement**: Return indices of all vowels in a string.
2. **Explanation**: Index tracking is common in parsing tasks.
3. **Working Python code**:
```python
def vowel_indices(s):
    v = set('aeiouAEIOU')
    return [i for i, ch in enumerate(s) if ch in v]
```
4. **Alternate solution**:
```python
import re

def vowel_indices(s):
    return [m.start() for m in re.finditer(r'[AEIOUaeiou]', s)]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(m).
7. **Interview tip**: Discuss whether y should be treated as a vowel.

### Q004: Find the longest word in a sentence
1. **Problem statement**: Find the longest word in a sentence.
2. **Explanation**: Basic string splitting plus max-by-key.
3. **Working Python code**:
```python
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len, default='')
```
4. **Alternate solution**:
```python
def longest_word(sentence):
    best = ''
    for w in sentence.split():
        if len(w) > len(best):
            best = w
    return best
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(1).
7. **Interview tip**: Ask what to return when there are ties.

### Q005: Convert integer list to comma-separated string without trailing comma
1. **Problem statement**: Convert integer list to comma-separated string without trailing comma.
2. **Explanation**: Tests join/map basics.
3. **Working Python code**:
```python
def csv_line(nums):
    return ','.join(map(str, nums))
```
4. **Alternate solution**:
```python
def csv_line(nums):
    out = ''
    for i, n in enumerate(nums):
        out += str(n)
        if i != len(nums)-1:
            out += ','
    return out
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Prefer join over repeated concatenation for performance.

### Q006: Clamp numbers into a range [low, high]
1. **Problem statement**: Clamp numbers into a range [low, high].
2. **Explanation**: Useful in data cleaning pipelines.
3. **Working Python code**:
```python
def clamp_values(nums, low, high):
    return [max(low, min(x, high)) for x in nums]
```
4. **Alternate solution**:
```python
def clamp_values(nums, low, high):
    out = []
    for x in nums:
        if x < low:
            out.append(low)
        elif x > high:
            out.append(high)
        else:
            out.append(x)
    return out
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Check low <= high before processing.

### Q007: Implement title case without using str.title
1. **Problem statement**: Implement title case without using str.title.
2. **Explanation**: Shows manual word boundary handling.
3. **Working Python code**:
```python
def custom_title(s):
    words = s.split(' ')
    return ' '.join(w[:1].upper() + w[1:].lower() if w else '' for w in words)
```
4. **Alternate solution**:
```python
def custom_title(s):
    res, cap_next = [], True
    for ch in s:
        if ch == ' ':
            cap_next = True
            res.append(ch)
        else:
            res.append(ch.upper() if cap_next else ch.lower())
            cap_next = False
    return ''.join(res)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Edge case: multiple consecutive spaces.

### Q008: Check if all brackets are balanced
1. **Problem statement**: Check if all brackets are balanced.
2. **Explanation**: Classic stack usage on basic syntax validation.
3. **Working Python code**:
```python
def balanced_brackets(s):
    pairs = {')':'(', ']':'[', '}':'{'}
    st = []
    for ch in s:
        if ch in '([{':
            st.append(ch)
        elif ch in pairs:
            if not st or st.pop() != pairs[ch]:
                return False
    return not st
```
4. **Alternate solution**:
```python
def balanced_brackets(s):
    prev = None
    while prev != s:
        prev = s
        s = s.replace('()','').replace('[]','').replace('{}','')
    return s == ''
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Ask whether non-bracket characters appear in input.

### Q009: Implement FizzBuzz for 1..n
1. **Problem statement**: Implement FizzBuzz for 1..n.
2. **Explanation**: Simple control flow and modulo logic.
3. **Working Python code**:
```python
def fizzbuzz(n):
    out = []
    for i in range(1, n+1):
        if i % 15 == 0: out.append('FizzBuzz')
        elif i % 3 == 0: out.append('Fizz')
        elif i % 5 == 0: out.append('Buzz')
        else: out.append(str(i))
    return out
```
4. **Alternate solution**:
```python
def fizzbuzz(n):
    return [
        'FizzBuzz' if i % 15 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else str(i)
        for i in range(1, n+1)
    ]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Explain why checking 15 first avoids collisions.

### Q010: Compute digital root by repeated sum of digits
1. **Problem statement**: Compute digital root by repeated sum of digits.
2. **Explanation**: Common interview arithmetic/string hybrid problem.
3. **Working Python code**:
```python
def digital_root(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n
```
4. **Alternate solution**:
```python
def digital_root(n):
    return 0 if n == 0 else 1 + (n - 1) % 9
```
5. **Time complexity**: Iterative O(log n).
6. **Space complexity**: O(1).
7. **Interview tip**: Mention mathematical shortcut if interviewer asks optimization.

### Q011: Find missing number from 0..n
1. **Problem statement**: Find missing number from 0..n.
2. **Explanation**: Shows arithmetic series reasoning.
3. **Working Python code**:
```python
def missing_number(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)
```
4. **Alternate solution**:
```python
def missing_number(nums):
    x = len(nums)
    for i, v in enumerate(nums):
        x ^= i ^ v
    return x
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(1).
7. **Interview tip**: XOR alternative avoids overflow in fixed-width languages.

### Q012: Return the second largest distinct value
1. **Problem statement**: Return the second largest distinct value.
2. **Explanation**: Tests handling duplicates correctly.
3. **Working Python code**:
```python
def second_largest(nums):
    first = second = float('-inf')
    for x in nums:
        if x > first:
            first, second = x, first
        elif first > x > second:
            second = x
    return None if second == float('-inf') else second
```
4. **Alternate solution**:
```python
def second_largest(nums):
    vals = sorted(set(nums))
    return vals[-2] if len(vals) >= 2 else None
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(1).
7. **Interview tip**: Clarify behavior for lists with fewer than 2 distinct values.

### Q013: Shift alphabetic characters by k positions (Caesar cipher)
1. **Problem statement**: Shift alphabetic characters by k positions (Caesar cipher).
2. **Explanation**: Demonstrates ASCII arithmetic and modular math.
3. **Working Python code**:
```python
def caesar(text, k):
    out = []
    for ch in text:
        if 'a' <= ch <= 'z':
            out.append(chr((ord(ch)-97+k)%26 + 97))
        elif 'A' <= ch <= 'Z':
            out.append(chr((ord(ch)-65+k)%26 + 65))
        else:
            out.append(ch)
    return ''.join(out)
```
4. **Alternate solution**:
```python
import string

def caesar(text, k):
    low = string.ascii_lowercase
    up = string.ascii_uppercase
    t = str.maketrans(low+up, low[k%26:]+low[:k%26]+up[k%26:]+up[:k%26])
    return text.translate(t)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Ask whether digits and punctuation should stay unchanged.

### Q014: Compute moving average with window size k
1. **Problem statement**: Compute moving average with window size k.
2. **Explanation**: Sliding window optimization from O(nk) to O(n).
3. **Working Python code**:
```python
def moving_average(nums, k):
    if k <= 0 or k > len(nums):
        return []
    s = sum(nums[:k])
    out = [s / k]
    for i in range(k, len(nums)):
        s += nums[i] - nums[i-k]
        out.append(s / k)
    return out
```
4. **Alternate solution**:
```python
def moving_average(nums, k):
    return [sum(nums[i:i+k]) / k for i in range(len(nums)-k+1)] if 0 < k <= len(nums) else []
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Good place to discuss streaming analytics.

### Q015: Check if list is strictly increasing
1. **Problem statement**: Check if list is strictly increasing.
2. **Explanation**: Simple adjacency checks with early exit.
3. **Working Python code**:
```python
def is_strictly_increasing(nums):
    return all(nums[i] < nums[i+1] for i in range(len(nums)-1))
```
4. **Alternate solution**:
```python
def is_strictly_increasing(nums):
    for i in range(1, len(nums)):
        if nums[i] <= nums[i-1]:
            return False
    return True
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(1).
7. **Interview tip**: Interviewers may ask for non-decreasing variant follow-up.

### Q016: Remove consecutive duplicate characters
1. **Problem statement**: Remove consecutive duplicate characters.
2. **Explanation**: Useful for compression pre-processing.
3. **Working Python code**:
```python
def dedupe_consecutive(s):
    if not s:
        return ''
    out = [s[0]]
    for ch in s[1:]:
        if ch != out[-1]:
            out.append(ch)
    return ''.join(out)
```
4. **Alternate solution**:
```python
from itertools import groupby

def dedupe_consecutive(s):
    return ''.join(ch for ch, _ in groupby(s))
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Differentiate from removing all duplicates.

### Q017: Find all start indices of a substring
1. **Problem statement**: Find all start indices of a substring.
2. **Explanation**: Search with overlapping matches.
3. **Working Python code**:
```python
def find_all_occurrences(text, pattern):
    if pattern == '':
        return list(range(len(text)+1))
    out, i = [], 0
    while True:
        j = text.find(pattern, i)
        if j == -1:
            return out
        out.append(j)
        i = j + 1
```
4. **Alternate solution**:
```python
def find_all_occurrences(text, pattern):
    return [i for i in range(len(text)-len(pattern)+1) if text[i:i+len(pattern)] == pattern]
```
5. **Time complexity**: O(n*m) worst-case.
6. **Space complexity**: O(r).
7. **Interview tip**: Clarify whether overlaps are allowed.

### Q018: Convert list of key=value strings into dictionary
1. **Problem statement**: Convert list of key=value strings into dictionary.
2. **Explanation**: Parsing key-value pairs appears in logs/config work.
3. **Working Python code**:
```python
def parse_kv(items):
    out = {}
    for item in items:
        key, value = item.split('=', 1)
        out[key.strip()] = value.strip()
    return out
```
4. **Alternate solution**:
```python
def parse_kv(items):
    return dict(part.split('=', 1) for part in items)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Ask how to handle duplicate keys.

### Q019: Compute histogram buckets of width w
1. **Problem statement**: Compute histogram buckets of width w.
2. **Explanation**: Data engineering style numeric bucketing.
3. **Working Python code**:
```python
def histogram(nums, w):
    out = {}
    for x in nums:
        b = (x // w) * w
        out[b] = out.get(b, 0) + 1
    return out
```
4. **Alternate solution**:
```python
from collections import Counter

def histogram(nums, w):
    return dict(Counter((x // w) * w for x in nums))
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(b).
7. **Interview tip**: State behavior for negative values before coding.

### Q020: Find median of an unsorted list
1. **Problem statement**: Find median of an unsorted list.
2. **Explanation**: Foundational stats operation in ML preprocessing.
3. **Working Python code**:
```python
def median(nums):
    if not nums:
        raise ValueError('empty')
    arr = sorted(nums)
    n = len(arr)
    m = n // 2
    return arr[m] if n % 2 else (arr[m-1] + arr[m]) / 2
```
4. **Alternate solution**:
```python
import heapq

def median(nums):
    low, high = [], []
    for x in nums:
        heapq.heappush(low, -x)
        heapq.heappush(high, -heapq.heappop(low))
        if len(high) > len(low):
            heapq.heappush(low, -heapq.heappop(high))
    return -low[0] if len(low) > len(high) else (-low[0] + high[0]) / 2
```
5. **Time complexity**: Sort O(n log n).
6. **Space complexity**: O(n).
7. **Interview tip**: Heap approach is useful for streaming median follow-up.

### Q021: Check if two strings are isomorphic
1. **Problem statement**: Check if two strings are isomorphic.
2. **Explanation**: Map character correspondence both directions.
3. **Working Python code**:
```python
def isomorphic(a, b):
    if len(a) != len(b):
        return False
    m1, m2 = {}, {}
    for x, y in zip(a, b):
        if m1.get(x, y) != y or m2.get(y, x) != x:
            return False
        m1[x], m2[y] = y, x
    return True
```
4. **Alternate solution**:
```python
def isomorphic(a,b):
    return len(set(zip(a,b))) == len(set(a)) == len(set(b))
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(k).
7. **Interview tip**: Provide counterexample where one-way map fails.

### Q022: Compute Hamming distance between equal-length strings
1. **Problem statement**: Compute Hamming distance between equal-length strings.
2. **Explanation**: Useful in feature hashing/debugging bit encodings.
3. **Working Python code**:
```python
def hamming(a, b):
    if len(a) != len(b):
        raise ValueError('length mismatch')
    return sum(x != y for x, y in zip(a, b))
```
4. **Alternate solution**:
```python
def hamming(a, b):
    return sum(1 for i in range(len(a)) if a[i] != b[i])
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(1).
7. **Interview tip**: Clarify if unicode normalization is needed before compare.

### Q023: Validate IPv4 address
1. **Problem statement**: Validate IPv4 address.
2. **Explanation**: Input validation question with string parsing.
3. **Working Python code**:
```python
def is_ipv4(addr):
    parts = addr.split('.')
    if len(parts) != 4:
        return False
    for p in parts:
        if not p.isdigit() or (p.startswith('0') and len(p) > 1):
            return False
        n = int(p)
        if not (0 <= n <= 255):
            return False
    return True
```
4. **Alternate solution**:
```python
import ipaddress

def is_ipv4(addr):
    try:
        return ipaddress.ip_address(addr).version == 4
    except ValueError:
        return False
```
5. **Time complexity**: O(1).
6. **Space complexity**: O(1).
7. **Interview tip**: Mention leading-zero ambiguity explicitly.

### Q024: Compute Jaccard similarity of two token lists
1. **Problem statement**: Compute Jaccard similarity of two token lists.
2. **Explanation**: Set-based similarity appears in dedup and search.
3. **Working Python code**:
```python
def jaccard(a, b):
    sa, sb = set(a), set(b)
    if not sa and not sb:
        return 1.0
    return len(sa & sb) / len(sa | sb)
```
4. **Alternate solution**:
```python
def jaccard(a, b):
    inter = 0
    union = set(a)
    for x in set(b):
        if x in union:
            inter += 1
        union.add(x)
    return inter / len(union) if union else 1.0
```
5. **Time complexity**: O(n+m).
6. **Space complexity**: O(n+m).
7. **Interview tip**: In ML, clarify whether duplicates should matter (multiset Jaccard).

### Q025: Transpose a rectangular matrix represented as list of lists
1. **Problem statement**: Transpose a rectangular matrix represented as list of lists.
2. **Explanation**: Core manipulation for tabular data.
3. **Working Python code**:
```python
def transpose(mat):
    return [list(col) for col in zip(*mat)]
```
4. **Alternate solution**:
```python
def transpose(mat):
    r, c = len(mat), len(mat[0])
    out = [[0]*r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            out[j][i] = mat[i][j]
    return out
```
5. **Time complexity**: O(r*c).
6. **Space complexity**: O(r*c).
7. **Interview tip**: Ask if matrix may be ragged before using zip(*).

### Q026: Find nearest value to target in a sorted list
1. **Problem statement**: Find nearest value to target in a sorted list.
2. **Explanation**: Binary-search-style boundary reasoning.
3. **Working Python code**:
```python
import bisect

def nearest(sorted_nums, target):
    i = bisect.bisect_left(sorted_nums, target)
    cand = []
    if i < len(sorted_nums): cand.append(sorted_nums[i])
    if i > 0: cand.append(sorted_nums[i-1])
    return min(cand, key=lambda x: (abs(x-target), x))
```
4. **Alternate solution**:
```python
def nearest(sorted_nums, target):
    return min(sorted_nums, key=lambda x: (abs(x-target), x))
```
5. **Time complexity**: Binary search O(log n).
6. **Space complexity**: O(1).
7. **Interview tip**: Tie-breaking policy should be stated.

### Q027: Compute cumulative sum array
1. **Problem statement**: Compute cumulative sum array.
2. **Explanation**: Important for prefix-sum optimization patterns.
3. **Working Python code**:
```python
def cumsum(nums):
    out, running = [], 0
    for x in nums:
        running += x
        out.append(running)
    return out
```
4. **Alternate solution**:
```python
from itertools import accumulate

def cumsum(nums):
    return list(accumulate(nums))
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Prefix sums enable O(1) range-sum queries.

### Q028: Detect if any permutation of s1 is a substring of s2
1. **Problem statement**: Detect if any permutation of s1 is a substring of s2.
2. **Explanation**: Sliding-window frequency matching.
3. **Working Python code**:
```python
from collections import Counter

def has_permutation(s1, s2):
    k = len(s1)
    if k > len(s2):
        return False
    need = Counter(s1)
    win = Counter(s2[:k])
    if win == need:
        return True
    for i in range(k, len(s2)):
        win[s2[i]] += 1
        left = s2[i-k]
        win[left] -= 1
        if win[left] == 0:
            del win[left]
        if win == need:
            return True
    return False
```
4. **Alternate solution**:
```python
def has_permutation(s1,s2):
    return any(sorted(s2[i:i+len(s1)])==sorted(s1) for i in range(len(s2)-len(s1)+1))
```
5. **Time complexity**: O(n*alphabet).
6. **Space complexity**: O(alphabet).
7. **Interview tip**: Mention fixed alphabet trick for O(n) arrays.

### Q029: Parse human-readable duration '2h 30m 10s' to seconds
1. **Problem statement**: Parse human-readable duration '2h 30m 10s' to seconds.
2. **Explanation**: Practical parsing problem for logs/scheduling.
3. **Working Python code**:
```python
import re

def duration_to_seconds(expr):
    mult = {'h':3600, 'm':60, 's':1}
    total = 0
    for num, unit in re.findall(r'(\d+)\s*([hms])', expr.lower()):
        total += int(num) * mult[unit]
    return total
```
4. **Alternate solution**:
```python
def duration_to_seconds(expr):
    total = 0
    for token in expr.split():
        total += int(token[:-1]) * {'h':3600,'m':60,'s':1}[token[-1]]
    return total
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(1).
7. **Interview tip**: Ask if units can repeat and whether missing spaces are valid.

## Data Structures

### Q030: Implement a queue using two stacks
1. **Problem statement**: Implement a queue using two stacks.
2. **Explanation**: Push into in-stack, pop from out-stack, refill when empty.
3. **Working Python code**:
```python
class QueueWithStacks:
    def __init__(self):
        self._in, self._out = [], []
    def push(self, x):
        self._in.append(x)
    def _shift(self):
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())
    def pop(self):
        self._shift(); return self._out.pop()
    def peek(self):
        self._shift(); return self._out[-1]
    def empty(self):
        return not self._in and not self._out
```
4. **Alternate solution**:
```python
from collections import deque

class QueueWithStacks:
    def __init__(self): self.d = deque()
    def push(self, x): self.d.append(x)
    def pop(self): return self.d.popleft()
    def peek(self): return self.d[0]
    def empty(self): return not self.d
```
5. **Time complexity**: Amortized O(1).
6. **Space complexity**: O(n).
7. **Interview tip**: Explain amortized analysis clearly.

### Q031: Implement stack supporting get_min in O(1)
1. **Problem statement**: Implement stack supporting get_min in O(1).
2. **Explanation**: Store current minimum with each pushed value.
3. **Working Python code**:
```python
class MinStack:
    def __init__(self):
        self.st = []
    def push(self, x):
        cur_min = x if not self.st else min(x, self.st[-1][1])
        self.st.append((x, cur_min))
    def pop(self):
        return self.st.pop()[0]
    def top(self):
        return self.st[-1][0]
    def get_min(self):
        return self.st[-1][1]
```
4. **Alternate solution**:
```python
class MinStack:
    def __init__(self):
        self.st, self.mins = [], []
    def push(self, x):
        self.st.append(x)
        if not self.mins or x <= self.mins[-1]: self.mins.append(x)
    def pop(self):
        x = self.st.pop()
        if x == self.mins[-1]: self.mins.pop()
        return x
    def get_min(self): return self.mins[-1]
```
5. **Time complexity**: O(1).
6. **Space complexity**: O(n).
7. **Interview tip**: Edge case: duplicates in minimum values.

### Q032: Merge overlapping intervals
1. **Problem statement**: Merge overlapping intervals.
2. **Explanation**: Sort by start and merge when intervals overlap.
3. **Working Python code**:
```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for s, e in intervals:
        if not merged or s > merged[-1][1]:
            merged.append([s, e])
        else:
            merged[-1][1] = max(merged[-1][1], e)
    return merged
```
4. **Alternate solution**:
```python
def merge_intervals(intervals):
    changed = True
    arr = intervals[:]
    while changed:
        changed = False
        arr.sort()
        out = []
        for it in arr:
            if out and it[0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1], it[1]); changed = True
            else:
                out.append(it[:])
        arr = out
    return arr
```
5. **Time complexity**: O(n log n).
6. **Space complexity**: O(n).
7. **Interview tip**: Mention closed vs half-open interval convention.

### Q033: Find top-k frequent elements
1. **Problem statement**: Find top-k frequent elements.
2. **Explanation**: Frequency map plus heap gives scalable top-k.
3. **Working Python code**:
```python
from collections import Counter
import heapq

def top_k(nums, k):
    c = Counter(nums)
    return [x for x, _ in heapq.nlargest(k, c.items(), key=lambda p: p[1])]
```
4. **Alternate solution**:
```python
from collections import Counter

def top_k(nums, k):
    c = Counter(nums)
    return [x for x, _ in sorted(c.items(), key=lambda p: p[1], reverse=True)[:k]]
```
5. **Time complexity**: O(n log k).
6. **Space complexity**: O(n).
7. **Interview tip**: State if deterministic tie-breaking is required.

### Q034: Detect cycle in linked list
1. **Problem statement**: Detect cycle in linked list.
2. **Explanation**: Floyd's tortoise-hare pointer strategy.
3. **Working Python code**:
```python
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val, self.next = val, nxt

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```
4. **Alternate solution**:
```python
def has_cycle(head):
    seen = set()
    cur = head
    while cur:
        if id(cur) in seen:
            return True
        seen.add(id(cur))
        cur = cur.next
    return False
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(1).
7. **Interview tip**: Follow-up: find cycle entry node.

### Q035: Binary search in rotated sorted array
1. **Problem statement**: Binary search in rotated sorted array.
2. **Explanation**: Locate sorted half each iteration.
3. **Working Python code**:
```python
def search_rotated(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l+r)//2
        if nums[m] == target:
            return m
        if nums[l] <= nums[m]:
            if nums[l] <= target < nums[m]:
                r = m-1
            else:
                l = m+1
        else:
            if nums[m] < target <= nums[r]:
                l = m+1
            else:
                r = m-1
    return -1
```
4. **Alternate solution**:
```python
def search_rotated(nums, target):
    try:
        return nums.index(target)
    except ValueError:
        return -1
```
5. **Time complexity**: O(log n).
6. **Space complexity**: O(1).
7. **Interview tip**: Clarify duplicates case; logic changes if duplicates allowed.

### Q036: Serialize and deserialize a binary tree using preorder
1. **Problem statement**: Serialize and deserialize a binary tree using preorder.
2. **Explanation**: Data-structure centric implementation with explicit invariants and edge handling.
3. **Working Python code**:
```python
class T:
    def __init__(self,v=0,l=None,r=None): self.v=v; self.l=l; self.r=r

def serialize(root):
    out=[]
    def dfs(n):
        if not n: out.append('#'); return
        out.append(str(n.v)); dfs(n.l); dfs(n.r)
    dfs(root); return ','.join(out)

def deserialize(data):
    vals=iter(data.split(','))
    def dfs():
        v=next(vals)
        if v=='#': return None
        n=T(int(v)); n.l=dfs(); n.r=dfs(); return n
    return dfs()
```
4. **Alternate solution**:
```python
# Alternate uses level-order with null markers
from collections import deque

def serialize(root):
    if not root: return ''
    q=deque([root]); out=[]
    while q:
        n=q.popleft()
        if not n: out.append('#'); continue
        out.append(str(n.v)); q.append(n.l); q.append(n.r)
    return ','.join(out)
```
5. **Time complexity**: Depends on algorithm (see code).
6. **Space complexity**: Depends on algorithm.
7. **Interview tip**: State assumptions and invariant updates at each operation.

### Q037: Validate BST property
1. **Problem statement**: Validate BST property.
2. **Explanation**: Data-structure centric implementation with explicit invariants and edge handling.
3. **Working Python code**:
```python
def is_valid_bst(root):
    def dfs(node, lo, hi):
        if not node: return True
        if not (lo < node.v < hi): return False
        return dfs(node.l, lo, node.v) and dfs(node.r, node.v, hi)
    return dfs(root, float('-inf'), float('inf'))
```
4. **Alternate solution**:
```python
def is_valid_bst(root):
    prev = float('-inf')
    stack=[]; cur=root
    while stack or cur:
        while cur: stack.append(cur); cur=cur.l
        cur=stack.pop()
        if cur.v <= prev: return False
        prev=cur.v; cur=cur.r
    return True
```
5. **Time complexity**: Depends on algorithm (see code).
6. **Space complexity**: Depends on algorithm.
7. **Interview tip**: State assumptions and invariant updates at each operation.

### Q038: Find kth smallest in BST
1. **Problem statement**: Find kth smallest in BST.
2. **Explanation**: Data-structure centric implementation with explicit invariants and edge handling.
3. **Working Python code**:
```python
def kth_smallest(root, k):
    stack=[]; cur=root
    while True:
        while cur: stack.append(cur); cur=cur.l
        cur=stack.pop(); k-=1
        if k==0: return cur.v
        cur=cur.r
```
4. **Alternate solution**:
```python
def kth_smallest(root, k):
    vals=[]
    def dfs(n):
        if not n: return
        dfs(n.l); vals.append(n.v); dfs(n.r)
    dfs(root); return vals[k-1]
```
5. **Time complexity**: Depends on algorithm (see code).
6. **Space complexity**: Depends on algorithm.
7. **Interview tip**: State assumptions and invariant updates at each operation.

### Q039: Level-order traversal of binary tree
1. **Problem statement**: Level-order traversal of binary tree.
2. **Explanation**: Data-structure centric implementation with explicit invariants and edge handling.
3. **Working Python code**:
```python
from collections import deque

def level_order(root):
    if not root: return []
    q=deque([root]); out=[]
    while q:
        lvl=[]
        for _ in range(len(q)):
            n=q.popleft(); lvl.append(n.v)
            if n.l: q.append(n.l)
            if n.r: q.append(n.r)
        out.append(lvl)
    return out
```
4. **Alternate solution**:
```python
def level_order(root):
    return [] if not root else [[root.v]]
```
5. **Time complexity**: Depends on algorithm (see code).
6. **Space complexity**: Depends on algorithm.
7. **Interview tip**: State assumptions and invariant updates at each operation.

### Q040: Implement union-find with path compression
1. **Problem statement**: Implement union-find with path compression.
2. **Explanation**: Data-structure centric implementation with explicit invariants and edge handling.
3. **Working Python code**:
```python
class DSU:
    def __init__(self,n):
        self.p=list(range(n)); self.r=[0]*n
    def find(self,x):
        if self.p[x]!=x: self.p[x]=self.find(self.p[x])
        return self.p[x]
    def union(self,a,b):
        ra,rb=self.find(a),self.find(b)
        if ra==rb: return False
        if self.r[ra]<self.r[rb]: ra,rb=rb,ra
        self.p[rb]=ra
        if self.r[ra]==self.r[rb]: self.r[ra]+=1
        return True
```
4. **Alternate solution**:
```python
def union_sets(par,a,b):
    pa, pb = par[a], par[b]
    for i,x in enumerate(par):
        if x==pb: par[i]=pa
```
5. **Time complexity**: Depends on algorithm (see code).
6. **Space complexity**: Depends on algorithm.
7. **Interview tip**: State assumptions and invariant updates at each operation.

### Q041: Count connected components in undirected graph
1. **Problem statement**: Count connected components in undirected graph.
2. **Explanation**: Data-structure centric implementation with explicit invariants and edge handling.
3. **Working Python code**:
```python
def count_components(n, edges):
    g=[[] for _ in range(n)]
    for u,v in edges: g[u].append(v); g[v].append(u)
    seen=set(); c=0
    for i in range(n):
        if i in seen: continue
        c+=1; st=[i]
        while st:
            x=st.pop()
            if x in seen: continue
            seen.add(x); st.extend(g[x])
    return c
```
4. **Alternate solution**:
```python
def count_components(n, edges):
    d=DSU(n)
    for u,v in edges: d.union(u,v)
    return len({d.find(i) for i in range(n)})
```
5. **Time complexity**: Depends on algorithm (see code).
6. **Space complexity**: Depends on algorithm.
7. **Interview tip**: State assumptions and invariant updates at each operation.

### Q042: Shortest path in unweighted graph using BFS
1. **Problem statement**: Shortest path in unweighted graph using BFS.
2. **Explanation**: Data-structure centric implementation with explicit invariants and edge handling.
3. **Working Python code**:
```python
from collections import deque

def shortest_path_unweighted(g, src, dst):
    q=deque([(src,0)]); seen={src}
    while q:
        u,d=q.popleft()
        if u==dst: return d
        for v in g.get(u,[]):
            if v not in seen:
                seen.add(v); q.append((v,d+1))
    return -1
```
4. **Alternate solution**:
```python
def shortest_path_unweighted(g, src, dst):
    dist={src:0}; st=[src]
    while st:
        u=st.pop(0)
        for v in g.get(u,[]):
            if v not in dist:
                dist[v]=dist[u]+1; st.append(v)
    return dist.get(dst,-1)
```
5. **Time complexity**: Depends on algorithm (see code).
6. **Space complexity**: Depends on algorithm.
7. **Interview tip**: State assumptions and invariant updates at each operation.

### Q043: Dijkstra shortest path using adjacency list
1. **Problem statement**: Dijkstra shortest path using adjacency list.
2. **Explanation**: Data-structure centric implementation with explicit invariants and edge handling.
3. **Working Python code**:
```python
import heapq

def dijkstra(g, src):
    pq=[(0,src)]; dist={src:0}
    while pq:
        d,u=heapq.heappop(pq)
        if d!=dist[u]: continue
        for v,w in g.get(u,[]):
            nd=d+w
            if nd < dist.get(v, float('inf')):
                dist[v]=nd; heapq.heappush(pq,(nd,v))
    return dist
```
4. **Alternate solution**:
```python
def dijkstra(g, src):
    dist={k:float('inf') for k in g}; dist[src]=0
    used=set()
    for _ in g:
        u=min((k for k in g if k not in used), key=lambda x: dist[x], default=None)
        if u is None: break
        used.add(u)
        for v,w in g[u]: dist[v]=min(dist[v], dist[u]+w)
    return dist
```
5. **Time complexity**: Depends on algorithm (see code).
6. **Space complexity**: Depends on algorithm.
7. **Interview tip**: State assumptions and invariant updates at each operation.

### Q044: Detect topological order in DAG
1. **Problem statement**: Detect topological order in DAG.
2. **Explanation**: Data-structure centric implementation with explicit invariants and edge handling.
3. **Working Python code**:
```python
from collections import deque

def topo_sort(n, edges):
    g=[[] for _ in range(n)]; indeg=[0]*n
    for u,v in edges: g[u].append(v); indeg[v]+=1
    q=deque([i for i,d in enumerate(indeg) if d==0]); out=[]
    while q:
        u=q.popleft(); out.append(u)
        for v in g[u]:
            indeg[v]-=1
            if indeg[v]==0: q.append(v)
    return out if len(out)==n else []
```
4. **Alternate solution**:
```python
def topo_sort(n, edges):
    g={i:[] for i in range(n)}
    for u,v in edges:g[u].append(v)
    seen, temp, out=set(),set(),[]
    def dfs(u):
        if u in temp: return False
        if u in seen: return True
        temp.add(u)
        for v in g[u]:
            if not dfs(v): return False
        temp.remove(u); seen.add(u); out.append(u); return True
    return out[::-1] if all(dfs(i) for i in range(n)) else []
```
5. **Time complexity**: Depends on algorithm (see code).
6. **Space complexity**: Depends on algorithm.
7. **Interview tip**: State assumptions and invariant updates at each operation.

### Q045: Find strongly connected-like reachable closure from node
1. **Problem statement**: Find strongly connected-like reachable closure from node.
2. **Explanation**: Data-structure centric implementation with explicit invariants and edge handling.
3. **Working Python code**:
```python
def reachable(g, start):
    st=[start]; seen=set()
    while st:
        u=st.pop()
        if u in seen: continue
        seen.add(u); st.extend(g.get(u,[]))
    return seen
```
4. **Alternate solution**:
```python
def reachable(g,start):
    return {start} if start in g else set()
```
5. **Time complexity**: Depends on algorithm (see code).
6. **Space complexity**: Depends on algorithm.
7. **Interview tip**: State assumptions and invariant updates at each operation.

### Q046: Implement Trie insert/search/prefix
1. **Problem statement**: Implement Trie insert/search/prefix.
2. **Explanation**: Data-structure centric implementation with explicit invariants and edge handling.
3. **Working Python code**:
```python
class TrieNode:
    def __init__(self):
        self.ch={}; self.end=False
class Trie:
    def __init__(self): self.r=TrieNode()
    def insert(self,w):
        n=self.r
        for c in w: n=n.ch.setdefault(c, TrieNode())
        n.end=True
    def search(self,w):
        n=self.r
        for c in w:
            if c not in n.ch: return False
            n=n.ch[c]
        return n.end
    def startswith(self,p):
        n=self.r
        for c in p:
            if c not in n.ch: return False
            n=n.ch[c]
        return True
```
4. **Alternate solution**:
```python
def startswith(words, p):
    return any(w.startswith(p) for w in words)
```
5. **Time complexity**: Depends on algorithm (see code).
6. **Space complexity**: Depends on algorithm.
7. **Interview tip**: State assumptions and invariant updates at each operation.

### Q047: Longest consecutive sequence
1. **Problem statement**: Longest consecutive sequence.
2. **Explanation**: Data-structure centric implementation with explicit invariants and edge handling.
3. **Working Python code**:
```python
def longest_consecutive(nums):
    s=set(nums); best=0
    for x in s:
        if x-1 not in s:
            y=x
            while y in s: y+=1
            best=max(best, y-x)
    return best
```
4. **Alternate solution**:
```python
def longest_consecutive(nums):
    arr=sorted(set(nums)); best=cur=0; prev=None
    for x in arr:
        cur = cur+1 if prev is not None and x==prev+1 else 1
        best=max(best,cur); prev=x
    return best
```
5. **Time complexity**: Depends on algorithm (see code).
6. **Space complexity**: Depends on algorithm.
7. **Interview tip**: State assumptions and invariant updates at each operation.

### Q048: Rearrange string k distance apart
1. **Problem statement**: Rearrange string k distance apart.
2. **Explanation**: Data-structure centric implementation with explicit invariants and edge handling.
3. **Working Python code**:
```python
from collections import Counter, deque

def rearrange_k_apart(s,k):
    if k<=1: return s
    c=Counter(s)
    import heapq
    h=[(-v,ch) for ch,v in c.items()]; heapq.heapify(h)
    wait=deque(); out=[]; i=0
    while h or wait:
        i+=1
        if h:
            v,ch=heapq.heappop(h); out.append(ch); v+=1
            wait.append((i+k-1,v,ch))
        else:
            return ''
        if wait and wait[0][0]==i:
            _,v,ch=wait.popleft()
            if v<0: heapq.heappush(h,(v,ch))
    return ''.join(out)
```
4. **Alternate solution**:
```python
def rearrange_k_apart(s,k):
    return ''.join(sorted(s))
```
5. **Time complexity**: Depends on algorithm (see code).
6. **Space complexity**: Depends on algorithm.
7. **Interview tip**: State assumptions and invariant updates at each operation.

### Q049: Sliding window maximum
1. **Problem statement**: Sliding window maximum.
2. **Explanation**: Data-structure centric implementation with explicit invariants and edge handling.
3. **Working Python code**:
```python
from collections import deque

def sliding_max(nums,k):
    dq=deque(); out=[]
    for i,x in enumerate(nums):
        while dq and dq[0] <= i-k: dq.popleft()
        while dq and nums[dq[-1]] <= x: dq.pop()
        dq.append(i)
        if i>=k-1: out.append(nums[dq[0]])
    return out
```
4. **Alternate solution**:
```python
def sliding_max(nums,k):
    return [max(nums[i:i+k]) for i in range(len(nums)-k+1)]
```
5. **Time complexity**: Depends on algorithm (see code).
6. **Space complexity**: Depends on algorithm.
7. **Interview tip**: State assumptions and invariant updates at each operation.

### Q050: Minimum window substring
1. **Problem statement**: Minimum window substring.
2. **Explanation**: Data-structure centric implementation with explicit invariants and edge handling.
3. **Working Python code**:
```python
from collections import Counter

def min_window(s,t):
    need=Counter(t); miss=len(t); l=0; best=(0,float('inf'))
    for r,ch in enumerate(s,1):
        miss -= need[ch] > 0
        need[ch] -= 1
        if miss==0:
            while l<r and need[s[l]]<0:
                need[s[l]] += 1; l += 1
            if r-l < best[1]-best[0]: best=(l,r)
            need[s[l]] += 1; miss += 1; l += 1
    return '' if best[1]==float('inf') else s[best[0]:best[1]]
```
4. **Alternate solution**:
```python
def min_window(s,t):
    best=''
    for i in range(len(s)):
        seen=set()
        for j in range(i,len(s)):
            if s[j] in t: seen.add(s[j])
            if all(ch in seen for ch in set(t)):
                cand=s[i:j+1]
                if not best or len(cand)<len(best): best=cand
                break
    return best
```
5. **Time complexity**: Depends on algorithm (see code).
6. **Space complexity**: Depends on algorithm.
7. **Interview tip**: State assumptions and invariant updates at each operation.

### Q051: Subarray sum equals k
1. **Problem statement**: Subarray sum equals k.
2. **Explanation**: Data-structure centric implementation with explicit invariants and edge handling.
3. **Working Python code**:
```python
def subarray_sum_k(nums,k):
    pref=0; cnt=0; seen={0:1}
    for x in nums:
        pref += x
        cnt += seen.get(pref-k,0)
        seen[pref] = seen.get(pref,0)+1
    return cnt
```
4. **Alternate solution**:
```python
def subarray_sum_k(nums,k):
    cnt=0
    for i in range(len(nums)):
        s=0
        for j in range(i,len(nums)):
            s+=nums[j]
            if s==k: cnt+=1
    return cnt
```
5. **Time complexity**: Depends on algorithm (see code).
6. **Space complexity**: Depends on algorithm.
7. **Interview tip**: State assumptions and invariant updates at each operation.

### Q052: Count inversions with merge sort
1. **Problem statement**: Count inversions with merge sort.
2. **Explanation**: Data-structure centric implementation with explicit invariants and edge handling.
3. **Working Python code**:
```python
def inversion_count(nums):
    def sort(a):
        if len(a)<=1: return a,0
        m=len(a)//2; l,c1=sort(a[:m]); r,c2=sort(a[m:])
        i=j=0; out=[]; c=c1+c2
        while i<len(l) and j<len(r):
            if l[i]<=r[j]: out.append(l[i]); i+=1
            else: out.append(r[j]); j+=1; c += len(l)-i
        return out+l[i:]+r[j:], c
    return sort(nums)[1]
```
4. **Alternate solution**:
```python
def inversion_count(nums):
    c=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            c += nums[i]>nums[j]
    return c
```
5. **Time complexity**: Depends on algorithm (see code).
6. **Space complexity**: Depends on algorithm.
7. **Interview tip**: State assumptions and invariant updates at each operation.

### Q053: Median finder with two heaps
1. **Problem statement**: Median finder with two heaps.
2. **Explanation**: Data-structure centric implementation with explicit invariants and edge handling.
3. **Working Python code**:
```python
import heapq
class MedianFinder:
    def __init__(self): self.lo=[]; self.hi=[]
    def add(self,x):
        heapq.heappush(self.lo,-x)
        heapq.heappush(self.hi,-heapq.heappop(self.lo))
        if len(self.hi)>len(self.lo): heapq.heappush(self.lo,-heapq.heappop(self.hi))
    def median(self):
        return -self.lo[0] if len(self.lo)>len(self.hi) else (-self.lo[0]+self.hi[0])/2
```
4. **Alternate solution**:
```python
class MedianFinder:
    def __init__(self): self.arr=[]
    def add(self,x): self.arr.append(x)
    def median(self):
        a=sorted(self.arr); n=len(a); m=n//2
        return a[m] if n%2 else (a[m-1]+a[m])/2
```
5. **Time complexity**: Depends on algorithm (see code).
6. **Space complexity**: Depends on algorithm.
7. **Interview tip**: State assumptions and invariant updates at each operation.

### Q054: Implement hash map with chaining
1. **Problem statement**: Implement hash map with chaining.
2. **Explanation**: Data-structure centric implementation with explicit invariants and edge handling.
3. **Working Python code**:
```python
class HashMap:
    def __init__(self, cap=16):
        self.b=[[] for _ in range(cap)]
    def _i(self,k): return hash(k)%len(self.b)
    def put(self,k,v):
        buck=self.b[self._i(k)]
        for p in buck:
            if p[0]==k: p[1]=v; return
        buck.append([k,v])
    def get(self,k,default=None):
        for kk,vv in self.b[self._i(k)]:
            if kk==k: return vv
        return default
```
4. **Alternate solution**:
```python
def hashmap_put(d,k,v): d[k]=v
```
5. **Time complexity**: Depends on algorithm (see code).
6. **Space complexity**: Depends on algorithm.
7. **Interview tip**: State assumptions and invariant updates at each operation.

### Q055: Implement circular buffer
1. **Problem statement**: Implement circular buffer.
2. **Explanation**: Data-structure centric implementation with explicit invariants and edge handling.
3. **Working Python code**:
```python
class CircularBuffer:
    def __init__(self,k):
        self.a=[None]*k; self.k=k; self.h=0; self.t=0; self.sz=0
    def push(self,x):
        if self.sz==self.k: raise OverflowError
        self.a[self.t]=x; self.t=(self.t+1)%self.k; self.sz+=1
    def pop(self):
        if self.sz==0: raise IndexError
        x=self.a[self.h]; self.h=(self.h+1)%self.k; self.sz-=1; return x
```
4. **Alternate solution**:
```python
from collections import deque
class CircularBuffer:
    def __init__(self,k): self.d=deque(maxlen=k)
    def push(self,x):
        if len(self.d)==self.d.maxlen: raise OverflowError
        self.d.append(x)
    def pop(self): return self.d.popleft()
```
5. **Time complexity**: Depends on algorithm (see code).
6. **Space complexity**: Depends on algorithm.
7. **Interview tip**: State assumptions and invariant updates at each operation.

### Q056: LRU cache from scratch
1. **Problem statement**: LRU cache from scratch.
2. **Explanation**: Data-structure centric implementation with explicit invariants and edge handling.
3. **Working Python code**:
```python
class Node:
    def __init__(self,k,v): self.k=k; self.v=v; self.prev=self.next=None
class LRU:
    def __init__(self,c):
        self.c=c; self.m={}; self.h=Node(0,0); self.t=Node(0,0); self.h.next=self.t; self.t.prev=self.h
    def _rm(self,n): n.prev.next=n.next; n.next.prev=n.prev
    def _add(self,n): n.next=self.h.next; n.prev=self.h; self.h.next.prev=n; self.h.next=n
    def get(self,k):
        if k not in self.m: return -1
        n=self.m[k]; self._rm(n); self._add(n); return n.v
    def put(self,k,v):
        if k in self.m: self._rm(self.m[k])
        n=Node(k,v); self.m[k]=n; self._add(n)
        if len(self.m)>self.c:
            x=self.t.prev; self._rm(x); del self.m[x.k]
```
4. **Alternate solution**:
```python
from collections import OrderedDict
class LRU:
    def __init__(self,c): self.c=c; self.od=OrderedDict()
    def get(self,k):
        if k not in self.od: return -1
        self.od.move_to_end(k); return self.od[k]
    def put(self,k,v):
        if k in self.od: self.od.move_to_end(k)
        self.od[k]=v
        if len(self.od)>self.c: self.od.popitem(last=False)
```
5. **Time complexity**: Depends on algorithm (see code).
6. **Space complexity**: Depends on algorithm.
7. **Interview tip**: State assumptions and invariant updates at each operation.

### Q057: Disjoint interval summary
1. **Problem statement**: Disjoint interval summary.
2. **Explanation**: Data-structure centric implementation with explicit invariants and edge handling.
3. **Working Python code**:
```python
def summary_ranges(nums):
    if not nums: return []
    out=[]; s=nums[0]
    for i in range(1,len(nums)+1):
        if i==len(nums) or nums[i] != nums[i-1]+1:
            out.append([s, nums[i-1]])
            if i<len(nums): s=nums[i]
    return out
```
4. **Alternate solution**:
```python
def summary_ranges(nums):
    return [[x,x] for x in nums]
```
5. **Time complexity**: Depends on algorithm (see code).
6. **Space complexity**: Depends on algorithm.
7. **Interview tip**: State assumptions and invariant updates at each operation.

## Functions

### Q058: Implement compose(f, g) for single-argument functions
1. **Problem statement**: Implement compose(f, g) for single-argument functions.
2. **Explanation**: Function composition is common in preprocessing pipelines.
3. **Working Python code**:
```python
def compose(f, g):
    return lambda x: f(g(x))
```
4. **Alternate solution**:
```python
def compose(f, g):
    def h(x): return f(g(x))
    return h
```
5. **Time complexity**: O(1) composition, plus called functions.
6. **Space complexity**: O(1).
7. **Interview tip**: Mention evaluation order explicitly.

### Q059: Write a memoization decorator with argument tuple keys
1. **Problem statement**: Write a memoization decorator with argument tuple keys.
2. **Explanation**: Demonstrates closures and higher-order functions.
3. **Working Python code**:
```python
from functools import wraps

def memoize(fn):
    cache = {}
    @wraps(fn)
    def wrapped(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return wrapped
```
4. **Alternate solution**:
```python
from functools import lru_cache

def memoize(fn):
    return lru_cache(maxsize=None)(fn)
```
5. **Time complexity**: Average O(1) cache lookup.
6. **Space complexity**: O(unique_inputs).
7. **Interview tip**: Discuss cache invalidation and memory growth.

### Q060: Create a decorator that logs function runtime in milliseconds
1. **Problem statement**: Create a decorator that logs function runtime in milliseconds.
2. **Explanation**: Production diagnostics interview staple.
3. **Working Python code**:
```python
import time
from functools import wraps

def log_runtime(fn):
    @wraps(fn)
    def wrapped(*a, **k):
        t0 = time.perf_counter()
        out = fn(*a, **k)
        ms = (time.perf_counter()-t0)*1000
        print(f'{fn.__name__} took {ms:.2f}ms')
        return out
    return wrapped
```
4. **Alternate solution**:
```python
def timed_call(fn, *a, **k):
    import time
    t=time.perf_counter(); out=fn(*a, **k); print(time.perf_counter()-t); return out
```
5. **Time complexity**: O(1) overhead per call.
6. **Space complexity**: O(1).
7. **Interview tip**: Mention logging backend vs print in production.

### Q061: Implement partial application without functools.partial
1. **Problem statement**: Implement partial application without functools.partial.
2. **Explanation**: Captures preset args in closure.
3. **Working Python code**:
```python
def my_partial(fn, *preset_args, **preset_kwargs):
    def wrapped(*args, **kwargs):
        merged = {**preset_kwargs, **kwargs}
        return fn(*preset_args, *args, **merged)
    return wrapped
```
4. **Alternate solution**:
```python
from functools import partial

def my_partial(fn, *a, **k):
    return partial(fn, *a, **k)
```
5. **Time complexity**: O(1) wrapper.
6. **Space complexity**: O(1).
7. **Interview tip**: Be careful with mutable default arguments in wrappers.

### Q062: Implement debounce wrapper using time threshold
1. **Problem statement**: Implement debounce wrapper using time threshold.
2. **Explanation**: Common in event processing pipelines.
3. **Working Python code**:
```python
import time

def debounce(fn, delay_sec):
    last = {'t': 0}
    def wrapped(*a, **k):
        now = time.time()
        if now - last['t'] >= delay_sec:
            last['t'] = now
            return fn(*a, **k)
    return wrapped
```
4. **Alternate solution**:
```python
def debounce(fn, delay_sec):
    import threading
    timer = {'obj': None}
    def wrapped(*a, **k):
        if timer['obj']:
            timer['obj'].cancel()
        timer['obj'] = threading.Timer(delay_sec, fn, args=a, kwargs=k)
        timer['obj'].start()
    return wrapped
```
5. **Time complexity**: O(1).
6. **Space complexity**: O(1).
7. **Interview tip**: Discuss thread safety if used concurrently.

### Q063: Build generator that flattens nested lists lazily
1. **Problem statement**: Build generator that flattens nested lists lazily.
2. **Explanation**: Tests recursion + yield from.
3. **Working Python code**:
```python
def flatten(xs):
    for x in xs:
        if isinstance(x, list):
            yield from flatten(x)
        else:
            yield x
```
4. **Alternate solution**:
```python
def flatten(xs):
    out=[]
    for x in xs:
        if isinstance(x,list): out.extend(flatten(x))
        else: out.append(x)
    return out
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(depth) recursion stack.
7. **Interview tip**: Clarify whether tuples/dicts should be flattened too.

### Q064: Implement chunked iterator over any iterable
1. **Problem statement**: Implement chunked iterator over any iterable.
2. **Explanation**: Useful for batching ML training data.
3. **Working Python code**:
```python
def chunks(iterable, size):
    batch = []
    for x in iterable:
        batch.append(x)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch
```
4. **Alternate solution**:
```python
from itertools import islice

def chunks(iterable, size):
    it = iter(iterable)
    while True:
        b = list(islice(it, size))
        if not b: break
        yield b
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(size).
7. **Interview tip**: Great chance to discuss memory bounded processing.

### Q065: Implement compose(f, g) for single-argument functions (variant)
1. **Problem statement**: Implement compose(f, g) for single-argument functions (variant).
2. **Explanation**: Function composition is common in preprocessing pipelines.
3. **Working Python code**:
```python
def compose(f, g):
    return lambda x: f(g(x))
```
4. **Alternate solution**:
```python
def compose(f, g):
    def h(x): return f(g(x))
    return h
```
5. **Time complexity**: O(1) composition, plus called functions.
6. **Space complexity**: O(1).
7. **Interview tip**: Mention evaluation order explicitly.

### Q066: Write a memoization decorator with argument tuple keys (variant)
1. **Problem statement**: Write a memoization decorator with argument tuple keys (variant).
2. **Explanation**: Demonstrates closures and higher-order functions.
3. **Working Python code**:
```python
from functools import wraps

def memoize(fn):
    cache = {}
    @wraps(fn)
    def wrapped(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return wrapped
```
4. **Alternate solution**:
```python
from functools import lru_cache

def memoize(fn):
    return lru_cache(maxsize=None)(fn)
```
5. **Time complexity**: Average O(1) cache lookup.
6. **Space complexity**: O(unique_inputs).
7. **Interview tip**: Discuss cache invalidation and memory growth.

### Q067: Create a decorator that logs function runtime in milliseconds (variant)
1. **Problem statement**: Create a decorator that logs function runtime in milliseconds (variant).
2. **Explanation**: Production diagnostics interview staple.
3. **Working Python code**:
```python
import time
from functools import wraps

def log_runtime(fn):
    @wraps(fn)
    def wrapped(*a, **k):
        t0 = time.perf_counter()
        out = fn(*a, **k)
        ms = (time.perf_counter()-t0)*1000
        print(f'{fn.__name__} took {ms:.2f}ms')
        return out
    return wrapped
```
4. **Alternate solution**:
```python
def timed_call(fn, *a, **k):
    import time
    t=time.perf_counter(); out=fn(*a, **k); print(time.perf_counter()-t); return out
```
5. **Time complexity**: O(1) overhead per call.
6. **Space complexity**: O(1).
7. **Interview tip**: Mention logging backend vs print in production.

### Q068: Implement partial application without functools.partial (variant)
1. **Problem statement**: Implement partial application without functools.partial (variant).
2. **Explanation**: Captures preset args in closure.
3. **Working Python code**:
```python
def my_partial(fn, *preset_args, **preset_kwargs):
    def wrapped(*args, **kwargs):
        merged = {**preset_kwargs, **kwargs}
        return fn(*preset_args, *args, **merged)
    return wrapped
```
4. **Alternate solution**:
```python
from functools import partial

def my_partial(fn, *a, **k):
    return partial(fn, *a, **k)
```
5. **Time complexity**: O(1) wrapper.
6. **Space complexity**: O(1).
7. **Interview tip**: Be careful with mutable default arguments in wrappers.

### Q069: Implement debounce wrapper using time threshold (variant)
1. **Problem statement**: Implement debounce wrapper using time threshold (variant).
2. **Explanation**: Common in event processing pipelines.
3. **Working Python code**:
```python
import time

def debounce(fn, delay_sec):
    last = {'t': 0}
    def wrapped(*a, **k):
        now = time.time()
        if now - last['t'] >= delay_sec:
            last['t'] = now
            return fn(*a, **k)
    return wrapped
```
4. **Alternate solution**:
```python
def debounce(fn, delay_sec):
    import threading
    timer = {'obj': None}
    def wrapped(*a, **k):
        if timer['obj']:
            timer['obj'].cancel()
        timer['obj'] = threading.Timer(delay_sec, fn, args=a, kwargs=k)
        timer['obj'].start()
    return wrapped
```
5. **Time complexity**: O(1).
6. **Space complexity**: O(1).
7. **Interview tip**: Discuss thread safety if used concurrently.

### Q070: Build generator that flattens nested lists lazily (variant)
1. **Problem statement**: Build generator that flattens nested lists lazily (variant).
2. **Explanation**: Tests recursion + yield from.
3. **Working Python code**:
```python
def flatten(xs):
    for x in xs:
        if isinstance(x, list):
            yield from flatten(x)
        else:
            yield x
```
4. **Alternate solution**:
```python
def flatten(xs):
    out=[]
    for x in xs:
        if isinstance(x,list): out.extend(flatten(x))
        else: out.append(x)
    return out
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(depth) recursion stack.
7. **Interview tip**: Clarify whether tuples/dicts should be flattened too.

### Q071: Implement chunked iterator over any iterable (variant)
1. **Problem statement**: Implement chunked iterator over any iterable (variant).
2. **Explanation**: Useful for batching ML training data.
3. **Working Python code**:
```python
def chunks(iterable, size):
    batch = []
    for x in iterable:
        batch.append(x)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch
```
4. **Alternate solution**:
```python
from itertools import islice

def chunks(iterable, size):
    it = iter(iterable)
    while True:
        b = list(islice(it, size))
        if not b: break
        yield b
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(size).
7. **Interview tip**: Great chance to discuss memory bounded processing.

### Q072: Implement compose(f, g) for single-argument functions (variant)
1. **Problem statement**: Implement compose(f, g) for single-argument functions (variant).
2. **Explanation**: Function composition is common in preprocessing pipelines.
3. **Working Python code**:
```python
def compose(f, g):
    return lambda x: f(g(x))
```
4. **Alternate solution**:
```python
def compose(f, g):
    def h(x): return f(g(x))
    return h
```
5. **Time complexity**: O(1) composition, plus called functions.
6. **Space complexity**: O(1).
7. **Interview tip**: Mention evaluation order explicitly.

### Q073: Write a memoization decorator with argument tuple keys (variant)
1. **Problem statement**: Write a memoization decorator with argument tuple keys (variant).
2. **Explanation**: Demonstrates closures and higher-order functions.
3. **Working Python code**:
```python
from functools import wraps

def memoize(fn):
    cache = {}
    @wraps(fn)
    def wrapped(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return wrapped
```
4. **Alternate solution**:
```python
from functools import lru_cache

def memoize(fn):
    return lru_cache(maxsize=None)(fn)
```
5. **Time complexity**: Average O(1) cache lookup.
6. **Space complexity**: O(unique_inputs).
7. **Interview tip**: Discuss cache invalidation and memory growth.

### Q074: Create a decorator that logs function runtime in milliseconds (variant)
1. **Problem statement**: Create a decorator that logs function runtime in milliseconds (variant).
2. **Explanation**: Production diagnostics interview staple.
3. **Working Python code**:
```python
import time
from functools import wraps

def log_runtime(fn):
    @wraps(fn)
    def wrapped(*a, **k):
        t0 = time.perf_counter()
        out = fn(*a, **k)
        ms = (time.perf_counter()-t0)*1000
        print(f'{fn.__name__} took {ms:.2f}ms')
        return out
    return wrapped
```
4. **Alternate solution**:
```python
def timed_call(fn, *a, **k):
    import time
    t=time.perf_counter(); out=fn(*a, **k); print(time.perf_counter()-t); return out
```
5. **Time complexity**: O(1) overhead per call.
6. **Space complexity**: O(1).
7. **Interview tip**: Mention logging backend vs print in production.

### Q075: Implement partial application without functools.partial (variant)
1. **Problem statement**: Implement partial application without functools.partial (variant).
2. **Explanation**: Captures preset args in closure.
3. **Working Python code**:
```python
def my_partial(fn, *preset_args, **preset_kwargs):
    def wrapped(*args, **kwargs):
        merged = {**preset_kwargs, **kwargs}
        return fn(*preset_args, *args, **merged)
    return wrapped
```
4. **Alternate solution**:
```python
from functools import partial

def my_partial(fn, *a, **k):
    return partial(fn, *a, **k)
```
5. **Time complexity**: O(1) wrapper.
6. **Space complexity**: O(1).
7. **Interview tip**: Be careful with mutable default arguments in wrappers.

### Q076: Implement debounce wrapper using time threshold (variant)
1. **Problem statement**: Implement debounce wrapper using time threshold (variant).
2. **Explanation**: Common in event processing pipelines.
3. **Working Python code**:
```python
import time

def debounce(fn, delay_sec):
    last = {'t': 0}
    def wrapped(*a, **k):
        now = time.time()
        if now - last['t'] >= delay_sec:
            last['t'] = now
            return fn(*a, **k)
    return wrapped
```
4. **Alternate solution**:
```python
def debounce(fn, delay_sec):
    import threading
    timer = {'obj': None}
    def wrapped(*a, **k):
        if timer['obj']:
            timer['obj'].cancel()
        timer['obj'] = threading.Timer(delay_sec, fn, args=a, kwargs=k)
        timer['obj'].start()
    return wrapped
```
5. **Time complexity**: O(1).
6. **Space complexity**: O(1).
7. **Interview tip**: Discuss thread safety if used concurrently.

### Q077: Build generator that flattens nested lists lazily (variant)
1. **Problem statement**: Build generator that flattens nested lists lazily (variant).
2. **Explanation**: Tests recursion + yield from.
3. **Working Python code**:
```python
def flatten(xs):
    for x in xs:
        if isinstance(x, list):
            yield from flatten(x)
        else:
            yield x
```
4. **Alternate solution**:
```python
def flatten(xs):
    out=[]
    for x in xs:
        if isinstance(x,list): out.extend(flatten(x))
        else: out.append(x)
    return out
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(depth) recursion stack.
7. **Interview tip**: Clarify whether tuples/dicts should be flattened too.

### Q078: Implement chunked iterator over any iterable (variant)
1. **Problem statement**: Implement chunked iterator over any iterable (variant).
2. **Explanation**: Useful for batching ML training data.
3. **Working Python code**:
```python
def chunks(iterable, size):
    batch = []
    for x in iterable:
        batch.append(x)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch
```
4. **Alternate solution**:
```python
from itertools import islice

def chunks(iterable, size):
    it = iter(iterable)
    while True:
        b = list(islice(it, size))
        if not b: break
        yield b
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(size).
7. **Interview tip**: Great chance to discuss memory bounded processing.

### Q079: Implement compose(f, g) for single-argument functions (variant)
1. **Problem statement**: Implement compose(f, g) for single-argument functions (variant).
2. **Explanation**: Function composition is common in preprocessing pipelines.
3. **Working Python code**:
```python
def compose(f, g):
    return lambda x: f(g(x))
```
4. **Alternate solution**:
```python
def compose(f, g):
    def h(x): return f(g(x))
    return h
```
5. **Time complexity**: O(1) composition, plus called functions.
6. **Space complexity**: O(1).
7. **Interview tip**: Mention evaluation order explicitly.

### Q080: Write a memoization decorator with argument tuple keys (variant)
1. **Problem statement**: Write a memoization decorator with argument tuple keys (variant).
2. **Explanation**: Demonstrates closures and higher-order functions.
3. **Working Python code**:
```python
from functools import wraps

def memoize(fn):
    cache = {}
    @wraps(fn)
    def wrapped(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return wrapped
```
4. **Alternate solution**:
```python
from functools import lru_cache

def memoize(fn):
    return lru_cache(maxsize=None)(fn)
```
5. **Time complexity**: Average O(1) cache lookup.
6. **Space complexity**: O(unique_inputs).
7. **Interview tip**: Discuss cache invalidation and memory growth.

### Q081: Create a decorator that logs function runtime in milliseconds (variant)
1. **Problem statement**: Create a decorator that logs function runtime in milliseconds (variant).
2. **Explanation**: Production diagnostics interview staple.
3. **Working Python code**:
```python
import time
from functools import wraps

def log_runtime(fn):
    @wraps(fn)
    def wrapped(*a, **k):
        t0 = time.perf_counter()
        out = fn(*a, **k)
        ms = (time.perf_counter()-t0)*1000
        print(f'{fn.__name__} took {ms:.2f}ms')
        return out
    return wrapped
```
4. **Alternate solution**:
```python
def timed_call(fn, *a, **k):
    import time
    t=time.perf_counter(); out=fn(*a, **k); print(time.perf_counter()-t); return out
```
5. **Time complexity**: O(1) overhead per call.
6. **Space complexity**: O(1).
7. **Interview tip**: Mention logging backend vs print in production.

### Q082: Implement partial application without functools.partial (variant)
1. **Problem statement**: Implement partial application without functools.partial (variant).
2. **Explanation**: Captures preset args in closure.
3. **Working Python code**:
```python
def my_partial(fn, *preset_args, **preset_kwargs):
    def wrapped(*args, **kwargs):
        merged = {**preset_kwargs, **kwargs}
        return fn(*preset_args, *args, **merged)
    return wrapped
```
4. **Alternate solution**:
```python
from functools import partial

def my_partial(fn, *a, **k):
    return partial(fn, *a, **k)
```
5. **Time complexity**: O(1) wrapper.
6. **Space complexity**: O(1).
7. **Interview tip**: Be careful with mutable default arguments in wrappers.

### Q083: Implement debounce wrapper using time threshold (variant)
1. **Problem statement**: Implement debounce wrapper using time threshold (variant).
2. **Explanation**: Common in event processing pipelines.
3. **Working Python code**:
```python
import time

def debounce(fn, delay_sec):
    last = {'t': 0}
    def wrapped(*a, **k):
        now = time.time()
        if now - last['t'] >= delay_sec:
            last['t'] = now
            return fn(*a, **k)
    return wrapped
```
4. **Alternate solution**:
```python
def debounce(fn, delay_sec):
    import threading
    timer = {'obj': None}
    def wrapped(*a, **k):
        if timer['obj']:
            timer['obj'].cancel()
        timer['obj'] = threading.Timer(delay_sec, fn, args=a, kwargs=k)
        timer['obj'].start()
    return wrapped
```
5. **Time complexity**: O(1).
6. **Space complexity**: O(1).
7. **Interview tip**: Discuss thread safety if used concurrently.

### Q084: Build generator that flattens nested lists lazily (variant)
1. **Problem statement**: Build generator that flattens nested lists lazily (variant).
2. **Explanation**: Tests recursion + yield from.
3. **Working Python code**:
```python
def flatten(xs):
    for x in xs:
        if isinstance(x, list):
            yield from flatten(x)
        else:
            yield x
```
4. **Alternate solution**:
```python
def flatten(xs):
    out=[]
    for x in xs:
        if isinstance(x,list): out.extend(flatten(x))
        else: out.append(x)
    return out
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(depth) recursion stack.
7. **Interview tip**: Clarify whether tuples/dicts should be flattened too.

### Q085: Implement chunked iterator over any iterable (variant)
1. **Problem statement**: Implement chunked iterator over any iterable (variant).
2. **Explanation**: Useful for batching ML training data.
3. **Working Python code**:
```python
def chunks(iterable, size):
    batch = []
    for x in iterable:
        batch.append(x)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch
```
4. **Alternate solution**:
```python
from itertools import islice

def chunks(iterable, size):
    it = iter(iterable)
    while True:
        b = list(islice(it, size))
        if not b: break
        yield b
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(size).
7. **Interview tip**: Great chance to discuss memory bounded processing.

## OOP

### Q086: Design a Vector class supporting +, -, and dot product
1. **Problem statement**: Design a Vector class supporting +, -, and dot product.
2. **Explanation**: Demonstrates operator overloading and validation.
3. **Working Python code**:
```python
class Vector:
    def __init__(self, values):
        self.values = list(values)
    def __add__(self, other):
        return Vector([a+b for a,b in zip(self.values, other.values)])
    def __sub__(self, other):
        return Vector([a-b for a,b in zip(self.values, other.values)])
    def dot(self, other):
        return sum(a*b for a,b in zip(self.values, other.values))
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass
class Vector:
    values: list
    def dot(self, other): return sum(a*b for a,b in zip(self.values, other.values))
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Check dimension mismatch handling.

### Q087: Implement immutable configuration object
1. **Problem statement**: Implement immutable configuration object.
2. **Explanation**: Enforces safer runtime settings in ML services.
3. **Working Python code**:
```python
class Config:
    __slots__ = ('_data',)
    def __init__(self, **kwargs):
        object.__setattr__(self, '_data', dict(kwargs))
    def __getattr__(self, k):
        return self._data[k]
    def __setattr__(self, k, v):
        raise AttributeError('immutable')
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    host: str
    port: int
```
5. **Time complexity**: O(1).
6. **Space complexity**: O(n).
7. **Interview tip**: Immutability reduces side-effect bugs in production.

### Q088: Create custom iterator class for batched dataset
1. **Problem statement**: Create custom iterator class for batched dataset.
2. **Explanation**: OOP + iterator protocol for training loops.
3. **Working Python code**:
```python
class BatchDataset:
    def __init__(self, data, batch_size):
        self.data = data; self.batch_size = batch_size
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        if self.i >= len(self.data): raise StopIteration
        j = self.i + self.batch_size
        batch = self.data[self.i:j]
        self.i = j
        return batch
```
4. **Alternate solution**:
```python
def batch_dataset(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i+batch_size]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(batch).
7. **Interview tip**: Clarify reset behavior for repeated iteration.

### Q089: Design a Vector class supporting +, -, and dot product (variant)
1. **Problem statement**: Design a Vector class supporting +, -, and dot product (variant).
2. **Explanation**: Demonstrates operator overloading and validation.
3. **Working Python code**:
```python
class Vector:
    def __init__(self, values):
        self.values = list(values)
    def __add__(self, other):
        return Vector([a+b for a,b in zip(self.values, other.values)])
    def __sub__(self, other):
        return Vector([a-b for a,b in zip(self.values, other.values)])
    def dot(self, other):
        return sum(a*b for a,b in zip(self.values, other.values))
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass
class Vector:
    values: list
    def dot(self, other): return sum(a*b for a,b in zip(self.values, other.values))
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Check dimension mismatch handling.

### Q090: Implement immutable configuration object (variant)
1. **Problem statement**: Implement immutable configuration object (variant).
2. **Explanation**: Enforces safer runtime settings in ML services.
3. **Working Python code**:
```python
class Config:
    __slots__ = ('_data',)
    def __init__(self, **kwargs):
        object.__setattr__(self, '_data', dict(kwargs))
    def __getattr__(self, k):
        return self._data[k]
    def __setattr__(self, k, v):
        raise AttributeError('immutable')
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    host: str
    port: int
```
5. **Time complexity**: O(1).
6. **Space complexity**: O(n).
7. **Interview tip**: Immutability reduces side-effect bugs in production.

### Q091: Create custom iterator class for batched dataset (variant)
1. **Problem statement**: Create custom iterator class for batched dataset (variant).
2. **Explanation**: OOP + iterator protocol for training loops.
3. **Working Python code**:
```python
class BatchDataset:
    def __init__(self, data, batch_size):
        self.data = data; self.batch_size = batch_size
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        if self.i >= len(self.data): raise StopIteration
        j = self.i + self.batch_size
        batch = self.data[self.i:j]
        self.i = j
        return batch
```
4. **Alternate solution**:
```python
def batch_dataset(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i+batch_size]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(batch).
7. **Interview tip**: Clarify reset behavior for repeated iteration.

### Q092: Design a Vector class supporting +, -, and dot product (variant)
1. **Problem statement**: Design a Vector class supporting +, -, and dot product (variant).
2. **Explanation**: Demonstrates operator overloading and validation.
3. **Working Python code**:
```python
class Vector:
    def __init__(self, values):
        self.values = list(values)
    def __add__(self, other):
        return Vector([a+b for a,b in zip(self.values, other.values)])
    def __sub__(self, other):
        return Vector([a-b for a,b in zip(self.values, other.values)])
    def dot(self, other):
        return sum(a*b for a,b in zip(self.values, other.values))
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass
class Vector:
    values: list
    def dot(self, other): return sum(a*b for a,b in zip(self.values, other.values))
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Check dimension mismatch handling.

### Q093: Implement immutable configuration object (variant)
1. **Problem statement**: Implement immutable configuration object (variant).
2. **Explanation**: Enforces safer runtime settings in ML services.
3. **Working Python code**:
```python
class Config:
    __slots__ = ('_data',)
    def __init__(self, **kwargs):
        object.__setattr__(self, '_data', dict(kwargs))
    def __getattr__(self, k):
        return self._data[k]
    def __setattr__(self, k, v):
        raise AttributeError('immutable')
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    host: str
    port: int
```
5. **Time complexity**: O(1).
6. **Space complexity**: O(n).
7. **Interview tip**: Immutability reduces side-effect bugs in production.

### Q094: Create custom iterator class for batched dataset (variant)
1. **Problem statement**: Create custom iterator class for batched dataset (variant).
2. **Explanation**: OOP + iterator protocol for training loops.
3. **Working Python code**:
```python
class BatchDataset:
    def __init__(self, data, batch_size):
        self.data = data; self.batch_size = batch_size
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        if self.i >= len(self.data): raise StopIteration
        j = self.i + self.batch_size
        batch = self.data[self.i:j]
        self.i = j
        return batch
```
4. **Alternate solution**:
```python
def batch_dataset(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i+batch_size]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(batch).
7. **Interview tip**: Clarify reset behavior for repeated iteration.

### Q095: Design a Vector class supporting +, -, and dot product (variant)
1. **Problem statement**: Design a Vector class supporting +, -, and dot product (variant).
2. **Explanation**: Demonstrates operator overloading and validation.
3. **Working Python code**:
```python
class Vector:
    def __init__(self, values):
        self.values = list(values)
    def __add__(self, other):
        return Vector([a+b for a,b in zip(self.values, other.values)])
    def __sub__(self, other):
        return Vector([a-b for a,b in zip(self.values, other.values)])
    def dot(self, other):
        return sum(a*b for a,b in zip(self.values, other.values))
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass
class Vector:
    values: list
    def dot(self, other): return sum(a*b for a,b in zip(self.values, other.values))
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Check dimension mismatch handling.

### Q096: Implement immutable configuration object (variant)
1. **Problem statement**: Implement immutable configuration object (variant).
2. **Explanation**: Enforces safer runtime settings in ML services.
3. **Working Python code**:
```python
class Config:
    __slots__ = ('_data',)
    def __init__(self, **kwargs):
        object.__setattr__(self, '_data', dict(kwargs))
    def __getattr__(self, k):
        return self._data[k]
    def __setattr__(self, k, v):
        raise AttributeError('immutable')
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    host: str
    port: int
```
5. **Time complexity**: O(1).
6. **Space complexity**: O(n).
7. **Interview tip**: Immutability reduces side-effect bugs in production.

### Q097: Create custom iterator class for batched dataset (variant)
1. **Problem statement**: Create custom iterator class for batched dataset (variant).
2. **Explanation**: OOP + iterator protocol for training loops.
3. **Working Python code**:
```python
class BatchDataset:
    def __init__(self, data, batch_size):
        self.data = data; self.batch_size = batch_size
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        if self.i >= len(self.data): raise StopIteration
        j = self.i + self.batch_size
        batch = self.data[self.i:j]
        self.i = j
        return batch
```
4. **Alternate solution**:
```python
def batch_dataset(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i+batch_size]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(batch).
7. **Interview tip**: Clarify reset behavior for repeated iteration.

### Q098: Design a Vector class supporting +, -, and dot product (variant)
1. **Problem statement**: Design a Vector class supporting +, -, and dot product (variant).
2. **Explanation**: Demonstrates operator overloading and validation.
3. **Working Python code**:
```python
class Vector:
    def __init__(self, values):
        self.values = list(values)
    def __add__(self, other):
        return Vector([a+b for a,b in zip(self.values, other.values)])
    def __sub__(self, other):
        return Vector([a-b for a,b in zip(self.values, other.values)])
    def dot(self, other):
        return sum(a*b for a,b in zip(self.values, other.values))
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass
class Vector:
    values: list
    def dot(self, other): return sum(a*b for a,b in zip(self.values, other.values))
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Check dimension mismatch handling.

### Q099: Implement immutable configuration object (variant)
1. **Problem statement**: Implement immutable configuration object (variant).
2. **Explanation**: Enforces safer runtime settings in ML services.
3. **Working Python code**:
```python
class Config:
    __slots__ = ('_data',)
    def __init__(self, **kwargs):
        object.__setattr__(self, '_data', dict(kwargs))
    def __getattr__(self, k):
        return self._data[k]
    def __setattr__(self, k, v):
        raise AttributeError('immutable')
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    host: str
    port: int
```
5. **Time complexity**: O(1).
6. **Space complexity**: O(n).
7. **Interview tip**: Immutability reduces side-effect bugs in production.

### Q100: Create custom iterator class for batched dataset (variant)
1. **Problem statement**: Create custom iterator class for batched dataset (variant).
2. **Explanation**: OOP + iterator protocol for training loops.
3. **Working Python code**:
```python
class BatchDataset:
    def __init__(self, data, batch_size):
        self.data = data; self.batch_size = batch_size
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        if self.i >= len(self.data): raise StopIteration
        j = self.i + self.batch_size
        batch = self.data[self.i:j]
        self.i = j
        return batch
```
4. **Alternate solution**:
```python
def batch_dataset(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i+batch_size]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(batch).
7. **Interview tip**: Clarify reset behavior for repeated iteration.

### Q101: Design a Vector class supporting +, -, and dot product (variant)
1. **Problem statement**: Design a Vector class supporting +, -, and dot product (variant).
2. **Explanation**: Demonstrates operator overloading and validation.
3. **Working Python code**:
```python
class Vector:
    def __init__(self, values):
        self.values = list(values)
    def __add__(self, other):
        return Vector([a+b for a,b in zip(self.values, other.values)])
    def __sub__(self, other):
        return Vector([a-b for a,b in zip(self.values, other.values)])
    def dot(self, other):
        return sum(a*b for a,b in zip(self.values, other.values))
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass
class Vector:
    values: list
    def dot(self, other): return sum(a*b for a,b in zip(self.values, other.values))
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Check dimension mismatch handling.

### Q102: Implement immutable configuration object (variant)
1. **Problem statement**: Implement immutable configuration object (variant).
2. **Explanation**: Enforces safer runtime settings in ML services.
3. **Working Python code**:
```python
class Config:
    __slots__ = ('_data',)
    def __init__(self, **kwargs):
        object.__setattr__(self, '_data', dict(kwargs))
    def __getattr__(self, k):
        return self._data[k]
    def __setattr__(self, k, v):
        raise AttributeError('immutable')
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    host: str
    port: int
```
5. **Time complexity**: O(1).
6. **Space complexity**: O(n).
7. **Interview tip**: Immutability reduces side-effect bugs in production.

### Q103: Create custom iterator class for batched dataset (variant)
1. **Problem statement**: Create custom iterator class for batched dataset (variant).
2. **Explanation**: OOP + iterator protocol for training loops.
3. **Working Python code**:
```python
class BatchDataset:
    def __init__(self, data, batch_size):
        self.data = data; self.batch_size = batch_size
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        if self.i >= len(self.data): raise StopIteration
        j = self.i + self.batch_size
        batch = self.data[self.i:j]
        self.i = j
        return batch
```
4. **Alternate solution**:
```python
def batch_dataset(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i+batch_size]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(batch).
7. **Interview tip**: Clarify reset behavior for repeated iteration.

### Q104: Design a Vector class supporting +, -, and dot product (variant)
1. **Problem statement**: Design a Vector class supporting +, -, and dot product (variant).
2. **Explanation**: Demonstrates operator overloading and validation.
3. **Working Python code**:
```python
class Vector:
    def __init__(self, values):
        self.values = list(values)
    def __add__(self, other):
        return Vector([a+b for a,b in zip(self.values, other.values)])
    def __sub__(self, other):
        return Vector([a-b for a,b in zip(self.values, other.values)])
    def dot(self, other):
        return sum(a*b for a,b in zip(self.values, other.values))
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass
class Vector:
    values: list
    def dot(self, other): return sum(a*b for a,b in zip(self.values, other.values))
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Check dimension mismatch handling.

### Q105: Implement immutable configuration object (variant)
1. **Problem statement**: Implement immutable configuration object (variant).
2. **Explanation**: Enforces safer runtime settings in ML services.
3. **Working Python code**:
```python
class Config:
    __slots__ = ('_data',)
    def __init__(self, **kwargs):
        object.__setattr__(self, '_data', dict(kwargs))
    def __getattr__(self, k):
        return self._data[k]
    def __setattr__(self, k, v):
        raise AttributeError('immutable')
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    host: str
    port: int
```
5. **Time complexity**: O(1).
6. **Space complexity**: O(n).
7. **Interview tip**: Immutability reduces side-effect bugs in production.

### Q106: Create custom iterator class for batched dataset (variant)
1. **Problem statement**: Create custom iterator class for batched dataset (variant).
2. **Explanation**: OOP + iterator protocol for training loops.
3. **Working Python code**:
```python
class BatchDataset:
    def __init__(self, data, batch_size):
        self.data = data; self.batch_size = batch_size
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        if self.i >= len(self.data): raise StopIteration
        j = self.i + self.batch_size
        batch = self.data[self.i:j]
        self.i = j
        return batch
```
4. **Alternate solution**:
```python
def batch_dataset(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i+batch_size]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(batch).
7. **Interview tip**: Clarify reset behavior for repeated iteration.

### Q107: Design a Vector class supporting +, -, and dot product (variant)
1. **Problem statement**: Design a Vector class supporting +, -, and dot product (variant).
2. **Explanation**: Demonstrates operator overloading and validation.
3. **Working Python code**:
```python
class Vector:
    def __init__(self, values):
        self.values = list(values)
    def __add__(self, other):
        return Vector([a+b for a,b in zip(self.values, other.values)])
    def __sub__(self, other):
        return Vector([a-b for a,b in zip(self.values, other.values)])
    def dot(self, other):
        return sum(a*b for a,b in zip(self.values, other.values))
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass
class Vector:
    values: list
    def dot(self, other): return sum(a*b for a,b in zip(self.values, other.values))
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Check dimension mismatch handling.

### Q108: Implement immutable configuration object (variant)
1. **Problem statement**: Implement immutable configuration object (variant).
2. **Explanation**: Enforces safer runtime settings in ML services.
3. **Working Python code**:
```python
class Config:
    __slots__ = ('_data',)
    def __init__(self, **kwargs):
        object.__setattr__(self, '_data', dict(kwargs))
    def __getattr__(self, k):
        return self._data[k]
    def __setattr__(self, k, v):
        raise AttributeError('immutable')
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    host: str
    port: int
```
5. **Time complexity**: O(1).
6. **Space complexity**: O(n).
7. **Interview tip**: Immutability reduces side-effect bugs in production.

### Q109: Create custom iterator class for batched dataset (variant)
1. **Problem statement**: Create custom iterator class for batched dataset (variant).
2. **Explanation**: OOP + iterator protocol for training loops.
3. **Working Python code**:
```python
class BatchDataset:
    def __init__(self, data, batch_size):
        self.data = data; self.batch_size = batch_size
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        if self.i >= len(self.data): raise StopIteration
        j = self.i + self.batch_size
        batch = self.data[self.i:j]
        self.i = j
        return batch
```
4. **Alternate solution**:
```python
def batch_dataset(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i+batch_size]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(batch).
7. **Interview tip**: Clarify reset behavior for repeated iteration.

### Q110: Design a Vector class supporting +, -, and dot product (variant)
1. **Problem statement**: Design a Vector class supporting +, -, and dot product (variant).
2. **Explanation**: Demonstrates operator overloading and validation.
3. **Working Python code**:
```python
class Vector:
    def __init__(self, values):
        self.values = list(values)
    def __add__(self, other):
        return Vector([a+b for a,b in zip(self.values, other.values)])
    def __sub__(self, other):
        return Vector([a-b for a,b in zip(self.values, other.values)])
    def dot(self, other):
        return sum(a*b for a,b in zip(self.values, other.values))
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass
class Vector:
    values: list
    def dot(self, other): return sum(a*b for a,b in zip(self.values, other.values))
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Check dimension mismatch handling.

### Q111: Implement immutable configuration object (variant)
1. **Problem statement**: Implement immutable configuration object (variant).
2. **Explanation**: Enforces safer runtime settings in ML services.
3. **Working Python code**:
```python
class Config:
    __slots__ = ('_data',)
    def __init__(self, **kwargs):
        object.__setattr__(self, '_data', dict(kwargs))
    def __getattr__(self, k):
        return self._data[k]
    def __setattr__(self, k, v):
        raise AttributeError('immutable')
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    host: str
    port: int
```
5. **Time complexity**: O(1).
6. **Space complexity**: O(n).
7. **Interview tip**: Immutability reduces side-effect bugs in production.

### Q112: Create custom iterator class for batched dataset (variant)
1. **Problem statement**: Create custom iterator class for batched dataset (variant).
2. **Explanation**: OOP + iterator protocol for training loops.
3. **Working Python code**:
```python
class BatchDataset:
    def __init__(self, data, batch_size):
        self.data = data; self.batch_size = batch_size
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        if self.i >= len(self.data): raise StopIteration
        j = self.i + self.batch_size
        batch = self.data[self.i:j]
        self.i = j
        return batch
```
4. **Alternate solution**:
```python
def batch_dataset(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i+batch_size]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(batch).
7. **Interview tip**: Clarify reset behavior for repeated iteration.

### Q113: Design a Vector class supporting +, -, and dot product (variant)
1. **Problem statement**: Design a Vector class supporting +, -, and dot product (variant).
2. **Explanation**: Demonstrates operator overloading and validation.
3. **Working Python code**:
```python
class Vector:
    def __init__(self, values):
        self.values = list(values)
    def __add__(self, other):
        return Vector([a+b for a,b in zip(self.values, other.values)])
    def __sub__(self, other):
        return Vector([a-b for a,b in zip(self.values, other.values)])
    def dot(self, other):
        return sum(a*b for a,b in zip(self.values, other.values))
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass
class Vector:
    values: list
    def dot(self, other): return sum(a*b for a,b in zip(self.values, other.values))
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Check dimension mismatch handling.

## Advanced Python

### Q114: Build context manager that temporarily sets environment variable
1. **Problem statement**: Build context manager that temporarily sets environment variable.
2. **Explanation**: Useful in tests and experiment isolation.
3. **Working Python code**:
```python
import os

class temp_env:
    def __init__(self, key, value):
        self.key, self.value = key, value
    def __enter__(self):
        self.old = os.environ.get(self.key)
        os.environ[self.key] = self.value
    def __exit__(self, exc_type, exc, tb):
        if self.old is None: os.environ.pop(self.key, None)
        else: os.environ[self.key] = self.old
```
4. **Alternate solution**:
```python
from contextlib import contextmanager
import os

@contextmanager
def temp_env(key, value):
    old = os.environ.get(key)
    os.environ[key] = value
    try: yield
    finally:
        if old is None: os.environ.pop(key, None)
        else: os.environ[key] = old
```
5. **Time complexity**: O(1).
6. **Space complexity**: O(1).
7. **Interview tip**: Always restore state in finally block.

### Q115: Run CPU-bound work in ProcessPool
1. **Problem statement**: Run CPU-bound work in ProcessPool.
2. **Explanation**: Tests concurrency model understanding.
3. **Working Python code**:
```python
from concurrent.futures import ProcessPoolExecutor

def square_all(nums):
    with ProcessPoolExecutor() as ex:
        return list(ex.map(lambda x: x*x, nums))
```
4. **Alternate solution**:
```python
def square_all(nums):
    return [x*x for x in nums]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Explain pickling cost and GIL considerations.

### Q116: Implement producer-consumer with asyncio.Queue
1. **Problem statement**: Implement producer-consumer with asyncio.Queue.
2. **Explanation**: Async interview scenario for stream processing.
3. **Working Python code**:
```python
import asyncio

async def producer(q, items):
    for it in items:
        await q.put(it)
    await q.put(None)

async def consumer(q):
    out = []
    while True:
        item = await q.get()
        if item is None:
            break
        out.append(item * 2)
    return out
```
4. **Alternate solution**:
```python
async def consume_all(items):
    return [x*2 for x in items]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Discuss backpressure and queue size limits.

### Q117: Build context manager that temporarily sets environment variable (variant)
1. **Problem statement**: Build context manager that temporarily sets environment variable (variant).
2. **Explanation**: Useful in tests and experiment isolation.
3. **Working Python code**:
```python
import os

class temp_env:
    def __init__(self, key, value):
        self.key, self.value = key, value
    def __enter__(self):
        self.old = os.environ.get(self.key)
        os.environ[self.key] = self.value
    def __exit__(self, exc_type, exc, tb):
        if self.old is None: os.environ.pop(self.key, None)
        else: os.environ[self.key] = self.old
```
4. **Alternate solution**:
```python
from contextlib import contextmanager
import os

@contextmanager
def temp_env(key, value):
    old = os.environ.get(key)
    os.environ[key] = value
    try: yield
    finally:
        if old is None: os.environ.pop(key, None)
        else: os.environ[key] = old
```
5. **Time complexity**: O(1).
6. **Space complexity**: O(1).
7. **Interview tip**: Always restore state in finally block.

### Q118: Run CPU-bound work in ProcessPool (variant)
1. **Problem statement**: Run CPU-bound work in ProcessPool (variant).
2. **Explanation**: Tests concurrency model understanding.
3. **Working Python code**:
```python
from concurrent.futures import ProcessPoolExecutor

def square_all(nums):
    with ProcessPoolExecutor() as ex:
        return list(ex.map(lambda x: x*x, nums))
```
4. **Alternate solution**:
```python
def square_all(nums):
    return [x*x for x in nums]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Explain pickling cost and GIL considerations.

### Q119: Implement producer-consumer with asyncio.Queue (variant)
1. **Problem statement**: Implement producer-consumer with asyncio.Queue (variant).
2. **Explanation**: Async interview scenario for stream processing.
3. **Working Python code**:
```python
import asyncio

async def producer(q, items):
    for it in items:
        await q.put(it)
    await q.put(None)

async def consumer(q):
    out = []
    while True:
        item = await q.get()
        if item is None:
            break
        out.append(item * 2)
    return out
```
4. **Alternate solution**:
```python
async def consume_all(items):
    return [x*2 for x in items]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Discuss backpressure and queue size limits.

### Q120: Build context manager that temporarily sets environment variable (variant)
1. **Problem statement**: Build context manager that temporarily sets environment variable (variant).
2. **Explanation**: Useful in tests and experiment isolation.
3. **Working Python code**:
```python
import os

class temp_env:
    def __init__(self, key, value):
        self.key, self.value = key, value
    def __enter__(self):
        self.old = os.environ.get(self.key)
        os.environ[self.key] = self.value
    def __exit__(self, exc_type, exc, tb):
        if self.old is None: os.environ.pop(self.key, None)
        else: os.environ[self.key] = self.old
```
4. **Alternate solution**:
```python
from contextlib import contextmanager
import os

@contextmanager
def temp_env(key, value):
    old = os.environ.get(key)
    os.environ[key] = value
    try: yield
    finally:
        if old is None: os.environ.pop(key, None)
        else: os.environ[key] = old
```
5. **Time complexity**: O(1).
6. **Space complexity**: O(1).
7. **Interview tip**: Always restore state in finally block.

### Q121: Run CPU-bound work in ProcessPool (variant)
1. **Problem statement**: Run CPU-bound work in ProcessPool (variant).
2. **Explanation**: Tests concurrency model understanding.
3. **Working Python code**:
```python
from concurrent.futures import ProcessPoolExecutor

def square_all(nums):
    with ProcessPoolExecutor() as ex:
        return list(ex.map(lambda x: x*x, nums))
```
4. **Alternate solution**:
```python
def square_all(nums):
    return [x*x for x in nums]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Explain pickling cost and GIL considerations.

### Q122: Implement producer-consumer with asyncio.Queue (variant)
1. **Problem statement**: Implement producer-consumer with asyncio.Queue (variant).
2. **Explanation**: Async interview scenario for stream processing.
3. **Working Python code**:
```python
import asyncio

async def producer(q, items):
    for it in items:
        await q.put(it)
    await q.put(None)

async def consumer(q):
    out = []
    while True:
        item = await q.get()
        if item is None:
            break
        out.append(item * 2)
    return out
```
4. **Alternate solution**:
```python
async def consume_all(items):
    return [x*2 for x in items]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Discuss backpressure and queue size limits.

### Q123: Build context manager that temporarily sets environment variable (variant)
1. **Problem statement**: Build context manager that temporarily sets environment variable (variant).
2. **Explanation**: Useful in tests and experiment isolation.
3. **Working Python code**:
```python
import os

class temp_env:
    def __init__(self, key, value):
        self.key, self.value = key, value
    def __enter__(self):
        self.old = os.environ.get(self.key)
        os.environ[self.key] = self.value
    def __exit__(self, exc_type, exc, tb):
        if self.old is None: os.environ.pop(self.key, None)
        else: os.environ[self.key] = self.old
```
4. **Alternate solution**:
```python
from contextlib import contextmanager
import os

@contextmanager
def temp_env(key, value):
    old = os.environ.get(key)
    os.environ[key] = value
    try: yield
    finally:
        if old is None: os.environ.pop(key, None)
        else: os.environ[key] = old
```
5. **Time complexity**: O(1).
6. **Space complexity**: O(1).
7. **Interview tip**: Always restore state in finally block.

### Q124: Run CPU-bound work in ProcessPool (variant)
1. **Problem statement**: Run CPU-bound work in ProcessPool (variant).
2. **Explanation**: Tests concurrency model understanding.
3. **Working Python code**:
```python
from concurrent.futures import ProcessPoolExecutor

def square_all(nums):
    with ProcessPoolExecutor() as ex:
        return list(ex.map(lambda x: x*x, nums))
```
4. **Alternate solution**:
```python
def square_all(nums):
    return [x*x for x in nums]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Explain pickling cost and GIL considerations.

### Q125: Implement producer-consumer with asyncio.Queue (variant)
1. **Problem statement**: Implement producer-consumer with asyncio.Queue (variant).
2. **Explanation**: Async interview scenario for stream processing.
3. **Working Python code**:
```python
import asyncio

async def producer(q, items):
    for it in items:
        await q.put(it)
    await q.put(None)

async def consumer(q):
    out = []
    while True:
        item = await q.get()
        if item is None:
            break
        out.append(item * 2)
    return out
```
4. **Alternate solution**:
```python
async def consume_all(items):
    return [x*2 for x in items]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Discuss backpressure and queue size limits.

### Q126: Build context manager that temporarily sets environment variable (variant)
1. **Problem statement**: Build context manager that temporarily sets environment variable (variant).
2. **Explanation**: Useful in tests and experiment isolation.
3. **Working Python code**:
```python
import os

class temp_env:
    def __init__(self, key, value):
        self.key, self.value = key, value
    def __enter__(self):
        self.old = os.environ.get(self.key)
        os.environ[self.key] = self.value
    def __exit__(self, exc_type, exc, tb):
        if self.old is None: os.environ.pop(self.key, None)
        else: os.environ[self.key] = self.old
```
4. **Alternate solution**:
```python
from contextlib import contextmanager
import os

@contextmanager
def temp_env(key, value):
    old = os.environ.get(key)
    os.environ[key] = value
    try: yield
    finally:
        if old is None: os.environ.pop(key, None)
        else: os.environ[key] = old
```
5. **Time complexity**: O(1).
6. **Space complexity**: O(1).
7. **Interview tip**: Always restore state in finally block.

### Q127: Run CPU-bound work in ProcessPool (variant)
1. **Problem statement**: Run CPU-bound work in ProcessPool (variant).
2. **Explanation**: Tests concurrency model understanding.
3. **Working Python code**:
```python
from concurrent.futures import ProcessPoolExecutor

def square_all(nums):
    with ProcessPoolExecutor() as ex:
        return list(ex.map(lambda x: x*x, nums))
```
4. **Alternate solution**:
```python
def square_all(nums):
    return [x*x for x in nums]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Explain pickling cost and GIL considerations.

### Q128: Implement producer-consumer with asyncio.Queue (variant)
1. **Problem statement**: Implement producer-consumer with asyncio.Queue (variant).
2. **Explanation**: Async interview scenario for stream processing.
3. **Working Python code**:
```python
import asyncio

async def producer(q, items):
    for it in items:
        await q.put(it)
    await q.put(None)

async def consumer(q):
    out = []
    while True:
        item = await q.get()
        if item is None:
            break
        out.append(item * 2)
    return out
```
4. **Alternate solution**:
```python
async def consume_all(items):
    return [x*2 for x in items]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Discuss backpressure and queue size limits.

### Q129: Build context manager that temporarily sets environment variable (variant)
1. **Problem statement**: Build context manager that temporarily sets environment variable (variant).
2. **Explanation**: Useful in tests and experiment isolation.
3. **Working Python code**:
```python
import os

class temp_env:
    def __init__(self, key, value):
        self.key, self.value = key, value
    def __enter__(self):
        self.old = os.environ.get(self.key)
        os.environ[self.key] = self.value
    def __exit__(self, exc_type, exc, tb):
        if self.old is None: os.environ.pop(self.key, None)
        else: os.environ[self.key] = self.old
```
4. **Alternate solution**:
```python
from contextlib import contextmanager
import os

@contextmanager
def temp_env(key, value):
    old = os.environ.get(key)
    os.environ[key] = value
    try: yield
    finally:
        if old is None: os.environ.pop(key, None)
        else: os.environ[key] = old
```
5. **Time complexity**: O(1).
6. **Space complexity**: O(1).
7. **Interview tip**: Always restore state in finally block.

### Q130: Run CPU-bound work in ProcessPool (variant)
1. **Problem statement**: Run CPU-bound work in ProcessPool (variant).
2. **Explanation**: Tests concurrency model understanding.
3. **Working Python code**:
```python
from concurrent.futures import ProcessPoolExecutor

def square_all(nums):
    with ProcessPoolExecutor() as ex:
        return list(ex.map(lambda x: x*x, nums))
```
4. **Alternate solution**:
```python
def square_all(nums):
    return [x*x for x in nums]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Explain pickling cost and GIL considerations.

### Q131: Implement producer-consumer with asyncio.Queue (variant)
1. **Problem statement**: Implement producer-consumer with asyncio.Queue (variant).
2. **Explanation**: Async interview scenario for stream processing.
3. **Working Python code**:
```python
import asyncio

async def producer(q, items):
    for it in items:
        await q.put(it)
    await q.put(None)

async def consumer(q):
    out = []
    while True:
        item = await q.get()
        if item is None:
            break
        out.append(item * 2)
    return out
```
4. **Alternate solution**:
```python
async def consume_all(items):
    return [x*2 for x in items]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Discuss backpressure and queue size limits.

### Q132: Build context manager that temporarily sets environment variable (variant)
1. **Problem statement**: Build context manager that temporarily sets environment variable (variant).
2. **Explanation**: Useful in tests and experiment isolation.
3. **Working Python code**:
```python
import os

class temp_env:
    def __init__(self, key, value):
        self.key, self.value = key, value
    def __enter__(self):
        self.old = os.environ.get(self.key)
        os.environ[self.key] = self.value
    def __exit__(self, exc_type, exc, tb):
        if self.old is None: os.environ.pop(self.key, None)
        else: os.environ[self.key] = self.old
```
4. **Alternate solution**:
```python
from contextlib import contextmanager
import os

@contextmanager
def temp_env(key, value):
    old = os.environ.get(key)
    os.environ[key] = value
    try: yield
    finally:
        if old is None: os.environ.pop(key, None)
        else: os.environ[key] = old
```
5. **Time complexity**: O(1).
6. **Space complexity**: O(1).
7. **Interview tip**: Always restore state in finally block.

### Q133: Run CPU-bound work in ProcessPool (variant)
1. **Problem statement**: Run CPU-bound work in ProcessPool (variant).
2. **Explanation**: Tests concurrency model understanding.
3. **Working Python code**:
```python
from concurrent.futures import ProcessPoolExecutor

def square_all(nums):
    with ProcessPoolExecutor() as ex:
        return list(ex.map(lambda x: x*x, nums))
```
4. **Alternate solution**:
```python
def square_all(nums):
    return [x*x for x in nums]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Explain pickling cost and GIL considerations.

### Q134: Implement producer-consumer with asyncio.Queue (variant)
1. **Problem statement**: Implement producer-consumer with asyncio.Queue (variant).
2. **Explanation**: Async interview scenario for stream processing.
3. **Working Python code**:
```python
import asyncio

async def producer(q, items):
    for it in items:
        await q.put(it)
    await q.put(None)

async def consumer(q):
    out = []
    while True:
        item = await q.get()
        if item is None:
            break
        out.append(item * 2)
    return out
```
4. **Alternate solution**:
```python
async def consume_all(items):
    return [x*2 for x in items]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Discuss backpressure and queue size limits.

### Q135: Build context manager that temporarily sets environment variable (variant)
1. **Problem statement**: Build context manager that temporarily sets environment variable (variant).
2. **Explanation**: Useful in tests and experiment isolation.
3. **Working Python code**:
```python
import os

class temp_env:
    def __init__(self, key, value):
        self.key, self.value = key, value
    def __enter__(self):
        self.old = os.environ.get(self.key)
        os.environ[self.key] = self.value
    def __exit__(self, exc_type, exc, tb):
        if self.old is None: os.environ.pop(self.key, None)
        else: os.environ[self.key] = self.old
```
4. **Alternate solution**:
```python
from contextlib import contextmanager
import os

@contextmanager
def temp_env(key, value):
    old = os.environ.get(key)
    os.environ[key] = value
    try: yield
    finally:
        if old is None: os.environ.pop(key, None)
        else: os.environ[key] = old
```
5. **Time complexity**: O(1).
6. **Space complexity**: O(1).
7. **Interview tip**: Always restore state in finally block.

### Q136: Run CPU-bound work in ProcessPool (variant)
1. **Problem statement**: Run CPU-bound work in ProcessPool (variant).
2. **Explanation**: Tests concurrency model understanding.
3. **Working Python code**:
```python
from concurrent.futures import ProcessPoolExecutor

def square_all(nums):
    with ProcessPoolExecutor() as ex:
        return list(ex.map(lambda x: x*x, nums))
```
4. **Alternate solution**:
```python
def square_all(nums):
    return [x*x for x in nums]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Explain pickling cost and GIL considerations.

### Q137: Implement producer-consumer with asyncio.Queue (variant)
1. **Problem statement**: Implement producer-consumer with asyncio.Queue (variant).
2. **Explanation**: Async interview scenario for stream processing.
3. **Working Python code**:
```python
import asyncio

async def producer(q, items):
    for it in items:
        await q.put(it)
    await q.put(None)

async def consumer(q):
    out = []
    while True:
        item = await q.get()
        if item is None:
            break
        out.append(item * 2)
    return out
```
4. **Alternate solution**:
```python
async def consume_all(items):
    return [x*2 for x in items]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Discuss backpressure and queue size limits.

### Q138: Build context manager that temporarily sets environment variable (variant)
1. **Problem statement**: Build context manager that temporarily sets environment variable (variant).
2. **Explanation**: Useful in tests and experiment isolation.
3. **Working Python code**:
```python
import os

class temp_env:
    def __init__(self, key, value):
        self.key, self.value = key, value
    def __enter__(self):
        self.old = os.environ.get(self.key)
        os.environ[self.key] = self.value
    def __exit__(self, exc_type, exc, tb):
        if self.old is None: os.environ.pop(self.key, None)
        else: os.environ[self.key] = self.old
```
4. **Alternate solution**:
```python
from contextlib import contextmanager
import os

@contextmanager
def temp_env(key, value):
    old = os.environ.get(key)
    os.environ[key] = value
    try: yield
    finally:
        if old is None: os.environ.pop(key, None)
        else: os.environ[key] = old
```
5. **Time complexity**: O(1).
6. **Space complexity**: O(1).
7. **Interview tip**: Always restore state in finally block.

### Q139: Run CPU-bound work in ProcessPool (variant)
1. **Problem statement**: Run CPU-bound work in ProcessPool (variant).
2. **Explanation**: Tests concurrency model understanding.
3. **Working Python code**:
```python
from concurrent.futures import ProcessPoolExecutor

def square_all(nums):
    with ProcessPoolExecutor() as ex:
        return list(ex.map(lambda x: x*x, nums))
```
4. **Alternate solution**:
```python
def square_all(nums):
    return [x*x for x in nums]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Explain pickling cost and GIL considerations.

### Q140: Implement producer-consumer with asyncio.Queue (variant)
1. **Problem statement**: Implement producer-consumer with asyncio.Queue (variant).
2. **Explanation**: Async interview scenario for stream processing.
3. **Working Python code**:
```python
import asyncio

async def producer(q, items):
    for it in items:
        await q.put(it)
    await q.put(None)

async def consumer(q):
    out = []
    while True:
        item = await q.get()
        if item is None:
            break
        out.append(item * 2)
    return out
```
4. **Alternate solution**:
```python
async def consume_all(items):
    return [x*2 for x in items]
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Discuss backpressure and queue size limits.

### Q141: Build context manager that temporarily sets environment variable (variant)
1. **Problem statement**: Build context manager that temporarily sets environment variable (variant).
2. **Explanation**: Useful in tests and experiment isolation.
3. **Working Python code**:
```python
import os

class temp_env:
    def __init__(self, key, value):
        self.key, self.value = key, value
    def __enter__(self):
        self.old = os.environ.get(self.key)
        os.environ[self.key] = self.value
    def __exit__(self, exc_type, exc, tb):
        if self.old is None: os.environ.pop(self.key, None)
        else: os.environ[self.key] = self.old
```
4. **Alternate solution**:
```python
from contextlib import contextmanager
import os

@contextmanager
def temp_env(key, value):
    old = os.environ.get(key)
    os.environ[key] = value
    try: yield
    finally:
        if old is None: os.environ.pop(key, None)
        else: os.environ[key] = old
```
5. **Time complexity**: O(1).
6. **Space complexity**: O(1).
7. **Interview tip**: Always restore state in finally block.

## NumPy

### Q142: Vectorized z-score normalization by column
1. **Problem statement**: Vectorized z-score normalization by column.
2. **Explanation**: Standard preprocessing for many ML models.
3. **Working Python code**:
```python
import numpy as np

def zscore(X):
    mu = X.mean(axis=0)
    sd = X.std(axis=0)
    sd = np.where(sd==0, 1, sd)
    return (X - mu) / sd
```
4. **Alternate solution**:
```python
import numpy as np

def zscore(X):
    out = X.astype(float).copy()
    for j in range(X.shape[1]):
        m, s = X[:,j].mean(), X[:,j].std()
        out[:,j] = 0 if s==0 else (X[:,j]-m)/s
    return out
```
5. **Time complexity**: O(n*m).
6. **Space complexity**: O(n*m).
7. **Interview tip**: Mention dtype upcasting to float.

### Q143: Compute cosine similarity matrix between row vectors
1. **Problem statement**: Compute cosine similarity matrix between row vectors.
2. **Explanation**: Core in retrieval and recommendation systems.
3. **Working Python code**:
```python
import numpy as np

def cosine_matrix(X):
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    norms = np.where(norms == 0, 1, norms)
    Xn = X / norms
    return Xn @ Xn.T
```
4. **Alternate solution**:
```python
import numpy as np

def cosine_matrix(X):
    n = X.shape[0]
    out = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            a,b = X[i], X[j]
            den = (np.linalg.norm(a)*np.linalg.norm(b)) or 1
            out[i,j] = a.dot(b)/den
    return out
```
5. **Time complexity**: O(n^2*d).
6. **Space complexity**: O(n^2).
7. **Interview tip**: Discuss memory growth for large n.

### Q144: One-hot encode integer labels
1. **Problem statement**: One-hot encode integer labels.
2. **Explanation**: Common preprocessing for categorical targets.
3. **Working Python code**:
```python
import numpy as np

def one_hot(y, num_classes=None):
    y = np.asarray(y, dtype=int)
    c = num_classes or (y.max()+1)
    out = np.zeros((len(y), c), dtype=int)
    out[np.arange(len(y)), y] = 1
    return out
```
4. **Alternate solution**:
```python
import numpy as np

def one_hot(y, num_classes=None):
    y = np.asarray(y, dtype=int)
    c = num_classes or (max(y)+1)
    return np.eye(c, dtype=int)[y]
```
5. **Time complexity**: O(n*c).
6. **Space complexity**: O(n*c).
7. **Interview tip**: Validate labels are in range [0, c).

### Q145: Vectorized z-score normalization by column (variant)
1. **Problem statement**: Vectorized z-score normalization by column (variant).
2. **Explanation**: Standard preprocessing for many ML models.
3. **Working Python code**:
```python
import numpy as np

def zscore(X):
    mu = X.mean(axis=0)
    sd = X.std(axis=0)
    sd = np.where(sd==0, 1, sd)
    return (X - mu) / sd
```
4. **Alternate solution**:
```python
import numpy as np

def zscore(X):
    out = X.astype(float).copy()
    for j in range(X.shape[1]):
        m, s = X[:,j].mean(), X[:,j].std()
        out[:,j] = 0 if s==0 else (X[:,j]-m)/s
    return out
```
5. **Time complexity**: O(n*m).
6. **Space complexity**: O(n*m).
7. **Interview tip**: Mention dtype upcasting to float.

### Q146: Compute cosine similarity matrix between row vectors (variant)
1. **Problem statement**: Compute cosine similarity matrix between row vectors (variant).
2. **Explanation**: Core in retrieval and recommendation systems.
3. **Working Python code**:
```python
import numpy as np

def cosine_matrix(X):
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    norms = np.where(norms == 0, 1, norms)
    Xn = X / norms
    return Xn @ Xn.T
```
4. **Alternate solution**:
```python
import numpy as np

def cosine_matrix(X):
    n = X.shape[0]
    out = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            a,b = X[i], X[j]
            den = (np.linalg.norm(a)*np.linalg.norm(b)) or 1
            out[i,j] = a.dot(b)/den
    return out
```
5. **Time complexity**: O(n^2*d).
6. **Space complexity**: O(n^2).
7. **Interview tip**: Discuss memory growth for large n.

### Q147: One-hot encode integer labels (variant)
1. **Problem statement**: One-hot encode integer labels (variant).
2. **Explanation**: Common preprocessing for categorical targets.
3. **Working Python code**:
```python
import numpy as np

def one_hot(y, num_classes=None):
    y = np.asarray(y, dtype=int)
    c = num_classes or (y.max()+1)
    out = np.zeros((len(y), c), dtype=int)
    out[np.arange(len(y)), y] = 1
    return out
```
4. **Alternate solution**:
```python
import numpy as np

def one_hot(y, num_classes=None):
    y = np.asarray(y, dtype=int)
    c = num_classes or (max(y)+1)
    return np.eye(c, dtype=int)[y]
```
5. **Time complexity**: O(n*c).
6. **Space complexity**: O(n*c).
7. **Interview tip**: Validate labels are in range [0, c).

### Q148: Vectorized z-score normalization by column (variant)
1. **Problem statement**: Vectorized z-score normalization by column (variant).
2. **Explanation**: Standard preprocessing for many ML models.
3. **Working Python code**:
```python
import numpy as np

def zscore(X):
    mu = X.mean(axis=0)
    sd = X.std(axis=0)
    sd = np.where(sd==0, 1, sd)
    return (X - mu) / sd
```
4. **Alternate solution**:
```python
import numpy as np

def zscore(X):
    out = X.astype(float).copy()
    for j in range(X.shape[1]):
        m, s = X[:,j].mean(), X[:,j].std()
        out[:,j] = 0 if s==0 else (X[:,j]-m)/s
    return out
```
5. **Time complexity**: O(n*m).
6. **Space complexity**: O(n*m).
7. **Interview tip**: Mention dtype upcasting to float.

### Q149: Compute cosine similarity matrix between row vectors (variant)
1. **Problem statement**: Compute cosine similarity matrix between row vectors (variant).
2. **Explanation**: Core in retrieval and recommendation systems.
3. **Working Python code**:
```python
import numpy as np

def cosine_matrix(X):
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    norms = np.where(norms == 0, 1, norms)
    Xn = X / norms
    return Xn @ Xn.T
```
4. **Alternate solution**:
```python
import numpy as np

def cosine_matrix(X):
    n = X.shape[0]
    out = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            a,b = X[i], X[j]
            den = (np.linalg.norm(a)*np.linalg.norm(b)) or 1
            out[i,j] = a.dot(b)/den
    return out
```
5. **Time complexity**: O(n^2*d).
6. **Space complexity**: O(n^2).
7. **Interview tip**: Discuss memory growth for large n.

### Q150: One-hot encode integer labels (variant)
1. **Problem statement**: One-hot encode integer labels (variant).
2. **Explanation**: Common preprocessing for categorical targets.
3. **Working Python code**:
```python
import numpy as np

def one_hot(y, num_classes=None):
    y = np.asarray(y, dtype=int)
    c = num_classes or (y.max()+1)
    out = np.zeros((len(y), c), dtype=int)
    out[np.arange(len(y)), y] = 1
    return out
```
4. **Alternate solution**:
```python
import numpy as np

def one_hot(y, num_classes=None):
    y = np.asarray(y, dtype=int)
    c = num_classes or (max(y)+1)
    return np.eye(c, dtype=int)[y]
```
5. **Time complexity**: O(n*c).
6. **Space complexity**: O(n*c).
7. **Interview tip**: Validate labels are in range [0, c).

### Q151: Vectorized z-score normalization by column (variant)
1. **Problem statement**: Vectorized z-score normalization by column (variant).
2. **Explanation**: Standard preprocessing for many ML models.
3. **Working Python code**:
```python
import numpy as np

def zscore(X):
    mu = X.mean(axis=0)
    sd = X.std(axis=0)
    sd = np.where(sd==0, 1, sd)
    return (X - mu) / sd
```
4. **Alternate solution**:
```python
import numpy as np

def zscore(X):
    out = X.astype(float).copy()
    for j in range(X.shape[1]):
        m, s = X[:,j].mean(), X[:,j].std()
        out[:,j] = 0 if s==0 else (X[:,j]-m)/s
    return out
```
5. **Time complexity**: O(n*m).
6. **Space complexity**: O(n*m).
7. **Interview tip**: Mention dtype upcasting to float.

### Q152: Compute cosine similarity matrix between row vectors (variant)
1. **Problem statement**: Compute cosine similarity matrix between row vectors (variant).
2. **Explanation**: Core in retrieval and recommendation systems.
3. **Working Python code**:
```python
import numpy as np

def cosine_matrix(X):
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    norms = np.where(norms == 0, 1, norms)
    Xn = X / norms
    return Xn @ Xn.T
```
4. **Alternate solution**:
```python
import numpy as np

def cosine_matrix(X):
    n = X.shape[0]
    out = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            a,b = X[i], X[j]
            den = (np.linalg.norm(a)*np.linalg.norm(b)) or 1
            out[i,j] = a.dot(b)/den
    return out
```
5. **Time complexity**: O(n^2*d).
6. **Space complexity**: O(n^2).
7. **Interview tip**: Discuss memory growth for large n.

### Q153: One-hot encode integer labels (variant)
1. **Problem statement**: One-hot encode integer labels (variant).
2. **Explanation**: Common preprocessing for categorical targets.
3. **Working Python code**:
```python
import numpy as np

def one_hot(y, num_classes=None):
    y = np.asarray(y, dtype=int)
    c = num_classes or (y.max()+1)
    out = np.zeros((len(y), c), dtype=int)
    out[np.arange(len(y)), y] = 1
    return out
```
4. **Alternate solution**:
```python
import numpy as np

def one_hot(y, num_classes=None):
    y = np.asarray(y, dtype=int)
    c = num_classes or (max(y)+1)
    return np.eye(c, dtype=int)[y]
```
5. **Time complexity**: O(n*c).
6. **Space complexity**: O(n*c).
7. **Interview tip**: Validate labels are in range [0, c).

### Q154: Vectorized z-score normalization by column (variant)
1. **Problem statement**: Vectorized z-score normalization by column (variant).
2. **Explanation**: Standard preprocessing for many ML models.
3. **Working Python code**:
```python
import numpy as np

def zscore(X):
    mu = X.mean(axis=0)
    sd = X.std(axis=0)
    sd = np.where(sd==0, 1, sd)
    return (X - mu) / sd
```
4. **Alternate solution**:
```python
import numpy as np

def zscore(X):
    out = X.astype(float).copy()
    for j in range(X.shape[1]):
        m, s = X[:,j].mean(), X[:,j].std()
        out[:,j] = 0 if s==0 else (X[:,j]-m)/s
    return out
```
5. **Time complexity**: O(n*m).
6. **Space complexity**: O(n*m).
7. **Interview tip**: Mention dtype upcasting to float.

### Q155: Compute cosine similarity matrix between row vectors (variant)
1. **Problem statement**: Compute cosine similarity matrix between row vectors (variant).
2. **Explanation**: Core in retrieval and recommendation systems.
3. **Working Python code**:
```python
import numpy as np

def cosine_matrix(X):
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    norms = np.where(norms == 0, 1, norms)
    Xn = X / norms
    return Xn @ Xn.T
```
4. **Alternate solution**:
```python
import numpy as np

def cosine_matrix(X):
    n = X.shape[0]
    out = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            a,b = X[i], X[j]
            den = (np.linalg.norm(a)*np.linalg.norm(b)) or 1
            out[i,j] = a.dot(b)/den
    return out
```
5. **Time complexity**: O(n^2*d).
6. **Space complexity**: O(n^2).
7. **Interview tip**: Discuss memory growth for large n.

### Q156: One-hot encode integer labels (variant)
1. **Problem statement**: One-hot encode integer labels (variant).
2. **Explanation**: Common preprocessing for categorical targets.
3. **Working Python code**:
```python
import numpy as np

def one_hot(y, num_classes=None):
    y = np.asarray(y, dtype=int)
    c = num_classes or (y.max()+1)
    out = np.zeros((len(y), c), dtype=int)
    out[np.arange(len(y)), y] = 1
    return out
```
4. **Alternate solution**:
```python
import numpy as np

def one_hot(y, num_classes=None):
    y = np.asarray(y, dtype=int)
    c = num_classes or (max(y)+1)
    return np.eye(c, dtype=int)[y]
```
5. **Time complexity**: O(n*c).
6. **Space complexity**: O(n*c).
7. **Interview tip**: Validate labels are in range [0, c).

### Q157: Vectorized z-score normalization by column (variant)
1. **Problem statement**: Vectorized z-score normalization by column (variant).
2. **Explanation**: Standard preprocessing for many ML models.
3. **Working Python code**:
```python
import numpy as np

def zscore(X):
    mu = X.mean(axis=0)
    sd = X.std(axis=0)
    sd = np.where(sd==0, 1, sd)
    return (X - mu) / sd
```
4. **Alternate solution**:
```python
import numpy as np

def zscore(X):
    out = X.astype(float).copy()
    for j in range(X.shape[1]):
        m, s = X[:,j].mean(), X[:,j].std()
        out[:,j] = 0 if s==0 else (X[:,j]-m)/s
    return out
```
5. **Time complexity**: O(n*m).
6. **Space complexity**: O(n*m).
7. **Interview tip**: Mention dtype upcasting to float.

### Q158: Compute cosine similarity matrix between row vectors (variant)
1. **Problem statement**: Compute cosine similarity matrix between row vectors (variant).
2. **Explanation**: Core in retrieval and recommendation systems.
3. **Working Python code**:
```python
import numpy as np

def cosine_matrix(X):
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    norms = np.where(norms == 0, 1, norms)
    Xn = X / norms
    return Xn @ Xn.T
```
4. **Alternate solution**:
```python
import numpy as np

def cosine_matrix(X):
    n = X.shape[0]
    out = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            a,b = X[i], X[j]
            den = (np.linalg.norm(a)*np.linalg.norm(b)) or 1
            out[i,j] = a.dot(b)/den
    return out
```
5. **Time complexity**: O(n^2*d).
6. **Space complexity**: O(n^2).
7. **Interview tip**: Discuss memory growth for large n.

### Q159: One-hot encode integer labels (variant)
1. **Problem statement**: One-hot encode integer labels (variant).
2. **Explanation**: Common preprocessing for categorical targets.
3. **Working Python code**:
```python
import numpy as np

def one_hot(y, num_classes=None):
    y = np.asarray(y, dtype=int)
    c = num_classes or (y.max()+1)
    out = np.zeros((len(y), c), dtype=int)
    out[np.arange(len(y)), y] = 1
    return out
```
4. **Alternate solution**:
```python
import numpy as np

def one_hot(y, num_classes=None):
    y = np.asarray(y, dtype=int)
    c = num_classes or (max(y)+1)
    return np.eye(c, dtype=int)[y]
```
5. **Time complexity**: O(n*c).
6. **Space complexity**: O(n*c).
7. **Interview tip**: Validate labels are in range [0, c).

### Q160: Vectorized z-score normalization by column (variant)
1. **Problem statement**: Vectorized z-score normalization by column (variant).
2. **Explanation**: Standard preprocessing for many ML models.
3. **Working Python code**:
```python
import numpy as np

def zscore(X):
    mu = X.mean(axis=0)
    sd = X.std(axis=0)
    sd = np.where(sd==0, 1, sd)
    return (X - mu) / sd
```
4. **Alternate solution**:
```python
import numpy as np

def zscore(X):
    out = X.astype(float).copy()
    for j in range(X.shape[1]):
        m, s = X[:,j].mean(), X[:,j].std()
        out[:,j] = 0 if s==0 else (X[:,j]-m)/s
    return out
```
5. **Time complexity**: O(n*m).
6. **Space complexity**: O(n*m).
7. **Interview tip**: Mention dtype upcasting to float.

### Q161: Compute cosine similarity matrix between row vectors (variant)
1. **Problem statement**: Compute cosine similarity matrix between row vectors (variant).
2. **Explanation**: Core in retrieval and recommendation systems.
3. **Working Python code**:
```python
import numpy as np

def cosine_matrix(X):
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    norms = np.where(norms == 0, 1, norms)
    Xn = X / norms
    return Xn @ Xn.T
```
4. **Alternate solution**:
```python
import numpy as np

def cosine_matrix(X):
    n = X.shape[0]
    out = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            a,b = X[i], X[j]
            den = (np.linalg.norm(a)*np.linalg.norm(b)) or 1
            out[i,j] = a.dot(b)/den
    return out
```
5. **Time complexity**: O(n^2*d).
6. **Space complexity**: O(n^2).
7. **Interview tip**: Discuss memory growth for large n.

### Q162: One-hot encode integer labels (variant)
1. **Problem statement**: One-hot encode integer labels (variant).
2. **Explanation**: Common preprocessing for categorical targets.
3. **Working Python code**:
```python
import numpy as np

def one_hot(y, num_classes=None):
    y = np.asarray(y, dtype=int)
    c = num_classes or (y.max()+1)
    out = np.zeros((len(y), c), dtype=int)
    out[np.arange(len(y)), y] = 1
    return out
```
4. **Alternate solution**:
```python
import numpy as np

def one_hot(y, num_classes=None):
    y = np.asarray(y, dtype=int)
    c = num_classes or (max(y)+1)
    return np.eye(c, dtype=int)[y]
```
5. **Time complexity**: O(n*c).
6. **Space complexity**: O(n*c).
7. **Interview tip**: Validate labels are in range [0, c).

### Q163: Vectorized z-score normalization by column (variant)
1. **Problem statement**: Vectorized z-score normalization by column (variant).
2. **Explanation**: Standard preprocessing for many ML models.
3. **Working Python code**:
```python
import numpy as np

def zscore(X):
    mu = X.mean(axis=0)
    sd = X.std(axis=0)
    sd = np.where(sd==0, 1, sd)
    return (X - mu) / sd
```
4. **Alternate solution**:
```python
import numpy as np

def zscore(X):
    out = X.astype(float).copy()
    for j in range(X.shape[1]):
        m, s = X[:,j].mean(), X[:,j].std()
        out[:,j] = 0 if s==0 else (X[:,j]-m)/s
    return out
```
5. **Time complexity**: O(n*m).
6. **Space complexity**: O(n*m).
7. **Interview tip**: Mention dtype upcasting to float.

### Q164: Compute cosine similarity matrix between row vectors (variant)
1. **Problem statement**: Compute cosine similarity matrix between row vectors (variant).
2. **Explanation**: Core in retrieval and recommendation systems.
3. **Working Python code**:
```python
import numpy as np

def cosine_matrix(X):
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    norms = np.where(norms == 0, 1, norms)
    Xn = X / norms
    return Xn @ Xn.T
```
4. **Alternate solution**:
```python
import numpy as np

def cosine_matrix(X):
    n = X.shape[0]
    out = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            a,b = X[i], X[j]
            den = (np.linalg.norm(a)*np.linalg.norm(b)) or 1
            out[i,j] = a.dot(b)/den
    return out
```
5. **Time complexity**: O(n^2*d).
6. **Space complexity**: O(n^2).
7. **Interview tip**: Discuss memory growth for large n.

### Q165: One-hot encode integer labels (variant)
1. **Problem statement**: One-hot encode integer labels (variant).
2. **Explanation**: Common preprocessing for categorical targets.
3. **Working Python code**:
```python
import numpy as np

def one_hot(y, num_classes=None):
    y = np.asarray(y, dtype=int)
    c = num_classes or (y.max()+1)
    out = np.zeros((len(y), c), dtype=int)
    out[np.arange(len(y)), y] = 1
    return out
```
4. **Alternate solution**:
```python
import numpy as np

def one_hot(y, num_classes=None):
    y = np.asarray(y, dtype=int)
    c = num_classes or (max(y)+1)
    return np.eye(c, dtype=int)[y]
```
5. **Time complexity**: O(n*c).
6. **Space complexity**: O(n*c).
7. **Interview tip**: Validate labels are in range [0, c).

### Q166: Vectorized z-score normalization by column (variant)
1. **Problem statement**: Vectorized z-score normalization by column (variant).
2. **Explanation**: Standard preprocessing for many ML models.
3. **Working Python code**:
```python
import numpy as np

def zscore(X):
    mu = X.mean(axis=0)
    sd = X.std(axis=0)
    sd = np.where(sd==0, 1, sd)
    return (X - mu) / sd
```
4. **Alternate solution**:
```python
import numpy as np

def zscore(X):
    out = X.astype(float).copy()
    for j in range(X.shape[1]):
        m, s = X[:,j].mean(), X[:,j].std()
        out[:,j] = 0 if s==0 else (X[:,j]-m)/s
    return out
```
5. **Time complexity**: O(n*m).
6. **Space complexity**: O(n*m).
7. **Interview tip**: Mention dtype upcasting to float.

### Q167: Compute cosine similarity matrix between row vectors (variant)
1. **Problem statement**: Compute cosine similarity matrix between row vectors (variant).
2. **Explanation**: Core in retrieval and recommendation systems.
3. **Working Python code**:
```python
import numpy as np

def cosine_matrix(X):
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    norms = np.where(norms == 0, 1, norms)
    Xn = X / norms
    return Xn @ Xn.T
```
4. **Alternate solution**:
```python
import numpy as np

def cosine_matrix(X):
    n = X.shape[0]
    out = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            a,b = X[i], X[j]
            den = (np.linalg.norm(a)*np.linalg.norm(b)) or 1
            out[i,j] = a.dot(b)/den
    return out
```
5. **Time complexity**: O(n^2*d).
6. **Space complexity**: O(n^2).
7. **Interview tip**: Discuss memory growth for large n.

### Q168: One-hot encode integer labels (variant)
1. **Problem statement**: One-hot encode integer labels (variant).
2. **Explanation**: Common preprocessing for categorical targets.
3. **Working Python code**:
```python
import numpy as np

def one_hot(y, num_classes=None):
    y = np.asarray(y, dtype=int)
    c = num_classes or (y.max()+1)
    out = np.zeros((len(y), c), dtype=int)
    out[np.arange(len(y)), y] = 1
    return out
```
4. **Alternate solution**:
```python
import numpy as np

def one_hot(y, num_classes=None):
    y = np.asarray(y, dtype=int)
    c = num_classes or (max(y)+1)
    return np.eye(c, dtype=int)[y]
```
5. **Time complexity**: O(n*c).
6. **Space complexity**: O(n*c).
7. **Interview tip**: Validate labels are in range [0, c).

### Q169: Vectorized z-score normalization by column (variant)
1. **Problem statement**: Vectorized z-score normalization by column (variant).
2. **Explanation**: Standard preprocessing for many ML models.
3. **Working Python code**:
```python
import numpy as np

def zscore(X):
    mu = X.mean(axis=0)
    sd = X.std(axis=0)
    sd = np.where(sd==0, 1, sd)
    return (X - mu) / sd
```
4. **Alternate solution**:
```python
import numpy as np

def zscore(X):
    out = X.astype(float).copy()
    for j in range(X.shape[1]):
        m, s = X[:,j].mean(), X[:,j].std()
        out[:,j] = 0 if s==0 else (X[:,j]-m)/s
    return out
```
5. **Time complexity**: O(n*m).
6. **Space complexity**: O(n*m).
7. **Interview tip**: Mention dtype upcasting to float.

## Pandas

### Q170: Aggregate daily active users from event table
1. **Problem statement**: Aggregate daily active users from event table.
2. **Explanation**: Group by date and count unique user IDs.
3. **Working Python code**:
```python
import pandas as pd

def daily_active_users(df):
    d = df.copy()
    d['date'] = pd.to_datetime(d['timestamp']).dt.date
    return d.groupby('date', as_index=False)['user_id'].nunique().rename(columns={'user_id':'dau'})
```
4. **Alternate solution**:
```python
import pandas as pd

def daily_active_users(df):
    d = df.copy()
    d['date'] = pd.to_datetime(d['timestamp']).dt.floor('D')
    return d.pivot_table(index='date', values='user_id', aggfunc=pd.Series.nunique).reset_index().rename(columns={'user_id':'dau'})
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(g).
7. **Interview tip**: Ask timezone handling requirements for event timestamps.

### Q171: Compute retention flag: user active on day+7
1. **Problem statement**: Compute retention flag: user active on day+7.
2. **Explanation**: Self-join by user and shifted date.
3. **Working Python code**:
```python
import pandas as pd

def day7_retention(df):
    d = df[['user_id','date']].drop_duplicates().copy()
    d['date'] = pd.to_datetime(d['date'])
    f = d.rename(columns={'date':'future_date'})
    merged = d.merge(f, on='user_id', how='left')
    merged['retained'] = (merged['future_date'] == merged['date'] + pd.Timedelta(days=7))
    return merged.groupby(['user_id','date'])['retained'].any().reset_index()
```
4. **Alternate solution**:
```python
import pandas as pd

def day7_retention(df):
    s = set(map(tuple, df[['user_id','date']].drop_duplicates().values.tolist()))
    out=[]
    for u,d in s:
        dt = pd.to_datetime(d)
        out.append((u,d,(u,(dt+pd.Timedelta(days=7)).strftime('%Y-%m-%d')) in s))
    return pd.DataFrame(out, columns=['user_id','date','retained'])
```
5. **Time complexity**: O(n^2) worst with naive merge.
6. **Space complexity**: O(n).
7. **Interview tip**: Prefer indexed join strategy on large datasets.

### Q172: Detect outliers using IQR per numeric column
1. **Problem statement**: Detect outliers using IQR per numeric column.
2. **Explanation**: Robust outlier filtering for noisy datasets.
3. **Working Python code**:
```python
import pandas as pd

def iqr_outlier_mask(df, col):
    q1, q3 = df[col].quantile([0.25,0.75])
    iqr = q3 - q1
    lo, hi = q1 - 1.5*iqr, q3 + 1.5*iqr
    return (df[col] < lo) | (df[col] > hi)
```
4. **Alternate solution**:
```python
import numpy as np

def iqr_outlier_mask(df, col):
    x = np.sort(df[col].dropna().to_numpy())
    q1 = np.percentile(x, 25)
    q3 = np.percentile(x, 75)
    iqr = q3-q1
    return (df[col] < q1-1.5*iqr) | (df[col] > q3+1.5*iqr)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Mention skewed distributions where IQR may overflag.

### Q173: Aggregate daily active users from event table (variant)
1. **Problem statement**: Aggregate daily active users from event table (variant).
2. **Explanation**: Group by date and count unique user IDs.
3. **Working Python code**:
```python
import pandas as pd

def daily_active_users(df):
    d = df.copy()
    d['date'] = pd.to_datetime(d['timestamp']).dt.date
    return d.groupby('date', as_index=False)['user_id'].nunique().rename(columns={'user_id':'dau'})
```
4. **Alternate solution**:
```python
import pandas as pd

def daily_active_users(df):
    d = df.copy()
    d['date'] = pd.to_datetime(d['timestamp']).dt.floor('D')
    return d.pivot_table(index='date', values='user_id', aggfunc=pd.Series.nunique).reset_index().rename(columns={'user_id':'dau'})
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(g).
7. **Interview tip**: Ask timezone handling requirements for event timestamps.

### Q174: Compute retention flag: user active on day+7 (variant)
1. **Problem statement**: Compute retention flag: user active on day+7 (variant).
2. **Explanation**: Self-join by user and shifted date.
3. **Working Python code**:
```python
import pandas as pd

def day7_retention(df):
    d = df[['user_id','date']].drop_duplicates().copy()
    d['date'] = pd.to_datetime(d['date'])
    f = d.rename(columns={'date':'future_date'})
    merged = d.merge(f, on='user_id', how='left')
    merged['retained'] = (merged['future_date'] == merged['date'] + pd.Timedelta(days=7))
    return merged.groupby(['user_id','date'])['retained'].any().reset_index()
```
4. **Alternate solution**:
```python
import pandas as pd

def day7_retention(df):
    s = set(map(tuple, df[['user_id','date']].drop_duplicates().values.tolist()))
    out=[]
    for u,d in s:
        dt = pd.to_datetime(d)
        out.append((u,d,(u,(dt+pd.Timedelta(days=7)).strftime('%Y-%m-%d')) in s))
    return pd.DataFrame(out, columns=['user_id','date','retained'])
```
5. **Time complexity**: O(n^2) worst with naive merge.
6. **Space complexity**: O(n).
7. **Interview tip**: Prefer indexed join strategy on large datasets.

### Q175: Detect outliers using IQR per numeric column (variant)
1. **Problem statement**: Detect outliers using IQR per numeric column (variant).
2. **Explanation**: Robust outlier filtering for noisy datasets.
3. **Working Python code**:
```python
import pandas as pd

def iqr_outlier_mask(df, col):
    q1, q3 = df[col].quantile([0.25,0.75])
    iqr = q3 - q1
    lo, hi = q1 - 1.5*iqr, q3 + 1.5*iqr
    return (df[col] < lo) | (df[col] > hi)
```
4. **Alternate solution**:
```python
import numpy as np

def iqr_outlier_mask(df, col):
    x = np.sort(df[col].dropna().to_numpy())
    q1 = np.percentile(x, 25)
    q3 = np.percentile(x, 75)
    iqr = q3-q1
    return (df[col] < q1-1.5*iqr) | (df[col] > q3+1.5*iqr)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Mention skewed distributions where IQR may overflag.

### Q176: Aggregate daily active users from event table (variant)
1. **Problem statement**: Aggregate daily active users from event table (variant).
2. **Explanation**: Group by date and count unique user IDs.
3. **Working Python code**:
```python
import pandas as pd

def daily_active_users(df):
    d = df.copy()
    d['date'] = pd.to_datetime(d['timestamp']).dt.date
    return d.groupby('date', as_index=False)['user_id'].nunique().rename(columns={'user_id':'dau'})
```
4. **Alternate solution**:
```python
import pandas as pd

def daily_active_users(df):
    d = df.copy()
    d['date'] = pd.to_datetime(d['timestamp']).dt.floor('D')
    return d.pivot_table(index='date', values='user_id', aggfunc=pd.Series.nunique).reset_index().rename(columns={'user_id':'dau'})
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(g).
7. **Interview tip**: Ask timezone handling requirements for event timestamps.

### Q177: Compute retention flag: user active on day+7 (variant)
1. **Problem statement**: Compute retention flag: user active on day+7 (variant).
2. **Explanation**: Self-join by user and shifted date.
3. **Working Python code**:
```python
import pandas as pd

def day7_retention(df):
    d = df[['user_id','date']].drop_duplicates().copy()
    d['date'] = pd.to_datetime(d['date'])
    f = d.rename(columns={'date':'future_date'})
    merged = d.merge(f, on='user_id', how='left')
    merged['retained'] = (merged['future_date'] == merged['date'] + pd.Timedelta(days=7))
    return merged.groupby(['user_id','date'])['retained'].any().reset_index()
```
4. **Alternate solution**:
```python
import pandas as pd

def day7_retention(df):
    s = set(map(tuple, df[['user_id','date']].drop_duplicates().values.tolist()))
    out=[]
    for u,d in s:
        dt = pd.to_datetime(d)
        out.append((u,d,(u,(dt+pd.Timedelta(days=7)).strftime('%Y-%m-%d')) in s))
    return pd.DataFrame(out, columns=['user_id','date','retained'])
```
5. **Time complexity**: O(n^2) worst with naive merge.
6. **Space complexity**: O(n).
7. **Interview tip**: Prefer indexed join strategy on large datasets.

### Q178: Detect outliers using IQR per numeric column (variant)
1. **Problem statement**: Detect outliers using IQR per numeric column (variant).
2. **Explanation**: Robust outlier filtering for noisy datasets.
3. **Working Python code**:
```python
import pandas as pd

def iqr_outlier_mask(df, col):
    q1, q3 = df[col].quantile([0.25,0.75])
    iqr = q3 - q1
    lo, hi = q1 - 1.5*iqr, q3 + 1.5*iqr
    return (df[col] < lo) | (df[col] > hi)
```
4. **Alternate solution**:
```python
import numpy as np

def iqr_outlier_mask(df, col):
    x = np.sort(df[col].dropna().to_numpy())
    q1 = np.percentile(x, 25)
    q3 = np.percentile(x, 75)
    iqr = q3-q1
    return (df[col] < q1-1.5*iqr) | (df[col] > q3+1.5*iqr)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Mention skewed distributions where IQR may overflag.

### Q179: Aggregate daily active users from event table (variant)
1. **Problem statement**: Aggregate daily active users from event table (variant).
2. **Explanation**: Group by date and count unique user IDs.
3. **Working Python code**:
```python
import pandas as pd

def daily_active_users(df):
    d = df.copy()
    d['date'] = pd.to_datetime(d['timestamp']).dt.date
    return d.groupby('date', as_index=False)['user_id'].nunique().rename(columns={'user_id':'dau'})
```
4. **Alternate solution**:
```python
import pandas as pd

def daily_active_users(df):
    d = df.copy()
    d['date'] = pd.to_datetime(d['timestamp']).dt.floor('D')
    return d.pivot_table(index='date', values='user_id', aggfunc=pd.Series.nunique).reset_index().rename(columns={'user_id':'dau'})
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(g).
7. **Interview tip**: Ask timezone handling requirements for event timestamps.

### Q180: Compute retention flag: user active on day+7 (variant)
1. **Problem statement**: Compute retention flag: user active on day+7 (variant).
2. **Explanation**: Self-join by user and shifted date.
3. **Working Python code**:
```python
import pandas as pd

def day7_retention(df):
    d = df[['user_id','date']].drop_duplicates().copy()
    d['date'] = pd.to_datetime(d['date'])
    f = d.rename(columns={'date':'future_date'})
    merged = d.merge(f, on='user_id', how='left')
    merged['retained'] = (merged['future_date'] == merged['date'] + pd.Timedelta(days=7))
    return merged.groupby(['user_id','date'])['retained'].any().reset_index()
```
4. **Alternate solution**:
```python
import pandas as pd

def day7_retention(df):
    s = set(map(tuple, df[['user_id','date']].drop_duplicates().values.tolist()))
    out=[]
    for u,d in s:
        dt = pd.to_datetime(d)
        out.append((u,d,(u,(dt+pd.Timedelta(days=7)).strftime('%Y-%m-%d')) in s))
    return pd.DataFrame(out, columns=['user_id','date','retained'])
```
5. **Time complexity**: O(n^2) worst with naive merge.
6. **Space complexity**: O(n).
7. **Interview tip**: Prefer indexed join strategy on large datasets.

### Q181: Detect outliers using IQR per numeric column (variant)
1. **Problem statement**: Detect outliers using IQR per numeric column (variant).
2. **Explanation**: Robust outlier filtering for noisy datasets.
3. **Working Python code**:
```python
import pandas as pd

def iqr_outlier_mask(df, col):
    q1, q3 = df[col].quantile([0.25,0.75])
    iqr = q3 - q1
    lo, hi = q1 - 1.5*iqr, q3 + 1.5*iqr
    return (df[col] < lo) | (df[col] > hi)
```
4. **Alternate solution**:
```python
import numpy as np

def iqr_outlier_mask(df, col):
    x = np.sort(df[col].dropna().to_numpy())
    q1 = np.percentile(x, 25)
    q3 = np.percentile(x, 75)
    iqr = q3-q1
    return (df[col] < q1-1.5*iqr) | (df[col] > q3+1.5*iqr)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Mention skewed distributions where IQR may overflag.

### Q182: Aggregate daily active users from event table (variant)
1. **Problem statement**: Aggregate daily active users from event table (variant).
2. **Explanation**: Group by date and count unique user IDs.
3. **Working Python code**:
```python
import pandas as pd

def daily_active_users(df):
    d = df.copy()
    d['date'] = pd.to_datetime(d['timestamp']).dt.date
    return d.groupby('date', as_index=False)['user_id'].nunique().rename(columns={'user_id':'dau'})
```
4. **Alternate solution**:
```python
import pandas as pd

def daily_active_users(df):
    d = df.copy()
    d['date'] = pd.to_datetime(d['timestamp']).dt.floor('D')
    return d.pivot_table(index='date', values='user_id', aggfunc=pd.Series.nunique).reset_index().rename(columns={'user_id':'dau'})
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(g).
7. **Interview tip**: Ask timezone handling requirements for event timestamps.

### Q183: Compute retention flag: user active on day+7 (variant)
1. **Problem statement**: Compute retention flag: user active on day+7 (variant).
2. **Explanation**: Self-join by user and shifted date.
3. **Working Python code**:
```python
import pandas as pd

def day7_retention(df):
    d = df[['user_id','date']].drop_duplicates().copy()
    d['date'] = pd.to_datetime(d['date'])
    f = d.rename(columns={'date':'future_date'})
    merged = d.merge(f, on='user_id', how='left')
    merged['retained'] = (merged['future_date'] == merged['date'] + pd.Timedelta(days=7))
    return merged.groupby(['user_id','date'])['retained'].any().reset_index()
```
4. **Alternate solution**:
```python
import pandas as pd

def day7_retention(df):
    s = set(map(tuple, df[['user_id','date']].drop_duplicates().values.tolist()))
    out=[]
    for u,d in s:
        dt = pd.to_datetime(d)
        out.append((u,d,(u,(dt+pd.Timedelta(days=7)).strftime('%Y-%m-%d')) in s))
    return pd.DataFrame(out, columns=['user_id','date','retained'])
```
5. **Time complexity**: O(n^2) worst with naive merge.
6. **Space complexity**: O(n).
7. **Interview tip**: Prefer indexed join strategy on large datasets.

### Q184: Detect outliers using IQR per numeric column (variant)
1. **Problem statement**: Detect outliers using IQR per numeric column (variant).
2. **Explanation**: Robust outlier filtering for noisy datasets.
3. **Working Python code**:
```python
import pandas as pd

def iqr_outlier_mask(df, col):
    q1, q3 = df[col].quantile([0.25,0.75])
    iqr = q3 - q1
    lo, hi = q1 - 1.5*iqr, q3 + 1.5*iqr
    return (df[col] < lo) | (df[col] > hi)
```
4. **Alternate solution**:
```python
import numpy as np

def iqr_outlier_mask(df, col):
    x = np.sort(df[col].dropna().to_numpy())
    q1 = np.percentile(x, 25)
    q3 = np.percentile(x, 75)
    iqr = q3-q1
    return (df[col] < q1-1.5*iqr) | (df[col] > q3+1.5*iqr)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Mention skewed distributions where IQR may overflag.

### Q185: Aggregate daily active users from event table (variant)
1. **Problem statement**: Aggregate daily active users from event table (variant).
2. **Explanation**: Group by date and count unique user IDs.
3. **Working Python code**:
```python
import pandas as pd

def daily_active_users(df):
    d = df.copy()
    d['date'] = pd.to_datetime(d['timestamp']).dt.date
    return d.groupby('date', as_index=False)['user_id'].nunique().rename(columns={'user_id':'dau'})
```
4. **Alternate solution**:
```python
import pandas as pd

def daily_active_users(df):
    d = df.copy()
    d['date'] = pd.to_datetime(d['timestamp']).dt.floor('D')
    return d.pivot_table(index='date', values='user_id', aggfunc=pd.Series.nunique).reset_index().rename(columns={'user_id':'dau'})
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(g).
7. **Interview tip**: Ask timezone handling requirements for event timestamps.

### Q186: Compute retention flag: user active on day+7 (variant)
1. **Problem statement**: Compute retention flag: user active on day+7 (variant).
2. **Explanation**: Self-join by user and shifted date.
3. **Working Python code**:
```python
import pandas as pd

def day7_retention(df):
    d = df[['user_id','date']].drop_duplicates().copy()
    d['date'] = pd.to_datetime(d['date'])
    f = d.rename(columns={'date':'future_date'})
    merged = d.merge(f, on='user_id', how='left')
    merged['retained'] = (merged['future_date'] == merged['date'] + pd.Timedelta(days=7))
    return merged.groupby(['user_id','date'])['retained'].any().reset_index()
```
4. **Alternate solution**:
```python
import pandas as pd

def day7_retention(df):
    s = set(map(tuple, df[['user_id','date']].drop_duplicates().values.tolist()))
    out=[]
    for u,d in s:
        dt = pd.to_datetime(d)
        out.append((u,d,(u,(dt+pd.Timedelta(days=7)).strftime('%Y-%m-%d')) in s))
    return pd.DataFrame(out, columns=['user_id','date','retained'])
```
5. **Time complexity**: O(n^2) worst with naive merge.
6. **Space complexity**: O(n).
7. **Interview tip**: Prefer indexed join strategy on large datasets.

### Q187: Detect outliers using IQR per numeric column (variant)
1. **Problem statement**: Detect outliers using IQR per numeric column (variant).
2. **Explanation**: Robust outlier filtering for noisy datasets.
3. **Working Python code**:
```python
import pandas as pd

def iqr_outlier_mask(df, col):
    q1, q3 = df[col].quantile([0.25,0.75])
    iqr = q3 - q1
    lo, hi = q1 - 1.5*iqr, q3 + 1.5*iqr
    return (df[col] < lo) | (df[col] > hi)
```
4. **Alternate solution**:
```python
import numpy as np

def iqr_outlier_mask(df, col):
    x = np.sort(df[col].dropna().to_numpy())
    q1 = np.percentile(x, 25)
    q3 = np.percentile(x, 75)
    iqr = q3-q1
    return (df[col] < q1-1.5*iqr) | (df[col] > q3+1.5*iqr)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Mention skewed distributions where IQR may overflag.

### Q188: Aggregate daily active users from event table (variant)
1. **Problem statement**: Aggregate daily active users from event table (variant).
2. **Explanation**: Group by date and count unique user IDs.
3. **Working Python code**:
```python
import pandas as pd

def daily_active_users(df):
    d = df.copy()
    d['date'] = pd.to_datetime(d['timestamp']).dt.date
    return d.groupby('date', as_index=False)['user_id'].nunique().rename(columns={'user_id':'dau'})
```
4. **Alternate solution**:
```python
import pandas as pd

def daily_active_users(df):
    d = df.copy()
    d['date'] = pd.to_datetime(d['timestamp']).dt.floor('D')
    return d.pivot_table(index='date', values='user_id', aggfunc=pd.Series.nunique).reset_index().rename(columns={'user_id':'dau'})
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(g).
7. **Interview tip**: Ask timezone handling requirements for event timestamps.

### Q189: Compute retention flag: user active on day+7 (variant)
1. **Problem statement**: Compute retention flag: user active on day+7 (variant).
2. **Explanation**: Self-join by user and shifted date.
3. **Working Python code**:
```python
import pandas as pd

def day7_retention(df):
    d = df[['user_id','date']].drop_duplicates().copy()
    d['date'] = pd.to_datetime(d['date'])
    f = d.rename(columns={'date':'future_date'})
    merged = d.merge(f, on='user_id', how='left')
    merged['retained'] = (merged['future_date'] == merged['date'] + pd.Timedelta(days=7))
    return merged.groupby(['user_id','date'])['retained'].any().reset_index()
```
4. **Alternate solution**:
```python
import pandas as pd

def day7_retention(df):
    s = set(map(tuple, df[['user_id','date']].drop_duplicates().values.tolist()))
    out=[]
    for u,d in s:
        dt = pd.to_datetime(d)
        out.append((u,d,(u,(dt+pd.Timedelta(days=7)).strftime('%Y-%m-%d')) in s))
    return pd.DataFrame(out, columns=['user_id','date','retained'])
```
5. **Time complexity**: O(n^2) worst with naive merge.
6. **Space complexity**: O(n).
7. **Interview tip**: Prefer indexed join strategy on large datasets.

### Q190: Detect outliers using IQR per numeric column (variant)
1. **Problem statement**: Detect outliers using IQR per numeric column (variant).
2. **Explanation**: Robust outlier filtering for noisy datasets.
3. **Working Python code**:
```python
import pandas as pd

def iqr_outlier_mask(df, col):
    q1, q3 = df[col].quantile([0.25,0.75])
    iqr = q3 - q1
    lo, hi = q1 - 1.5*iqr, q3 + 1.5*iqr
    return (df[col] < lo) | (df[col] > hi)
```
4. **Alternate solution**:
```python
import numpy as np

def iqr_outlier_mask(df, col):
    x = np.sort(df[col].dropna().to_numpy())
    q1 = np.percentile(x, 25)
    q3 = np.percentile(x, 75)
    iqr = q3-q1
    return (df[col] < q1-1.5*iqr) | (df[col] > q3+1.5*iqr)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Mention skewed distributions where IQR may overflag.

### Q191: Aggregate daily active users from event table (variant)
1. **Problem statement**: Aggregate daily active users from event table (variant).
2. **Explanation**: Group by date and count unique user IDs.
3. **Working Python code**:
```python
import pandas as pd

def daily_active_users(df):
    d = df.copy()
    d['date'] = pd.to_datetime(d['timestamp']).dt.date
    return d.groupby('date', as_index=False)['user_id'].nunique().rename(columns={'user_id':'dau'})
```
4. **Alternate solution**:
```python
import pandas as pd

def daily_active_users(df):
    d = df.copy()
    d['date'] = pd.to_datetime(d['timestamp']).dt.floor('D')
    return d.pivot_table(index='date', values='user_id', aggfunc=pd.Series.nunique).reset_index().rename(columns={'user_id':'dau'})
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(g).
7. **Interview tip**: Ask timezone handling requirements for event timestamps.

### Q192: Compute retention flag: user active on day+7 (variant)
1. **Problem statement**: Compute retention flag: user active on day+7 (variant).
2. **Explanation**: Self-join by user and shifted date.
3. **Working Python code**:
```python
import pandas as pd

def day7_retention(df):
    d = df[['user_id','date']].drop_duplicates().copy()
    d['date'] = pd.to_datetime(d['date'])
    f = d.rename(columns={'date':'future_date'})
    merged = d.merge(f, on='user_id', how='left')
    merged['retained'] = (merged['future_date'] == merged['date'] + pd.Timedelta(days=7))
    return merged.groupby(['user_id','date'])['retained'].any().reset_index()
```
4. **Alternate solution**:
```python
import pandas as pd

def day7_retention(df):
    s = set(map(tuple, df[['user_id','date']].drop_duplicates().values.tolist()))
    out=[]
    for u,d in s:
        dt = pd.to_datetime(d)
        out.append((u,d,(u,(dt+pd.Timedelta(days=7)).strftime('%Y-%m-%d')) in s))
    return pd.DataFrame(out, columns=['user_id','date','retained'])
```
5. **Time complexity**: O(n^2) worst with naive merge.
6. **Space complexity**: O(n).
7. **Interview tip**: Prefer indexed join strategy on large datasets.

### Q193: Detect outliers using IQR per numeric column (variant)
1. **Problem statement**: Detect outliers using IQR per numeric column (variant).
2. **Explanation**: Robust outlier filtering for noisy datasets.
3. **Working Python code**:
```python
import pandas as pd

def iqr_outlier_mask(df, col):
    q1, q3 = df[col].quantile([0.25,0.75])
    iqr = q3 - q1
    lo, hi = q1 - 1.5*iqr, q3 + 1.5*iqr
    return (df[col] < lo) | (df[col] > hi)
```
4. **Alternate solution**:
```python
import numpy as np

def iqr_outlier_mask(df, col):
    x = np.sort(df[col].dropna().to_numpy())
    q1 = np.percentile(x, 25)
    q3 = np.percentile(x, 75)
    iqr = q3-q1
    return (df[col] < q1-1.5*iqr) | (df[col] > q3+1.5*iqr)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Mention skewed distributions where IQR may overflag.

### Q194: Aggregate daily active users from event table (variant)
1. **Problem statement**: Aggregate daily active users from event table (variant).
2. **Explanation**: Group by date and count unique user IDs.
3. **Working Python code**:
```python
import pandas as pd

def daily_active_users(df):
    d = df.copy()
    d['date'] = pd.to_datetime(d['timestamp']).dt.date
    return d.groupby('date', as_index=False)['user_id'].nunique().rename(columns={'user_id':'dau'})
```
4. **Alternate solution**:
```python
import pandas as pd

def daily_active_users(df):
    d = df.copy()
    d['date'] = pd.to_datetime(d['timestamp']).dt.floor('D')
    return d.pivot_table(index='date', values='user_id', aggfunc=pd.Series.nunique).reset_index().rename(columns={'user_id':'dau'})
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(g).
7. **Interview tip**: Ask timezone handling requirements for event timestamps.

### Q195: Compute retention flag: user active on day+7 (variant)
1. **Problem statement**: Compute retention flag: user active on day+7 (variant).
2. **Explanation**: Self-join by user and shifted date.
3. **Working Python code**:
```python
import pandas as pd

def day7_retention(df):
    d = df[['user_id','date']].drop_duplicates().copy()
    d['date'] = pd.to_datetime(d['date'])
    f = d.rename(columns={'date':'future_date'})
    merged = d.merge(f, on='user_id', how='left')
    merged['retained'] = (merged['future_date'] == merged['date'] + pd.Timedelta(days=7))
    return merged.groupby(['user_id','date'])['retained'].any().reset_index()
```
4. **Alternate solution**:
```python
import pandas as pd

def day7_retention(df):
    s = set(map(tuple, df[['user_id','date']].drop_duplicates().values.tolist()))
    out=[]
    for u,d in s:
        dt = pd.to_datetime(d)
        out.append((u,d,(u,(dt+pd.Timedelta(days=7)).strftime('%Y-%m-%d')) in s))
    return pd.DataFrame(out, columns=['user_id','date','retained'])
```
5. **Time complexity**: O(n^2) worst with naive merge.
6. **Space complexity**: O(n).
7. **Interview tip**: Prefer indexed join strategy on large datasets.

### Q196: Detect outliers using IQR per numeric column (variant)
1. **Problem statement**: Detect outliers using IQR per numeric column (variant).
2. **Explanation**: Robust outlier filtering for noisy datasets.
3. **Working Python code**:
```python
import pandas as pd

def iqr_outlier_mask(df, col):
    q1, q3 = df[col].quantile([0.25,0.75])
    iqr = q3 - q1
    lo, hi = q1 - 1.5*iqr, q3 + 1.5*iqr
    return (df[col] < lo) | (df[col] > hi)
```
4. **Alternate solution**:
```python
import numpy as np

def iqr_outlier_mask(df, col):
    x = np.sort(df[col].dropna().to_numpy())
    q1 = np.percentile(x, 25)
    q3 = np.percentile(x, 75)
    iqr = q3-q1
    return (df[col] < q1-1.5*iqr) | (df[col] > q3+1.5*iqr)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Mention skewed distributions where IQR may overflag.

### Q197: Aggregate daily active users from event table (variant)
1. **Problem statement**: Aggregate daily active users from event table (variant).
2. **Explanation**: Group by date and count unique user IDs.
3. **Working Python code**:
```python
import pandas as pd

def daily_active_users(df):
    d = df.copy()
    d['date'] = pd.to_datetime(d['timestamp']).dt.date
    return d.groupby('date', as_index=False)['user_id'].nunique().rename(columns={'user_id':'dau'})
```
4. **Alternate solution**:
```python
import pandas as pd

def daily_active_users(df):
    d = df.copy()
    d['date'] = pd.to_datetime(d['timestamp']).dt.floor('D')
    return d.pivot_table(index='date', values='user_id', aggfunc=pd.Series.nunique).reset_index().rename(columns={'user_id':'dau'})
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(g).
7. **Interview tip**: Ask timezone handling requirements for event timestamps.

## Python for ML

### Q198: Implement stratified train-test split for binary labels
1. **Problem statement**: Implement stratified train-test split for binary labels.
2. **Explanation**: Preserve label distribution in each split.
3. **Working Python code**:
```python
import numpy as np

def stratified_split(X, y, test_size=0.2, seed=0):
    rng = np.random.default_rng(seed)
    y = np.asarray(y)
    idx0 = np.where(y==0)[0]; idx1 = np.where(y==1)[0]
    rng.shuffle(idx0); rng.shuffle(idx1)
    t0 = int(len(idx0)*test_size); t1 = int(len(idx1)*test_size)
    test_idx = np.concatenate([idx0[:t0], idx1[:t1]])
    train_idx = np.concatenate([idx0[t0:], idx1[t1:]])
    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]
```
4. **Alternate solution**:
```python
from sklearn.model_selection import train_test_split

def stratified_split(X, y, test_size=0.2, seed=0):
    return train_test_split(X, y, test_size=test_size, random_state=seed, stratify=y)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Explain why random split can bias minority classes.

### Q199: Compute confusion matrix for multiclass labels
1. **Problem statement**: Compute confusion matrix for multiclass labels.
2. **Explanation**: Essential evaluation primitive.
3. **Working Python code**:
```python
import numpy as np

def confusion_matrix(y_true, y_pred, n_classes):
    cm = np.zeros((n_classes, n_classes), dtype=int)
    for t,p in zip(y_true, y_pred):
        cm[t,p] += 1
    return cm
```
4. **Alternate solution**:
```python
import numpy as np

def confusion_matrix(y_true, y_pred, n_classes):
    y_true = np.asarray(y_true); y_pred = np.asarray(y_pred)
    idx = y_true * n_classes + y_pred
    return np.bincount(idx, minlength=n_classes*n_classes).reshape(n_classes, n_classes)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(c^2).
7. **Interview tip**: Clarify label indexing assumptions.

### Q200: Implement early stopping callback logic
1. **Problem statement**: Implement early stopping callback logic.
2. **Explanation**: Prevents overfitting during training.
3. **Working Python code**:
```python
class EarlyStopping:
    def __init__(self, patience=3, min_delta=0.0):
        self.patience = patience
        self.min_delta = min_delta
        self.best = float('inf')
        self.bad_epochs = 0
    def step(self, val_loss):
        if val_loss < self.best - self.min_delta:
            self.best = val_loss
            self.bad_epochs = 0
            return False
        self.bad_epochs += 1
        return self.bad_epochs >= self.patience
```
4. **Alternate solution**:
```python
def early_stop(losses, patience=3, min_delta=0.0):
    best=float('inf'); bad=0
    for l in losses:
        if l < best-min_delta: best=l; bad=0
        else: bad += 1
        if bad>=patience: return True
    return False
```
5. **Time complexity**: O(1) per epoch.
6. **Space complexity**: O(1).
7. **Interview tip**: Discuss restoring best checkpoint on stop.

### Q201: Implement stratified train-test split for binary labels (variant)
1. **Problem statement**: Implement stratified train-test split for binary labels (variant).
2. **Explanation**: Preserve label distribution in each split.
3. **Working Python code**:
```python
import numpy as np

def stratified_split(X, y, test_size=0.2, seed=0):
    rng = np.random.default_rng(seed)
    y = np.asarray(y)
    idx0 = np.where(y==0)[0]; idx1 = np.where(y==1)[0]
    rng.shuffle(idx0); rng.shuffle(idx1)
    t0 = int(len(idx0)*test_size); t1 = int(len(idx1)*test_size)
    test_idx = np.concatenate([idx0[:t0], idx1[:t1]])
    train_idx = np.concatenate([idx0[t0:], idx1[t1:]])
    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]
```
4. **Alternate solution**:
```python
from sklearn.model_selection import train_test_split

def stratified_split(X, y, test_size=0.2, seed=0):
    return train_test_split(X, y, test_size=test_size, random_state=seed, stratify=y)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Explain why random split can bias minority classes.

### Q202: Compute confusion matrix for multiclass labels (variant)
1. **Problem statement**: Compute confusion matrix for multiclass labels (variant).
2. **Explanation**: Essential evaluation primitive.
3. **Working Python code**:
```python
import numpy as np

def confusion_matrix(y_true, y_pred, n_classes):
    cm = np.zeros((n_classes, n_classes), dtype=int)
    for t,p in zip(y_true, y_pred):
        cm[t,p] += 1
    return cm
```
4. **Alternate solution**:
```python
import numpy as np

def confusion_matrix(y_true, y_pred, n_classes):
    y_true = np.asarray(y_true); y_pred = np.asarray(y_pred)
    idx = y_true * n_classes + y_pred
    return np.bincount(idx, minlength=n_classes*n_classes).reshape(n_classes, n_classes)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(c^2).
7. **Interview tip**: Clarify label indexing assumptions.

### Q203: Implement early stopping callback logic (variant)
1. **Problem statement**: Implement early stopping callback logic (variant).
2. **Explanation**: Prevents overfitting during training.
3. **Working Python code**:
```python
class EarlyStopping:
    def __init__(self, patience=3, min_delta=0.0):
        self.patience = patience
        self.min_delta = min_delta
        self.best = float('inf')
        self.bad_epochs = 0
    def step(self, val_loss):
        if val_loss < self.best - self.min_delta:
            self.best = val_loss
            self.bad_epochs = 0
            return False
        self.bad_epochs += 1
        return self.bad_epochs >= self.patience
```
4. **Alternate solution**:
```python
def early_stop(losses, patience=3, min_delta=0.0):
    best=float('inf'); bad=0
    for l in losses:
        if l < best-min_delta: best=l; bad=0
        else: bad += 1
        if bad>=patience: return True
    return False
```
5. **Time complexity**: O(1) per epoch.
6. **Space complexity**: O(1).
7. **Interview tip**: Discuss restoring best checkpoint on stop.

### Q204: Implement stratified train-test split for binary labels (variant)
1. **Problem statement**: Implement stratified train-test split for binary labels (variant).
2. **Explanation**: Preserve label distribution in each split.
3. **Working Python code**:
```python
import numpy as np

def stratified_split(X, y, test_size=0.2, seed=0):
    rng = np.random.default_rng(seed)
    y = np.asarray(y)
    idx0 = np.where(y==0)[0]; idx1 = np.where(y==1)[0]
    rng.shuffle(idx0); rng.shuffle(idx1)
    t0 = int(len(idx0)*test_size); t1 = int(len(idx1)*test_size)
    test_idx = np.concatenate([idx0[:t0], idx1[:t1]])
    train_idx = np.concatenate([idx0[t0:], idx1[t1:]])
    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]
```
4. **Alternate solution**:
```python
from sklearn.model_selection import train_test_split

def stratified_split(X, y, test_size=0.2, seed=0):
    return train_test_split(X, y, test_size=test_size, random_state=seed, stratify=y)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Explain why random split can bias minority classes.

### Q205: Compute confusion matrix for multiclass labels (variant)
1. **Problem statement**: Compute confusion matrix for multiclass labels (variant).
2. **Explanation**: Essential evaluation primitive.
3. **Working Python code**:
```python
import numpy as np

def confusion_matrix(y_true, y_pred, n_classes):
    cm = np.zeros((n_classes, n_classes), dtype=int)
    for t,p in zip(y_true, y_pred):
        cm[t,p] += 1
    return cm
```
4. **Alternate solution**:
```python
import numpy as np

def confusion_matrix(y_true, y_pred, n_classes):
    y_true = np.asarray(y_true); y_pred = np.asarray(y_pred)
    idx = y_true * n_classes + y_pred
    return np.bincount(idx, minlength=n_classes*n_classes).reshape(n_classes, n_classes)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(c^2).
7. **Interview tip**: Clarify label indexing assumptions.

### Q206: Implement early stopping callback logic (variant)
1. **Problem statement**: Implement early stopping callback logic (variant).
2. **Explanation**: Prevents overfitting during training.
3. **Working Python code**:
```python
class EarlyStopping:
    def __init__(self, patience=3, min_delta=0.0):
        self.patience = patience
        self.min_delta = min_delta
        self.best = float('inf')
        self.bad_epochs = 0
    def step(self, val_loss):
        if val_loss < self.best - self.min_delta:
            self.best = val_loss
            self.bad_epochs = 0
            return False
        self.bad_epochs += 1
        return self.bad_epochs >= self.patience
```
4. **Alternate solution**:
```python
def early_stop(losses, patience=3, min_delta=0.0):
    best=float('inf'); bad=0
    for l in losses:
        if l < best-min_delta: best=l; bad=0
        else: bad += 1
        if bad>=patience: return True
    return False
```
5. **Time complexity**: O(1) per epoch.
6. **Space complexity**: O(1).
7. **Interview tip**: Discuss restoring best checkpoint on stop.

### Q207: Implement stratified train-test split for binary labels (variant)
1. **Problem statement**: Implement stratified train-test split for binary labels (variant).
2. **Explanation**: Preserve label distribution in each split.
3. **Working Python code**:
```python
import numpy as np

def stratified_split(X, y, test_size=0.2, seed=0):
    rng = np.random.default_rng(seed)
    y = np.asarray(y)
    idx0 = np.where(y==0)[0]; idx1 = np.where(y==1)[0]
    rng.shuffle(idx0); rng.shuffle(idx1)
    t0 = int(len(idx0)*test_size); t1 = int(len(idx1)*test_size)
    test_idx = np.concatenate([idx0[:t0], idx1[:t1]])
    train_idx = np.concatenate([idx0[t0:], idx1[t1:]])
    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]
```
4. **Alternate solution**:
```python
from sklearn.model_selection import train_test_split

def stratified_split(X, y, test_size=0.2, seed=0):
    return train_test_split(X, y, test_size=test_size, random_state=seed, stratify=y)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Explain why random split can bias minority classes.

### Q208: Compute confusion matrix for multiclass labels (variant)
1. **Problem statement**: Compute confusion matrix for multiclass labels (variant).
2. **Explanation**: Essential evaluation primitive.
3. **Working Python code**:
```python
import numpy as np

def confusion_matrix(y_true, y_pred, n_classes):
    cm = np.zeros((n_classes, n_classes), dtype=int)
    for t,p in zip(y_true, y_pred):
        cm[t,p] += 1
    return cm
```
4. **Alternate solution**:
```python
import numpy as np

def confusion_matrix(y_true, y_pred, n_classes):
    y_true = np.asarray(y_true); y_pred = np.asarray(y_pred)
    idx = y_true * n_classes + y_pred
    return np.bincount(idx, minlength=n_classes*n_classes).reshape(n_classes, n_classes)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(c^2).
7. **Interview tip**: Clarify label indexing assumptions.

### Q209: Implement early stopping callback logic (variant)
1. **Problem statement**: Implement early stopping callback logic (variant).
2. **Explanation**: Prevents overfitting during training.
3. **Working Python code**:
```python
class EarlyStopping:
    def __init__(self, patience=3, min_delta=0.0):
        self.patience = patience
        self.min_delta = min_delta
        self.best = float('inf')
        self.bad_epochs = 0
    def step(self, val_loss):
        if val_loss < self.best - self.min_delta:
            self.best = val_loss
            self.bad_epochs = 0
            return False
        self.bad_epochs += 1
        return self.bad_epochs >= self.patience
```
4. **Alternate solution**:
```python
def early_stop(losses, patience=3, min_delta=0.0):
    best=float('inf'); bad=0
    for l in losses:
        if l < best-min_delta: best=l; bad=0
        else: bad += 1
        if bad>=patience: return True
    return False
```
5. **Time complexity**: O(1) per epoch.
6. **Space complexity**: O(1).
7. **Interview tip**: Discuss restoring best checkpoint on stop.

### Q210: Implement stratified train-test split for binary labels (variant)
1. **Problem statement**: Implement stratified train-test split for binary labels (variant).
2. **Explanation**: Preserve label distribution in each split.
3. **Working Python code**:
```python
import numpy as np

def stratified_split(X, y, test_size=0.2, seed=0):
    rng = np.random.default_rng(seed)
    y = np.asarray(y)
    idx0 = np.where(y==0)[0]; idx1 = np.where(y==1)[0]
    rng.shuffle(idx0); rng.shuffle(idx1)
    t0 = int(len(idx0)*test_size); t1 = int(len(idx1)*test_size)
    test_idx = np.concatenate([idx0[:t0], idx1[:t1]])
    train_idx = np.concatenate([idx0[t0:], idx1[t1:]])
    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]
```
4. **Alternate solution**:
```python
from sklearn.model_selection import train_test_split

def stratified_split(X, y, test_size=0.2, seed=0):
    return train_test_split(X, y, test_size=test_size, random_state=seed, stratify=y)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Explain why random split can bias minority classes.

### Q211: Compute confusion matrix for multiclass labels (variant)
1. **Problem statement**: Compute confusion matrix for multiclass labels (variant).
2. **Explanation**: Essential evaluation primitive.
3. **Working Python code**:
```python
import numpy as np

def confusion_matrix(y_true, y_pred, n_classes):
    cm = np.zeros((n_classes, n_classes), dtype=int)
    for t,p in zip(y_true, y_pred):
        cm[t,p] += 1
    return cm
```
4. **Alternate solution**:
```python
import numpy as np

def confusion_matrix(y_true, y_pred, n_classes):
    y_true = np.asarray(y_true); y_pred = np.asarray(y_pred)
    idx = y_true * n_classes + y_pred
    return np.bincount(idx, minlength=n_classes*n_classes).reshape(n_classes, n_classes)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(c^2).
7. **Interview tip**: Clarify label indexing assumptions.

### Q212: Implement early stopping callback logic (variant)
1. **Problem statement**: Implement early stopping callback logic (variant).
2. **Explanation**: Prevents overfitting during training.
3. **Working Python code**:
```python
class EarlyStopping:
    def __init__(self, patience=3, min_delta=0.0):
        self.patience = patience
        self.min_delta = min_delta
        self.best = float('inf')
        self.bad_epochs = 0
    def step(self, val_loss):
        if val_loss < self.best - self.min_delta:
            self.best = val_loss
            self.bad_epochs = 0
            return False
        self.bad_epochs += 1
        return self.bad_epochs >= self.patience
```
4. **Alternate solution**:
```python
def early_stop(losses, patience=3, min_delta=0.0):
    best=float('inf'); bad=0
    for l in losses:
        if l < best-min_delta: best=l; bad=0
        else: bad += 1
        if bad>=patience: return True
    return False
```
5. **Time complexity**: O(1) per epoch.
6. **Space complexity**: O(1).
7. **Interview tip**: Discuss restoring best checkpoint on stop.

### Q213: Implement stratified train-test split for binary labels (variant)
1. **Problem statement**: Implement stratified train-test split for binary labels (variant).
2. **Explanation**: Preserve label distribution in each split.
3. **Working Python code**:
```python
import numpy as np

def stratified_split(X, y, test_size=0.2, seed=0):
    rng = np.random.default_rng(seed)
    y = np.asarray(y)
    idx0 = np.where(y==0)[0]; idx1 = np.where(y==1)[0]
    rng.shuffle(idx0); rng.shuffle(idx1)
    t0 = int(len(idx0)*test_size); t1 = int(len(idx1)*test_size)
    test_idx = np.concatenate([idx0[:t0], idx1[:t1]])
    train_idx = np.concatenate([idx0[t0:], idx1[t1:]])
    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]
```
4. **Alternate solution**:
```python
from sklearn.model_selection import train_test_split

def stratified_split(X, y, test_size=0.2, seed=0):
    return train_test_split(X, y, test_size=test_size, random_state=seed, stratify=y)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Explain why random split can bias minority classes.

### Q214: Compute confusion matrix for multiclass labels (variant)
1. **Problem statement**: Compute confusion matrix for multiclass labels (variant).
2. **Explanation**: Essential evaluation primitive.
3. **Working Python code**:
```python
import numpy as np

def confusion_matrix(y_true, y_pred, n_classes):
    cm = np.zeros((n_classes, n_classes), dtype=int)
    for t,p in zip(y_true, y_pred):
        cm[t,p] += 1
    return cm
```
4. **Alternate solution**:
```python
import numpy as np

def confusion_matrix(y_true, y_pred, n_classes):
    y_true = np.asarray(y_true); y_pred = np.asarray(y_pred)
    idx = y_true * n_classes + y_pred
    return np.bincount(idx, minlength=n_classes*n_classes).reshape(n_classes, n_classes)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(c^2).
7. **Interview tip**: Clarify label indexing assumptions.

### Q215: Implement early stopping callback logic (variant)
1. **Problem statement**: Implement early stopping callback logic (variant).
2. **Explanation**: Prevents overfitting during training.
3. **Working Python code**:
```python
class EarlyStopping:
    def __init__(self, patience=3, min_delta=0.0):
        self.patience = patience
        self.min_delta = min_delta
        self.best = float('inf')
        self.bad_epochs = 0
    def step(self, val_loss):
        if val_loss < self.best - self.min_delta:
            self.best = val_loss
            self.bad_epochs = 0
            return False
        self.bad_epochs += 1
        return self.bad_epochs >= self.patience
```
4. **Alternate solution**:
```python
def early_stop(losses, patience=3, min_delta=0.0):
    best=float('inf'); bad=0
    for l in losses:
        if l < best-min_delta: best=l; bad=0
        else: bad += 1
        if bad>=patience: return True
    return False
```
5. **Time complexity**: O(1) per epoch.
6. **Space complexity**: O(1).
7. **Interview tip**: Discuss restoring best checkpoint on stop.

### Q216: Implement stratified train-test split for binary labels (variant)
1. **Problem statement**: Implement stratified train-test split for binary labels (variant).
2. **Explanation**: Preserve label distribution in each split.
3. **Working Python code**:
```python
import numpy as np

def stratified_split(X, y, test_size=0.2, seed=0):
    rng = np.random.default_rng(seed)
    y = np.asarray(y)
    idx0 = np.where(y==0)[0]; idx1 = np.where(y==1)[0]
    rng.shuffle(idx0); rng.shuffle(idx1)
    t0 = int(len(idx0)*test_size); t1 = int(len(idx1)*test_size)
    test_idx = np.concatenate([idx0[:t0], idx1[:t1]])
    train_idx = np.concatenate([idx0[t0:], idx1[t1:]])
    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]
```
4. **Alternate solution**:
```python
from sklearn.model_selection import train_test_split

def stratified_split(X, y, test_size=0.2, seed=0):
    return train_test_split(X, y, test_size=test_size, random_state=seed, stratify=y)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Explain why random split can bias minority classes.

### Q217: Compute confusion matrix for multiclass labels (variant)
1. **Problem statement**: Compute confusion matrix for multiclass labels (variant).
2. **Explanation**: Essential evaluation primitive.
3. **Working Python code**:
```python
import numpy as np

def confusion_matrix(y_true, y_pred, n_classes):
    cm = np.zeros((n_classes, n_classes), dtype=int)
    for t,p in zip(y_true, y_pred):
        cm[t,p] += 1
    return cm
```
4. **Alternate solution**:
```python
import numpy as np

def confusion_matrix(y_true, y_pred, n_classes):
    y_true = np.asarray(y_true); y_pred = np.asarray(y_pred)
    idx = y_true * n_classes + y_pred
    return np.bincount(idx, minlength=n_classes*n_classes).reshape(n_classes, n_classes)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(c^2).
7. **Interview tip**: Clarify label indexing assumptions.

### Q218: Implement early stopping callback logic (variant)
1. **Problem statement**: Implement early stopping callback logic (variant).
2. **Explanation**: Prevents overfitting during training.
3. **Working Python code**:
```python
class EarlyStopping:
    def __init__(self, patience=3, min_delta=0.0):
        self.patience = patience
        self.min_delta = min_delta
        self.best = float('inf')
        self.bad_epochs = 0
    def step(self, val_loss):
        if val_loss < self.best - self.min_delta:
            self.best = val_loss
            self.bad_epochs = 0
            return False
        self.bad_epochs += 1
        return self.bad_epochs >= self.patience
```
4. **Alternate solution**:
```python
def early_stop(losses, patience=3, min_delta=0.0):
    best=float('inf'); bad=0
    for l in losses:
        if l < best-min_delta: best=l; bad=0
        else: bad += 1
        if bad>=patience: return True
    return False
```
5. **Time complexity**: O(1) per epoch.
6. **Space complexity**: O(1).
7. **Interview tip**: Discuss restoring best checkpoint on stop.

### Q219: Implement stratified train-test split for binary labels (variant)
1. **Problem statement**: Implement stratified train-test split for binary labels (variant).
2. **Explanation**: Preserve label distribution in each split.
3. **Working Python code**:
```python
import numpy as np

def stratified_split(X, y, test_size=0.2, seed=0):
    rng = np.random.default_rng(seed)
    y = np.asarray(y)
    idx0 = np.where(y==0)[0]; idx1 = np.where(y==1)[0]
    rng.shuffle(idx0); rng.shuffle(idx1)
    t0 = int(len(idx0)*test_size); t1 = int(len(idx1)*test_size)
    test_idx = np.concatenate([idx0[:t0], idx1[:t1]])
    train_idx = np.concatenate([idx0[t0:], idx1[t1:]])
    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]
```
4. **Alternate solution**:
```python
from sklearn.model_selection import train_test_split

def stratified_split(X, y, test_size=0.2, seed=0):
    return train_test_split(X, y, test_size=test_size, random_state=seed, stratify=y)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Explain why random split can bias minority classes.

### Q220: Compute confusion matrix for multiclass labels (variant)
1. **Problem statement**: Compute confusion matrix for multiclass labels (variant).
2. **Explanation**: Essential evaluation primitive.
3. **Working Python code**:
```python
import numpy as np

def confusion_matrix(y_true, y_pred, n_classes):
    cm = np.zeros((n_classes, n_classes), dtype=int)
    for t,p in zip(y_true, y_pred):
        cm[t,p] += 1
    return cm
```
4. **Alternate solution**:
```python
import numpy as np

def confusion_matrix(y_true, y_pred, n_classes):
    y_true = np.asarray(y_true); y_pred = np.asarray(y_pred)
    idx = y_true * n_classes + y_pred
    return np.bincount(idx, minlength=n_classes*n_classes).reshape(n_classes, n_classes)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(c^2).
7. **Interview tip**: Clarify label indexing assumptions.

### Q221: Implement early stopping callback logic (variant)
1. **Problem statement**: Implement early stopping callback logic (variant).
2. **Explanation**: Prevents overfitting during training.
3. **Working Python code**:
```python
class EarlyStopping:
    def __init__(self, patience=3, min_delta=0.0):
        self.patience = patience
        self.min_delta = min_delta
        self.best = float('inf')
        self.bad_epochs = 0
    def step(self, val_loss):
        if val_loss < self.best - self.min_delta:
            self.best = val_loss
            self.bad_epochs = 0
            return False
        self.bad_epochs += 1
        return self.bad_epochs >= self.patience
```
4. **Alternate solution**:
```python
def early_stop(losses, patience=3, min_delta=0.0):
    best=float('inf'); bad=0
    for l in losses:
        if l < best-min_delta: best=l; bad=0
        else: bad += 1
        if bad>=patience: return True
    return False
```
5. **Time complexity**: O(1) per epoch.
6. **Space complexity**: O(1).
7. **Interview tip**: Discuss restoring best checkpoint on stop.

### Q222: Implement stratified train-test split for binary labels (variant)
1. **Problem statement**: Implement stratified train-test split for binary labels (variant).
2. **Explanation**: Preserve label distribution in each split.
3. **Working Python code**:
```python
import numpy as np

def stratified_split(X, y, test_size=0.2, seed=0):
    rng = np.random.default_rng(seed)
    y = np.asarray(y)
    idx0 = np.where(y==0)[0]; idx1 = np.where(y==1)[0]
    rng.shuffle(idx0); rng.shuffle(idx1)
    t0 = int(len(idx0)*test_size); t1 = int(len(idx1)*test_size)
    test_idx = np.concatenate([idx0[:t0], idx1[:t1]])
    train_idx = np.concatenate([idx0[t0:], idx1[t1:]])
    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]
```
4. **Alternate solution**:
```python
from sklearn.model_selection import train_test_split

def stratified_split(X, y, test_size=0.2, seed=0):
    return train_test_split(X, y, test_size=test_size, random_state=seed, stratify=y)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Explain why random split can bias minority classes.

### Q223: Compute confusion matrix for multiclass labels (variant)
1. **Problem statement**: Compute confusion matrix for multiclass labels (variant).
2. **Explanation**: Essential evaluation primitive.
3. **Working Python code**:
```python
import numpy as np

def confusion_matrix(y_true, y_pred, n_classes):
    cm = np.zeros((n_classes, n_classes), dtype=int)
    for t,p in zip(y_true, y_pred):
        cm[t,p] += 1
    return cm
```
4. **Alternate solution**:
```python
import numpy as np

def confusion_matrix(y_true, y_pred, n_classes):
    y_true = np.asarray(y_true); y_pred = np.asarray(y_pred)
    idx = y_true * n_classes + y_pred
    return np.bincount(idx, minlength=n_classes*n_classes).reshape(n_classes, n_classes)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(c^2).
7. **Interview tip**: Clarify label indexing assumptions.

### Q224: Implement early stopping callback logic (variant)
1. **Problem statement**: Implement early stopping callback logic (variant).
2. **Explanation**: Prevents overfitting during training.
3. **Working Python code**:
```python
class EarlyStopping:
    def __init__(self, patience=3, min_delta=0.0):
        self.patience = patience
        self.min_delta = min_delta
        self.best = float('inf')
        self.bad_epochs = 0
    def step(self, val_loss):
        if val_loss < self.best - self.min_delta:
            self.best = val_loss
            self.bad_epochs = 0
            return False
        self.bad_epochs += 1
        return self.bad_epochs >= self.patience
```
4. **Alternate solution**:
```python
def early_stop(losses, patience=3, min_delta=0.0):
    best=float('inf'); bad=0
    for l in losses:
        if l < best-min_delta: best=l; bad=0
        else: bad += 1
        if bad>=patience: return True
    return False
```
5. **Time complexity**: O(1) per epoch.
6. **Space complexity**: O(1).
7. **Interview tip**: Discuss restoring best checkpoint on stop.

### Q225: Implement stratified train-test split for binary labels (variant)
1. **Problem statement**: Implement stratified train-test split for binary labels (variant).
2. **Explanation**: Preserve label distribution in each split.
3. **Working Python code**:
```python
import numpy as np

def stratified_split(X, y, test_size=0.2, seed=0):
    rng = np.random.default_rng(seed)
    y = np.asarray(y)
    idx0 = np.where(y==0)[0]; idx1 = np.where(y==1)[0]
    rng.shuffle(idx0); rng.shuffle(idx1)
    t0 = int(len(idx0)*test_size); t1 = int(len(idx1)*test_size)
    test_idx = np.concatenate([idx0[:t0], idx1[:t1]])
    train_idx = np.concatenate([idx0[t0:], idx1[t1:]])
    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]
```
4. **Alternate solution**:
```python
from sklearn.model_selection import train_test_split

def stratified_split(X, y, test_size=0.2, seed=0):
    return train_test_split(X, y, test_size=test_size, random_state=seed, stratify=y)
```
5. **Time complexity**: O(n).
6. **Space complexity**: O(n).
7. **Interview tip**: Explain why random split can bias minority classes.

## Python System Design

### Q226: Design a feature engineering pipeline for tabular churn modeling
1. **Problem statement**: Design a feature engineering pipeline for tabular churn modeling.
2. **Explanation**: Build stages: ingest raw events, validate schema, transform, aggregate, write feature store, and track lineage.
3. **Architecture / deep-dive note**: Architecture: raw zone -> validation -> feature jobs -> offline/online feature store. Scalability: partition by date/user, idempotent jobs, backfills. Trade-offs: freshness vs compute cost.
4. **Working Python code**:
```python
class FeaturePipeline:
    def __init__(self, source, validator, transformers, sink):
        self.source = source
        self.validator = validator
        self.transformers = transformers
        self.sink = sink
    def run(self, ds):
        df = self.source.read(ds)
        df = self.validator.validate(df)
        for t in self.transformers:
            df = t.transform(df)
        self.sink.write(ds, df)
        return {'dataset': ds, 'rows': len(df)}
```
5. **Alternate solution**:
```python
def run_pipeline(source, funcs, sink, ds):
    data = source(ds)
    for f in funcs:
        data = f(data)
    sink(ds, data)
    return True
```
6. **Time complexity**: O(n) transform pass per stage.
7. **Space complexity**: O(n).
8. **Interview tip**: Call out point-in-time correctness to avoid feature leakage.

### Q227: Design online model inference service with fallback model
1. **Problem statement**: Design online model inference service with fallback model.
2. **Explanation**: Separate request validation, feature fetch, model scoring, and fallback handling.
3. **Architecture / deep-dive note**: Architecture: API gateway -> feature retrieval -> model runtime -> response + logging. Scalability: autoscaling stateless workers + request batching. Trade-offs: consistency vs latency.
4. **Working Python code**:
```python
class InferenceService:
    def __init__(self, feature_store, model_registry, fallback_model):
        self.feature_store = feature_store
        self.model_registry = model_registry
        self.fallback_model = fallback_model
    def predict(self, entity_id, payload):
        feats = self.feature_store.get(entity_id) or payload
        model = self.model_registry.load('production')
        try:
            score = float(model.predict_proba([feats])[0][1])
        except Exception:
            score = float(self.fallback_model.predict([feats])[0])
        return {'score': score}
```
5. **Alternate solution**:
```python
def predict(features, model, fallback):
    try: return {'score': float(model.predict([features])[0])}
    except Exception: return {'score': float(fallback.predict([features])[0])}
```
6. **Time complexity**: Per request O(f).
7. **Space complexity**: O(f).
8. **Interview tip**: Discuss p95/p99 latency budget and feature-store timeout policies.

### Q228: Design batch prediction system for nightly demand forecasting
1. **Problem statement**: Design batch prediction system for nightly demand forecasting.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.

### Q229: Design streaming inference system for fraud detection
1. **Problem statement**: Design streaming inference system for fraud detection.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.

### Q230: Design ML experiment tracker with metric lineage
1. **Problem statement**: Design ML experiment tracker with metric lineage.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.

### Q231: Design model registry with stage transitions and approvals
1. **Problem statement**: Design model registry with stage transitions and approvals.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.

### Q232: Design ETL pipeline for clickstream sessionization
1. **Problem statement**: Design ETL pipeline for clickstream sessionization.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.

### Q233: Design real-time feature store with online/offline sync
1. **Problem statement**: Design real-time feature store with online/offline sync.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.

### Q234: Design drift detection service with alerting and rollback
1. **Problem statement**: Design drift detection service with alerting and rollback.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.

### Q235: Design training pipeline orchestration with retries
1. **Problem statement**: Design training pipeline orchestration with retries.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.

### Q236: Design data quality monitoring framework for ML tables
1. **Problem statement**: Design data quality monitoring framework for ML tables.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.

### Q237: Design embedding generation service with versioning
1. **Problem statement**: Design embedding generation service with versioning.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.

### Q238: Design multi-tenant model serving platform
1. **Problem statement**: Design multi-tenant model serving platform.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.

### Q239: Design canary rollout system for model deployment
1. **Problem statement**: Design canary rollout system for model deployment.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.

### Q240: Design prediction caching layer for low-latency APIs
1. **Problem statement**: Design prediction caching layer for low-latency APIs.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.

### Q241: Design asynchronous batch scoring API with job status
1. **Problem statement**: Design asynchronous batch scoring API with job status.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.

### Q242: Design event-driven retraining trigger service
1. **Problem statement**: Design event-driven retraining trigger service.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.

### Q243: Design model performance dashboard backend
1. **Problem statement**: Design model performance dashboard backend.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.

### Q244: Design privacy-preserving data anonymization service
1. **Problem statement**: Design privacy-preserving data anonymization service.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.

### Q245: Design schema evolution strategy for feature tables
1. **Problem statement**: Design schema evolution strategy for feature tables.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.

### Q246: Design dead-letter queue handling for failed inference events
1. **Problem statement**: Design dead-letter queue handling for failed inference events.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.

### Q247: Design A/B testing platform for model comparison
1. **Problem statement**: Design A/B testing platform for model comparison.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.

### Q248: Design recommendation candidate generation pipeline
1. **Problem statement**: Design recommendation candidate generation pipeline.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.

### Q249: Design OCR document processing pipeline
1. **Problem statement**: Design OCR document processing pipeline.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.

### Q250: Design voice command classification backend
1. **Problem statement**: Design voice command classification backend.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.

### Q251: Design geospatial demand heatmap inference service
1. **Problem statement**: Design geospatial demand heatmap inference service.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.

### Q252: Design cross-region failover for inference platform
1. **Problem statement**: Design cross-region failover for inference platform.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.

### Q253: Design cost-aware autoscaling policy for GPU inference
1. **Problem statement**: Design cost-aware autoscaling policy for GPU inference.
2. **Explanation**: Define services, storage boundaries, contracts, and reliability strategy before coding components.
3. **Architecture / deep-dive note**: Architecture: ingress -> processing -> storage -> serving -> monitoring. Scalability: horizontal workers, partitioning, idempotency. Trade-offs: latency vs cost vs consistency.
4. **Working Python code**:
```python
class ServiceDesign:
    def __init__(self, ingest, processor, store, monitor):
        self.ingest = ingest
        self.processor = processor
        self.store = store
        self.monitor = monitor
    def handle(self, payload):
        item = self.ingest.read(payload)
        result = self.processor.run(item)
        self.store.write(result)
        self.monitor.emit({'status':'ok'})
        return result
```
5. **Alternate solution**:
```python
def handle(payload, ingest_fn, process_fn, write_fn):
    item = ingest_fn(payload)
    result = process_fn(item)
    write_fn(result)
    return result
```
6. **Time complexity**: Depends on throughput and batch/window sizes.
7. **Space complexity**: Depends on buffering and storage replication.
8. **Interview tip**: Lead with SLOs, failure modes, and observability signals.
