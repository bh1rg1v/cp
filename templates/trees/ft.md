# Fenwick Tree (Binary Indexed Tree)

A Fenwick Tree is a data structure that efficiently supports prefix sum queries and point updates on an array. It uses the binary representation of indices to achieve O(log n) operations.

## Key Properties

- **1-indexed**: Internal array uses 1-based indexing for easier bit manipulation
- **Prefix Sums**: Efficiently calculates sum of elements from index 1 to i
- **Point Updates**: Adds values to individual array elements
- **Space Efficient**: Uses O(n) space

## Core Concept

Fenwick Tree uses the **Least Significant Bit (LSB)** trick:
- `i & (-i)` gives the LSB of i
- Each index i is responsible for a range of size equal to its LSB
- Tree structure is implicit in the indexing pattern

## Implementation Details

### Constructor
```python
def __init__(self, nums):
    self.n = len(nums)
    self.bit = [0] * (self.n + 1)  # 1-indexed
    for idx, val in enumerate(nums, 1):
        self.update(idx, val)
```

**Process:**
1. Create 1-indexed array of size n+1
2. Initialize all values to 0
3. Build tree by updating each element using enumerate

### Update Operation
```python
def update(self, idx, val):  # Add val to index idx (1-indexed)
    while idx <= self.n:
        self.bit[idx] += val
        idx += idx & (-idx)  # Move to next index
```

**Process:**
1. Start at index i
2. Add val to current index
3. Move to next responsible index using `i += i & (-i)`
4. Repeat until index exceeds n
**Example**: Updating index 3
- 3 (011₂) → 4 (100₂) → 8 (1000₂)
- Updates indices: 3, 4, 8

### Prefix Query Operation
```python
def prefixQuery(self, idx):  # Get prefix sum up to index idx (1-indexed)
    res = 0
    while idx > 0:
        res += self.bit[idx]
        idx -= idx & (-idx)  # Move to parent
    return res
```

### Range Query Operation
```python
def rangeQuery(self, l, r):  # Sum of [l..r] (1-indexed)
    return self.prefixQuery(r) - self.prefixQuery(l - 1)
```

**Process:**
1. Start at index i
2. Add current value to result
3. Move to parent index using `i -= i & (-i)`
4. Repeat until index becomes 0

**Example**: Querying prefix sum at index 7
- 7 (111₂) → 6 (110₂) → 4 (100₂) → 0
- Sums indices: 7, 6, 4

## Usage Examples

### Basic Operations
```python
# Initialize with array [1, 2, 3, 4, 5]
bit = BIT([1, 2, 3, 4, 5])

# Add 10 to index 3 (1-indexed)
bit.update(3, 10)  # Now array is [1, 2, 13, 4, 5]

# Get prefix sum up to index 3
print(bit.prefixQuery(3))  # Sum of [1, 2, 13] = 16

# Get prefix sum up to index 5
print(bit.prefixQuery(5))  # Sum of [1, 2, 13, 4, 5] = 25
```

### Range Sum Query
```python
# Built-in range query method
bit = BIT([1, 2, 3, 4, 5])
print(bit.rangeQuery(2, 4))  # Sum of indices 2,3,4 = 2+3+4 = 9

# Manual range query (equivalent)
def manualRangeSum(bit, l, r):
    if l == 1:
        return bit.prefixQuery(r)
    return bit.prefixQuery(r) - bit.prefixQuery(l - 1)
```

### Frequency Table / Counting
```python
# Count elements ≤ x
bit = BIT([0] * 1001)  # For values 1-1000

# Add element with value x
def addElement(bit, x):
    bit.update(x, 1)

# Count how many elements ≤ x
def countLE(bit, x):
    return bit.prefixQuery(x)

# Count elements in range [l, r]
def countRange(bit, l, r):
    return bit.rangeQuery(l, r)
```

### Inversion Counting
```python
def countInversions(arr):
    # Coordinate compression
    sorted_vals = sorted(set(arr))
    compress = {v: i+1 for i, v in enumerate(sorted_vals)}
    
    bit = BIT([0] * len(sorted_vals))
    inversions = 0
    
    for num in reversed(arr):
        compressed = compress[num]
        inversions += bit.prefixQuery(compressed - 1)  # Count smaller elements
        bit.update(compressed, 1)  # Add current element
    
    return inversions
```

### Point Update Techniques
```python
# Add/Subtract: Direct operation
bit.update(i, 5)    # Add 5 to index i
bit.update(i, -3)   # Subtract 3 from index i

# Set/Overwrite: Requires old value
def setValue(bit, i, newVal, oldVal):
    bit.update(i, newVal - oldVal)

# Toggle operations
def toggle(bit, i, isOn):
    bit.update(i, 1 if isOn else -1)

# Multiple updates
bit = BIT([1, 2, 3, 4, 5])
bit.update(2, 5)   # Add 5 to index 2
bit.update(4, -2)  # Subtract 2 from index 4
print(bit.prefixQuery(5))  # Updated sum
```

## Bit Manipulation Explained

### LSB (Least Significant Bit)
```python
def lsb(x):
    return x & (-x)

# Examples:
# lsb(6) = 6 & (-6) = 110₂ & 010₂ = 010₂ = 2
# lsb(8) = 8 & (-8) = 1000₂ & 1000₂ = 1000₂ = 8
```

### Index Responsibility
- Index 1 (001₂): Responsible for range [1,1] (size 1)
- Index 2 (010₂): Responsible for range [1,2] (size 2)
- Index 3 (011₂): Responsible for range [3,3] (size 1)
- Index 4 (100₂): Responsible for range [1,4] (size 4)

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Build | O(n log n) | O(n) |
| Update | O(log n) | O(1) |
| Query | O(log n) | O(1) |
| Range Sum | O(log n) | O(1) |

