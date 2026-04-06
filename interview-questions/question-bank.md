# 250+ Real Python Interview Questions for ML & AI Engineers

## Python Basics

### Q001: Find duplicate integers in a list while preserving first-seen order
1. **Question**: Find duplicate integers in a list while preserving first-seen order.
2. **Explanation**: Track seen values and duplicates separately so each duplicate appears once in output order.
3. **Working Python solution**:
```python
def find_duplicates(nums):
    seen, dup = set(), set()
    result = []
    for n in nums:
        if n in seen and n not in dup:
            dup.add(n)
            result.append(n)
        seen.add(n)
    return result
```
4. **Alternate solution**:
```python
from collections import Counter

def find_duplicates(nums):
    counts = Counter(nums)
    return [n for n in nums if counts[n] > 1 and nums.index(n) == nums.index(n)]
```
5. **Complexity analysis**: Time O(n), Space O(n).
6. **Interview tip**: Clarify whether duplicates should repeat in output or appear once.

### Q002: Check whether a string is a palindrome ignoring non-alphanumerics
1. **Question**: Check whether a string is a palindrome ignoring non-alphanumerics.
2. **Explanation**: Use two pointers and skip characters that are not letters or digits.
3. **Working Python solution**:
```python
def is_palindrome(text):
    i, j = 0, len(text) - 1
    while i < j:
        while i < j and not text[i].isalnum():
            i += 1
        while i < j and not text[j].isalnum():
            j -= 1
        if text[i].lower() != text[j].lower():
            return False
        i += 1
        j -= 1
    return True
```
4. **Alternate solution**:
```python
import re

def is_palindrome(text):
    s = re.sub(r'[^A-Za-z0-9]', '', text).lower()
    return s == s[::-1]
```
5. **Complexity analysis**: Time O(n), Space O(1) pointer approach.
6. **Interview tip**: Mention Unicode normalization if interviewer cares about international text.

### Q003: Return the first non-repeating character index
1. **Question**: Return the first non-repeating character index.
2. **Explanation**: Count each character, then scan original string for count 1.
3. **Working Python solution**:
```python
from collections import Counter

def first_unique_index(s):
    counts = Counter(s)
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1
```
4. **Alternate solution**:
```python
def first_unique_index(s):
    for i, ch in enumerate(s):
        if s.count(ch) == 1:
            return i
    return -1
```
5. **Complexity analysis**: Counter solution: O(n) time, O(k) space.
6. **Interview tip**: Discuss trade-off between one-pass count map and repeated scans.

### Q004: Implement run-length encoding for a string
1. **Question**: Implement run-length encoding for a string.
2. **Explanation**: Compress repeating characters into char+count format.
3. **Working Python solution**:
```python
def rle_encode(s):
    if not s:
        return ''
    out = []
    count = 1
    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i - 1]:
            count += 1
        else:
            out.append(f"{s[i-1]}{count}")
            count = 1
    return ''.join(out)
```
4. **Alternate solution**:
```python
from itertools import groupby

def rle_encode(s):
    return ''.join(f"{ch}{sum(1 for _ in grp)}" for ch, grp in groupby(s))
```
5. **Complexity analysis**: Time O(n), Space O(n).
6. **Interview tip**: Ask whether to keep single-count runs like a1 or just a.

### Q005: Convert a number to Roman numeral
1. **Question**: Convert a number to Roman numeral.
2. **Explanation**: Greedy subtraction with sorted numeral values.
3. **Working Python solution**:
```python
def int_to_roman(num):
    vals = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
    out = []
    for v, sym in vals:
        while num >= v:
            out.append(sym)
            num -= v
    return ''.join(out)
```
4. **Alternate solution**:
```python
def int_to_roman(num):
    thousands = ['', 'M', 'MM', 'MMM']
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    return thousands[num//1000] + hundreds[(num%1000)//100] + tens[(num%100)//10] + ones[num%10]
```
5. **Complexity analysis**: Time O(1), Space O(1) bounded symbols.
6. **Interview tip**: State valid input range explicitly (typically 1..3999).

### Q006: Compute factorial iteratively
1. **Question**: Compute factorial iteratively.
2. **Explanation**: Multiply values from 2..n.
3. **Working Python solution**:
```python
def factorial(n):
    if n < 0:
        raise ValueError('n must be non-negative')
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```
4. **Alternate solution**:
```python
def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)
```
5. **Complexity analysis**: O(n) time.
6. **Interview tip**: Explain recursion depth risk for large n.

### Q007: Generate first n Fibonacci numbers
1. **Question**: Generate first n Fibonacci numbers.
2. **Explanation**: Build sequence using previous two numbers.
3. **Working Python solution**:
```python
def fibonacci(n):
    if n <= 0:
        return []
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]
```
4. **Alternate solution**:
```python
def fibonacci(n):
    a = b = 1
    out = [0]
    for _ in range(n - 1):
        out.append(a)
        a, b = b, a + b
    return out
```
5. **Complexity analysis**: O(n) time O(n) space.
6. **Interview tip**: Confirm whether sequence starts with 0,1 or 1,1.

### Q008: Find maximum subarray sum (Kadane)
1. **Question**: Find maximum subarray sum (Kadane).
2. **Explanation**: Track best ending here and global best.
3. **Working Python solution**:
```python
def max_subarray(nums):
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
```
4. **Alternate solution**:
```python
def max_subarray(nums):
    best = float('-inf')
    for i in range(len(nums)):
        s = 0
        for j in range(i, len(nums)):
            s += nums[j]
            best = max(best, s)
    return best
```
5. **Complexity analysis**: Kadane O(n).
6. **Interview tip**: Interviewers expect Kadane after brute force discussion.

### Q009: Check if two strings are anagrams
1. **Question**: Check if two strings are anagrams.
2. **Explanation**: Compare character counts after normalization.
3. **Working Python solution**:
```python
from collections import Counter

def are_anagrams(a, b):
    return Counter(a.replace(' ','').lower()) == Counter(b.replace(' ','').lower())
```
4. **Alternate solution**:
```python
def are_anagrams(a, b):
    x = sorted(a.replace(' ','').lower())
    y = sorted(b.replace(' ','').lower())
    return x == y
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Ask whether spaces and case matter.

### Q010: Rotate list right by k
1. **Question**: Rotate list right by k.
2. **Explanation**: Use modulo and slicing.
3. **Working Python solution**:
```python
def rotate_right(nums, k):
    if not nums:
        return nums
    k %= len(nums)
    return nums[-k:] + nums[:-k]
```
4. **Alternate solution**:
```python
from collections import deque

def rotate_right(nums, k):
    d = deque(nums)
    d.rotate(k)
    return list(d)
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Mention in-place variant if needed.

### Q011: Find missing number from 0..n
1. **Question**: Find missing number from 0..n.
2. **Explanation**: Use arithmetic sum identity.
3. **Working Python solution**:
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
5. **Complexity analysis**: O(n).
6. **Interview tip**: Great chance to compare math vs XOR approach.

### Q012: Validate balanced parentheses
1. **Question**: Validate balanced parentheses.
2. **Explanation**: Stack open brackets and match closers.
3. **Working Python solution**:
```python
def is_valid_parentheses(s):
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
def is_valid_parentheses(s):
    prev = None
    while prev != s:
        prev = s
        s = s.replace('()','').replace('[]','').replace('{}','')
    return not s
```
5. **Complexity analysis**: Stack O(n).
6. **Interview tip**: Clarify whether non-bracket chars may appear.

### Q013: Find intersection of two lists with multiplicity
1. **Question**: Find intersection of two lists with multiplicity.
2. **Explanation**: Count one list then consume counts.
3. **Working Python solution**:
```python
from collections import Counter

def intersect(a, b):
    c = Counter(a)
    out = []
    for x in b:
        if c[x] > 0:
            out.append(x)
            c[x] -= 1
    return out
```
4. **Alternate solution**:
```python
def intersect(a,b):
    a.sort(); b.sort()
    i=j=0; out=[]
    while i<len(a) and j<len(b):
        if a[i]==b[j]: out.append(a[i]); i+=1; j+=1
        elif a[i]<b[j]: i+=1
        else: j+=1
    return out
```
5. **Complexity analysis**: O(n+m).
6. **Interview tip**: Mention multiplicity requirement explicitly.

### Q014: Group words by starting letter
1. **Question**: Group words by starting letter.
2. **Explanation**: Use dictionary accumulation.
3. **Working Python solution**:
```python
from collections import defaultdict

def group_by_first(words):
    out = defaultdict(list)
    for w in words:
        if w:
            out[w[0].lower()].append(w)
    return dict(out)
```
4. **Alternate solution**:
```python
def group_by_first(words):
    keys = sorted({w[0].lower() for w in words if w})
    return {k:[w for w in words if w and w[0].lower()==k] for k in keys}
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Discuss ordering guarantees if needed.

### Q015: Convert snake_case to camelCase
1. **Question**: Convert snake_case to camelCase.
2. **Explanation**: Split by underscore and title-case tail tokens.
3. **Working Python solution**:
```python
def snake_to_camel(name):
    parts = name.split('_')
    return parts[0] + ''.join(p.title() for p in parts[1:])
```
4. **Alternate solution**:
```python
import re

def snake_to_camel(name):
    return re.sub(r'_([a-zA-Z])', lambda m: m.group(1).upper(), name)
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Edge case: consecutive underscores.

### Q016: Count vowels in a string
1. **Question**: Count vowels in a string.
2. **Explanation**: Membership test over lowercase characters.
3. **Working Python solution**:
```python
def count_vowels(s):
    vowels = set('aeiou')
    return sum(ch.lower() in vowels for ch in s)
```
4. **Alternate solution**:
```python
import re

def count_vowels(s):
    return len(re.findall(r'[aeiouAEIOU]', s))
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Talk about unicode vowel handling if asked.

### Q017: Find longest common prefix
1. **Question**: Find longest common prefix.
2. **Explanation**: Shrink prefix until all strings start with it.
3. **Working Python solution**:
```python
def longest_common_prefix(words):
    if not words:
        return ''
    prefix = words[0]
    for w in words[1:]:
        while not w.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ''
    return prefix
```
4. **Alternate solution**:
```python
def longest_common_prefix(words):
    if not words: return ''
    s1, s2 = min(words), max(words)
    i = 0
    while i < len(s1) and s1[i] == s2[i]:
        i += 1
    return s1[:i]
```
5. **Complexity analysis**: O(S).
6. **Interview tip**: Useful trick: compare lexicographic min/max only.

### Q018: Merge two sorted lists
1. **Question**: Merge two sorted lists.
2. **Explanation**: Two-pointer merge routine.
3. **Working Python solution**:
```python
def merge_sorted(a, b):
    i=j=0; out=[]
    while i<len(a) and j<len(b):
        if a[i] <= b[j]: out.append(a[i]); i+=1
        else: out.append(b[j]); j+=1
    out.extend(a[i:]); out.extend(b[j:])
    return out
```
4. **Alternate solution**:
```python
import heapq

def merge_sorted(a,b):
    return list(heapq.merge(a,b))
```
5. **Complexity analysis**: O(n+m).
6. **Interview tip**: Mention this is same primitive used in merge sort.

### Q019: Find second largest unique number
1. **Question**: Find second largest unique number.
2. **Explanation**: Track top two distinct values.
3. **Working Python solution**:
```python
def second_largest(nums):
    first = second = float('-inf')
    for n in nums:
        if n > first:
            first, second = n, first
        elif first > n > second:
            second = n
    return None if second == float('-inf') else second
```
4. **Alternate solution**:
```python
def second_largest(nums):
    vals = sorted(set(nums))
    return vals[-2] if len(vals) >= 2 else None
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Ask behavior when fewer than two distinct values exist.

### Q020: Remove duplicates from sorted list in-place count
1. **Question**: Remove duplicates from sorted list in-place count.
2. **Explanation**: Overwrite array with unique frontier index.
3. **Working Python solution**:
```python
def dedupe_sorted(nums):
    if not nums:
        return 0
    w = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[w-1]:
            nums[w] = nums[i]
            w += 1
    return w
```
4. **Alternate solution**:
```python
def dedupe_sorted(nums):
    nums[:] = sorted(set(nums))
    return len(nums)
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: In-place constraint matters for this classic.

### Q021: Check if list is monotonic
1. **Question**: Check if list is monotonic.
2. **Explanation**: Track nondecreasing and nonincreasing flags.
3. **Working Python solution**:
```python
def is_monotonic(nums):
    inc = dec = True
    for i in range(1, len(nums)):
        inc &= nums[i] >= nums[i-1]
        dec &= nums[i] <= nums[i-1]
    return inc or dec
```
4. **Alternate solution**:
```python
def is_monotonic(nums):
    return nums == sorted(nums) or nums == sorted(nums, reverse=True)
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Good for discussing one-pass invariant reasoning.

### Q022: Two-sum indices
1. **Question**: Two-sum indices.
2. **Explanation**: Store prior complements in hash map.
3. **Working Python solution**:
```python
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target-x], i]
        seen[x] = i
    return []
```
4. **Alternate solution**:
```python
def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Clarify if exactly one answer exists.

### Q023: Find majority element
1. **Question**: Find majority element.
2. **Explanation**: Boyer-Moore voting algorithm.
3. **Working Python solution**:
```python
def majority_element(nums):
    cand = cnt = 0
    for n in nums:
        if cnt == 0:
            cand = n
        cnt += 1 if n == cand else -1
    return cand
```
4. **Alternate solution**:
```python
from collections import Counter

def majority_element(nums):
    return Counter(nums).most_common(1)[0][0]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Mention second pass if majority is not guaranteed.

### Q024: Find product of array except self
1. **Question**: Find product of array except self.
2. **Explanation**: Prefix and suffix products without division.
3. **Working Python solution**:
```python
def product_except_self(nums):
    n = len(nums)
    out = [1] * n
    p = 1
    for i in range(n):
        out[i] = p
        p *= nums[i]
    s = 1
    for i in range(n-1, -1, -1):
        out[i] *= s
        s *= nums[i]
    return out
```
4. **Alternate solution**:
```python
def product_except_self(nums):
    total = 1
    zero_count = nums.count(0)
    for x in nums:
        if x != 0:
            total *= x
    return [0 if zero_count > 1 else (total if x == 0 else (0 if zero_count else total//x)) for x in nums]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Be explicit on zero handling and division constraints.

### Q025: Sort characters by frequency
1. **Question**: Sort characters by frequency.
2. **Explanation**: Frequency map then sort by count descending.
3. **Working Python solution**:
```python
from collections import Counter

def frequency_sort(s):
    counts = Counter(s)
    return ''.join(ch * cnt for ch, cnt in sorted(counts.items(), key=lambda x: -x[1]))
```
4. **Alternate solution**:
```python
from collections import Counter
import heapq

def frequency_sort(s):
    c = Counter(s)
    heap = [(-v, k) for k, v in c.items()]
    heapq.heapify(heap)
    out = []
    while heap:
        v, k = heapq.heappop(heap)
        out.append(k * (-v))
    return ''.join(out)
```
5. **Complexity analysis**: O(n log k).
6. **Interview tip**: Mention tie-breaking is often unspecified.

### Q026: Check if ransom note can be built from magazine
1. **Question**: Check if ransom note can be built from magazine.
2. **Explanation**: Ensure each needed char count is available.
3. **Working Python solution**:
```python
from collections import Counter

def can_construct(note, magazine):
    need = Counter(note)
    have = Counter(magazine)
    return all(have[c] >= n for c, n in need.items())
```
4. **Alternate solution**:
```python
def can_construct(note, magazine):
    mag = list(magazine)
    for ch in note:
        if ch in mag:
            mag.remove(ch)
        else:
            return False
    return True
```
5. **Complexity analysis**: Counter O(n).
6. **Interview tip**: Great example for counting vs naive removal complexity.

### Q027: Determine if integer is power of two
1. **Question**: Determine if integer is power of two.
2. **Explanation**: Power of two has single set bit.
3. **Working Python solution**:
```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
```
4. **Alternate solution**:
```python
def is_power_of_two(n):
    if n <= 0:
        return False
    while n % 2 == 0:
        n //= 2
    return n == 1
```
5. **Complexity analysis**: Bit trick O(1).
6. **Interview tip**: Bit-manipulation follow-up appears often.

## Data Structures

### Q028: Implement LRU Cache with O(1) get/put
1. **Question**: Implement LRU Cache with O(1) get/put.
2. **Explanation**: Combine doubly linked list for recency with hash map for nodes.
3. **Working Python solution**:
```python
class Node:
    def __init__(self, k=0, v=0):
        self.k, self.v = k, v
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.map = {}
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p

    def _add_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._add_front(node)
        return node.v

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.v = value
            self._remove(node)
            self._add_front(node)
            return
        if len(self.map) == self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.k]
        node = Node(key, value)
        self.map[key] = node
        self._add_front(node)
```
4. **Alternate solution**:
```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.od = OrderedDict()

    def get(self, key):
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key, value):
        if key in self.od:
            self.od.move_to_end(key)
        self.od[key] = value
        if len(self.od) > self.cap:
            self.od.popitem(last=False)
```
5. **Complexity analysis**: O(1) average.
6. **Interview tip**: Be ready to explain why list+dict alone is insufficient without node pointers.

### Q029: Evaluate Reverse Polish Notation
1. **Question**: Evaluate Reverse Polish Notation.
2. **Explanation**: Use stack: push numbers, pop operands for operators.
3. **Working Python solution**:
```python
def eval_rpn(tokens):
    st = []
    for t in tokens:
        if t in '+-*/':
            b, a = st.pop(), st.pop()
            if t == '+': st.append(a + b)
            elif t == '-': st.append(a - b)
            elif t == '*': st.append(a * b)
            else: st.append(int(a / b))
        else:
            st.append(int(t))
    return st[-1]
```
4. **Alternate solution**:
```python
import operator

def eval_rpn(tokens):
    ops = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':lambda a,b:int(a/b)}
    st=[]
    for t in tokens:
        if t in ops:
            b,a=st.pop(),st.pop(); st.append(ops[t](a,b))
        else: st.append(int(t))
    return st.pop()
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Clarify integer division behavior for negatives.

### Q030: Data-structure variant: Return the first non-repeating character index
1. **Question**: Data-structure variant: Return the first non-repeating character index.
2. **Explanation**: Count each character, then scan original string for count 1. Use an explicit structure-focused discussion.
3. **Working Python solution**:
```python
from collections import Counter

def first_unique_index(s):
    counts = Counter(s)
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1
```
4. **Alternate solution**:
```python
def first_unique_index(s):
    for i, ch in enumerate(s):
        if s.count(ch) == 1:
            return i
    return -1
```
5. **Complexity analysis**: Counter solution: O(n) time, O(k) space.
6. **Interview tip**: Discuss trade-off between one-pass count map and repeated scans.

### Q031: Data-structure variant: Implement run-length encoding for a string
1. **Question**: Data-structure variant: Implement run-length encoding for a string.
2. **Explanation**: Compress repeating characters into char+count format. Use an explicit structure-focused discussion.
3. **Working Python solution**:
```python
def rle_encode(s):
    if not s:
        return ''
    out = []
    count = 1
    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i - 1]:
            count += 1
        else:
            out.append(f"{s[i-1]}{count}")
            count = 1
    return ''.join(out)
```
4. **Alternate solution**:
```python
from itertools import groupby

def rle_encode(s):
    return ''.join(f"{ch}{sum(1 for _ in grp)}" for ch, grp in groupby(s))
```
5. **Complexity analysis**: Time O(n), Space O(n).
6. **Interview tip**: Ask whether to keep single-count runs like a1 or just a.

### Q032: Data-structure variant: Convert a number to Roman numeral
1. **Question**: Data-structure variant: Convert a number to Roman numeral.
2. **Explanation**: Greedy subtraction with sorted numeral values. Use an explicit structure-focused discussion.
3. **Working Python solution**:
```python
def int_to_roman(num):
    vals = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
    out = []
    for v, sym in vals:
        while num >= v:
            out.append(sym)
            num -= v
    return ''.join(out)
```
4. **Alternate solution**:
```python
def int_to_roman(num):
    thousands = ['', 'M', 'MM', 'MMM']
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    return thousands[num//1000] + hundreds[(num%1000)//100] + tens[(num%100)//10] + ones[num%10]
```
5. **Complexity analysis**: Time O(1), Space O(1) bounded symbols.
6. **Interview tip**: State valid input range explicitly (typically 1..3999).

### Q033: Data-structure variant: Compute factorial iteratively
1. **Question**: Data-structure variant: Compute factorial iteratively.
2. **Explanation**: Multiply values from 2..n. Use an explicit structure-focused discussion.
3. **Working Python solution**:
```python
def factorial(n):
    if n < 0:
        raise ValueError('n must be non-negative')
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```
4. **Alternate solution**:
```python
def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)
```
5. **Complexity analysis**: O(n) time.
6. **Interview tip**: Explain recursion depth risk for large n.

### Q034: Data-structure variant: Generate first n Fibonacci numbers
1. **Question**: Data-structure variant: Generate first n Fibonacci numbers.
2. **Explanation**: Build sequence using previous two numbers. Use an explicit structure-focused discussion.
3. **Working Python solution**:
```python
def fibonacci(n):
    if n <= 0:
        return []
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]
```
4. **Alternate solution**:
```python
def fibonacci(n):
    a = b = 1
    out = [0]
    for _ in range(n - 1):
        out.append(a)
        a, b = b, a + b
    return out
```
5. **Complexity analysis**: O(n) time O(n) space.
6. **Interview tip**: Confirm whether sequence starts with 0,1 or 1,1.

### Q035: Data-structure variant: Find maximum subarray sum (Kadane)
1. **Question**: Data-structure variant: Find maximum subarray sum (Kadane).
2. **Explanation**: Track best ending here and global best. Use an explicit structure-focused discussion.
3. **Working Python solution**:
```python
def max_subarray(nums):
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
```
4. **Alternate solution**:
```python
def max_subarray(nums):
    best = float('-inf')
    for i in range(len(nums)):
        s = 0
        for j in range(i, len(nums)):
            s += nums[j]
            best = max(best, s)
    return best
```
5. **Complexity analysis**: Kadane O(n).
6. **Interview tip**: Interviewers expect Kadane after brute force discussion.

### Q036: Data-structure variant: Check if two strings are anagrams
1. **Question**: Data-structure variant: Check if two strings are anagrams.
2. **Explanation**: Compare character counts after normalization. Use an explicit structure-focused discussion.
3. **Working Python solution**:
```python
from collections import Counter

def are_anagrams(a, b):
    return Counter(a.replace(' ','').lower()) == Counter(b.replace(' ','').lower())
```
4. **Alternate solution**:
```python
def are_anagrams(a, b):
    x = sorted(a.replace(' ','').lower())
    y = sorted(b.replace(' ','').lower())
    return x == y
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Ask whether spaces and case matter.

### Q037: Data-structure variant: Rotate list right by k
1. **Question**: Data-structure variant: Rotate list right by k.
2. **Explanation**: Use modulo and slicing. Use an explicit structure-focused discussion.
3. **Working Python solution**:
```python
def rotate_right(nums, k):
    if not nums:
        return nums
    k %= len(nums)
    return nums[-k:] + nums[:-k]
```
4. **Alternate solution**:
```python
from collections import deque

def rotate_right(nums, k):
    d = deque(nums)
    d.rotate(k)
    return list(d)
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Mention in-place variant if needed.

### Q038: Data-structure variant: Find missing number from 0..n
1. **Question**: Data-structure variant: Find missing number from 0..n.
2. **Explanation**: Use arithmetic sum identity. Use an explicit structure-focused discussion.
3. **Working Python solution**:
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
5. **Complexity analysis**: O(n).
6. **Interview tip**: Great chance to compare math vs XOR approach.