## Advantages

- **Efficient Updates**: O(log n) point updates vs O(n) for prefix arrays
- **Fast Queries**: O(log n) prefix sums vs O(n) for naive approach
- **Space Efficient**: Only O(n) extra space needed
- **Simple Implementation**: Fewer lines of code than segment trees
- **Cache Friendly**: Sequential memory access pattern
- **Versatile**: Can be extended for 2D, range updates, etc.
- **No Recursion**: Iterative implementation avoids stack overflow

## Disadvantages

- **Limited Operations**: Only supports associative operations (sum, XOR, etc.)
- **1-indexed**: Requires careful index management
- **Not Intuitive**: Bit manipulation can be confusing
- **Range Updates**: Requires difference array technique for efficiency
- **No Range Min/Max**: Cannot efficiently support min/max queries
- **Fixed Size**: Cannot dynamically resize like some other structures

## What Fenwick Tree Can Handle

### Core Applications
- **Range Sums**: Prefix and range sum queries with updates
- **Frequency Tables**: Count occurrences, maintain dynamic histograms
- **Inversion Counting**: Count inversions and reverse pairs efficiently
- **Order Statistics**: k-th element queries with dynamic updates
- **Multi-dimensional**: 2D BITs for submatrix operations

### Problem Keywords That Hint BIT Usage
- **Prefix sum / Cumulative sum**
- **Number of elements ≤ x / Count of smaller elements**
- **Count of inversions / reverse pairs**
- **Frequency table / occurrences**
- **Dynamic array with updates**
- **Insert and query counts efficiently**
- **Order statistics (find k-th element, rank queries)**
- **2D prefix sums with updates**
- **Range sum queries + point updates**

## ✅ What's Possible

- **Add/Subtract**: Point updates with positive/negative values
- **Set/Overwrite**: Indirect via `update(i, new_val - old_val)`
- **Frequency Counting**: Increment/decrement counts dynamically
- **Toggle Operations**: On-off switches (+1 for on, -1 for off)
- **XOR Operations**: Any associative, invertible operation

## ❌ What's Not Possible

- **Direct Replace**: Without knowing old value (needs delta calculation)
- **Non-linear Updates**: Multiply all elements, bitwise ops
- **Min/Max Updates**: Range minimum/maximum operations
- **Arbitrary Operations**: Limited to associative, invertible operations

## Use Cases

### Competitive Programming
- **Range Sum Queries**: Most common application
- **Inversion Counting**: Count inversions in array
- **Coordinate Compression**: Handle large coordinate ranges
- **Order Statistics**: Find kth smallest element with updates

### System Applications
- **Database Systems**: Maintaining running totals, aggregations
- **Financial Systems**: Portfolio value calculations, running P&L
- **Game Development**: Score tracking, leaderboard updates
- **Analytics**: Real-time metrics, sliding window calculations

### Advanced Applications
- **2D Fenwick Tree**: 2D range sum queries
- **Range Update Point Query**: Using difference arrays
- **Multiple Fenwick Trees**: Supporting multiple operations
- **Persistent Fenwick Tree**: Maintaining historical versions

## Extensions

### 2D Binary Indexed Tree
```python
class BIT2D:
    def __init__(self, matrix):
        self.rows, self.cols = len(matrix), len(matrix[0])
        self.bit = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        
    def update(self, r, c, val):
        i = r + 1
        while i <= self.rows:
            j = c + 1
            while j <= self.cols:
                self.bit[i][j] += val
                j += j & (-j)
            i += i & (-i)
```

### Range Update Point Query
```python
class RangeUpdateBIT:
    def __init__(self, n):
        self.bit = BIT([0] * n)
    
    def rangeUpdate(self, l, r, val):
        self.bit.update(l, val)
        if r + 1 <= self.bit.n:
            self.bit.update(r + 1, -val)
    
    def pointQuery(self, i):
        return self.bit.prefixQuery(i)
```

## Fenwick Tree vs Other Structures

| Structure | Update | Query | Space | Implementation |
|-----------|--------|-------|-------|----------------|
| Fenwick Tree | O(log n) | O(log n) | O(n) | Simple |
| Segment Tree | O(log n) | O(log n) | O(4n) | Complex |
| Prefix Array | O(n) | O(1) | O(n) | Trivial |
| Square Root | O(√n) | O(√n) | O(n) | Medium |

**When to Choose Fenwick Tree:**
- Need efficient point updates and range queries
- Operations are associative and invertible (sum, XOR, etc.)
- Memory usage is a concern
- Implementation simplicity is important
- Working with frequency counting or order statistics
- Problem involves counting inversions or smaller elements
- Need dynamic prefix sums

**When to Choose Segment Tree:**
- Need range updates
- Operations are not associative (min, max, gcd)
- Need lazy propagation
- Working with complex query types

## Common Pitfalls

1. **Index Confusion**: Remember Fenwick Tree is 1-indexed internally
2. **Overflow**: Be careful with large sums, use appropriate data types
3. **Operation Limitations**: Only works with associative, invertible operations
4. **Set Operations**: Need old value to compute delta for setting new values
5. **Range Queries**: Don't forget to handle l=1 case in range sum
6. **Coordinate Compression**: Remember to compress large value ranges

## References

- [Fenwick Tree - GeeksforGeeks](https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/)
- [Binary Indexed Tree - TopCoder](https://www.topcoder.com/thrive/articles/Binary%20Indexed%20Trees)
- [Fenwick Tree Tutorial - CP-Algorithms](https://cp-algorithms.com/data_structures/fenwick.html)