### Q039: Data-structure variant: Validate balanced parentheses
1. **Question**: Data-structure variant: Validate balanced parentheses.
2. **Explanation**: Stack open brackets and match closers. Use an explicit structure-focused discussion.
3. **Working Python solution**:
```python
def is_valid_parentheses(s):
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
def is_valid_parentheses(s):
    prev = None
    while prev != s:
        prev = s
        s = s.replace('()','').replace('[]','').replace('{}','')
    return not s
```
5. **Complexity analysis**: Stack O(n).
6. **Interview tip**: Clarify whether non-bracket chars may appear.

### Q040: Data-structure variant: Find intersection of two lists with multiplicity
1. **Question**: Data-structure variant: Find intersection of two lists with multiplicity.
2. **Explanation**: Count one list then consume counts. Use an explicit structure-focused discussion.
3. **Working Python solution**:
```python
from collections import Counter

def intersect(a, b):
    c = Counter(a)
    out = []
    for x in b:
        if c[x] > 0:
            out.append(x)
            c[x] -= 1
    return out
```
4. **Alternate solution**:
```python
def intersect(a,b):
    a.sort(); b.sort()
    i=j=0; out=[]
    while i<len(a) and j<len(b):
        if a[i]==b[j]: out.append(a[i]); i+=1; j+=1
        elif a[i]<b[j]: i+=1
        else: j+=1
    return out
```
5. **Complexity analysis**: O(n+m).
6. **Interview tip**: Mention multiplicity requirement explicitly.

### Q041: Data-structure variant: Group words by starting letter
1. **Question**: Data-structure variant: Group words by starting letter.
2. **Explanation**: Use dictionary accumulation. Use an explicit structure-focused discussion.
3. **Working Python solution**:
```python
from collections import defaultdict

def group_by_first(words):
    out = defaultdict(list)
    for w in words:
        if w:
            out[w[0].lower()].append(w)
    return dict(out)
```
4. **Alternate solution**:
```python
def group_by_first(words):
    keys = sorted({w[0].lower() for w in words if w})
    return {k:[w for w in words if w and w[0].lower()==k] for k in keys}
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Discuss ordering guarantees if needed.

### Q042: Data-structure variant: Convert snake_case to camelCase
1. **Question**: Data-structure variant: Convert snake_case to camelCase.
2. **Explanation**: Split by underscore and title-case tail tokens. Use an explicit structure-focused discussion.
3. **Working Python solution**:
```python
def snake_to_camel(name):
    parts = name.split('_')
    return parts[0] + ''.join(p.title() for p in parts[1:])
```
4. **Alternate solution**:
```python
import re

def snake_to_camel(name):
    return re.sub(r'_([a-zA-Z])', lambda m: m.group(1).upper(), name)
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Edge case: consecutive underscores.

### Q043: Data-structure variant: Count vowels in a string
1. **Question**: Data-structure variant: Count vowels in a string.
2. **Explanation**: Membership test over lowercase characters. Use an explicit structure-focused discussion.
3. **Working Python solution**:
```python
def count_vowels(s):
    vowels = set('aeiou')
    return sum(ch.lower() in vowels for ch in s)
```
4. **Alternate solution**:
```python
import re

def count_vowels(s):
    return len(re.findall(r'[aeiouAEIOU]', s))
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Talk about unicode vowel handling if asked.

### Q044: Data-structure variant: Find longest common prefix
1. **Question**: Data-structure variant: Find longest common prefix.
2. **Explanation**: Shrink prefix until all strings start with it. Use an explicit structure-focused discussion.
3. **Working Python solution**:
```python
def longest_common_prefix(words):
    if not words:
        return ''
    prefix = words[0]
    for w in words[1:]:
        while not w.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ''
    return prefix
```
4. **Alternate solution**:
```python
def longest_common_prefix(words):
    if not words: return ''
    s1, s2 = min(words), max(words)
    i = 0
    while i < len(s1) and s1[i] == s2[i]:
        i += 1
    return s1[:i]
```
5. **Complexity analysis**: O(S).
6. **Interview tip**: Useful trick: compare lexicographic min/max only.

### Q045: Data-structure variant: Merge two sorted lists
1. **Question**: Data-structure variant: Merge two sorted lists.
2. **Explanation**: Two-pointer merge routine. Use an explicit structure-focused discussion.
3. **Working Python solution**:
```python
def merge_sorted(a, b):
    i=j=0; out=[]
    while i<len(a) and j<len(b):
        if a[i] <= b[j]: out.append(a[i]); i+=1
        else: out.append(b[j]); j+=1
    out.extend(a[i:]); out.extend(b[j:])
    return out
```
4. **Alternate solution**:
```python
import heapq

def merge_sorted(a,b):
    return list(heapq.merge(a,b))
```
5. **Complexity analysis**: O(n+m).
6. **Interview tip**: Mention this is same primitive used in merge sort.

### Q046: Data-structure variant: Find second largest unique number
1. **Question**: Data-structure variant: Find second largest unique number.
2. **Explanation**: Track top two distinct values. Use an explicit structure-focused discussion.
3. **Working Python solution**:
```python
def second_largest(nums):
    first = second = float('-inf')
    for n in nums:
        if n > first:
            first, second = n, first
        elif first > n > second:
            second = n
    return None if second == float('-inf') else second
```
4. **Alternate solution**:
```python
def second_largest(nums):
    vals = sorted(set(nums))
    return vals[-2] if len(vals) >= 2 else None
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Ask behavior when fewer than two distinct values exist.

### Q047: Data-structure variant: Remove duplicates from sorted list in-place count
1. **Question**: Data-structure variant: Remove duplicates from sorted list in-place count.
2. **Explanation**: Overwrite array with unique frontier index. Use an explicit structure-focused discussion.
3. **Working Python solution**:
```python
def dedupe_sorted(nums):
    if not nums:
        return 0
    w = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[w-1]:
            nums[w] = nums[i]
            w += 1
    return w
```
4. **Alternate solution**:
```python
def dedupe_sorted(nums):
    nums[:] = sorted(set(nums))
    return len(nums)
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: In-place constraint matters for this classic.

### Q048: Data-structure variant: Check if list is monotonic
1. **Question**: Data-structure variant: Check if list is monotonic.
2. **Explanation**: Track nondecreasing and nonincreasing flags. Use an explicit structure-focused discussion.
3. **Working Python solution**:
```python
def is_monotonic(nums):
    inc = dec = True
    for i in range(1, len(nums)):
        inc &= nums[i] >= nums[i-1]
        dec &= nums[i] <= nums[i-1]
    return inc or dec
```
4. **Alternate solution**:
```python
def is_monotonic(nums):
    return nums == sorted(nums) or nums == sorted(nums, reverse=True)
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Good for discussing one-pass invariant reasoning.

### Q049: Data-structure variant: Two-sum indices
1. **Question**: Data-structure variant: Two-sum indices.
2. **Explanation**: Store prior complements in hash map. Use an explicit structure-focused discussion.
3. **Working Python solution**:
```python
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target-x], i]
        seen[x] = i
    return []
```
4. **Alternate solution**:
```python
def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Clarify if exactly one answer exists.

### Q050: Data-structure variant: Find majority element
1. **Question**: Data-structure variant: Find majority element.
2. **Explanation**: Boyer-Moore voting algorithm. Use an explicit structure-focused discussion.
3. **Working Python solution**:
```python
def majority_element(nums):
    cand = cnt = 0
    for n in nums:
        if cnt == 0:
            cand = n
        cnt += 1 if n == cand else -1
    return cand
```
4. **Alternate solution**:
```python
from collections import Counter

def majority_element(nums):
    return Counter(nums).most_common(1)[0][0]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Mention second pass if majority is not guaranteed.

### Q051: Data-structure variant: Find product of array except self
1. **Question**: Data-structure variant: Find product of array except self.
2. **Explanation**: Prefix and suffix products without division. Use an explicit structure-focused discussion.
3. **Working Python solution**:
```python
def product_except_self(nums):
    n = len(nums)
    out = [1] * n
    p = 1
    for i in range(n):
        out[i] = p
        p *= nums[i]
    s = 1
    for i in range(n-1, -1, -1):
        out[i] *= s
        s *= nums[i]
    return out
```
4. **Alternate solution**:
```python
def product_except_self(nums):
    total = 1
    zero_count = nums.count(0)
    for x in nums:
        if x != 0:
            total *= x
    return [0 if zero_count > 1 else (total if x == 0 else (0 if zero_count else total//x)) for x in nums]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Be explicit on zero handling and division constraints.

### Q052: Data-structure variant: Sort characters by frequency
1. **Question**: Data-structure variant: Sort characters by frequency.
2. **Explanation**: Frequency map then sort by count descending. Use an explicit structure-focused discussion.
3. **Working Python solution**:
```python
from collections import Counter

def frequency_sort(s):
    counts = Counter(s)
    return ''.join(ch * cnt for ch, cnt in sorted(counts.items(), key=lambda x: -x[1]))
```
4. **Alternate solution**:
```python
from collections import Counter
import heapq

def frequency_sort(s):
    c = Counter(s)
    heap = [(-v, k) for k, v in c.items()]
    heapq.heapify(heap)
    out = []
    while heap:
        v, k = heapq.heappop(heap)
        out.append(k * (-v))
    return ''.join(out)
```
5. **Complexity analysis**: O(n log k).
6. **Interview tip**: Mention tie-breaking is often unspecified.

### Q053: Data-structure variant: Check if ransom note can be built from magazine
1. **Question**: Data-structure variant: Check if ransom note can be built from magazine.
2. **Explanation**: Ensure each needed char count is available. Use an explicit structure-focused discussion.
3. **Working Python solution**:
```python
from collections import Counter

def can_construct(note, magazine):
    need = Counter(note)
    have = Counter(magazine)
    return all(have[c] >= n for c, n in need.items())
```
4. **Alternate solution**:
```python
def can_construct(note, magazine):
    mag = list(magazine)
    for ch in note:
        if ch in mag:
            mag.remove(ch)
        else:
            return False
    return True
```
5. **Complexity analysis**: Counter O(n).
6. **Interview tip**: Great example for counting vs naive removal complexity.

### Q054: Data-structure variant: Determine if integer is power of two
1. **Question**: Data-structure variant: Determine if integer is power of two.
2. **Explanation**: Power of two has single set bit. Use an explicit structure-focused discussion.
3. **Working Python solution**:
```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
```
4. **Alternate solution**:
```python
def is_power_of_two(n):
    if n <= 0:
        return False
    while n % 2 == 0:
        n //= 2
    return n == 1
```
5. **Complexity analysis**: Bit trick O(1).
6. **Interview tip**: Bit-manipulation follow-up appears often.

## Functions

### Q055: Function design challenge 1: Implement memoized Fibonacci using decorator
1. **Question**: Function design challenge 1: Implement memoized Fibonacci using decorator.
2. **Explanation**: Demonstrates higher-order functions and closure state.
3. **Working Python solution**:
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```
4. **Alternate solution**:
```python
def fib(n, memo=None):
    memo = memo or {0:0,1:1}
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Explain purity and cache invalidation trade-offs.

### Q056: Function design challenge 2: Write curry function for two-argument functions
1. **Question**: Function design challenge 2: Write curry function for two-argument functions.
2. **Explanation**: Return nested function capturing first argument.
3. **Working Python solution**:
```python
def curry2(fn):
    def first(a):
        def second(b):
            return fn(a, b)
        return second
    return first
```
4. **Alternate solution**:
```python
from functools import partial

def curry2(fn):
    return lambda a: partial(fn, a)
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Good moment to discuss closures and free variables.

### Q057: Function design challenge 3: Implement custom map function
1. **Question**: Function design challenge 3: Implement custom map function.
2. **Explanation**: Apply function lazily over iterable.
3. **Working Python solution**:
```python
def my_map(fn, iterable):
    for x in iterable:
        yield fn(x)
```
4. **Alternate solution**:
```python
def my_map(fn, iterable):
    return [fn(x) for x in iterable]
```
5. **Complexity analysis**: Generator O(n).
6. **Interview tip**: Mention iterator vs eager list trade-off.

### Q058: Function design challenge 4: Implement memoized Fibonacci using decorator
1. **Question**: Function design challenge 4: Implement memoized Fibonacci using decorator.
2. **Explanation**: Demonstrates higher-order functions and closure state.
3. **Working Python solution**:
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```
4. **Alternate solution**:
```python
def fib(n, memo=None):
    memo = memo or {0:0,1:1}
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Explain purity and cache invalidation trade-offs.

### Q059: Function design challenge 5: Write curry function for two-argument functions
1. **Question**: Function design challenge 5: Write curry function for two-argument functions.
2. **Explanation**: Return nested function capturing first argument.
3. **Working Python solution**:
```python
def curry2(fn):
    def first(a):
        def second(b):
            return fn(a, b)
        return second
    return first
```
4. **Alternate solution**:
```python
from functools import partial

def curry2(fn):
    return lambda a: partial(fn, a)
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Good moment to discuss closures and free variables.

### Q060: Function design challenge 6: Implement custom map function
1. **Question**: Function design challenge 6: Implement custom map function.
2. **Explanation**: Apply function lazily over iterable.
3. **Working Python solution**:
```python
def my_map(fn, iterable):
    for x in iterable:
        yield fn(x)
```
4. **Alternate solution**:
```python
def my_map(fn, iterable):
    return [fn(x) for x in iterable]
```
5. **Complexity analysis**: Generator O(n).
6. **Interview tip**: Mention iterator vs eager list trade-off.

### Q061: Function design challenge 7: Implement memoized Fibonacci using decorator
1. **Question**: Function design challenge 7: Implement memoized Fibonacci using decorator.
2. **Explanation**: Demonstrates higher-order functions and closure state.
3. **Working Python solution**:
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```
4. **Alternate solution**:
```python
def fib(n, memo=None):
    memo = memo or {0:0,1:1}
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Explain purity and cache invalidation trade-offs.

### Q062: Function design challenge 8: Write curry function for two-argument functions
1. **Question**: Function design challenge 8: Write curry function for two-argument functions.
2. **Explanation**: Return nested function capturing first argument.
3. **Working Python solution**:
```python
def curry2(fn):
    def first(a):
        def second(b):
            return fn(a, b)
        return second
    return first
```
4. **Alternate solution**:
```python
from functools import partial

def curry2(fn):
    return lambda a: partial(fn, a)
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Good moment to discuss closures and free variables.

### Q063: Function design challenge 9: Implement custom map function
1. **Question**: Function design challenge 9: Implement custom map function.
2. **Explanation**: Apply function lazily over iterable.
3. **Working Python solution**:
```python
def my_map(fn, iterable):
    for x in iterable:
        yield fn(x)
```
4. **Alternate solution**:
```python
def my_map(fn, iterable):
    return [fn(x) for x in iterable]
```
5. **Complexity analysis**: Generator O(n).
6. **Interview tip**: Mention iterator vs eager list trade-off.

### Q064: Function design challenge 10: Implement memoized Fibonacci using decorator
1. **Question**: Function design challenge 10: Implement memoized Fibonacci using decorator.
2. **Explanation**: Demonstrates higher-order functions and closure state.
3. **Working Python solution**:
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```
4. **Alternate solution**:
```python
def fib(n, memo=None):
    memo = memo or {0:0,1:1}
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Explain purity and cache invalidation trade-offs.

### Q065: Function design challenge 11: Write curry function for two-argument functions
1. **Question**: Function design challenge 11: Write curry function for two-argument functions.
2. **Explanation**: Return nested function capturing first argument.
3. **Working Python solution**:
```python
def curry2(fn):
    def first(a):
        def second(b):
            return fn(a, b)
        return second
    return first
```
4. **Alternate solution**:
```python
from functools import partial

def curry2(fn):
    return lambda a: partial(fn, a)
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Good moment to discuss closures and free variables.

### Q066: Function design challenge 12: Implement custom map function
1. **Question**: Function design challenge 12: Implement custom map function.
2. **Explanation**: Apply function lazily over iterable.
3. **Working Python solution**:
```python
def my_map(fn, iterable):
    for x in iterable:
        yield fn(x)
```
4. **Alternate solution**:
```python
def my_map(fn, iterable):
    return [fn(x) for x in iterable]
```
5. **Complexity analysis**: Generator O(n).
6. **Interview tip**: Mention iterator vs eager list trade-off.

### Q067: Function design challenge 13: Implement memoized Fibonacci using decorator
1. **Question**: Function design challenge 13: Implement memoized Fibonacci using decorator.
2. **Explanation**: Demonstrates higher-order functions and closure state.
3. **Working Python solution**:
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```
4. **Alternate solution**:
```python
def fib(n, memo=None):
    memo = memo or {0:0,1:1}
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Explain purity and cache invalidation trade-offs.

### Q068: Function design challenge 14: Write curry function for two-argument functions
1. **Question**: Function design challenge 14: Write curry function for two-argument functions.
2. **Explanation**: Return nested function capturing first argument.
3. **Working Python solution**:
```python
def curry2(fn):
    def first(a):
        def second(b):
            return fn(a, b)
        return second
    return first
```
4. **Alternate solution**:
```python
from functools import partial

def curry2(fn):
    return lambda a: partial(fn, a)
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Good moment to discuss closures and free variables.

### Q069: Function design challenge 15: Implement custom map function
1. **Question**: Function design challenge 15: Implement custom map function.
2. **Explanation**: Apply function lazily over iterable.
3. **Working Python solution**:
```python
def my_map(fn, iterable):
    for x in iterable:
        yield fn(x)
```
4. **Alternate solution**:
```python
def my_map(fn, iterable):
    return [fn(x) for x in iterable]
```
5. **Complexity analysis**: Generator O(n).
6. **Interview tip**: Mention iterator vs eager list trade-off.

### Q070: Function design challenge 16: Implement memoized Fibonacci using decorator
1. **Question**: Function design challenge 16: Implement memoized Fibonacci using decorator.
2. **Explanation**: Demonstrates higher-order functions and closure state.
3. **Working Python solution**:
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```
4. **Alternate solution**:
```python
def fib(n, memo=None):
    memo = memo or {0:0,1:1}
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Explain purity and cache invalidation trade-offs.

### Q071: Function design challenge 17: Write curry function for two-argument functions
1. **Question**: Function design challenge 17: Write curry function for two-argument functions.
2. **Explanation**: Return nested function capturing first argument.
3. **Working Python solution**:
```python
def curry2(fn):
    def first(a):
        def second(b):
            return fn(a, b)
        return second
    return first
```
4. **Alternate solution**:
```python
from functools import partial

def curry2(fn):
    return lambda a: partial(fn, a)
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Good moment to discuss closures and free variables.

### Q072: Function design challenge 18: Implement custom map function
1. **Question**: Function design challenge 18: Implement custom map function.
2. **Explanation**: Apply function lazily over iterable.
3. **Working Python solution**:
```python
def my_map(fn, iterable):
    for x in iterable:
        yield fn(x)
```
4. **Alternate solution**:
```python
def my_map(fn, iterable):
    return [fn(x) for x in iterable]
```
5. **Complexity analysis**: Generator O(n).
6. **Interview tip**: Mention iterator vs eager list trade-off.

### Q073: Function design challenge 19: Implement memoized Fibonacci using decorator
1. **Question**: Function design challenge 19: Implement memoized Fibonacci using decorator.
2. **Explanation**: Demonstrates higher-order functions and closure state.
3. **Working Python solution**:
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```
4. **Alternate solution**:
```python
def fib(n, memo=None):
    memo = memo or {0:0,1:1}
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Explain purity and cache invalidation trade-offs.

### Q074: Function design challenge 20: Write curry function for two-argument functions
1. **Question**: Function design challenge 20: Write curry function for two-argument functions.
2. **Explanation**: Return nested function capturing first argument.
3. **Working Python solution**:
```python
def curry2(fn):
    def first(a):
        def second(b):
            return fn(a, b)
        return second
    return first
```
4. **Alternate solution**:
```python
from functools import partial

def curry2(fn):
    return lambda a: partial(fn, a)
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Good moment to discuss closures and free variables.

### Q075: Function design challenge 21: Implement custom map function
1. **Question**: Function design challenge 21: Implement custom map function.
2. **Explanation**: Apply function lazily over iterable.
3. **Working Python solution**:
```python
def my_map(fn, iterable):
    for x in iterable:
        yield fn(x)
```
4. **Alternate solution**:
```python
def my_map(fn, iterable):
    return [fn(x) for x in iterable]
```
5. **Complexity analysis**: Generator O(n).
6. **Interview tip**: Mention iterator vs eager list trade-off.

### Q076: Function design challenge 22: Implement memoized Fibonacci using decorator
1. **Question**: Function design challenge 22: Implement memoized Fibonacci using decorator.
2. **Explanation**: Demonstrates higher-order functions and closure state.
3. **Working Python solution**:
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```
4. **Alternate solution**:
```python
def fib(n, memo=None):
    memo = memo or {0:0,1:1}
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Explain purity and cache invalidation trade-offs.

### Q077: Function design challenge 23: Write curry function for two-argument functions
1. **Question**: Function design challenge 23: Write curry function for two-argument functions.
2. **Explanation**: Return nested function capturing first argument.
3. **Working Python solution**:
```python
def curry2(fn):
    def first(a):
        def second(b):
            return fn(a, b)
        return second
    return first
```
4. **Alternate solution**:
```python
from functools import partial

def curry2(fn):
    return lambda a: partial(fn, a)
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Good moment to discuss closures and free variables.

### Q078: Function design challenge 24: Implement custom map function
1. **Question**: Function design challenge 24: Implement custom map function.
2. **Explanation**: Apply function lazily over iterable.
3. **Working Python solution**:
```python
def my_map(fn, iterable):
    for x in iterable:
        yield fn(x)
```
4. **Alternate solution**:
```python
def my_map(fn, iterable):
    return [fn(x) for x in iterable]
```
5. **Complexity analysis**: Generator O(n).
6. **Interview tip**: Mention iterator vs eager list trade-off.

### Q079: Function design challenge 25: Implement memoized Fibonacci using decorator
1. **Question**: Function design challenge 25: Implement memoized Fibonacci using decorator.
2. **Explanation**: Demonstrates higher-order functions and closure state.
3. **Working Python solution**:
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```
4. **Alternate solution**:
```python
def fib(n, memo=None):
    memo = memo or {0:0,1:1}
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Explain purity and cache invalidation trade-offs.

### Q080: Function design challenge 26: Write curry function for two-argument functions
1. **Question**: Function design challenge 26: Write curry function for two-argument functions.
2. **Explanation**: Return nested function capturing first argument.
3. **Working Python solution**:
```python
def curry2(fn):
    def first(a):
        def second(b):
            return fn(a, b)
        return second
    return first
```
4. **Alternate solution**:
```python
from functools import partial

def curry2(fn):
    return lambda a: partial(fn, a)
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Good moment to discuss closures and free variables.

### Q081: Function design challenge 27: Implement custom map function
1. **Question**: Function design challenge 27: Implement custom map function.
2. **Explanation**: Apply function lazily over iterable.
3. **Working Python solution**:
```python
def my_map(fn, iterable):
    for x in iterable:
        yield fn(x)
```
4. **Alternate solution**:
```python
def my_map(fn, iterable):
    return [fn(x) for x in iterable]
```
5. **Complexity analysis**: Generator O(n).
6. **Interview tip**: Mention iterator vs eager list trade-off.

### Q082: Function design challenge 28: Implement memoized Fibonacci using decorator
1. **Question**: Function design challenge 28: Implement memoized Fibonacci using decorator.
2. **Explanation**: Demonstrates higher-order functions and closure state.
3. **Working Python solution**:
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```
4. **Alternate solution**:
```python
def fib(n, memo=None):
    memo = memo or {0:0,1:1}
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Explain purity and cache invalidation trade-offs.

## OOP

### Q083: OOP question 1: Design a BankAccount class with deposit/withdraw and overdraft protection
1. **Question**: OOP question 1: Design a BankAccount class with deposit/withdraw and overdraft protection.
2. **Explanation**: Encapsulate balance and validate operations through methods.
3. **Working Python solution**:
```python
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self._balance = float(balance)

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('amount must be positive')
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('amount must be positive')
        if amount > self._balance:
            raise ValueError('insufficient funds')
        self._balance -= amount
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass
class BankAccount:
    owner: str
    balance: float = 0.0

    def deposit(self, amount):
        if amount <= 0: raise ValueError
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance: raise ValueError
        self.balance -= amount
```
5. **Complexity analysis**: O(1) per op.
6. **Interview tip**: Discuss invariants and why balance should be guarded.

### Q084: OOP question 2: Implement Shape hierarchy with polymorphic area()
1. **Question**: OOP question 2: Implement Shape hierarchy with polymorphic area().
2. **Explanation**: Use abstract base class and subclass implementations.
3. **Working Python solution**:
```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r * self.r

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h
```
4. **Alternate solution**:
```python
class Circle:
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r * self.r

class Rectangle:
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Explain open/closed principle with polymorphism.

### Q085: OOP question 3: Build an iterable custom Range class
1. **Question**: OOP question 3: Build an iterable custom Range class.
2. **Explanation**: Implement __iter__ and __next__ for lazy iteration.
3. **Working Python solution**:
```python
class MyRange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 0, start
        self.start, self.stop, self.step = start, stop, step

    def __iter__(self):
        self.cur = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.cur >= self.stop) or (self.step < 0 and self.cur <= self.stop):
            raise StopIteration
        val = self.cur
        self.cur += self.step
        return val
```
4. **Alternate solution**:
```python
def my_range(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    cur = start
    while (step > 0 and cur < stop) or (step < 0 and cur > stop):
        yield cur
        cur += step
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Great for explaining iterator protocol.

### Q086: OOP question 4: Design a BankAccount class with deposit/withdraw and overdraft protection
1. **Question**: OOP question 4: Design a BankAccount class with deposit/withdraw and overdraft protection.
2. **Explanation**: Encapsulate balance and validate operations through methods.
3. **Working Python solution**:
```python
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self._balance = float(balance)

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('amount must be positive')
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('amount must be positive')
        if amount > self._balance:
            raise ValueError('insufficient funds')
        self._balance -= amount
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass
class BankAccount:
    owner: str
    balance: float = 0.0

    def deposit(self, amount):
        if amount <= 0: raise ValueError
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance: raise ValueError
        self.balance -= amount
```
5. **Complexity analysis**: O(1) per op.
6. **Interview tip**: Discuss invariants and why balance should be guarded.

### Q087: OOP question 5: Implement Shape hierarchy with polymorphic area()
1. **Question**: OOP question 5: Implement Shape hierarchy with polymorphic area().
2. **Explanation**: Use abstract base class and subclass implementations.
3. **Working Python solution**:
```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r * self.r

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h
```
4. **Alternate solution**:
```python
class Circle:
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r * self.r

class Rectangle:
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Explain open/closed principle with polymorphism.

### Q088: OOP question 6: Build an iterable custom Range class
1. **Question**: OOP question 6: Build an iterable custom Range class.
2. **Explanation**: Implement __iter__ and __next__ for lazy iteration.
3. **Working Python solution**:
```python
class MyRange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 0, start
        self.start, self.stop, self.step = start, stop, step

    def __iter__(self):
        self.cur = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.cur >= self.stop) or (self.step < 0 and self.cur <= self.stop):
            raise StopIteration
        val = self.cur
        self.cur += self.step
        return val
```
4. **Alternate solution**:
```python
def my_range(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    cur = start
    while (step > 0 and cur < stop) or (step < 0 and cur > stop):
        yield cur
        cur += step
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Great for explaining iterator protocol.

### Q089: OOP question 7: Design a BankAccount class with deposit/withdraw and overdraft protection
1. **Question**: OOP question 7: Design a BankAccount class with deposit/withdraw and overdraft protection.
2. **Explanation**: Encapsulate balance and validate operations through methods.
3. **Working Python solution**:
```python
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self._balance = float(balance)

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('amount must be positive')
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('amount must be positive')
        if amount > self._balance:
            raise ValueError('insufficient funds')
        self._balance -= amount
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass
class BankAccount:
    owner: str
    balance: float = 0.0

    def deposit(self, amount):
        if amount <= 0: raise ValueError
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance: raise ValueError
        self.balance -= amount
```
5. **Complexity analysis**: O(1) per op.
6. **Interview tip**: Discuss invariants and why balance should be guarded.

### Q090: OOP question 8: Implement Shape hierarchy with polymorphic area()
1. **Question**: OOP question 8: Implement Shape hierarchy with polymorphic area().
2. **Explanation**: Use abstract base class and subclass implementations.
3. **Working Python solution**:
```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r * self.r

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h
```
4. **Alternate solution**:
```python
class Circle:
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r * self.r

class Rectangle:
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Explain open/closed principle with polymorphism.

### Q091: OOP question 9: Build an iterable custom Range class
1. **Question**: OOP question 9: Build an iterable custom Range class.
2. **Explanation**: Implement __iter__ and __next__ for lazy iteration.
3. **Working Python solution**:
```python
class MyRange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 0, start
        self.start, self.stop, self.step = start, stop, step

    def __iter__(self):
        self.cur = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.cur >= self.stop) or (self.step < 0 and self.cur <= self.stop):
            raise StopIteration
        val = self.cur
        self.cur += self.step
        return val
```
4. **Alternate solution**:
```python
def my_range(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    cur = start
    while (step > 0 and cur < stop) or (step < 0 and cur > stop):
        yield cur
        cur += step
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Great for explaining iterator protocol.

### Q092: OOP question 10: Design a BankAccount class with deposit/withdraw and overdraft protection
1. **Question**: OOP question 10: Design a BankAccount class with deposit/withdraw and overdraft protection.
2. **Explanation**: Encapsulate balance and validate operations through methods.
3. **Working Python solution**:
```python
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self._balance = float(balance)

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('amount must be positive')
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('amount must be positive')
        if amount > self._balance:
            raise ValueError('insufficient funds')
        self._balance -= amount
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass
class BankAccount:
    owner: str
    balance: float = 0.0

    def deposit(self, amount):
        if amount <= 0: raise ValueError
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance: raise ValueError
        self.balance -= amount
```
5. **Complexity analysis**: O(1) per op.
6. **Interview tip**: Discuss invariants and why balance should be guarded.

### Q093: OOP question 11: Implement Shape hierarchy with polymorphic area()
1. **Question**: OOP question 11: Implement Shape hierarchy with polymorphic area().
2. **Explanation**: Use abstract base class and subclass implementations.
3. **Working Python solution**:
```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r * self.r

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h
```
4. **Alternate solution**:
```python
class Circle:
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r * self.r

class Rectangle:
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Explain open/closed principle with polymorphism.

### Q094: OOP question 12: Build an iterable custom Range class
1. **Question**: OOP question 12: Build an iterable custom Range class.
2. **Explanation**: Implement __iter__ and __next__ for lazy iteration.
3. **Working Python solution**:
```python
class MyRange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 0, start
        self.start, self.stop, self.step = start, stop, step

    def __iter__(self):
        self.cur = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.cur >= self.stop) or (self.step < 0 and self.cur <= self.stop):
            raise StopIteration
        val = self.cur
        self.cur += self.step
        return val
```
4. **Alternate solution**:
```python
def my_range(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    cur = start
    while (step > 0 and cur < stop) or (step < 0 and cur > stop):
        yield cur
        cur += step
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Great for explaining iterator protocol.

### Q095: OOP question 13: Design a BankAccount class with deposit/withdraw and overdraft protection
1. **Question**: OOP question 13: Design a BankAccount class with deposit/withdraw and overdraft protection.
2. **Explanation**: Encapsulate balance and validate operations through methods.
3. **Working Python solution**:
```python
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self._balance = float(balance)

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('amount must be positive')
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('amount must be positive')
        if amount > self._balance:
            raise ValueError('insufficient funds')
        self._balance -= amount
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass
class BankAccount:
    owner: str
    balance: float = 0.0

    def deposit(self, amount):
        if amount <= 0: raise ValueError
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance: raise ValueError
        self.balance -= amount
```
5. **Complexity analysis**: O(1) per op.
6. **Interview tip**: Discuss invariants and why balance should be guarded.

### Q096: OOP question 14: Implement Shape hierarchy with polymorphic area()
1. **Question**: OOP question 14: Implement Shape hierarchy with polymorphic area().
2. **Explanation**: Use abstract base class and subclass implementations.
3. **Working Python solution**:
```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r * self.r

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h
```
4. **Alternate solution**:
```python
class Circle:
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r * self.r

class Rectangle:
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Explain open/closed principle with polymorphism.

### Q097: OOP question 15: Build an iterable custom Range class
1. **Question**: OOP question 15: Build an iterable custom Range class.
2. **Explanation**: Implement __iter__ and __next__ for lazy iteration.
3. **Working Python solution**:
```python
class MyRange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 0, start
        self.start, self.stop, self.step = start, stop, step

    def __iter__(self):
        self.cur = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.cur >= self.stop) or (self.step < 0 and self.cur <= self.stop):
            raise StopIteration
        val = self.cur
        self.cur += self.step
        return val
```
4. **Alternate solution**:
```python
def my_range(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    cur = start
    while (step > 0 and cur < stop) or (step < 0 and cur > stop):
        yield cur
        cur += step
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Great for explaining iterator protocol.

### Q098: OOP question 16: Design a BankAccount class with deposit/withdraw and overdraft protection
1. **Question**: OOP question 16: Design a BankAccount class with deposit/withdraw and overdraft protection.
2. **Explanation**: Encapsulate balance and validate operations through methods.
3. **Working Python solution**:
```python
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self._balance = float(balance)

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('amount must be positive')
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('amount must be positive')
        if amount > self._balance:
            raise ValueError('insufficient funds')
        self._balance -= amount
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass
class BankAccount:
    owner: str
    balance: float = 0.0

    def deposit(self, amount):
        if amount <= 0: raise ValueError
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance: raise ValueError
        self.balance -= amount
```
5. **Complexity analysis**: O(1) per op.
6. **Interview tip**: Discuss invariants and why balance should be guarded.

### Q099: OOP question 17: Implement Shape hierarchy with polymorphic area()
1. **Question**: OOP question 17: Implement Shape hierarchy with polymorphic area().
2. **Explanation**: Use abstract base class and subclass implementations.
3. **Working Python solution**:
```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r * self.r

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h
```
4. **Alternate solution**:
```python
class Circle:
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r * self.r

class Rectangle:
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Explain open/closed principle with polymorphism.

### Q100: OOP question 18: Build an iterable custom Range class
1. **Question**: OOP question 18: Build an iterable custom Range class.
2. **Explanation**: Implement __iter__ and __next__ for lazy iteration.
3. **Working Python solution**:
```python
class MyRange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 0, start
        self.start, self.stop, self.step = start, stop, step

    def __iter__(self):
        self.cur = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.cur >= self.stop) or (self.step < 0 and self.cur <= self.stop):
            raise StopIteration
        val = self.cur
        self.cur += self.step
        return val
```
4. **Alternate solution**:
```python
def my_range(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    cur = start
    while (step > 0 and cur < stop) or (step < 0 and cur > stop):
        yield cur
        cur += step
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Great for explaining iterator protocol.

### Q101: OOP question 19: Design a BankAccount class with deposit/withdraw and overdraft protection
1. **Question**: OOP question 19: Design a BankAccount class with deposit/withdraw and overdraft protection.
2. **Explanation**: Encapsulate balance and validate operations through methods.
3. **Working Python solution**:
```python
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self._balance = float(balance)

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('amount must be positive')
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('amount must be positive')
        if amount > self._balance:
            raise ValueError('insufficient funds')
        self._balance -= amount
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass
class BankAccount:
    owner: str
    balance: float = 0.0

    def deposit(self, amount):
        if amount <= 0: raise ValueError
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance: raise ValueError
        self.balance -= amount
```
5. **Complexity analysis**: O(1) per op.
6. **Interview tip**: Discuss invariants and why balance should be guarded.

### Q102: OOP question 20: Implement Shape hierarchy with polymorphic area()
1. **Question**: OOP question 20: Implement Shape hierarchy with polymorphic area().
2. **Explanation**: Use abstract base class and subclass implementations.
3. **Working Python solution**:
```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r * self.r

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h
```
4. **Alternate solution**:
```python
class Circle:
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r * self.r

class Rectangle:
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Explain open/closed principle with polymorphism.

### Q103: OOP question 21: Build an iterable custom Range class
1. **Question**: OOP question 21: Build an iterable custom Range class.
2. **Explanation**: Implement __iter__ and __next__ for lazy iteration.
3. **Working Python solution**:
```python
class MyRange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 0, start
        self.start, self.stop, self.step = start, stop, step

    def __iter__(self):
        self.cur = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.cur >= self.stop) or (self.step < 0 and self.cur <= self.stop):
            raise StopIteration
        val = self.cur
        self.cur += self.step
        return val
```
4. **Alternate solution**:
```python
def my_range(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    cur = start
    while (step > 0 and cur < stop) or (step < 0 and cur > stop):
        yield cur
        cur += step
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Great for explaining iterator protocol.

### Q104: OOP question 22: Design a BankAccount class with deposit/withdraw and overdraft protection
1. **Question**: OOP question 22: Design a BankAccount class with deposit/withdraw and overdraft protection.
2. **Explanation**: Encapsulate balance and validate operations through methods.
3. **Working Python solution**:
```python
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self._balance = float(balance)

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('amount must be positive')
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('amount must be positive')
        if amount > self._balance:
            raise ValueError('insufficient funds')
        self._balance -= amount
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass
class BankAccount:
    owner: str
    balance: float = 0.0

    def deposit(self, amount):
        if amount <= 0: raise ValueError
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance: raise ValueError
        self.balance -= amount
```
5. **Complexity analysis**: O(1) per op.
6. **Interview tip**: Discuss invariants and why balance should be guarded.

### Q105: OOP question 23: Implement Shape hierarchy with polymorphic area()
1. **Question**: OOP question 23: Implement Shape hierarchy with polymorphic area().
2. **Explanation**: Use abstract base class and subclass implementations.
3. **Working Python solution**:
```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r * self.r

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h
```
4. **Alternate solution**:
```python
class Circle:
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r * self.r

class Rectangle:
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Explain open/closed principle with polymorphism.

### Q106: OOP question 24: Build an iterable custom Range class
1. **Question**: OOP question 24: Build an iterable custom Range class.
2. **Explanation**: Implement __iter__ and __next__ for lazy iteration.
3. **Working Python solution**:
```python
class MyRange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 0, start
        self.start, self.stop, self.step = start, stop, step

    def __iter__(self):
        self.cur = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.cur >= self.stop) or (self.step < 0 and self.cur <= self.stop):
            raise StopIteration
        val = self.cur
        self.cur += self.step
        return val
```
4. **Alternate solution**:
```python
def my_range(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    cur = start
    while (step > 0 and cur < stop) or (step < 0 and cur > stop):
        yield cur
        cur += step
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Great for explaining iterator protocol.

### Q107: OOP question 25: Design a BankAccount class with deposit/withdraw and overdraft protection
1. **Question**: OOP question 25: Design a BankAccount class with deposit/withdraw and overdraft protection.
2. **Explanation**: Encapsulate balance and validate operations through methods.
3. **Working Python solution**:
```python
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self._balance = float(balance)

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('amount must be positive')
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('amount must be positive')
        if amount > self._balance:
            raise ValueError('insufficient funds')
        self._balance -= amount
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass
class BankAccount:
    owner: str
    balance: float = 0.0

    def deposit(self, amount):
        if amount <= 0: raise ValueError
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance: raise ValueError
        self.balance -= amount
```
5. **Complexity analysis**: O(1) per op.
6. **Interview tip**: Discuss invariants and why balance should be guarded.

### Q108: OOP question 26: Implement Shape hierarchy with polymorphic area()
1. **Question**: OOP question 26: Implement Shape hierarchy with polymorphic area().
2. **Explanation**: Use abstract base class and subclass implementations.
3. **Working Python solution**:
```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r * self.r

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h
```
4. **Alternate solution**:
```python
class Circle:
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r * self.r

class Rectangle:
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Explain open/closed principle with polymorphism.

### Q109: OOP question 27: Build an iterable custom Range class
1. **Question**: OOP question 27: Build an iterable custom Range class.
2. **Explanation**: Implement __iter__ and __next__ for lazy iteration.
3. **Working Python solution**:
```python
class MyRange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 0, start
        self.start, self.stop, self.step = start, stop, step

    def __iter__(self):
        self.cur = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.cur >= self.stop) or (self.step < 0 and self.cur <= self.stop):
            raise StopIteration
        val = self.cur
        self.cur += self.step
        return val
```
4. **Alternate solution**:
```python
def my_range(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    cur = start
    while (step > 0 and cur < stop) or (step < 0 and cur > stop):
        yield cur
        cur += step
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Great for explaining iterator protocol.

### Q110: OOP question 28: Design a BankAccount class with deposit/withdraw and overdraft protection
1. **Question**: OOP question 28: Design a BankAccount class with deposit/withdraw and overdraft protection.
2. **Explanation**: Encapsulate balance and validate operations through methods.
3. **Working Python solution**:
```python
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self._balance = float(balance)

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('amount must be positive')
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('amount must be positive')
        if amount > self._balance:
            raise ValueError('insufficient funds')
        self._balance -= amount
```
4. **Alternate solution**:
```python
from dataclasses import dataclass

@dataclass
class BankAccount:
    owner: str
    balance: float = 0.0

    def deposit(self, amount):
        if amount <= 0: raise ValueError
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance: raise ValueError
        self.balance -= amount
```
5. **Complexity analysis**: O(1) per op.
6. **Interview tip**: Discuss invariants and why balance should be guarded.

## Advanced Python

### Q111: Advanced Python question 1: Write retry decorator with exponential backoff
1. **Question**: Advanced Python question 1: Write retry decorator with exponential backoff.
2. **Explanation**: Decorator wraps function and retries transient failures.
3. **Working Python solution**:
```python
import time
from functools import wraps

def retry(max_attempts=3, base_delay=0.1):
    def deco(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            last = None
            for attempt in range(max_attempts):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    last = e
                    if attempt < max_attempts - 1:
                        time.sleep(base_delay * (2 ** attempt))
            raise last
        return wrapper
    return deco
```
4. **Alternate solution**:
```python
def retry(max_attempts=3):
    def deco(fn):
        def wrapper(*a, **k):
            for _ in range(max_attempts):
                try:
                    return fn(*a, **k)
                except Exception:
                    pass
            return fn(*a, **k)
        return wrapper
    return deco
```
5. **Complexity analysis**: Per call O(attempts).
6. **Interview tip**: Mention which exceptions should be retried.

### Q112: Advanced Python question 2: Implement context manager for timing blocks
1. **Question**: Advanced Python question 2: Implement context manager for timing blocks.
2. **Explanation**: Use __enter__/__exit__ or contextmanager.
3. **Working Python solution**:
```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start
```
4. **Alternate solution**:
```python
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.perf_counter()
    try:
        yield
    finally:
        print(time.perf_counter() - start)
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Good place to discuss deterministic cleanup.

### Q113: Advanced Python question 3: Run coroutines concurrently with asyncio.gather
1. **Question**: Advanced Python question 3: Run coroutines concurrently with asyncio.gather.
2. **Explanation**: Define async tasks and gather results.
3. **Working Python solution**:
```python
import asyncio

async def fetch(x):
    await asyncio.sleep(0.01)
    return x * x

async def main(vals):
    return await asyncio.gather(*(fetch(v) for v in vals))
```
4. **Alternate solution**:
```python
import asyncio

async def main(vals):
    out = []
    for v in vals:
        out.append(await fetch(v))
    return out
```
5. **Complexity analysis**: Concurrent wall time near max(task).
6. **Interview tip**: Explain when async is better than threads.

### Q114: Advanced Python question 4: Write retry decorator with exponential backoff
1. **Question**: Advanced Python question 4: Write retry decorator with exponential backoff.
2. **Explanation**: Decorator wraps function and retries transient failures.
3. **Working Python solution**:
```python
import time
from functools import wraps

def retry(max_attempts=3, base_delay=0.1):
    def deco(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            last = None
            for attempt in range(max_attempts):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    last = e
                    if attempt < max_attempts - 1:
                        time.sleep(base_delay * (2 ** attempt))
            raise last
        return wrapper
    return deco
```
4. **Alternate solution**:
```python
def retry(max_attempts=3):
    def deco(fn):
        def wrapper(*a, **k):
            for _ in range(max_attempts):
                try:
                    return fn(*a, **k)
                except Exception:
                    pass
            return fn(*a, **k)
        return wrapper
    return deco
```
5. **Complexity analysis**: Per call O(attempts).
6. **Interview tip**: Mention which exceptions should be retried.

### Q115: Advanced Python question 5: Implement context manager for timing blocks
1. **Question**: Advanced Python question 5: Implement context manager for timing blocks.
2. **Explanation**: Use __enter__/__exit__ or contextmanager.
3. **Working Python solution**:
```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start
```
4. **Alternate solution**:
```python
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.perf_counter()
    try:
        yield
    finally:
        print(time.perf_counter() - start)
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Good place to discuss deterministic cleanup.

### Q116: Advanced Python question 6: Run coroutines concurrently with asyncio.gather
1. **Question**: Advanced Python question 6: Run coroutines concurrently with asyncio.gather.
2. **Explanation**: Define async tasks and gather results.
3. **Working Python solution**:
```python
import asyncio

async def fetch(x):
    await asyncio.sleep(0.01)
    return x * x

async def main(vals):
    return await asyncio.gather(*(fetch(v) for v in vals))
```
4. **Alternate solution**:
```python
import asyncio

async def main(vals):
    out = []
    for v in vals:
        out.append(await fetch(v))
    return out
```
5. **Complexity analysis**: Concurrent wall time near max(task).
6. **Interview tip**: Explain when async is better than threads.

### Q117: Advanced Python question 7: Write retry decorator with exponential backoff
1. **Question**: Advanced Python question 7: Write retry decorator with exponential backoff.
2. **Explanation**: Decorator wraps function and retries transient failures.
3. **Working Python solution**:
```python
import time
from functools import wraps

def retry(max_attempts=3, base_delay=0.1):
    def deco(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            last = None
            for attempt in range(max_attempts):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    last = e
                    if attempt < max_attempts - 1:
                        time.sleep(base_delay * (2 ** attempt))
            raise last
        return wrapper
    return deco
```
4. **Alternate solution**:
```python
def retry(max_attempts=3):
    def deco(fn):
        def wrapper(*a, **k):
            for _ in range(max_attempts):
                try:
                    return fn(*a, **k)
                except Exception:
                    pass
            return fn(*a, **k)
        return wrapper
    return deco
```
5. **Complexity analysis**: Per call O(attempts).
6. **Interview tip**: Mention which exceptions should be retried.

### Q118: Advanced Python question 8: Implement context manager for timing blocks
1. **Question**: Advanced Python question 8: Implement context manager for timing blocks.
2. **Explanation**: Use __enter__/__exit__ or contextmanager.
3. **Working Python solution**:
```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start
```
4. **Alternate solution**:
```python
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.perf_counter()
    try:
        yield
    finally:
        print(time.perf_counter() - start)
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Good place to discuss deterministic cleanup.

### Q119: Advanced Python question 9: Run coroutines concurrently with asyncio.gather
1. **Question**: Advanced Python question 9: Run coroutines concurrently with asyncio.gather.
2. **Explanation**: Define async tasks and gather results.
3. **Working Python solution**:
```python
import asyncio

async def fetch(x):
    await asyncio.sleep(0.01)
    return x * x

async def main(vals):
    return await asyncio.gather(*(fetch(v) for v in vals))
```
4. **Alternate solution**:
```python
import asyncio

async def main(vals):
    out = []
    for v in vals:
        out.append(await fetch(v))
    return out
```
5. **Complexity analysis**: Concurrent wall time near max(task).
6. **Interview tip**: Explain when async is better than threads.

### Q120: Advanced Python question 10: Write retry decorator with exponential backoff
1. **Question**: Advanced Python question 10: Write retry decorator with exponential backoff.
2. **Explanation**: Decorator wraps function and retries transient failures.
3. **Working Python solution**:
```python
import time
from functools import wraps

def retry(max_attempts=3, base_delay=0.1):
    def deco(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            last = None
            for attempt in range(max_attempts):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    last = e
                    if attempt < max_attempts - 1:
                        time.sleep(base_delay * (2 ** attempt))
            raise last
        return wrapper
    return deco
```
4. **Alternate solution**:
```python
def retry(max_attempts=3):
    def deco(fn):
        def wrapper(*a, **k):
            for _ in range(max_attempts):
                try:
                    return fn(*a, **k)
                except Exception:
                    pass
            return fn(*a, **k)
        return wrapper
    return deco
```
5. **Complexity analysis**: Per call O(attempts).
6. **Interview tip**: Mention which exceptions should be retried.

### Q121: Advanced Python question 11: Implement context manager for timing blocks
1. **Question**: Advanced Python question 11: Implement context manager for timing blocks.
2. **Explanation**: Use __enter__/__exit__ or contextmanager.
3. **Working Python solution**:
```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start
```
4. **Alternate solution**:
```python
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.perf_counter()
    try:
        yield
    finally:
        print(time.perf_counter() - start)
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Good place to discuss deterministic cleanup.

### Q122: Advanced Python question 12: Run coroutines concurrently with asyncio.gather
1. **Question**: Advanced Python question 12: Run coroutines concurrently with asyncio.gather.
2. **Explanation**: Define async tasks and gather results.
3. **Working Python solution**:
```python
import asyncio

async def fetch(x):
    await asyncio.sleep(0.01)
    return x * x

async def main(vals):
    return await asyncio.gather(*(fetch(v) for v in vals))
```
4. **Alternate solution**:
```python
import asyncio

async def main(vals):
    out = []
    for v in vals:
        out.append(await fetch(v))
    return out
```
5. **Complexity analysis**: Concurrent wall time near max(task).
6. **Interview tip**: Explain when async is better than threads.

### Q123: Advanced Python question 13: Write retry decorator with exponential backoff
1. **Question**: Advanced Python question 13: Write retry decorator with exponential backoff.
2. **Explanation**: Decorator wraps function and retries transient failures.
3. **Working Python solution**:
```python
import time
from functools import wraps

def retry(max_attempts=3, base_delay=0.1):
    def deco(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            last = None
            for attempt in range(max_attempts):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    last = e
                    if attempt < max_attempts - 1:
                        time.sleep(base_delay * (2 ** attempt))
            raise last
        return wrapper
    return deco
```
4. **Alternate solution**:
```python
def retry(max_attempts=3):
    def deco(fn):
        def wrapper(*a, **k):
            for _ in range(max_attempts):
                try:
                    return fn(*a, **k)
                except Exception:
                    pass
            return fn(*a, **k)
        return wrapper
    return deco
```
5. **Complexity analysis**: Per call O(attempts).
6. **Interview tip**: Mention which exceptions should be retried.

### Q124: Advanced Python question 14: Implement context manager for timing blocks
1. **Question**: Advanced Python question 14: Implement context manager for timing blocks.
2. **Explanation**: Use __enter__/__exit__ or contextmanager.
3. **Working Python solution**:
```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start
```
4. **Alternate solution**:
```python
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.perf_counter()
    try:
        yield
    finally:
        print(time.perf_counter() - start)
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Good place to discuss deterministic cleanup.

### Q125: Advanced Python question 15: Run coroutines concurrently with asyncio.gather
1. **Question**: Advanced Python question 15: Run coroutines concurrently with asyncio.gather.
2. **Explanation**: Define async tasks and gather results.
3. **Working Python solution**:
```python
import asyncio

async def fetch(x):
    await asyncio.sleep(0.01)
    return x * x

async def main(vals):
    return await asyncio.gather(*(fetch(v) for v in vals))
```
4. **Alternate solution**:
```python
import asyncio

async def main(vals):
    out = []
    for v in vals:
        out.append(await fetch(v))
    return out
```
5. **Complexity analysis**: Concurrent wall time near max(task).
6. **Interview tip**: Explain when async is better than threads.

### Q126: Advanced Python question 16: Write retry decorator with exponential backoff
1. **Question**: Advanced Python question 16: Write retry decorator with exponential backoff.
2. **Explanation**: Decorator wraps function and retries transient failures.
3. **Working Python solution**:
```python
import time
from functools import wraps

def retry(max_attempts=3, base_delay=0.1):
    def deco(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            last = None
            for attempt in range(max_attempts):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    last = e
                    if attempt < max_attempts - 1:
                        time.sleep(base_delay * (2 ** attempt))
            raise last
        return wrapper
    return deco
```
4. **Alternate solution**:
```python
def retry(max_attempts=3):
    def deco(fn):
        def wrapper(*a, **k):
            for _ in range(max_attempts):
                try:
                    return fn(*a, **k)
                except Exception:
                    pass
            return fn(*a, **k)
        return wrapper
    return deco
```
5. **Complexity analysis**: Per call O(attempts).
6. **Interview tip**: Mention which exceptions should be retried.

### Q127: Advanced Python question 17: Implement context manager for timing blocks
1. **Question**: Advanced Python question 17: Implement context manager for timing blocks.
2. **Explanation**: Use __enter__/__exit__ or contextmanager.
3. **Working Python solution**:
```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start
```
4. **Alternate solution**:
```python
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.perf_counter()
    try:
        yield
    finally:
        print(time.perf_counter() - start)
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Good place to discuss deterministic cleanup.

### Q128: Advanced Python question 18: Run coroutines concurrently with asyncio.gather
1. **Question**: Advanced Python question 18: Run coroutines concurrently with asyncio.gather.
2. **Explanation**: Define async tasks and gather results.
3. **Working Python solution**:
```python
import asyncio

async def fetch(x):
    await asyncio.sleep(0.01)
    return x * x

async def main(vals):
    return await asyncio.gather(*(fetch(v) for v in vals))
```
4. **Alternate solution**:
```python
import asyncio

async def main(vals):
    out = []
    for v in vals:
        out.append(await fetch(v))
    return out
```
5. **Complexity analysis**: Concurrent wall time near max(task).
6. **Interview tip**: Explain when async is better than threads.

### Q129: Advanced Python question 19: Write retry decorator with exponential backoff
1. **Question**: Advanced Python question 19: Write retry decorator with exponential backoff.
2. **Explanation**: Decorator wraps function and retries transient failures.
3. **Working Python solution**:
```python
import time
from functools import wraps

def retry(max_attempts=3, base_delay=0.1):
    def deco(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            last = None
            for attempt in range(max_attempts):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    last = e
                    if attempt < max_attempts - 1:
                        time.sleep(base_delay * (2 ** attempt))
            raise last
        return wrapper
    return deco
```
4. **Alternate solution**:
```python
def retry(max_attempts=3):
    def deco(fn):
        def wrapper(*a, **k):
            for _ in range(max_attempts):
                try:
                    return fn(*a, **k)
                except Exception:
                    pass
            return fn(*a, **k)
        return wrapper
    return deco
```
5. **Complexity analysis**: Per call O(attempts).
6. **Interview tip**: Mention which exceptions should be retried.

### Q130: Advanced Python question 20: Implement context manager for timing blocks
1. **Question**: Advanced Python question 20: Implement context manager for timing blocks.
2. **Explanation**: Use __enter__/__exit__ or contextmanager.
3. **Working Python solution**:
```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start
```
4. **Alternate solution**:
```python
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.perf_counter()
    try:
        yield
    finally:
        print(time.perf_counter() - start)
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Good place to discuss deterministic cleanup.

### Q131: Advanced Python question 21: Run coroutines concurrently with asyncio.gather
1. **Question**: Advanced Python question 21: Run coroutines concurrently with asyncio.gather.
2. **Explanation**: Define async tasks and gather results.
3. **Working Python solution**:
```python
import asyncio

async def fetch(x):
    await asyncio.sleep(0.01)
    return x * x

async def main(vals):
    return await asyncio.gather(*(fetch(v) for v in vals))
```
4. **Alternate solution**:
```python
import asyncio

async def main(vals):
    out = []
    for v in vals:
        out.append(await fetch(v))
    return out
```
5. **Complexity analysis**: Concurrent wall time near max(task).
6. **Interview tip**: Explain when async is better than threads.

### Q132: Advanced Python question 22: Write retry decorator with exponential backoff
1. **Question**: Advanced Python question 22: Write retry decorator with exponential backoff.
2. **Explanation**: Decorator wraps function and retries transient failures.
3. **Working Python solution**:
```python
import time
from functools import wraps

def retry(max_attempts=3, base_delay=0.1):
    def deco(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            last = None
            for attempt in range(max_attempts):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    last = e
                    if attempt < max_attempts - 1:
                        time.sleep(base_delay * (2 ** attempt))
            raise last
        return wrapper
    return deco
```
4. **Alternate solution**:
```python
def retry(max_attempts=3):
    def deco(fn):
        def wrapper(*a, **k):
            for _ in range(max_attempts):
                try:
                    return fn(*a, **k)
                except Exception:
                    pass
            return fn(*a, **k)
        return wrapper
    return deco
```
5. **Complexity analysis**: Per call O(attempts).
6. **Interview tip**: Mention which exceptions should be retried.

### Q133: Advanced Python question 23: Implement context manager for timing blocks
1. **Question**: Advanced Python question 23: Implement context manager for timing blocks.
2. **Explanation**: Use __enter__/__exit__ or contextmanager.
3. **Working Python solution**:
```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start
```
4. **Alternate solution**:
```python
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.perf_counter()
    try:
        yield
    finally:
        print(time.perf_counter() - start)
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Good place to discuss deterministic cleanup.

### Q134: Advanced Python question 24: Run coroutines concurrently with asyncio.gather
1. **Question**: Advanced Python question 24: Run coroutines concurrently with asyncio.gather.
2. **Explanation**: Define async tasks and gather results.
3. **Working Python solution**:
```python
import asyncio

async def fetch(x):
    await asyncio.sleep(0.01)
    return x * x

async def main(vals):
    return await asyncio.gather(*(fetch(v) for v in vals))
```
4. **Alternate solution**:
```python
import asyncio

async def main(vals):
    out = []
    for v in vals:
        out.append(await fetch(v))
    return out
```
5. **Complexity analysis**: Concurrent wall time near max(task).
6. **Interview tip**: Explain when async is better than threads.

### Q135: Advanced Python question 25: Write retry decorator with exponential backoff
1. **Question**: Advanced Python question 25: Write retry decorator with exponential backoff.
2. **Explanation**: Decorator wraps function and retries transient failures.
3. **Working Python solution**:
```python
import time
from functools import wraps

def retry(max_attempts=3, base_delay=0.1):
    def deco(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            last = None
            for attempt in range(max_attempts):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    last = e
                    if attempt < max_attempts - 1:
                        time.sleep(base_delay * (2 ** attempt))
            raise last
        return wrapper
    return deco
```
4. **Alternate solution**:
```python
def retry(max_attempts=3):
    def deco(fn):
        def wrapper(*a, **k):
            for _ in range(max_attempts):
                try:
                    return fn(*a, **k)
                except Exception:
                    pass
            return fn(*a, **k)
        return wrapper
    return deco
```
5. **Complexity analysis**: Per call O(attempts).
6. **Interview tip**: Mention which exceptions should be retried.

### Q136: Advanced Python question 26: Implement context manager for timing blocks
1. **Question**: Advanced Python question 26: Implement context manager for timing blocks.
2. **Explanation**: Use __enter__/__exit__ or contextmanager.
3. **Working Python solution**:
```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start
```
4. **Alternate solution**:
```python
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.perf_counter()
    try:
        yield
    finally:
        print(time.perf_counter() - start)
```
5. **Complexity analysis**: O(1).
6. **Interview tip**: Good place to discuss deterministic cleanup.

### Q137: Advanced Python question 27: Run coroutines concurrently with asyncio.gather
1. **Question**: Advanced Python question 27: Run coroutines concurrently with asyncio.gather.
2. **Explanation**: Define async tasks and gather results.
3. **Working Python solution**:
```python
import asyncio

async def fetch(x):
    await asyncio.sleep(0.01)
    return x * x

async def main(vals):
    return await asyncio.gather(*(fetch(v) for v in vals))
```
4. **Alternate solution**:
```python
import asyncio

async def main(vals):
    out = []
    for v in vals:
        out.append(await fetch(v))
    return out
```
5. **Complexity analysis**: Concurrent wall time near max(task).
6. **Interview tip**: Explain when async is better than threads.

### Q138: Advanced Python question 28: Write retry decorator with exponential backoff
1. **Question**: Advanced Python question 28: Write retry decorator with exponential backoff.
2. **Explanation**: Decorator wraps function and retries transient failures.
3. **Working Python solution**:
```python
import time
from functools import wraps

def retry(max_attempts=3, base_delay=0.1):
    def deco(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            last = None
            for attempt in range(max_attempts):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    last = e
                    if attempt < max_attempts - 1:
                        time.sleep(base_delay * (2 ** attempt))
            raise last
        return wrapper
    return deco
```
4. **Alternate solution**:
```python
def retry(max_attempts=3):
    def deco(fn):
        def wrapper(*a, **k):
            for _ in range(max_attempts):
                try:
                    return fn(*a, **k)
                except Exception:
                    pass
            return fn(*a, **k)
        return wrapper
    return deco
```
5. **Complexity analysis**: Per call O(attempts).
6. **Interview tip**: Mention which exceptions should be retried.

## NumPy

### Q139: NumPy problem 1: Standardize each column in a matrix
1. **Question**: NumPy problem 1: Standardize each column in a matrix.
2. **Explanation**: Subtract column mean and divide by standard deviation.
3. **Working Python solution**:
```python
import numpy as np

def standardize_cols(X):
    mu = X.mean(axis=0)
    sigma = X.std(axis=0)
    sigma = np.where(sigma == 0, 1, sigma)
    return (X - mu) / sigma
```
4. **Alternate solution**:
```python
import numpy as np

def standardize_cols(X):
    return np.apply_along_axis(lambda c: (c - c.mean()) / (c.std() or 1), 0, X)
```
5. **Complexity analysis**: O(n*m).
6. **Interview tip**: Mention numerical stability and zero-variance columns.

### Q140: NumPy problem 2: Compute pairwise Euclidean distances between two matrices
1. **Question**: NumPy problem 2: Compute pairwise Euclidean distances between two matrices.
2. **Explanation**: Use broadcasting to avoid Python loops.
3. **Working Python solution**:
```python
import numpy as np

def pairwise_dist(A, B):
    diff = A[:, None, :] - B[None, :, :]
    return np.sqrt((diff ** 2).sum(axis=2))
```
4. **Alternate solution**:
```python
import numpy as np

def pairwise_dist(A, B):
    out = np.empty((A.shape[0], B.shape[0]))
    for i, a in enumerate(A):
        out[i] = np.sqrt(((B - a) ** 2).sum(axis=1))
    return out
```
5. **Complexity analysis**: Broadcasting O(n*m*d).
6. **Interview tip**: Interviewers like hearing memory trade-offs of broadcasting.

### Q141: NumPy problem 3: Implement min-max scaling for each feature
1. **Question**: NumPy problem 3: Implement min-max scaling for each feature.
2. **Explanation**: Transform values into [0,1] per column.
3. **Working Python solution**:
```python
import numpy as np

def minmax_scale(X):
    mn, mx = X.min(axis=0), X.max(axis=0)
    span = np.where(mx - mn == 0, 1, mx - mn)
    return (X - mn) / span
```
4. **Alternate solution**:
```python
import numpy as np

def minmax_scale(X):
    out = X.copy().astype(float)
    for j in range(X.shape[1]):
        mn, mx = X[:, j].min(), X[:, j].max()
        out[:, j] = 0 if mx == mn else (X[:, j] - mn) / (mx - mn)
    return out
```
5. **Complexity analysis**: O(n*m).
6. **Interview tip**: Call out dtype conversion to float to avoid integer truncation.

### Q142: NumPy problem 4: Standardize each column in a matrix
1. **Question**: NumPy problem 4: Standardize each column in a matrix.
2. **Explanation**: Subtract column mean and divide by standard deviation.
3. **Working Python solution**:
```python
import numpy as np

def standardize_cols(X):
    mu = X.mean(axis=0)
    sigma = X.std(axis=0)
    sigma = np.where(sigma == 0, 1, sigma)
    return (X - mu) / sigma
```
4. **Alternate solution**:
```python
import numpy as np

def standardize_cols(X):
    return np.apply_along_axis(lambda c: (c - c.mean()) / (c.std() or 1), 0, X)
```
5. **Complexity analysis**: O(n*m).
6. **Interview tip**: Mention numerical stability and zero-variance columns.

### Q143: NumPy problem 5: Compute pairwise Euclidean distances between two matrices
1. **Question**: NumPy problem 5: Compute pairwise Euclidean distances between two matrices.
2. **Explanation**: Use broadcasting to avoid Python loops.
3. **Working Python solution**:
```python
import numpy as np

def pairwise_dist(A, B):
    diff = A[:, None, :] - B[None, :, :]
    return np.sqrt((diff ** 2).sum(axis=2))
```
4. **Alternate solution**:
```python
import numpy as np

def pairwise_dist(A, B):
    out = np.empty((A.shape[0], B.shape[0]))
    for i, a in enumerate(A):
        out[i] = np.sqrt(((B - a) ** 2).sum(axis=1))
    return out
```
5. **Complexity analysis**: Broadcasting O(n*m*d).
6. **Interview tip**: Interviewers like hearing memory trade-offs of broadcasting.

### Q144: NumPy problem 6: Implement min-max scaling for each feature
1. **Question**: NumPy problem 6: Implement min-max scaling for each feature.
2. **Explanation**: Transform values into [0,1] per column.
3. **Working Python solution**:
```python
import numpy as np

def minmax_scale(X):
    mn, mx = X.min(axis=0), X.max(axis=0)
    span = np.where(mx - mn == 0, 1, mx - mn)
    return (X - mn) / span
```
4. **Alternate solution**:
```python
import numpy as np

def minmax_scale(X):
    out = X.copy().astype(float)
    for j in range(X.shape[1]):
        mn, mx = X[:, j].min(), X[:, j].max()
        out[:, j] = 0 if mx == mn else (X[:, j] - mn) / (mx - mn)
    return out
```
5. **Complexity analysis**: O(n*m).
6. **Interview tip**: Call out dtype conversion to float to avoid integer truncation.

### Q145: NumPy problem 7: Standardize each column in a matrix
1. **Question**: NumPy problem 7: Standardize each column in a matrix.
2. **Explanation**: Subtract column mean and divide by standard deviation.
3. **Working Python solution**:
```python
import numpy as np

def standardize_cols(X):
    mu = X.mean(axis=0)
    sigma = X.std(axis=0)
    sigma = np.where(sigma == 0, 1, sigma)
    return (X - mu) / sigma
```
4. **Alternate solution**:
```python
import numpy as np

def standardize_cols(X):
    return np.apply_along_axis(lambda c: (c - c.mean()) / (c.std() or 1), 0, X)
```
5. **Complexity analysis**: O(n*m).
6. **Interview tip**: Mention numerical stability and zero-variance columns.

### Q146: NumPy problem 8: Compute pairwise Euclidean distances between two matrices
1. **Question**: NumPy problem 8: Compute pairwise Euclidean distances between two matrices.
2. **Explanation**: Use broadcasting to avoid Python loops.
3. **Working Python solution**:
```python
import numpy as np

def pairwise_dist(A, B):
    diff = A[:, None, :] - B[None, :, :]
    return np.sqrt((diff ** 2).sum(axis=2))
```
4. **Alternate solution**:
```python
import numpy as np

def pairwise_dist(A, B):
    out = np.empty((A.shape[0], B.shape[0]))
    for i, a in enumerate(A):
        out[i] = np.sqrt(((B - a) ** 2).sum(axis=1))
    return out
```
5. **Complexity analysis**: Broadcasting O(n*m*d).
6. **Interview tip**: Interviewers like hearing memory trade-offs of broadcasting.

### Q147: NumPy problem 9: Implement min-max scaling for each feature
1. **Question**: NumPy problem 9: Implement min-max scaling for each feature.
2. **Explanation**: Transform values into [0,1] per column.
3. **Working Python solution**:
```python
import numpy as np

def minmax_scale(X):
    mn, mx = X.min(axis=0), X.max(axis=0)
    span = np.where(mx - mn == 0, 1, mx - mn)
    return (X - mn) / span
```
4. **Alternate solution**:
```python
import numpy as np

def minmax_scale(X):
    out = X.copy().astype(float)
    for j in range(X.shape[1]):
        mn, mx = X[:, j].min(), X[:, j].max()
        out[:, j] = 0 if mx == mn else (X[:, j] - mn) / (mx - mn)
    return out
```
5. **Complexity analysis**: O(n*m).
6. **Interview tip**: Call out dtype conversion to float to avoid integer truncation.

### Q148: NumPy problem 10: Standardize each column in a matrix
1. **Question**: NumPy problem 10: Standardize each column in a matrix.
2. **Explanation**: Subtract column mean and divide by standard deviation.
3. **Working Python solution**:
```python
import numpy as np

def standardize_cols(X):
    mu = X.mean(axis=0)
    sigma = X.std(axis=0)
    sigma = np.where(sigma == 0, 1, sigma)
    return (X - mu) / sigma
```
4. **Alternate solution**:
```python
import numpy as np

def standardize_cols(X):
    return np.apply_along_axis(lambda c: (c - c.mean()) / (c.std() or 1), 0, X)
```
5. **Complexity analysis**: O(n*m).
6. **Interview tip**: Mention numerical stability and zero-variance columns.

### Q149: NumPy problem 11: Compute pairwise Euclidean distances between two matrices
1. **Question**: NumPy problem 11: Compute pairwise Euclidean distances between two matrices.
2. **Explanation**: Use broadcasting to avoid Python loops.
3. **Working Python solution**:
```python
import numpy as np

def pairwise_dist(A, B):
    diff = A[:, None, :] - B[None, :, :]
    return np.sqrt((diff ** 2).sum(axis=2))
```
4. **Alternate solution**:
```python
import numpy as np

def pairwise_dist(A, B):
    out = np.empty((A.shape[0], B.shape[0]))
    for i, a in enumerate(A):
        out[i] = np.sqrt(((B - a) ** 2).sum(axis=1))
    return out
```
5. **Complexity analysis**: Broadcasting O(n*m*d).
6. **Interview tip**: Interviewers like hearing memory trade-offs of broadcasting.

### Q150: NumPy problem 12: Implement min-max scaling for each feature
1. **Question**: NumPy problem 12: Implement min-max scaling for each feature.
2. **Explanation**: Transform values into [0,1] per column.
3. **Working Python solution**:
```python
import numpy as np

def minmax_scale(X):
    mn, mx = X.min(axis=0), X.max(axis=0)
    span = np.where(mx - mn == 0, 1, mx - mn)
    return (X - mn) / span
```
4. **Alternate solution**:
```python
import numpy as np

def minmax_scale(X):
    out = X.copy().astype(float)
    for j in range(X.shape[1]):
        mn, mx = X[:, j].min(), X[:, j].max()
        out[:, j] = 0 if mx == mn else (X[:, j] - mn) / (mx - mn)
    return out
```
5. **Complexity analysis**: O(n*m).
6. **Interview tip**: Call out dtype conversion to float to avoid integer truncation.

### Q151: NumPy problem 13: Standardize each column in a matrix
1. **Question**: NumPy problem 13: Standardize each column in a matrix.
2. **Explanation**: Subtract column mean and divide by standard deviation.
3. **Working Python solution**:
```python
import numpy as np

def standardize_cols(X):
    mu = X.mean(axis=0)
    sigma = X.std(axis=0)
    sigma = np.where(sigma == 0, 1, sigma)
    return (X - mu) / sigma
```
4. **Alternate solution**:
```python
import numpy as np

def standardize_cols(X):
    return np.apply_along_axis(lambda c: (c - c.mean()) / (c.std() or 1), 0, X)
```
5. **Complexity analysis**: O(n*m).
6. **Interview tip**: Mention numerical stability and zero-variance columns.

### Q152: NumPy problem 14: Compute pairwise Euclidean distances between two matrices
1. **Question**: NumPy problem 14: Compute pairwise Euclidean distances between two matrices.
2. **Explanation**: Use broadcasting to avoid Python loops.
3. **Working Python solution**:
```python
import numpy as np

def pairwise_dist(A, B):
    diff = A[:, None, :] - B[None, :, :]
    return np.sqrt((diff ** 2).sum(axis=2))
```
4. **Alternate solution**:
```python
import numpy as np

def pairwise_dist(A, B):
    out = np.empty((A.shape[0], B.shape[0]))
    for i, a in enumerate(A):
        out[i] = np.sqrt(((B - a) ** 2).sum(axis=1))
    return out
```
5. **Complexity analysis**: Broadcasting O(n*m*d).
6. **Interview tip**: Interviewers like hearing memory trade-offs of broadcasting.

### Q153: NumPy problem 15: Implement min-max scaling for each feature
1. **Question**: NumPy problem 15: Implement min-max scaling for each feature.
2. **Explanation**: Transform values into [0,1] per column.
3. **Working Python solution**:
```python
import numpy as np

def minmax_scale(X):
    mn, mx = X.min(axis=0), X.max(axis=0)
    span = np.where(mx - mn == 0, 1, mx - mn)
    return (X - mn) / span
```
4. **Alternate solution**:
```python
import numpy as np

def minmax_scale(X):
    out = X.copy().astype(float)
    for j in range(X.shape[1]):
        mn, mx = X[:, j].min(), X[:, j].max()
        out[:, j] = 0 if mx == mn else (X[:, j] - mn) / (mx - mn)
    return out
```
5. **Complexity analysis**: O(n*m).
6. **Interview tip**: Call out dtype conversion to float to avoid integer truncation.

### Q154: NumPy problem 16: Standardize each column in a matrix
1. **Question**: NumPy problem 16: Standardize each column in a matrix.
2. **Explanation**: Subtract column mean and divide by standard deviation.
3. **Working Python solution**:
```python
import numpy as np

def standardize_cols(X):
    mu = X.mean(axis=0)
    sigma = X.std(axis=0)
    sigma = np.where(sigma == 0, 1, sigma)
    return (X - mu) / sigma
```
4. **Alternate solution**:
```python
import numpy as np

def standardize_cols(X):
    return np.apply_along_axis(lambda c: (c - c.mean()) / (c.std() or 1), 0, X)
```
5. **Complexity analysis**: O(n*m).
6. **Interview tip**: Mention numerical stability and zero-variance columns.

### Q155: NumPy problem 17: Compute pairwise Euclidean distances between two matrices
1. **Question**: NumPy problem 17: Compute pairwise Euclidean distances between two matrices.
2. **Explanation**: Use broadcasting to avoid Python loops.
3. **Working Python solution**:
```python
import numpy as np

def pairwise_dist(A, B):
    diff = A[:, None, :] - B[None, :, :]
    return np.sqrt((diff ** 2).sum(axis=2))
```
4. **Alternate solution**:
```python
import numpy as np

def pairwise_dist(A, B):
    out = np.empty((A.shape[0], B.shape[0]))
    for i, a in enumerate(A):
        out[i] = np.sqrt(((B - a) ** 2).sum(axis=1))
    return out
```
5. **Complexity analysis**: Broadcasting O(n*m*d).
6. **Interview tip**: Interviewers like hearing memory trade-offs of broadcasting.

### Q156: NumPy problem 18: Implement min-max scaling for each feature
1. **Question**: NumPy problem 18: Implement min-max scaling for each feature.
2. **Explanation**: Transform values into [0,1] per column.
3. **Working Python solution**:
```python
import numpy as np

def minmax_scale(X):
    mn, mx = X.min(axis=0), X.max(axis=0)
    span = np.where(mx - mn == 0, 1, mx - mn)
    return (X - mn) / span
```
4. **Alternate solution**:
```python
import numpy as np

def minmax_scale(X):
    out = X.copy().astype(float)
    for j in range(X.shape[1]):
        mn, mx = X[:, j].min(), X[:, j].max()
        out[:, j] = 0 if mx == mn else (X[:, j] - mn) / (mx - mn)
    return out
```
5. **Complexity analysis**: O(n*m).
6. **Interview tip**: Call out dtype conversion to float to avoid integer truncation.

### Q157: NumPy problem 19: Standardize each column in a matrix
1. **Question**: NumPy problem 19: Standardize each column in a matrix.
2. **Explanation**: Subtract column mean and divide by standard deviation.
3. **Working Python solution**:
```python
import numpy as np

def standardize_cols(X):
    mu = X.mean(axis=0)
    sigma = X.std(axis=0)
    sigma = np.where(sigma == 0, 1, sigma)
    return (X - mu) / sigma
```
4. **Alternate solution**:
```python
import numpy as np

def standardize_cols(X):
    return np.apply_along_axis(lambda c: (c - c.mean()) / (c.std() or 1), 0, X)
```
5. **Complexity analysis**: O(n*m).
6. **Interview tip**: Mention numerical stability and zero-variance columns.

### Q158: NumPy problem 20: Compute pairwise Euclidean distances between two matrices
1. **Question**: NumPy problem 20: Compute pairwise Euclidean distances between two matrices.
2. **Explanation**: Use broadcasting to avoid Python loops.
3. **Working Python solution**:
```python
import numpy as np

def pairwise_dist(A, B):
    diff = A[:, None, :] - B[None, :, :]
    return np.sqrt((diff ** 2).sum(axis=2))
```
4. **Alternate solution**:
```python
import numpy as np

def pairwise_dist(A, B):
    out = np.empty((A.shape[0], B.shape[0]))
    for i, a in enumerate(A):
        out[i] = np.sqrt(((B - a) ** 2).sum(axis=1))
    return out
```
5. **Complexity analysis**: Broadcasting O(n*m*d).
6. **Interview tip**: Interviewers like hearing memory trade-offs of broadcasting.

### Q159: NumPy problem 21: Implement min-max scaling for each feature
1. **Question**: NumPy problem 21: Implement min-max scaling for each feature.
2. **Explanation**: Transform values into [0,1] per column.
3. **Working Python solution**:
```python
import numpy as np

def minmax_scale(X):
    mn, mx = X.min(axis=0), X.max(axis=0)
    span = np.where(mx - mn == 0, 1, mx - mn)
    return (X - mn) / span
```
4. **Alternate solution**:
```python
import numpy as np

def minmax_scale(X):
    out = X.copy().astype(float)
    for j in range(X.shape[1]):
        mn, mx = X[:, j].min(), X[:, j].max()
        out[:, j] = 0 if mx == mn else (X[:, j] - mn) / (mx - mn)
    return out
```
5. **Complexity analysis**: O(n*m).
6. **Interview tip**: Call out dtype conversion to float to avoid integer truncation.

### Q160: NumPy problem 22: Standardize each column in a matrix
1. **Question**: NumPy problem 22: Standardize each column in a matrix.
2. **Explanation**: Subtract column mean and divide by standard deviation.
3. **Working Python solution**:
```python
import numpy as np

def standardize_cols(X):
    mu = X.mean(axis=0)
    sigma = X.std(axis=0)
    sigma = np.where(sigma == 0, 1, sigma)
    return (X - mu) / sigma
```
4. **Alternate solution**:
```python
import numpy as np

def standardize_cols(X):
    return np.apply_along_axis(lambda c: (c - c.mean()) / (c.std() or 1), 0, X)
```
5. **Complexity analysis**: O(n*m).
6. **Interview tip**: Mention numerical stability and zero-variance columns.

### Q161: NumPy problem 23: Compute pairwise Euclidean distances between two matrices
1. **Question**: NumPy problem 23: Compute pairwise Euclidean distances between two matrices.
2. **Explanation**: Use broadcasting to avoid Python loops.
3. **Working Python solution**:
```python
import numpy as np

def pairwise_dist(A, B):
    diff = A[:, None, :] - B[None, :, :]
    return np.sqrt((diff ** 2).sum(axis=2))
```
4. **Alternate solution**:
```python
import numpy as np

def pairwise_dist(A, B):
    out = np.empty((A.shape[0], B.shape[0]))
    for i, a in enumerate(A):
        out[i] = np.sqrt(((B - a) ** 2).sum(axis=1))
    return out
```
5. **Complexity analysis**: Broadcasting O(n*m*d).
6. **Interview tip**: Interviewers like hearing memory trade-offs of broadcasting.

### Q162: NumPy problem 24: Implement min-max scaling for each feature
1. **Question**: NumPy problem 24: Implement min-max scaling for each feature.
2. **Explanation**: Transform values into [0,1] per column.
3. **Working Python solution**:
```python
import numpy as np

def minmax_scale(X):
    mn, mx = X.min(axis=0), X.max(axis=0)
    span = np.where(mx - mn == 0, 1, mx - mn)
    return (X - mn) / span
```
4. **Alternate solution**:
```python
import numpy as np

def minmax_scale(X):
    out = X.copy().astype(float)
    for j in range(X.shape[1]):
        mn, mx = X[:, j].min(), X[:, j].max()
        out[:, j] = 0 if mx == mn else (X[:, j] - mn) / (mx - mn)
    return out
```
5. **Complexity analysis**: O(n*m).
6. **Interview tip**: Call out dtype conversion to float to avoid integer truncation.

### Q163: NumPy problem 25: Standardize each column in a matrix
1. **Question**: NumPy problem 25: Standardize each column in a matrix.
2. **Explanation**: Subtract column mean and divide by standard deviation.
3. **Working Python solution**:
```python
import numpy as np

def standardize_cols(X):
    mu = X.mean(axis=0)
    sigma = X.std(axis=0)
    sigma = np.where(sigma == 0, 1, sigma)
    return (X - mu) / sigma
```
4. **Alternate solution**:
```python
import numpy as np

def standardize_cols(X):
    return np.apply_along_axis(lambda c: (c - c.mean()) / (c.std() or 1), 0, X)
```
5. **Complexity analysis**: O(n*m).
6. **Interview tip**: Mention numerical stability and zero-variance columns.

### Q164: NumPy problem 26: Compute pairwise Euclidean distances between two matrices
1. **Question**: NumPy problem 26: Compute pairwise Euclidean distances between two matrices.
2. **Explanation**: Use broadcasting to avoid Python loops.
3. **Working Python solution**:
```python
import numpy as np

def pairwise_dist(A, B):
    diff = A[:, None, :] - B[None, :, :]
    return np.sqrt((diff ** 2).sum(axis=2))
```
4. **Alternate solution**:
```python
import numpy as np

def pairwise_dist(A, B):
    out = np.empty((A.shape[0], B.shape[0]))
    for i, a in enumerate(A):
        out[i] = np.sqrt(((B - a) ** 2).sum(axis=1))
    return out
```
5. **Complexity analysis**: Broadcasting O(n*m*d).
6. **Interview tip**: Interviewers like hearing memory trade-offs of broadcasting.

### Q165: NumPy problem 27: Implement min-max scaling for each feature
1. **Question**: NumPy problem 27: Implement min-max scaling for each feature.
2. **Explanation**: Transform values into [0,1] per column.
3. **Working Python solution**:
```python
import numpy as np

def minmax_scale(X):
    mn, mx = X.min(axis=0), X.max(axis=0)
    span = np.where(mx - mn == 0, 1, mx - mn)
    return (X - mn) / span
```
4. **Alternate solution**:
```python
import numpy as np

def minmax_scale(X):
    out = X.copy().astype(float)
    for j in range(X.shape[1]):
        mn, mx = X[:, j].min(), X[:, j].max()
        out[:, j] = 0 if mx == mn else (X[:, j] - mn) / (mx - mn)
    return out
```
5. **Complexity analysis**: O(n*m).
6. **Interview tip**: Call out dtype conversion to float to avoid integer truncation.

### Q166: NumPy problem 28: Standardize each column in a matrix
1. **Question**: NumPy problem 28: Standardize each column in a matrix.
2. **Explanation**: Subtract column mean and divide by standard deviation.
3. **Working Python solution**:
```python
import numpy as np

def standardize_cols(X):
    mu = X.mean(axis=0)
    sigma = X.std(axis=0)
    sigma = np.where(sigma == 0, 1, sigma)
    return (X - mu) / sigma
```
4. **Alternate solution**:
```python
import numpy as np

def standardize_cols(X):
    return np.apply_along_axis(lambda c: (c - c.mean()) / (c.std() or 1), 0, X)
```
5. **Complexity analysis**: O(n*m).
6. **Interview tip**: Mention numerical stability and zero-variance columns.

## Pandas

### Q167: Pandas problem 1: Get top 3 products by revenue per category
1. **Question**: Pandas problem 1: Get top 3 products by revenue per category.
2. **Explanation**: Use groupby and nlargest on aggregated revenue.
3. **Working Python solution**:
```python
import pandas as pd

def top_products(df):
    revenue = df.assign(revenue=df['price'] * df['qty'])
    agg = revenue.groupby(['category', 'product'], as_index=False)['revenue'].sum()
    return agg.sort_values(['category', 'revenue'], ascending=[True, False]).groupby('category').head(3)
```
4. **Alternate solution**:
```python
import pandas as pd

def top_products(df):
    df = df.copy()
    df['revenue'] = df['price'] * df['qty']
    return (df.pivot_table(index='product', columns='category', values='revenue', aggfunc='sum')
              .apply(lambda col: col.nlargest(3).dropna().index.tolist()))
```
5. **Complexity analysis**: O(n log n).
6. **Interview tip**: Check interviewer preference for tidy output vs nested lists.

### Q168: Pandas problem 2: Fill missing age by median within each city
1. **Question**: Pandas problem 2: Fill missing age by median within each city.
2. **Explanation**: Group-wise imputation with transform.
3. **Working Python solution**:
```python
import pandas as pd

def impute_age(df):
    out = df.copy()
    out['age'] = out['age'].fillna(out.groupby('city')['age'].transform('median'))
    return out
```
4. **Alternate solution**:
```python
import pandas as pd

def impute_age(df):
    out = df.copy()
    med = out.groupby('city')['age'].median().to_dict()
    out['age'] = out.apply(lambda r: med[r['city']] if pd.isna(r['age']) else r['age'], axis=1)
    return out
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Mention leakage risk if used before train/test split.

### Q169: Pandas problem 3: Compute 7-day rolling mean per user
1. **Question**: Pandas problem 3: Compute 7-day rolling mean per user.
2. **Explanation**: Sort by user/date and apply rolling window.
3. **Working Python solution**:
```python
import pandas as pd

def rolling_user_mean(df):
    d = df.sort_values(['user_id', 'date']).copy()
    d['rolling_7'] = d.groupby('user_id')['value'].transform(lambda s: s.rolling(7, min_periods=1).mean())
    return d
```
4. **Alternate solution**:
```python
import pandas as pd

def rolling_user_mean(df):
    parts = []
    for uid, g in df.sort_values('date').groupby('user_id'):
        g = g.copy()
        g['rolling_7'] = g['value'].rolling(7, min_periods=1).mean()
        parts.append(g)
    return pd.concat(parts).sort_index()
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Ensure date dtype is datetime before time ops.

### Q170: Pandas problem 4: Get top 3 products by revenue per category
1. **Question**: Pandas problem 4: Get top 3 products by revenue per category.
2. **Explanation**: Use groupby and nlargest on aggregated revenue.
3. **Working Python solution**:
```python
import pandas as pd

def top_products(df):
    revenue = df.assign(revenue=df['price'] * df['qty'])
    agg = revenue.groupby(['category', 'product'], as_index=False)['revenue'].sum()
    return agg.sort_values(['category', 'revenue'], ascending=[True, False]).groupby('category').head(3)
```
4. **Alternate solution**:
```python
import pandas as pd

def top_products(df):
    df = df.copy()
    df['revenue'] = df['price'] * df['qty']
    return (df.pivot_table(index='product', columns='category', values='revenue', aggfunc='sum')
              .apply(lambda col: col.nlargest(3).dropna().index.tolist()))
```
5. **Complexity analysis**: O(n log n).
6. **Interview tip**: Check interviewer preference for tidy output vs nested lists.

### Q171: Pandas problem 5: Fill missing age by median within each city
1. **Question**: Pandas problem 5: Fill missing age by median within each city.
2. **Explanation**: Group-wise imputation with transform.
3. **Working Python solution**:
```python
import pandas as pd

def impute_age(df):
    out = df.copy()
    out['age'] = out['age'].fillna(out.groupby('city')['age'].transform('median'))
    return out
```
4. **Alternate solution**:
```python
import pandas as pd

def impute_age(df):
    out = df.copy()
    med = out.groupby('city')['age'].median().to_dict()
    out['age'] = out.apply(lambda r: med[r['city']] if pd.isna(r['age']) else r['age'], axis=1)
    return out
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Mention leakage risk if used before train/test split.

### Q172: Pandas problem 6: Compute 7-day rolling mean per user
1. **Question**: Pandas problem 6: Compute 7-day rolling mean per user.
2. **Explanation**: Sort by user/date and apply rolling window.
3. **Working Python solution**:
```python
import pandas as pd

def rolling_user_mean(df):
    d = df.sort_values(['user_id', 'date']).copy()
    d['rolling_7'] = d.groupby('user_id')['value'].transform(lambda s: s.rolling(7, min_periods=1).mean())
    return d
```
4. **Alternate solution**:
```python
import pandas as pd

def rolling_user_mean(df):
    parts = []
    for uid, g in df.sort_values('date').groupby('user_id'):
        g = g.copy()
        g['rolling_7'] = g['value'].rolling(7, min_periods=1).mean()
        parts.append(g)
    return pd.concat(parts).sort_index()
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Ensure date dtype is datetime before time ops.

### Q173: Pandas problem 7: Get top 3 products by revenue per category
1. **Question**: Pandas problem 7: Get top 3 products by revenue per category.
2. **Explanation**: Use groupby and nlargest on aggregated revenue.
3. **Working Python solution**:
```python
import pandas as pd

def top_products(df):
    revenue = df.assign(revenue=df['price'] * df['qty'])
    agg = revenue.groupby(['category', 'product'], as_index=False)['revenue'].sum()
    return agg.sort_values(['category', 'revenue'], ascending=[True, False]).groupby('category').head(3)
```
4. **Alternate solution**:
```python
import pandas as pd

def top_products(df):
    df = df.copy()
    df['revenue'] = df['price'] * df['qty']
    return (df.pivot_table(index='product', columns='category', values='revenue', aggfunc='sum')
              .apply(lambda col: col.nlargest(3).dropna().index.tolist()))
```
5. **Complexity analysis**: O(n log n).
6. **Interview tip**: Check interviewer preference for tidy output vs nested lists.

### Q174: Pandas problem 8: Fill missing age by median within each city
1. **Question**: Pandas problem 8: Fill missing age by median within each city.
2. **Explanation**: Group-wise imputation with transform.
3. **Working Python solution**:
```python
import pandas as pd

def impute_age(df):
    out = df.copy()
    out['age'] = out['age'].fillna(out.groupby('city')['age'].transform('median'))
    return out
```
4. **Alternate solution**:
```python
import pandas as pd

def impute_age(df):
    out = df.copy()
    med = out.groupby('city')['age'].median().to_dict()
    out['age'] = out.apply(lambda r: med[r['city']] if pd.isna(r['age']) else r['age'], axis=1)
    return out
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Mention leakage risk if used before train/test split.

### Q175: Pandas problem 9: Compute 7-day rolling mean per user
1. **Question**: Pandas problem 9: Compute 7-day rolling mean per user.
2. **Explanation**: Sort by user/date and apply rolling window.
3. **Working Python solution**:
```python
import pandas as pd

def rolling_user_mean(df):
    d = df.sort_values(['user_id', 'date']).copy()
    d['rolling_7'] = d.groupby('user_id')['value'].transform(lambda s: s.rolling(7, min_periods=1).mean())
    return d
```
4. **Alternate solution**:
```python
import pandas as pd

def rolling_user_mean(df):
    parts = []
    for uid, g in df.sort_values('date').groupby('user_id'):
        g = g.copy()
        g['rolling_7'] = g['value'].rolling(7, min_periods=1).mean()
        parts.append(g)
    return pd.concat(parts).sort_index()
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Ensure date dtype is datetime before time ops.

### Q176: Pandas problem 10: Get top 3 products by revenue per category
1. **Question**: Pandas problem 10: Get top 3 products by revenue per category.
2. **Explanation**: Use groupby and nlargest on aggregated revenue.
3. **Working Python solution**:
```python
import pandas as pd

def top_products(df):
    revenue = df.assign(revenue=df['price'] * df['qty'])
    agg = revenue.groupby(['category', 'product'], as_index=False)['revenue'].sum()
    return agg.sort_values(['category', 'revenue'], ascending=[True, False]).groupby('category').head(3)
```
4. **Alternate solution**:
```python
import pandas as pd

def top_products(df):
    df = df.copy()
    df['revenue'] = df['price'] * df['qty']
    return (df.pivot_table(index='product', columns='category', values='revenue', aggfunc='sum')
              .apply(lambda col: col.nlargest(3).dropna().index.tolist()))
```
5. **Complexity analysis**: O(n log n).
6. **Interview tip**: Check interviewer preference for tidy output vs nested lists.

### Q177: Pandas problem 11: Fill missing age by median within each city
1. **Question**: Pandas problem 11: Fill missing age by median within each city.
2. **Explanation**: Group-wise imputation with transform.
3. **Working Python solution**:
```python
import pandas as pd

def impute_age(df):
    out = df.copy()
    out['age'] = out['age'].fillna(out.groupby('city')['age'].transform('median'))
    return out
```
4. **Alternate solution**:
```python
import pandas as pd

def impute_age(df):
    out = df.copy()
    med = out.groupby('city')['age'].median().to_dict()
    out['age'] = out.apply(lambda r: med[r['city']] if pd.isna(r['age']) else r['age'], axis=1)
    return out
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Mention leakage risk if used before train/test split.

### Q178: Pandas problem 12: Compute 7-day rolling mean per user
1. **Question**: Pandas problem 12: Compute 7-day rolling mean per user.
2. **Explanation**: Sort by user/date and apply rolling window.
3. **Working Python solution**:
```python
import pandas as pd

def rolling_user_mean(df):
    d = df.sort_values(['user_id', 'date']).copy()
    d['rolling_7'] = d.groupby('user_id')['value'].transform(lambda s: s.rolling(7, min_periods=1).mean())
    return d
```
4. **Alternate solution**:
```python
import pandas as pd

def rolling_user_mean(df):
    parts = []
    for uid, g in df.sort_values('date').groupby('user_id'):
        g = g.copy()
        g['rolling_7'] = g['value'].rolling(7, min_periods=1).mean()
        parts.append(g)
    return pd.concat(parts).sort_index()
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Ensure date dtype is datetime before time ops.

### Q179: Pandas problem 13: Get top 3 products by revenue per category
1. **Question**: Pandas problem 13: Get top 3 products by revenue per category.
2. **Explanation**: Use groupby and nlargest on aggregated revenue.
3. **Working Python solution**:
```python
import pandas as pd

def top_products(df):
    revenue = df.assign(revenue=df['price'] * df['qty'])
    agg = revenue.groupby(['category', 'product'], as_index=False)['revenue'].sum()
    return agg.sort_values(['category', 'revenue'], ascending=[True, False]).groupby('category').head(3)
```
4. **Alternate solution**:
```python
import pandas as pd

def top_products(df):
    df = df.copy()
    df['revenue'] = df['price'] * df['qty']
    return (df.pivot_table(index='product', columns='category', values='revenue', aggfunc='sum')
              .apply(lambda col: col.nlargest(3).dropna().index.tolist()))
```
5. **Complexity analysis**: O(n log n).
6. **Interview tip**: Check interviewer preference for tidy output vs nested lists.

### Q180: Pandas problem 14: Fill missing age by median within each city
1. **Question**: Pandas problem 14: Fill missing age by median within each city.
2. **Explanation**: Group-wise imputation with transform.
3. **Working Python solution**:
```python
import pandas as pd

def impute_age(df):
    out = df.copy()
    out['age'] = out['age'].fillna(out.groupby('city')['age'].transform('median'))
    return out
```
4. **Alternate solution**:
```python
import pandas as pd

def impute_age(df):
    out = df.copy()
    med = out.groupby('city')['age'].median().to_dict()
    out['age'] = out.apply(lambda r: med[r['city']] if pd.isna(r['age']) else r['age'], axis=1)
    return out
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Mention leakage risk if used before train/test split.

### Q181: Pandas problem 15: Compute 7-day rolling mean per user
1. **Question**: Pandas problem 15: Compute 7-day rolling mean per user.
2. **Explanation**: Sort by user/date and apply rolling window.
3. **Working Python solution**:
```python
import pandas as pd

def rolling_user_mean(df):
    d = df.sort_values(['user_id', 'date']).copy()
    d['rolling_7'] = d.groupby('user_id')['value'].transform(lambda s: s.rolling(7, min_periods=1).mean())
    return d
```
4. **Alternate solution**:
```python
import pandas as pd

def rolling_user_mean(df):
    parts = []
    for uid, g in df.sort_values('date').groupby('user_id'):
        g = g.copy()
        g['rolling_7'] = g['value'].rolling(7, min_periods=1).mean()
        parts.append(g)
    return pd.concat(parts).sort_index()
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Ensure date dtype is datetime before time ops.

### Q182: Pandas problem 16: Get top 3 products by revenue per category
1. **Question**: Pandas problem 16: Get top 3 products by revenue per category.
2. **Explanation**: Use groupby and nlargest on aggregated revenue.
3. **Working Python solution**:
```python
import pandas as pd

def top_products(df):
    revenue = df.assign(revenue=df['price'] * df['qty'])
    agg = revenue.groupby(['category', 'product'], as_index=False)['revenue'].sum()
    return agg.sort_values(['category', 'revenue'], ascending=[True, False]).groupby('category').head(3)
```
4. **Alternate solution**:
```python
import pandas as pd

def top_products(df):
    df = df.copy()
    df['revenue'] = df['price'] * df['qty']
    return (df.pivot_table(index='product', columns='category', values='revenue', aggfunc='sum')
              .apply(lambda col: col.nlargest(3).dropna().index.tolist()))
```
5. **Complexity analysis**: O(n log n).
6. **Interview tip**: Check interviewer preference for tidy output vs nested lists.

### Q183: Pandas problem 17: Fill missing age by median within each city
1. **Question**: Pandas problem 17: Fill missing age by median within each city.
2. **Explanation**: Group-wise imputation with transform.
3. **Working Python solution**:
```python
import pandas as pd

def impute_age(df):
    out = df.copy()
    out['age'] = out['age'].fillna(out.groupby('city')['age'].transform('median'))
    return out
```
4. **Alternate solution**:
```python
import pandas as pd

def impute_age(df):
    out = df.copy()
    med = out.groupby('city')['age'].median().to_dict()
    out['age'] = out.apply(lambda r: med[r['city']] if pd.isna(r['age']) else r['age'], axis=1)
    return out
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Mention leakage risk if used before train/test split.

### Q184: Pandas problem 18: Compute 7-day rolling mean per user
1. **Question**: Pandas problem 18: Compute 7-day rolling mean per user.
2. **Explanation**: Sort by user/date and apply rolling window.
3. **Working Python solution**:
```python
import pandas as pd

def rolling_user_mean(df):
    d = df.sort_values(['user_id', 'date']).copy()
    d['rolling_7'] = d.groupby('user_id')['value'].transform(lambda s: s.rolling(7, min_periods=1).mean())
    return d
```
4. **Alternate solution**:
```python
import pandas as pd

def rolling_user_mean(df):
    parts = []
    for uid, g in df.sort_values('date').groupby('user_id'):
        g = g.copy()
        g['rolling_7'] = g['value'].rolling(7, min_periods=1).mean()
        parts.append(g)
    return pd.concat(parts).sort_index()
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Ensure date dtype is datetime before time ops.

### Q185: Pandas problem 19: Get top 3 products by revenue per category
1. **Question**: Pandas problem 19: Get top 3 products by revenue per category.
2. **Explanation**: Use groupby and nlargest on aggregated revenue.
3. **Working Python solution**:
```python
import pandas as pd

def top_products(df):
    revenue = df.assign(revenue=df['price'] * df['qty'])
    agg = revenue.groupby(['category', 'product'], as_index=False)['revenue'].sum()
    return agg.sort_values(['category', 'revenue'], ascending=[True, False]).groupby('category').head(3)
```
4. **Alternate solution**:
```python
import pandas as pd

def top_products(df):
    df = df.copy()
    df['revenue'] = df['price'] * df['qty']
    return (df.pivot_table(index='product', columns='category', values='revenue', aggfunc='sum')
              .apply(lambda col: col.nlargest(3).dropna().index.tolist()))
```
5. **Complexity analysis**: O(n log n).
6. **Interview tip**: Check interviewer preference for tidy output vs nested lists.

### Q186: Pandas problem 20: Fill missing age by median within each city
1. **Question**: Pandas problem 20: Fill missing age by median within each city.
2. **Explanation**: Group-wise imputation with transform.
3. **Working Python solution**:
```python
import pandas as pd

def impute_age(df):
    out = df.copy()
    out['age'] = out['age'].fillna(out.groupby('city')['age'].transform('median'))
    return out
```
4. **Alternate solution**:
```python
import pandas as pd

def impute_age(df):
    out = df.copy()
    med = out.groupby('city')['age'].median().to_dict()
    out['age'] = out.apply(lambda r: med[r['city']] if pd.isna(r['age']) else r['age'], axis=1)
    return out
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Mention leakage risk if used before train/test split.

### Q187: Pandas problem 21: Compute 7-day rolling mean per user
1. **Question**: Pandas problem 21: Compute 7-day rolling mean per user.
2. **Explanation**: Sort by user/date and apply rolling window.
3. **Working Python solution**:
```python
import pandas as pd

def rolling_user_mean(df):
    d = df.sort_values(['user_id', 'date']).copy()
    d['rolling_7'] = d.groupby('user_id')['value'].transform(lambda s: s.rolling(7, min_periods=1).mean())
    return d
```
4. **Alternate solution**:
```python
import pandas as pd

def rolling_user_mean(df):
    parts = []
    for uid, g in df.sort_values('date').groupby('user_id'):
        g = g.copy()
        g['rolling_7'] = g['value'].rolling(7, min_periods=1).mean()
        parts.append(g)
    return pd.concat(parts).sort_index()
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Ensure date dtype is datetime before time ops.

### Q188: Pandas problem 22: Get top 3 products by revenue per category
1. **Question**: Pandas problem 22: Get top 3 products by revenue per category.
2. **Explanation**: Use groupby and nlargest on aggregated revenue.
3. **Working Python solution**:
```python
import pandas as pd

def top_products(df):
    revenue = df.assign(revenue=df['price'] * df['qty'])
    agg = revenue.groupby(['category', 'product'], as_index=False)['revenue'].sum()
    return agg.sort_values(['category', 'revenue'], ascending=[True, False]).groupby('category').head(3)
```
4. **Alternate solution**:
```python
import pandas as pd

def top_products(df):
    df = df.copy()
    df['revenue'] = df['price'] * df['qty']
    return (df.pivot_table(index='product', columns='category', values='revenue', aggfunc='sum')
              .apply(lambda col: col.nlargest(3).dropna().index.tolist()))
```
5. **Complexity analysis**: O(n log n).
6. **Interview tip**: Check interviewer preference for tidy output vs nested lists.

### Q189: Pandas problem 23: Fill missing age by median within each city
1. **Question**: Pandas problem 23: Fill missing age by median within each city.
2. **Explanation**: Group-wise imputation with transform.
3. **Working Python solution**:
```python
import pandas as pd

def impute_age(df):
    out = df.copy()
    out['age'] = out['age'].fillna(out.groupby('city')['age'].transform('median'))
    return out
```
4. **Alternate solution**:
```python
import pandas as pd

def impute_age(df):
    out = df.copy()
    med = out.groupby('city')['age'].median().to_dict()
    out['age'] = out.apply(lambda r: med[r['city']] if pd.isna(r['age']) else r['age'], axis=1)
    return out
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Mention leakage risk if used before train/test split.

### Q190: Pandas problem 24: Compute 7-day rolling mean per user
1. **Question**: Pandas problem 24: Compute 7-day rolling mean per user.
2. **Explanation**: Sort by user/date and apply rolling window.
3. **Working Python solution**:
```python
import pandas as pd

def rolling_user_mean(df):
    d = df.sort_values(['user_id', 'date']).copy()
    d['rolling_7'] = d.groupby('user_id')['value'].transform(lambda s: s.rolling(7, min_periods=1).mean())
    return d
```
4. **Alternate solution**:
```python
import pandas as pd

def rolling_user_mean(df):
    parts = []
    for uid, g in df.sort_values('date').groupby('user_id'):
        g = g.copy()
        g['rolling_7'] = g['value'].rolling(7, min_periods=1).mean()
        parts.append(g)
    return pd.concat(parts).sort_index()
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Ensure date dtype is datetime before time ops.

### Q191: Pandas problem 25: Get top 3 products by revenue per category
1. **Question**: Pandas problem 25: Get top 3 products by revenue per category.
2. **Explanation**: Use groupby and nlargest on aggregated revenue.
3. **Working Python solution**:
```python
import pandas as pd

def top_products(df):
    revenue = df.assign(revenue=df['price'] * df['qty'])
    agg = revenue.groupby(['category', 'product'], as_index=False)['revenue'].sum()
    return agg.sort_values(['category', 'revenue'], ascending=[True, False]).groupby('category').head(3)
```
4. **Alternate solution**:
```python
import pandas as pd

def top_products(df):
    df = df.copy()
    df['revenue'] = df['price'] * df['qty']
    return (df.pivot_table(index='product', columns='category', values='revenue', aggfunc='sum')
              .apply(lambda col: col.nlargest(3).dropna().index.tolist()))
```
5. **Complexity analysis**: O(n log n).
6. **Interview tip**: Check interviewer preference for tidy output vs nested lists.

### Q192: Pandas problem 26: Fill missing age by median within each city
1. **Question**: Pandas problem 26: Fill missing age by median within each city.
2. **Explanation**: Group-wise imputation with transform.
3. **Working Python solution**:
```python
import pandas as pd

def impute_age(df):
    out = df.copy()
    out['age'] = out['age'].fillna(out.groupby('city')['age'].transform('median'))
    return out
```
4. **Alternate solution**:
```python
import pandas as pd

def impute_age(df):
    out = df.copy()
    med = out.groupby('city')['age'].median().to_dict()
    out['age'] = out.apply(lambda r: med[r['city']] if pd.isna(r['age']) else r['age'], axis=1)
    return out
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Mention leakage risk if used before train/test split.

### Q193: Pandas problem 27: Compute 7-day rolling mean per user
1. **Question**: Pandas problem 27: Compute 7-day rolling mean per user.
2. **Explanation**: Sort by user/date and apply rolling window.
3. **Working Python solution**:
```python
import pandas as pd

def rolling_user_mean(df):
    d = df.sort_values(['user_id', 'date']).copy()
    d['rolling_7'] = d.groupby('user_id')['value'].transform(lambda s: s.rolling(7, min_periods=1).mean())
    return d
```
4. **Alternate solution**:
```python
import pandas as pd

def rolling_user_mean(df):
    parts = []
    for uid, g in df.sort_values('date').groupby('user_id'):
        g = g.copy()
        g['rolling_7'] = g['value'].rolling(7, min_periods=1).mean()
        parts.append(g)
    return pd.concat(parts).sort_index()
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Ensure date dtype is datetime before time ops.

### Q194: Pandas problem 28: Get top 3 products by revenue per category
1. **Question**: Pandas problem 28: Get top 3 products by revenue per category.
2. **Explanation**: Use groupby and nlargest on aggregated revenue.
3. **Working Python solution**:
```python
import pandas as pd

def top_products(df):
    revenue = df.assign(revenue=df['price'] * df['qty'])
    agg = revenue.groupby(['category', 'product'], as_index=False)['revenue'].sum()
    return agg.sort_values(['category', 'revenue'], ascending=[True, False]).groupby('category').head(3)
```
4. **Alternate solution**:
```python
import pandas as pd

def top_products(df):
    df = df.copy()
    df['revenue'] = df['price'] * df['qty']
    return (df.pivot_table(index='product', columns='category', values='revenue', aggfunc='sum')
              .apply(lambda col: col.nlargest(3).dropna().index.tolist()))
```
5. **Complexity analysis**: O(n log n).
6. **Interview tip**: Check interviewer preference for tidy output vs nested lists.

## ML-related Python

### Q195: ML Python question 1: Implement train/validation split with reproducible shuffle
1. **Question**: ML Python question 1: Implement train/validation split with reproducible shuffle.
2. **Explanation**: Shuffle indices with random seed and split by ratio.
3. **Working Python solution**:
```python
import numpy as np

def train_val_split(X, y, val_ratio=0.2, seed=42):
    rng = np.random.default_rng(seed)
    idx = np.arange(len(X))
    rng.shuffle(idx)
    cut = int(len(X) * (1 - val_ratio))
    tr, va = idx[:cut], idx[cut:]
    return X[tr], X[va], y[tr], y[va]
```
4. **Alternate solution**:
```python
def train_val_split(X, y, val_ratio=0.2):
    cut = int(len(X) * (1 - val_ratio))
    return X[:cut], X[cut:], y[:cut], y[cut:]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Discuss why random split can break time-series tasks.

### Q196: ML Python question 2: Compute binary classification metrics from predictions
1. **Question**: ML Python question 2: Compute binary classification metrics from predictions.
2. **Explanation**: Derive precision, recall, F1, and accuracy from confusion counts.
3. **Working Python solution**:
```python
def classification_metrics(y_true, y_pred):
    tp = sum(1 for t,p in zip(y_true,y_pred) if t==1 and p==1)
    tn = sum(1 for t,p in zip(y_true,y_pred) if t==0 and p==0)
    fp = sum(1 for t,p in zip(y_true,y_pred) if t==0 and p==1)
    fn = sum(1 for t,p in zip(y_true,y_pred) if t==1 and p==0)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2*precision*recall/(precision+recall) if precision+recall else 0.0
    acc = (tp+tn)/len(y_true) if y_true else 0.0
    return {'precision':precision,'recall':recall,'f1':f1,'accuracy':acc}
```
4. **Alternate solution**:
```python
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

def classification_metrics(y_true, y_pred):
    return {
        'precision': precision_score(y_true,y_pred,zero_division=0),
        'recall': recall_score(y_true,y_pred,zero_division=0),
        'f1': f1_score(y_true,y_pred,zero_division=0),
        'accuracy': accuracy_score(y_true,y_pred)
    }
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Explicitly handle divide-by-zero cases.

### Q197: ML Python question 3: Build mini-batch generator for SGD
1. **Question**: ML Python question 3: Build mini-batch generator for SGD.
2. **Explanation**: Yield slices of shuffled arrays in batch_size chunks.
3. **Working Python solution**:
```python
import numpy as np

def batch_iter(X, y, batch_size, seed=0):
    rng = np.random.default_rng(seed)
    idx = np.arange(len(X))
    rng.shuffle(idx)
    for i in range(0, len(idx), batch_size):
        b = idx[i:i+batch_size]
        yield X[b], y[b]
```
4. **Alternate solution**:
```python
def batch_iter(X, y, batch_size, seed=0):
    for i in range(0, len(X), batch_size):
        yield X[i:i+batch_size], y[i:i+batch_size]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Mention memory benefit of generators in training loops.

### Q198: ML Python question 4: Implement train/validation split with reproducible shuffle
1. **Question**: ML Python question 4: Implement train/validation split with reproducible shuffle.
2. **Explanation**: Shuffle indices with random seed and split by ratio.
3. **Working Python solution**:
```python
import numpy as np

def train_val_split(X, y, val_ratio=0.2, seed=42):
    rng = np.random.default_rng(seed)
    idx = np.arange(len(X))
    rng.shuffle(idx)
    cut = int(len(X) * (1 - val_ratio))
    tr, va = idx[:cut], idx[cut:]
    return X[tr], X[va], y[tr], y[va]
```
4. **Alternate solution**:
```python
def train_val_split(X, y, val_ratio=0.2):
    cut = int(len(X) * (1 - val_ratio))
    return X[:cut], X[cut:], y[:cut], y[cut:]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Discuss why random split can break time-series tasks.

### Q199: ML Python question 5: Compute binary classification metrics from predictions
1. **Question**: ML Python question 5: Compute binary classification metrics from predictions.
2. **Explanation**: Derive precision, recall, F1, and accuracy from confusion counts.
3. **Working Python solution**:
```python
def classification_metrics(y_true, y_pred):
    tp = sum(1 for t,p in zip(y_true,y_pred) if t==1 and p==1)
    tn = sum(1 for t,p in zip(y_true,y_pred) if t==0 and p==0)
    fp = sum(1 for t,p in zip(y_true,y_pred) if t==0 and p==1)
    fn = sum(1 for t,p in zip(y_true,y_pred) if t==1 and p==0)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2*precision*recall/(precision+recall) if precision+recall else 0.0
    acc = (tp+tn)/len(y_true) if y_true else 0.0
    return {'precision':precision,'recall':recall,'f1':f1,'accuracy':acc}
```
4. **Alternate solution**:
```python
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

def classification_metrics(y_true, y_pred):
    return {
        'precision': precision_score(y_true,y_pred,zero_division=0),
        'recall': recall_score(y_true,y_pred,zero_division=0),
        'f1': f1_score(y_true,y_pred,zero_division=0),
        'accuracy': accuracy_score(y_true,y_pred)
    }
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Explicitly handle divide-by-zero cases.

### Q200: ML Python question 6: Build mini-batch generator for SGD
1. **Question**: ML Python question 6: Build mini-batch generator for SGD.
2. **Explanation**: Yield slices of shuffled arrays in batch_size chunks.
3. **Working Python solution**:
```python
import numpy as np

def batch_iter(X, y, batch_size, seed=0):
    rng = np.random.default_rng(seed)
    idx = np.arange(len(X))
    rng.shuffle(idx)
    for i in range(0, len(idx), batch_size):
        b = idx[i:i+batch_size]
        yield X[b], y[b]
```
4. **Alternate solution**:
```python
def batch_iter(X, y, batch_size, seed=0):
    for i in range(0, len(X), batch_size):
        yield X[i:i+batch_size], y[i:i+batch_size]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Mention memory benefit of generators in training loops.

### Q201: ML Python question 7: Implement train/validation split with reproducible shuffle
1. **Question**: ML Python question 7: Implement train/validation split with reproducible shuffle.
2. **Explanation**: Shuffle indices with random seed and split by ratio.
3. **Working Python solution**:
```python
import numpy as np

def train_val_split(X, y, val_ratio=0.2, seed=42):
    rng = np.random.default_rng(seed)
    idx = np.arange(len(X))
    rng.shuffle(idx)
    cut = int(len(X) * (1 - val_ratio))
    tr, va = idx[:cut], idx[cut:]
    return X[tr], X[va], y[tr], y[va]
```
4. **Alternate solution**:
```python
def train_val_split(X, y, val_ratio=0.2):
    cut = int(len(X) * (1 - val_ratio))
    return X[:cut], X[cut:], y[:cut], y[cut:]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Discuss why random split can break time-series tasks.

### Q202: ML Python question 8: Compute binary classification metrics from predictions
1. **Question**: ML Python question 8: Compute binary classification metrics from predictions.
2. **Explanation**: Derive precision, recall, F1, and accuracy from confusion counts.
3. **Working Python solution**:
```python
def classification_metrics(y_true, y_pred):
    tp = sum(1 for t,p in zip(y_true,y_pred) if t==1 and p==1)
    tn = sum(1 for t,p in zip(y_true,y_pred) if t==0 and p==0)
    fp = sum(1 for t,p in zip(y_true,y_pred) if t==0 and p==1)
    fn = sum(1 for t,p in zip(y_true,y_pred) if t==1 and p==0)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2*precision*recall/(precision+recall) if precision+recall else 0.0
    acc = (tp+tn)/len(y_true) if y_true else 0.0
    return {'precision':precision,'recall':recall,'f1':f1,'accuracy':acc}
```
4. **Alternate solution**:
```python
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

def classification_metrics(y_true, y_pred):
    return {
        'precision': precision_score(y_true,y_pred,zero_division=0),
        'recall': recall_score(y_true,y_pred,zero_division=0),
        'f1': f1_score(y_true,y_pred,zero_division=0),
        'accuracy': accuracy_score(y_true,y_pred)
    }
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Explicitly handle divide-by-zero cases.

### Q203: ML Python question 9: Build mini-batch generator for SGD
1. **Question**: ML Python question 9: Build mini-batch generator for SGD.
2. **Explanation**: Yield slices of shuffled arrays in batch_size chunks.
3. **Working Python solution**:
```python
import numpy as np

def batch_iter(X, y, batch_size, seed=0):
    rng = np.random.default_rng(seed)
    idx = np.arange(len(X))
    rng.shuffle(idx)
    for i in range(0, len(idx), batch_size):
        b = idx[i:i+batch_size]
        yield X[b], y[b]
```
4. **Alternate solution**:
```python
def batch_iter(X, y, batch_size, seed=0):
    for i in range(0, len(X), batch_size):
        yield X[i:i+batch_size], y[i:i+batch_size]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Mention memory benefit of generators in training loops.

### Q204: ML Python question 10: Implement train/validation split with reproducible shuffle
1. **Question**: ML Python question 10: Implement train/validation split with reproducible shuffle.
2. **Explanation**: Shuffle indices with random seed and split by ratio.
3. **Working Python solution**:
```python
import numpy as np

def train_val_split(X, y, val_ratio=0.2, seed=42):
    rng = np.random.default_rng(seed)
    idx = np.arange(len(X))
    rng.shuffle(idx)
    cut = int(len(X) * (1 - val_ratio))
    tr, va = idx[:cut], idx[cut:]
    return X[tr], X[va], y[tr], y[va]
```
4. **Alternate solution**:
```python
def train_val_split(X, y, val_ratio=0.2):
    cut = int(len(X) * (1 - val_ratio))
    return X[:cut], X[cut:], y[:cut], y[cut:]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Discuss why random split can break time-series tasks.

### Q205: ML Python question 11: Compute binary classification metrics from predictions
1. **Question**: ML Python question 11: Compute binary classification metrics from predictions.
2. **Explanation**: Derive precision, recall, F1, and accuracy from confusion counts.
3. **Working Python solution**:
```python
def classification_metrics(y_true, y_pred):
    tp = sum(1 for t,p in zip(y_true,y_pred) if t==1 and p==1)
    tn = sum(1 for t,p in zip(y_true,y_pred) if t==0 and p==0)
    fp = sum(1 for t,p in zip(y_true,y_pred) if t==0 and p==1)
    fn = sum(1 for t,p in zip(y_true,y_pred) if t==1 and p==0)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2*precision*recall/(precision+recall) if precision+recall else 0.0
    acc = (tp+tn)/len(y_true) if y_true else 0.0
    return {'precision':precision,'recall':recall,'f1':f1,'accuracy':acc}
```
4. **Alternate solution**:
```python
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

def classification_metrics(y_true, y_pred):
    return {
        'precision': precision_score(y_true,y_pred,zero_division=0),
        'recall': recall_score(y_true,y_pred,zero_division=0),
        'f1': f1_score(y_true,y_pred,zero_division=0),
        'accuracy': accuracy_score(y_true,y_pred)
    }
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Explicitly handle divide-by-zero cases.

### Q206: ML Python question 12: Build mini-batch generator for SGD
1. **Question**: ML Python question 12: Build mini-batch generator for SGD.
2. **Explanation**: Yield slices of shuffled arrays in batch_size chunks.
3. **Working Python solution**:
```python
import numpy as np

def batch_iter(X, y, batch_size, seed=0):
    rng = np.random.default_rng(seed)
    idx = np.arange(len(X))
    rng.shuffle(idx)
    for i in range(0, len(idx), batch_size):
        b = idx[i:i+batch_size]
        yield X[b], y[b]
```
4. **Alternate solution**:
```python
def batch_iter(X, y, batch_size, seed=0):
    for i in range(0, len(X), batch_size):
        yield X[i:i+batch_size], y[i:i+batch_size]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Mention memory benefit of generators in training loops.

### Q207: ML Python question 13: Implement train/validation split with reproducible shuffle
1. **Question**: ML Python question 13: Implement train/validation split with reproducible shuffle.
2. **Explanation**: Shuffle indices with random seed and split by ratio.
3. **Working Python solution**:
```python
import numpy as np

def train_val_split(X, y, val_ratio=0.2, seed=42):
    rng = np.random.default_rng(seed)
    idx = np.arange(len(X))
    rng.shuffle(idx)
    cut = int(len(X) * (1 - val_ratio))
    tr, va = idx[:cut], idx[cut:]
    return X[tr], X[va], y[tr], y[va]
```
4. **Alternate solution**:
```python
def train_val_split(X, y, val_ratio=0.2):
    cut = int(len(X) * (1 - val_ratio))
    return X[:cut], X[cut:], y[:cut], y[cut:]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Discuss why random split can break time-series tasks.

### Q208: ML Python question 14: Compute binary classification metrics from predictions
1. **Question**: ML Python question 14: Compute binary classification metrics from predictions.
2. **Explanation**: Derive precision, recall, F1, and accuracy from confusion counts.
3. **Working Python solution**:
```python
def classification_metrics(y_true, y_pred):
    tp = sum(1 for t,p in zip(y_true,y_pred) if t==1 and p==1)
    tn = sum(1 for t,p in zip(y_true,y_pred) if t==0 and p==0)
    fp = sum(1 for t,p in zip(y_true,y_pred) if t==0 and p==1)
    fn = sum(1 for t,p in zip(y_true,y_pred) if t==1 and p==0)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2*precision*recall/(precision+recall) if precision+recall else 0.0
    acc = (tp+tn)/len(y_true) if y_true else 0.0
    return {'precision':precision,'recall':recall,'f1':f1,'accuracy':acc}
```
4. **Alternate solution**:
```python
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

def classification_metrics(y_true, y_pred):
    return {
        'precision': precision_score(y_true,y_pred,zero_division=0),
        'recall': recall_score(y_true,y_pred,zero_division=0),
        'f1': f1_score(y_true,y_pred,zero_division=0),
        'accuracy': accuracy_score(y_true,y_pred)
    }
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Explicitly handle divide-by-zero cases.

### Q209: ML Python question 15: Build mini-batch generator for SGD
1. **Question**: ML Python question 15: Build mini-batch generator for SGD.
2. **Explanation**: Yield slices of shuffled arrays in batch_size chunks.
3. **Working Python solution**:
```python
import numpy as np

def batch_iter(X, y, batch_size, seed=0):
    rng = np.random.default_rng(seed)
    idx = np.arange(len(X))
    rng.shuffle(idx)
    for i in range(0, len(idx), batch_size):
        b = idx[i:i+batch_size]
        yield X[b], y[b]
```
4. **Alternate solution**:
```python
def batch_iter(X, y, batch_size, seed=0):
    for i in range(0, len(X), batch_size):
        yield X[i:i+batch_size], y[i:i+batch_size]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Mention memory benefit of generators in training loops.

### Q210: ML Python question 16: Implement train/validation split with reproducible shuffle
1. **Question**: ML Python question 16: Implement train/validation split with reproducible shuffle.
2. **Explanation**: Shuffle indices with random seed and split by ratio.
3. **Working Python solution**:
```python
import numpy as np

def train_val_split(X, y, val_ratio=0.2, seed=42):
    rng = np.random.default_rng(seed)
    idx = np.arange(len(X))
    rng.shuffle(idx)
    cut = int(len(X) * (1 - val_ratio))
    tr, va = idx[:cut], idx[cut:]
    return X[tr], X[va], y[tr], y[va]
```
4. **Alternate solution**:
```python
def train_val_split(X, y, val_ratio=0.2):
    cut = int(len(X) * (1 - val_ratio))
    return X[:cut], X[cut:], y[:cut], y[cut:]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Discuss why random split can break time-series tasks.

### Q211: ML Python question 17: Compute binary classification metrics from predictions
1. **Question**: ML Python question 17: Compute binary classification metrics from predictions.
2. **Explanation**: Derive precision, recall, F1, and accuracy from confusion counts.
3. **Working Python solution**:
```python
def classification_metrics(y_true, y_pred):
    tp = sum(1 for t,p in zip(y_true,y_pred) if t==1 and p==1)
    tn = sum(1 for t,p in zip(y_true,y_pred) if t==0 and p==0)
    fp = sum(1 for t,p in zip(y_true,y_pred) if t==0 and p==1)
    fn = sum(1 for t,p in zip(y_true,y_pred) if t==1 and p==0)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2*precision*recall/(precision+recall) if precision+recall else 0.0
    acc = (tp+tn)/len(y_true) if y_true else 0.0
    return {'precision':precision,'recall':recall,'f1':f1,'accuracy':acc}
```
4. **Alternate solution**:
```python
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

def classification_metrics(y_true, y_pred):
    return {
        'precision': precision_score(y_true,y_pred,zero_division=0),
        'recall': recall_score(y_true,y_pred,zero_division=0),
        'f1': f1_score(y_true,y_pred,zero_division=0),
        'accuracy': accuracy_score(y_true,y_pred)
    }
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Explicitly handle divide-by-zero cases.

### Q212: ML Python question 18: Build mini-batch generator for SGD
1. **Question**: ML Python question 18: Build mini-batch generator for SGD.
2. **Explanation**: Yield slices of shuffled arrays in batch_size chunks.
3. **Working Python solution**:
```python
import numpy as np

def batch_iter(X, y, batch_size, seed=0):
    rng = np.random.default_rng(seed)
    idx = np.arange(len(X))
    rng.shuffle(idx)
    for i in range(0, len(idx), batch_size):
        b = idx[i:i+batch_size]
        yield X[b], y[b]
```
4. **Alternate solution**:
```python
def batch_iter(X, y, batch_size, seed=0):
    for i in range(0, len(X), batch_size):
        yield X[i:i+batch_size], y[i:i+batch_size]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Mention memory benefit of generators in training loops.

### Q213: ML Python question 19: Implement train/validation split with reproducible shuffle
1. **Question**: ML Python question 19: Implement train/validation split with reproducible shuffle.
2. **Explanation**: Shuffle indices with random seed and split by ratio.
3. **Working Python solution**:
```python
import numpy as np

def train_val_split(X, y, val_ratio=0.2, seed=42):
    rng = np.random.default_rng(seed)
    idx = np.arange(len(X))
    rng.shuffle(idx)
    cut = int(len(X) * (1 - val_ratio))
    tr, va = idx[:cut], idx[cut:]
    return X[tr], X[va], y[tr], y[va]
```
4. **Alternate solution**:
```python
def train_val_split(X, y, val_ratio=0.2):
    cut = int(len(X) * (1 - val_ratio))
    return X[:cut], X[cut:], y[:cut], y[cut:]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Discuss why random split can break time-series tasks.

### Q214: ML Python question 20: Compute binary classification metrics from predictions
1. **Question**: ML Python question 20: Compute binary classification metrics from predictions.
2. **Explanation**: Derive precision, recall, F1, and accuracy from confusion counts.
3. **Working Python solution**:
```python
def classification_metrics(y_true, y_pred):
    tp = sum(1 for t,p in zip(y_true,y_pred) if t==1 and p==1)
    tn = sum(1 for t,p in zip(y_true,y_pred) if t==0 and p==0)
    fp = sum(1 for t,p in zip(y_true,y_pred) if t==0 and p==1)
    fn = sum(1 for t,p in zip(y_true,y_pred) if t==1 and p==0)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2*precision*recall/(precision+recall) if precision+recall else 0.0
    acc = (tp+tn)/len(y_true) if y_true else 0.0
    return {'precision':precision,'recall':recall,'f1':f1,'accuracy':acc}
```
4. **Alternate solution**:
```python
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

def classification_metrics(y_true, y_pred):
    return {
        'precision': precision_score(y_true,y_pred,zero_division=0),
        'recall': recall_score(y_true,y_pred,zero_division=0),
        'f1': f1_score(y_true,y_pred,zero_division=0),
        'accuracy': accuracy_score(y_true,y_pred)
    }
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Explicitly handle divide-by-zero cases.

### Q215: ML Python question 21: Build mini-batch generator for SGD
1. **Question**: ML Python question 21: Build mini-batch generator for SGD.
2. **Explanation**: Yield slices of shuffled arrays in batch_size chunks.
3. **Working Python solution**:
```python
import numpy as np

def batch_iter(X, y, batch_size, seed=0):
    rng = np.random.default_rng(seed)
    idx = np.arange(len(X))
    rng.shuffle(idx)
    for i in range(0, len(idx), batch_size):
        b = idx[i:i+batch_size]
        yield X[b], y[b]
```
4. **Alternate solution**:
```python
def batch_iter(X, y, batch_size, seed=0):
    for i in range(0, len(X), batch_size):
        yield X[i:i+batch_size], y[i:i+batch_size]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Mention memory benefit of generators in training loops.

### Q216: ML Python question 22: Implement train/validation split with reproducible shuffle
1. **Question**: ML Python question 22: Implement train/validation split with reproducible shuffle.
2. **Explanation**: Shuffle indices with random seed and split by ratio.
3. **Working Python solution**:
```python
import numpy as np

def train_val_split(X, y, val_ratio=0.2, seed=42):
    rng = np.random.default_rng(seed)
    idx = np.arange(len(X))
    rng.shuffle(idx)
    cut = int(len(X) * (1 - val_ratio))
    tr, va = idx[:cut], idx[cut:]
    return X[tr], X[va], y[tr], y[va]
```
4. **Alternate solution**:
```python
def train_val_split(X, y, val_ratio=0.2):
    cut = int(len(X) * (1 - val_ratio))
    return X[:cut], X[cut:], y[:cut], y[cut:]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Discuss why random split can break time-series tasks.

### Q217: ML Python question 23: Compute binary classification metrics from predictions
1. **Question**: ML Python question 23: Compute binary classification metrics from predictions.
2. **Explanation**: Derive precision, recall, F1, and accuracy from confusion counts.
3. **Working Python solution**:
```python
def classification_metrics(y_true, y_pred):
    tp = sum(1 for t,p in zip(y_true,y_pred) if t==1 and p==1)
    tn = sum(1 for t,p in zip(y_true,y_pred) if t==0 and p==0)
    fp = sum(1 for t,p in zip(y_true,y_pred) if t==0 and p==1)
    fn = sum(1 for t,p in zip(y_true,y_pred) if t==1 and p==0)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2*precision*recall/(precision+recall) if precision+recall else 0.0
    acc = (tp+tn)/len(y_true) if y_true else 0.0
    return {'precision':precision,'recall':recall,'f1':f1,'accuracy':acc}
```
4. **Alternate solution**:
```python
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

def classification_metrics(y_true, y_pred):
    return {
        'precision': precision_score(y_true,y_pred,zero_division=0),
        'recall': recall_score(y_true,y_pred,zero_division=0),
        'f1': f1_score(y_true,y_pred,zero_division=0),
        'accuracy': accuracy_score(y_true,y_pred)
    }
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Explicitly handle divide-by-zero cases.

### Q218: ML Python question 24: Build mini-batch generator for SGD
1. **Question**: ML Python question 24: Build mini-batch generator for SGD.
2. **Explanation**: Yield slices of shuffled arrays in batch_size chunks.
3. **Working Python solution**:
```python
import numpy as np

def batch_iter(X, y, batch_size, seed=0):
    rng = np.random.default_rng(seed)
    idx = np.arange(len(X))
    rng.shuffle(idx)
    for i in range(0, len(idx), batch_size):
        b = idx[i:i+batch_size]
        yield X[b], y[b]
```
4. **Alternate solution**:
```python
def batch_iter(X, y, batch_size, seed=0):
    for i in range(0, len(X), batch_size):
        yield X[i:i+batch_size], y[i:i+batch_size]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Mention memory benefit of generators in training loops.

### Q219: ML Python question 25: Implement train/validation split with reproducible shuffle
1. **Question**: ML Python question 25: Implement train/validation split with reproducible shuffle.
2. **Explanation**: Shuffle indices with random seed and split by ratio.
3. **Working Python solution**:
```python
import numpy as np

def train_val_split(X, y, val_ratio=0.2, seed=42):
    rng = np.random.default_rng(seed)
    idx = np.arange(len(X))
    rng.shuffle(idx)
    cut = int(len(X) * (1 - val_ratio))
    tr, va = idx[:cut], idx[cut:]
    return X[tr], X[va], y[tr], y[va]
```
4. **Alternate solution**:
```python
def train_val_split(X, y, val_ratio=0.2):
    cut = int(len(X) * (1 - val_ratio))
    return X[:cut], X[cut:], y[:cut], y[cut:]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Discuss why random split can break time-series tasks.

### Q220: ML Python question 26: Compute binary classification metrics from predictions
1. **Question**: ML Python question 26: Compute binary classification metrics from predictions.
2. **Explanation**: Derive precision, recall, F1, and accuracy from confusion counts.
3. **Working Python solution**:
```python
def classification_metrics(y_true, y_pred):
    tp = sum(1 for t,p in zip(y_true,y_pred) if t==1 and p==1)
    tn = sum(1 for t,p in zip(y_true,y_pred) if t==0 and p==0)
    fp = sum(1 for t,p in zip(y_true,y_pred) if t==0 and p==1)
    fn = sum(1 for t,p in zip(y_true,y_pred) if t==1 and p==0)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2*precision*recall/(precision+recall) if precision+recall else 0.0
    acc = (tp+tn)/len(y_true) if y_true else 0.0
    return {'precision':precision,'recall':recall,'f1':f1,'accuracy':acc}
```
4. **Alternate solution**:
```python
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

def classification_metrics(y_true, y_pred):
    return {
        'precision': precision_score(y_true,y_pred,zero_division=0),
        'recall': recall_score(y_true,y_pred,zero_division=0),
        'f1': f1_score(y_true,y_pred,zero_division=0),
        'accuracy': accuracy_score(y_true,y_pred)
    }
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Explicitly handle divide-by-zero cases.

### Q221: ML Python question 27: Build mini-batch generator for SGD
1. **Question**: ML Python question 27: Build mini-batch generator for SGD.
2. **Explanation**: Yield slices of shuffled arrays in batch_size chunks.
3. **Working Python solution**:
```python
import numpy as np

def batch_iter(X, y, batch_size, seed=0):
    rng = np.random.default_rng(seed)
    idx = np.arange(len(X))
    rng.shuffle(idx)
    for i in range(0, len(idx), batch_size):
        b = idx[i:i+batch_size]
        yield X[b], y[b]
```
4. **Alternate solution**:
```python
def batch_iter(X, y, batch_size, seed=0):
    for i in range(0, len(X), batch_size):
        yield X[i:i+batch_size], y[i:i+batch_size]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Mention memory benefit of generators in training loops.

### Q222: ML Python question 28: Implement train/validation split with reproducible shuffle
1. **Question**: ML Python question 28: Implement train/validation split with reproducible shuffle.
2. **Explanation**: Shuffle indices with random seed and split by ratio.
3. **Working Python solution**:
```python
import numpy as np

def train_val_split(X, y, val_ratio=0.2, seed=42):
    rng = np.random.default_rng(seed)
    idx = np.arange(len(X))
    rng.shuffle(idx)
    cut = int(len(X) * (1 - val_ratio))
    tr, va = idx[:cut], idx[cut:]
    return X[tr], X[va], y[tr], y[va]
```
4. **Alternate solution**:
```python
def train_val_split(X, y, val_ratio=0.2):
    cut = int(len(X) * (1 - val_ratio))
    return X[:cut], X[cut:], y[:cut], y[cut:]
```
5. **Complexity analysis**: O(n).
6. **Interview tip**: Discuss why random split can break time-series tasks.

## System Design (Python for ML)

### Q223: System design question 1: Design a batch feature engineering pipeline for daily model retraining
1. **Question**: System design question 1: Design a batch feature engineering pipeline for daily model retraining.
2. **Explanation**: Define ingestion, validation, transformation, feature store write, and orchestration boundaries.
3. **Working Python solution**:
```python
from dataclasses import dataclass

@dataclass
class BatchFeaturePipeline:
    reader: object
    validator: object
    transformer: object
    feature_store: object

    def run(self, ds: str):
        raw = self.reader.read(ds)
        clean = self.validator.validate(raw)
        feats = self.transformer.transform(clean)
        self.feature_store.write(ds, feats)
        return {'dataset': ds, 'rows': len(feats)}
```
4. **Alternate solution**:
```python
def run_pipeline(reader, checks, transformers, sink, ds):
    data = reader(ds)
    for check in checks:
        data = check(data)
    for tfm in transformers:
        data = tfm(data)
    sink(ds, data)
    return True
```
5. **Complexity analysis**: Throughput dominated by I/O and transformation cost..
6. **Interview tip**: State SLA/SLO, data freshness target, and backfill strategy early.

### Q224: System design question 2: Design online model serving with feature lookup and fallback
1. **Question**: System design question 2: Design online model serving with feature lookup and fallback.
2. **Explanation**: Split request path into input validation, feature retrieval, model inference, and response logging.
3. **Working Python solution**:
```python
class OnlinePredictor:
    def __init__(self, feature_store, model_registry, logger):
        self.feature_store = feature_store
        self.model_registry = model_registry
        self.logger = logger

    def predict(self, user_id, payload):
        feats = self.feature_store.get_online(user_id) or payload
        model = self.model_registry.load('production')
        score = float(model.predict_proba([feats])[0][1])
        self.logger.log({'user_id': user_id, 'score': score})
        return {'score': score}
```
4. **Alternate solution**:
```python
def predict(request, model, default_features):
    features = request.get('features', default_features)
    return {'score': float(model.predict([features])[0])}
```
5. **Complexity analysis**: Latency budget is key; each hop adds p99 cost..
6. **Interview tip**: Discuss caching, circuit breakers, and model fallback paths.

### Q225: System design question 3: Design a feature store with offline and online consistency
1. **Question**: System design question 3: Design a feature store with offline and online consistency.
2. **Explanation**: Use shared feature definitions and materialization jobs to keep parity.
3. **Working Python solution**:
```python
class FeatureStoreService:
    def __init__(self, offline_repo, online_kv):
        self.offline_repo = offline_repo
        self.online_kv = online_kv

    def materialize(self, feature_name, rows):
        for key, value in rows:
            self.online_kv[(feature_name, key)] = value
        self.offline_repo.append(feature_name, rows)

    def get_online(self, feature_name, entity_id):
        return self.online_kv.get((feature_name, entity_id))
```
4. **Alternate solution**:
```python
class SimpleFeatureStore:
    def __init__(self):
        self.offline = {}
        self.online = {}
    def put(self, key, value):
        self.offline.setdefault(key, []).append(value); self.online[key] = value
```
5. **Complexity analysis**: Write amplification vs freshness trade-off..
6. **Interview tip**: Interviewers look for point-in-time correctness considerations.

### Q226: System design question 4: Design scalable ETL for clickstream events
1. **Question**: System design question 4: Design scalable ETL for clickstream events.
2. **Explanation**: Partition by event date/hour and process idempotently.
3. **Working Python solution**:
```python
def etl_job(source, parser, sink, checkpoint):
    for event in source.read_since(checkpoint.load()):
        rec = parser(event)
        if rec is None:
            continue
        sink.write_partition(rec['event_date'], rec)
    checkpoint.save(source.latest_offset())
```
4. **Alternate solution**:
```python
def etl_job(source, sink):
    data = [e for e in source if 'event' in e]
    sink.extend(data)
```
5. **Complexity analysis**: O(n) events per run.
6. **Interview tip**: Mention replay strategy and deduplication keys.

### Q227: System design question 5: Design a batch feature engineering pipeline for daily model retraining
1. **Question**: System design question 5: Design a batch feature engineering pipeline for daily model retraining.
2. **Explanation**: Define ingestion, validation, transformation, feature store write, and orchestration boundaries.
3. **Working Python solution**:
```python
from dataclasses import dataclass

@dataclass
class BatchFeaturePipeline:
    reader: object
    validator: object
    transformer: object
    feature_store: object

    def run(self, ds: str):
        raw = self.reader.read(ds)
        clean = self.validator.validate(raw)
        feats = self.transformer.transform(clean)
        self.feature_store.write(ds, feats)
        return {'dataset': ds, 'rows': len(feats)}
```
4. **Alternate solution**:
```python
def run_pipeline(reader, checks, transformers, sink, ds):
    data = reader(ds)
    for check in checks:
        data = check(data)
    for tfm in transformers:
        data = tfm(data)
    sink(ds, data)
    return True
```
5. **Complexity analysis**: Throughput dominated by I/O and transformation cost..
6. **Interview tip**: State SLA/SLO, data freshness target, and backfill strategy early.

### Q228: System design question 6: Design online model serving with feature lookup and fallback
1. **Question**: System design question 6: Design online model serving with feature lookup and fallback.
2. **Explanation**: Split request path into input validation, feature retrieval, model inference, and response logging.
3. **Working Python solution**:
```python
class OnlinePredictor:
    def __init__(self, feature_store, model_registry, logger):
        self.feature_store = feature_store
        self.model_registry = model_registry
        self.logger = logger

    def predict(self, user_id, payload):
        feats = self.feature_store.get_online(user_id) or payload
        model = self.model_registry.load('production')
        score = float(model.predict_proba([feats])[0][1])
        self.logger.log({'user_id': user_id, 'score': score})
        return {'score': score}
```
4. **Alternate solution**:
```python
def predict(request, model, default_features):
    features = request.get('features', default_features)
    return {'score': float(model.predict([features])[0])}
```
5. **Complexity analysis**: Latency budget is key; each hop adds p99 cost..
6. **Interview tip**: Discuss caching, circuit breakers, and model fallback paths.

### Q229: System design question 7: Design a feature store with offline and online consistency
1. **Question**: System design question 7: Design a feature store with offline and online consistency.
2. **Explanation**: Use shared feature definitions and materialization jobs to keep parity.
3. **Working Python solution**:
```python
class FeatureStoreService:
    def __init__(self, offline_repo, online_kv):
        self.offline_repo = offline_repo
        self.online_kv = online_kv

    def materialize(self, feature_name, rows):
        for key, value in rows:
            self.online_kv[(feature_name, key)] = value
        self.offline_repo.append(feature_name, rows)

    def get_online(self, feature_name, entity_id):
        return self.online_kv.get((feature_name, entity_id))
```
4. **Alternate solution**:
```python
class SimpleFeatureStore:
    def __init__(self):
        self.offline = {}
        self.online = {}
    def put(self, key, value):
        self.offline.setdefault(key, []).append(value); self.online[key] = value
```
5. **Complexity analysis**: Write amplification vs freshness trade-off..
6. **Interview tip**: Interviewers look for point-in-time correctness considerations.

### Q230: System design question 8: Design scalable ETL for clickstream events
1. **Question**: System design question 8: Design scalable ETL for clickstream events.
2. **Explanation**: Partition by event date/hour and process idempotently.
3. **Working Python solution**:
```python
def etl_job(source, parser, sink, checkpoint):
    for event in source.read_since(checkpoint.load()):
        rec = parser(event)
        if rec is None:
            continue
        sink.write_partition(rec['event_date'], rec)
    checkpoint.save(source.latest_offset())
```
4. **Alternate solution**:
```python
def etl_job(source, sink):
    data = [e for e in source if 'event' in e]
    sink.extend(data)
```
5. **Complexity analysis**: O(n) events per run.
6. **Interview tip**: Mention replay strategy and deduplication keys.

### Q231: System design question 9: Design a batch feature engineering pipeline for daily model retraining
1. **Question**: System design question 9: Design a batch feature engineering pipeline for daily model retraining.
2. **Explanation**: Define ingestion, validation, transformation, feature store write, and orchestration boundaries.
3. **Working Python solution**:
```python
from dataclasses import dataclass

@dataclass
class BatchFeaturePipeline:
    reader: object
    validator: object
    transformer: object
    feature_store: object

    def run(self, ds: str):
        raw = self.reader.read(ds)
        clean = self.validator.validate(raw)
        feats = self.transformer.transform(clean)
        self.feature_store.write(ds, feats)
        return {'dataset': ds, 'rows': len(feats)}
```
4. **Alternate solution**:
```python
def run_pipeline(reader, checks, transformers, sink, ds):
    data = reader(ds)
    for check in checks:
        data = check(data)
    for tfm in transformers:
        data = tfm(data)
    sink(ds, data)
    return True
```
5. **Complexity analysis**: Throughput dominated by I/O and transformation cost..
6. **Interview tip**: State SLA/SLO, data freshness target, and backfill strategy early.

### Q232: System design question 10: Design online model serving with feature lookup and fallback
1. **Question**: System design question 10: Design online model serving with feature lookup and fallback.
2. **Explanation**: Split request path into input validation, feature retrieval, model inference, and response logging.
3. **Working Python solution**:
```python
class OnlinePredictor:
    def __init__(self, feature_store, model_registry, logger):
        self.feature_store = feature_store
        self.model_registry = model_registry
        self.logger = logger

    def predict(self, user_id, payload):
        feats = self.feature_store.get_online(user_id) or payload
        model = self.model_registry.load('production')
        score = float(model.predict_proba([feats])[0][1])
        self.logger.log({'user_id': user_id, 'score': score})
        return {'score': score}
```
4. **Alternate solution**:
```python
def predict(request, model, default_features):
    features = request.get('features', default_features)
    return {'score': float(model.predict([features])[0])}
```
5. **Complexity analysis**: Latency budget is key; each hop adds p99 cost..
6. **Interview tip**: Discuss caching, circuit breakers, and model fallback paths.

### Q233: System design question 11: Design a feature store with offline and online consistency
1. **Question**: System design question 11: Design a feature store with offline and online consistency.
2. **Explanation**: Use shared feature definitions and materialization jobs to keep parity.
3. **Working Python solution**:
```python
class FeatureStoreService:
    def __init__(self, offline_repo, online_kv):
        self.offline_repo = offline_repo
        self.online_kv = online_kv

    def materialize(self, feature_name, rows):
        for key, value in rows:
            self.online_kv[(feature_name, key)] = value
        self.offline_repo.append(feature_name, rows)

    def get_online(self, feature_name, entity_id):
        return self.online_kv.get((feature_name, entity_id))
```
4. **Alternate solution**:
```python
class SimpleFeatureStore:
    def __init__(self):
        self.offline = {}
        self.online = {}
    def put(self, key, value):
        self.offline.setdefault(key, []).append(value); self.online[key] = value
```
5. **Complexity analysis**: Write amplification vs freshness trade-off..
6. **Interview tip**: Interviewers look for point-in-time correctness considerations.

### Q234: System design question 12: Design scalable ETL for clickstream events
1. **Question**: System design question 12: Design scalable ETL for clickstream events.
2. **Explanation**: Partition by event date/hour and process idempotently.
3. **Working Python solution**:
```python
def etl_job(source, parser, sink, checkpoint):
    for event in source.read_since(checkpoint.load()):
        rec = parser(event)
        if rec is None:
            continue
        sink.write_partition(rec['event_date'], rec)
    checkpoint.save(source.latest_offset())
```
4. **Alternate solution**:
```python
def etl_job(source, sink):
    data = [e for e in source if 'event' in e]
    sink.extend(data)
```
5. **Complexity analysis**: O(n) events per run.
6. **Interview tip**: Mention replay strategy and deduplication keys.

### Q235: System design question 13: Design a batch feature engineering pipeline for daily model retraining
1. **Question**: System design question 13: Design a batch feature engineering pipeline for daily model retraining.
2. **Explanation**: Define ingestion, validation, transformation, feature store write, and orchestration boundaries.
3. **Working Python solution**:
```python
from dataclasses import dataclass

@dataclass
class BatchFeaturePipeline:
    reader: object
    validator: object
    transformer: object
    feature_store: object

    def run(self, ds: str):
        raw = self.reader.read(ds)
        clean = self.validator.validate(raw)
        feats = self.transformer.transform(clean)
        self.feature_store.write(ds, feats)
        return {'dataset': ds, 'rows': len(feats)}
```
4. **Alternate solution**:
```python
def run_pipeline(reader, checks, transformers, sink, ds):
    data = reader(ds)
    for check in checks:
        data = check(data)
    for tfm in transformers:
        data = tfm(data)
    sink(ds, data)
    return True
```
5. **Complexity analysis**: Throughput dominated by I/O and transformation cost..
6. **Interview tip**: State SLA/SLO, data freshness target, and backfill strategy early.

### Q236: System design question 14: Design online model serving with feature lookup and fallback
1. **Question**: System design question 14: Design online model serving with feature lookup and fallback.
2. **Explanation**: Split request path into input validation, feature retrieval, model inference, and response logging.
3. **Working Python solution**:
```python
class OnlinePredictor:
    def __init__(self, feature_store, model_registry, logger):
        self.feature_store = feature_store
        self.model_registry = model_registry
        self.logger = logger

    def predict(self, user_id, payload):
        feats = self.feature_store.get_online(user_id) or payload
        model = self.model_registry.load('production')
        score = float(model.predict_proba([feats])[0][1])
        self.logger.log({'user_id': user_id, 'score': score})
        return {'score': score}
```
4. **Alternate solution**:
```python
def predict(request, model, default_features):
    features = request.get('features', default_features)
    return {'score': float(model.predict([features])[0])}
```
5. **Complexity analysis**: Latency budget is key; each hop adds p99 cost..
6. **Interview tip**: Discuss caching, circuit breakers, and model fallback paths.

### Q237: System design question 15: Design a feature store with offline and online consistency
1. **Question**: System design question 15: Design a feature store with offline and online consistency.
2. **Explanation**: Use shared feature definitions and materialization jobs to keep parity.
3. **Working Python solution**:
```python
class FeatureStoreService:
    def __init__(self, offline_repo, online_kv):
        self.offline_repo = offline_repo
        self.online_kv = online_kv

    def materialize(self, feature_name, rows):
        for key, value in rows:
            self.online_kv[(feature_name, key)] = value
        self.offline_repo.append(feature_name, rows)

    def get_online(self, feature_name, entity_id):
        return self.online_kv.get((feature_name, entity_id))
```
4. **Alternate solution**:
```python
class SimpleFeatureStore:
    def __init__(self):
        self.offline = {}
        self.online = {}
    def put(self, key, value):
        self.offline.setdefault(key, []).append(value); self.online[key] = value
```
5. **Complexity analysis**: Write amplification vs freshness trade-off..
6. **Interview tip**: Interviewers look for point-in-time correctness considerations.

### Q238: System design question 16: Design scalable ETL for clickstream events
1. **Question**: System design question 16: Design scalable ETL for clickstream events.
2. **Explanation**: Partition by event date/hour and process idempotently.
3. **Working Python solution**:
```python
def etl_job(source, parser, sink, checkpoint):
    for event in source.read_since(checkpoint.load()):
        rec = parser(event)
        if rec is None:
            continue
        sink.write_partition(rec['event_date'], rec)
    checkpoint.save(source.latest_offset())
```
4. **Alternate solution**:
```python
def etl_job(source, sink):
    data = [e for e in source if 'event' in e]
    sink.extend(data)
```
5. **Complexity analysis**: O(n) events per run.
6. **Interview tip**: Mention replay strategy and deduplication keys.

### Q239: System design question 17: Design a batch feature engineering pipeline for daily model retraining
1. **Question**: System design question 17: Design a batch feature engineering pipeline for daily model retraining.
2. **Explanation**: Define ingestion, validation, transformation, feature store write, and orchestration boundaries.
3. **Working Python solution**:
```python
from dataclasses import dataclass

@dataclass
class BatchFeaturePipeline:
    reader: object
    validator: object
    transformer: object
    feature_store: object

    def run(self, ds: str):
        raw = self.reader.read(ds)
        clean = self.validator.validate(raw)
        feats = self.transformer.transform(clean)
        self.feature_store.write(ds, feats)
        return {'dataset': ds, 'rows': len(feats)}
```
4. **Alternate solution**:
```python
def run_pipeline(reader, checks, transformers, sink, ds):
    data = reader(ds)
    for check in checks:
        data = check(data)
    for tfm in transformers:
        data = tfm(data)
    sink(ds, data)
    return True
```
5. **Complexity analysis**: Throughput dominated by I/O and transformation cost..
6. **Interview tip**: State SLA/SLO, data freshness target, and backfill strategy early.

### Q240: System design question 18: Design online model serving with feature lookup and fallback
1. **Question**: System design question 18: Design online model serving with feature lookup and fallback.
2. **Explanation**: Split request path into input validation, feature retrieval, model inference, and response logging.
3. **Working Python solution**:
```python
class OnlinePredictor:
    def __init__(self, feature_store, model_registry, logger):
        self.feature_store = feature_store
        self.model_registry = model_registry
        self.logger = logger

    def predict(self, user_id, payload):
        feats = self.feature_store.get_online(user_id) or payload
        model = self.model_registry.load('production')
        score = float(model.predict_proba([feats])[0][1])
        self.logger.log({'user_id': user_id, 'score': score})
        return {'score': score}
```
4. **Alternate solution**:
```python
def predict(request, model, default_features):
    features = request.get('features', default_features)
    return {'score': float(model.predict([features])[0])}
```
5. **Complexity analysis**: Latency budget is key; each hop adds p99 cost..
6. **Interview tip**: Discuss caching, circuit breakers, and model fallback paths.

### Q241: System design question 19: Design a feature store with offline and online consistency
1. **Question**: System design question 19: Design a feature store with offline and online consistency.
2. **Explanation**: Use shared feature definitions and materialization jobs to keep parity.
3. **Working Python solution**:
```python
class FeatureStoreService:
    def __init__(self, offline_repo, online_kv):
        self.offline_repo = offline_repo
        self.online_kv = online_kv

    def materialize(self, feature_name, rows):
        for key, value in rows:
            self.online_kv[(feature_name, key)] = value
        self.offline_repo.append(feature_name, rows)

    def get_online(self, feature_name, entity_id):
        return self.online_kv.get((feature_name, entity_id))
```
4. **Alternate solution**:
```python
class SimpleFeatureStore:
    def __init__(self):
        self.offline = {}
        self.online = {}
    def put(self, key, value):
        self.offline.setdefault(key, []).append(value); self.online[key] = value
```
5. **Complexity analysis**: Write amplification vs freshness trade-off..
6. **Interview tip**: Interviewers look for point-in-time correctness considerations.

### Q242: System design question 20: Design scalable ETL for clickstream events
1. **Question**: System design question 20: Design scalable ETL for clickstream events.
2. **Explanation**: Partition by event date/hour and process idempotently.
3. **Working Python solution**:
```python
def etl_job(source, parser, sink, checkpoint):
    for event in source.read_since(checkpoint.load()):
        rec = parser(event)
        if rec is None:
            continue
        sink.write_partition(rec['event_date'], rec)
    checkpoint.save(source.latest_offset())
```
4. **Alternate solution**:
```python
def etl_job(source, sink):
    data = [e for e in source if 'event' in e]
    sink.extend(data)
```
5. **Complexity analysis**: O(n) events per run.
6. **Interview tip**: Mention replay strategy and deduplication keys.

### Q243: System design question 21: Design a batch feature engineering pipeline for daily model retraining
1. **Question**: System design question 21: Design a batch feature engineering pipeline for daily model retraining.
2. **Explanation**: Define ingestion, validation, transformation, feature store write, and orchestration boundaries.
3. **Working Python solution**:
```python
from dataclasses import dataclass

@dataclass
class BatchFeaturePipeline:
    reader: object
    validator: object
    transformer: object
    feature_store: object

    def run(self, ds: str):
        raw = self.reader.read(ds)
        clean = self.validator.validate(raw)
        feats = self.transformer.transform(clean)
        self.feature_store.write(ds, feats)
        return {'dataset': ds, 'rows': len(feats)}
```
4. **Alternate solution**:
```python
def run_pipeline(reader, checks, transformers, sink, ds):
    data = reader(ds)
    for check in checks:
        data = check(data)
    for tfm in transformers:
        data = tfm(data)
    sink(ds, data)
    return True
```
5. **Complexity analysis**: Throughput dominated by I/O and transformation cost..
6. **Interview tip**: State SLA/SLO, data freshness target, and backfill strategy early.

### Q244: System design question 22: Design online model serving with feature lookup and fallback
1. **Question**: System design question 22: Design online model serving with feature lookup and fallback.
2. **Explanation**: Split request path into input validation, feature retrieval, model inference, and response logging.
3. **Working Python solution**:
```python
class OnlinePredictor:
    def __init__(self, feature_store, model_registry, logger):
        self.feature_store = feature_store
        self.model_registry = model_registry
        self.logger = logger

    def predict(self, user_id, payload):
        feats = self.feature_store.get_online(user_id) or payload
        model = self.model_registry.load('production')
        score = float(model.predict_proba([feats])[0][1])
        self.logger.log({'user_id': user_id, 'score': score})
        return {'score': score}
```
4. **Alternate solution**:
```python
def predict(request, model, default_features):
    features = request.get('features', default_features)
    return {'score': float(model.predict([features])[0])}
```
5. **Complexity analysis**: Latency budget is key; each hop adds p99 cost..
6. **Interview tip**: Discuss caching, circuit breakers, and model fallback paths.

### Q245: System design question 23: Design a feature store with offline and online consistency
1. **Question**: System design question 23: Design a feature store with offline and online consistency.
2. **Explanation**: Use shared feature definitions and materialization jobs to keep parity.
3. **Working Python solution**:
```python
class FeatureStoreService:
    def __init__(self, offline_repo, online_kv):
        self.offline_repo = offline_repo
        self.online_kv = online_kv

    def materialize(self, feature_name, rows):
        for key, value in rows:
            self.online_kv[(feature_name, key)] = value
        self.offline_repo.append(feature_name, rows)

    def get_online(self, feature_name, entity_id):
        return self.online_kv.get((feature_name, entity_id))
```
4. **Alternate solution**:
```python
class SimpleFeatureStore:
    def __init__(self):
        self.offline = {}
        self.online = {}
    def put(self, key, value):
        self.offline.setdefault(key, []).append(value); self.online[key] = value
```
5. **Complexity analysis**: Write amplification vs freshness trade-off..
6. **Interview tip**: Interviewers look for point-in-time correctness considerations.

### Q246: System design question 24: Design scalable ETL for clickstream events
1. **Question**: System design question 24: Design scalable ETL for clickstream events.
2. **Explanation**: Partition by event date/hour and process idempotently.
3. **Working Python solution**:
```python
def etl_job(source, parser, sink, checkpoint):
    for event in source.read_since(checkpoint.load()):
        rec = parser(event)
        if rec is None:
            continue
        sink.write_partition(rec['event_date'], rec)
    checkpoint.save(source.latest_offset())
```
4. **Alternate solution**:
```python
def etl_job(source, sink):
    data = [e for e in source if 'event' in e]
    sink.extend(data)
```
5. **Complexity analysis**: O(n) events per run.
6. **Interview tip**: Mention replay strategy and deduplication keys.

### Q247: System design question 25: Design a batch feature engineering pipeline for daily model retraining
1. **Question**: System design question 25: Design a batch feature engineering pipeline for daily model retraining.
2. **Explanation**: Define ingestion, validation, transformation, feature store write, and orchestration boundaries.
3. **Working Python solution**:
```python
from dataclasses import dataclass

@dataclass
class BatchFeaturePipeline:
    reader: object
    validator: object
    transformer: object
    feature_store: object

    def run(self, ds: str):
        raw = self.reader.read(ds)
        clean = self.validator.validate(raw)
        feats = self.transformer.transform(clean)
        self.feature_store.write(ds, feats)
        return {'dataset': ds, 'rows': len(feats)}
```
4. **Alternate solution**:
```python
def run_pipeline(reader, checks, transformers, sink, ds):
    data = reader(ds)
    for check in checks:
        data = check(data)
    for tfm in transformers:
        data = tfm(data)
    sink(ds, data)
    return True
```
5. **Complexity analysis**: Throughput dominated by I/O and transformation cost..
6. **Interview tip**: State SLA/SLO, data freshness target, and backfill strategy early.

### Q248: System design question 26: Design online model serving with feature lookup and fallback
1. **Question**: System design question 26: Design online model serving with feature lookup and fallback.
2. **Explanation**: Split request path into input validation, feature retrieval, model inference, and response logging.
3. **Working Python solution**:
```python
class OnlinePredictor:
    def __init__(self, feature_store, model_registry, logger):
        self.feature_store = feature_store
        self.model_registry = model_registry
        self.logger = logger

    def predict(self, user_id, payload):
        feats = self.feature_store.get_online(user_id) or payload
        model = self.model_registry.load('production')
        score = float(model.predict_proba([feats])[0][1])
        self.logger.log({'user_id': user_id, 'score': score})
        return {'score': score}
```
4. **Alternate solution**:
```python
def predict(request, model, default_features):
    features = request.get('features', default_features)
    return {'score': float(model.predict([features])[0])}
```
5. **Complexity analysis**: Latency budget is key; each hop adds p99 cost..
6. **Interview tip**: Discuss caching, circuit breakers, and model fallback paths.

### Q249: System design question 27: Design a feature store with offline and online consistency
1. **Question**: System design question 27: Design a feature store with offline and online consistency.
2. **Explanation**: Use shared feature definitions and materialization jobs to keep parity.
3. **Working Python solution**:
```python
class FeatureStoreService:
    def __init__(self, offline_repo, online_kv):
        self.offline_repo = offline_repo
        self.online_kv = online_kv

    def materialize(self, feature_name, rows):
        for key, value in rows:
            self.online_kv[(feature_name, key)] = value
        self.offline_repo.append(feature_name, rows)

    def get_online(self, feature_name, entity_id):
        return self.online_kv.get((feature_name, entity_id))
```
4. **Alternate solution**:
```python
class SimpleFeatureStore:
    def __init__(self):
        self.offline = {}
        self.online = {}
    def put(self, key, value):
        self.offline.setdefault(key, []).append(value); self.online[key] = value
```
5. **Complexity analysis**: Write amplification vs freshness trade-off..
6. **Interview tip**: Interviewers look for point-in-time correctness considerations.

### Q250: System design question 28: Design scalable ETL for clickstream events
1. **Question**: System design question 28: Design scalable ETL for clickstream events.
2. **Explanation**: Partition by event date/hour and process idempotently.
3. **Working Python solution**:
```python
def etl_job(source, parser, sink, checkpoint):
    for event in source.read_since(checkpoint.load()):
        rec = parser(event)
        if rec is None:
            continue
        sink.write_partition(rec['event_date'], rec)
    checkpoint.save(source.latest_offset())
```
4. **Alternate solution**:
```python
def etl_job(source, sink):
    data = [e for e in source if 'event' in e]
    sink.extend(data)
```
5. **Complexity analysis**: O(n) events per run.
6. **Interview tip**: Mention replay strategy and deduplication keys.

### Q251: Design an ML experiment tracker with lineage
1. **Question**: Design an ML experiment tracker with lineage.
2. **Explanation**: Define metadata schema, storage strategy, query APIs, and alerting workflows required to run the platform in production.
3. **Working Python solution**:
```python
class Service:
    def __init__(self, store, notifier):
        self.store = store
        self.notifier = notifier
    def handle(self, payload):
        record_id = self.store.write(payload)
        if payload.get('alert'):
            self.notifier.send(payload['alert'])
        return {'id': record_id}
```
4. **Alternate solution**:
```python
def handle(payload, write_fn, notify_fn):
    record_id = write_fn(payload)
    if 'alert' in payload:
        notify_fn(payload['alert'])
    return {'id': record_id}
```
5. **Complexity analysis**: O(1) compute per request, dominated by storage/network I/O.
6. **Interview tip**: Anchor the design around SLOs, failure modes, and observability before diving into component choices.

### Q252: Design drift monitoring and automatic rollback service
1. **Question**: Design drift monitoring and automatic rollback service.
2. **Explanation**: Define metadata schema, storage strategy, query APIs, and alerting workflows required to run the platform in production.
3. **Working Python solution**:
```python
class Service:
    def __init__(self, store, notifier):
        self.store = store
        self.notifier = notifier
    def handle(self, payload):
        record_id = self.store.write(payload)
        if payload.get('alert'):
            self.notifier.send(payload['alert'])
        return {'id': record_id}
```
4. **Alternate solution**:
```python
def handle(payload, write_fn, notify_fn):
    record_id = write_fn(payload)
    if 'alert' in payload:
        notify_fn(payload['alert'])
    return {'id': record_id}
```
5. **Complexity analysis**: O(1) compute per request, dominated by storage/network I/O.
6. **Interview tip**: Anchor the design around SLOs, failure modes, and observability before diving into component choices.
