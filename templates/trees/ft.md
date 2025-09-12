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
    self.FT = [0] * (self.n + 1)  # 1-indexed
    for i in range(self.n):
        self.update(i + 1, nums[i])
```

**Process:**
1. Create 1-indexed array of size n+1
2. Initialize all values to 0
3. Build tree by updating each element

### Update Operation
```python
def update(self, i, val):  # Add val to index i (1-indexed)
    while i <= self.n:
        self.FT[i] += val
        i += i & (-i)  # Move to next index
```

**Process:**
1. Start at index i
2. Add val to current index
3. Move to next responsible index using `i += i & (-i)`
4. Repeat until index exceeds n
**Example**: Updating index 3
- 3 (011₂) → 4 (100₂) → 8 (1000₂)
- Updates indices: 3, 4, 8

### Query Operation
```python
def getSum(self, i):  # Get prefix sum up to index i (1-indexed)
    res = 0
    while i > 0:
        res += self.FT[i]
        i -= i & (-i)  # Move to parent
    return res
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
ft = FT([1, 2, 3, 4, 5])

# Add 10 to index 3 (0-indexed becomes 1-indexed)
ft.update(3, 10)  # Now array is [1, 2, 13, 4, 5]

# Get prefix sum up to index 3
print(ft.getSum(3))  # Sum of [1, 2, 13] = 16

# Get prefix sum up to index 5
print(ft.getSum(5))  # Sum of [1, 2, 13, 4, 5] = 25
```

### Range Sum Query
```python
def rangeSum(ft, l, r):  # Sum of [l..r] (1-indexed)
    if l == 1:
        return ft.getSum(r)
    return ft.getSum(r) - ft.getSum(l - 1)

# Example usage
ft = FT([1, 2, 3, 4, 5])
print(rangeSum(ft, 2, 4))  # Sum of indices 2,3,4 = 2+3+4 = 9
```

### Point Update vs Range Update
```python
# Point update: set arr[i] = val
def pointUpdate(ft, i, newVal, oldVal):
    ft.update(i, newVal - oldVal)

# Multiple updates
ft = FT([1, 2, 3, 4, 5])
ft.update(2, 5)   # Add 5 to index 2
ft.update(4, -2)  # Subtract 2 from index 4
print(ft.getSum(5))  # Updated sum
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

### 2D Fenwick Tree
```python
class FenwickTree2D:
    def __init__(self, matrix):
        self.rows, self.cols = len(matrix), len(matrix[0])
        self.tree = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        
    def update(self, r, c, val):
        i = r + 1
        while i <= self.rows:
            j = c + 1
            while j <= self.cols:
                self.tree[i][j] += val
                j += j & (-j)
            i += i & (-i)
```

### Range Update Point Query
```python
class RangeUpdateFT:
    def __init__(self, n):
        self.ft = FT([0] * n)
    
    def rangeUpdate(self, l, r, val):
        self.ft.update(l, val)
        if r + 1 <= self.ft.n:
            self.ft.update(r + 1, -val)
    
    def pointQuery(self, i):
        return self.ft.getSum(i)
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
- Operations are associative (sum, XOR, etc.)
- Memory usage is a concern
- Implementation simplicity is important
- Working with 1D arrays primarily

**When to Choose Segment Tree:**
- Need range updates
- Operations are not associative (min, max, gcd)
- Need lazy propagation
- Working with complex query types

## Common Pitfalls

1. **Index Confusion**: Remember Fenwick Tree is 1-indexed internally
2. **Overflow**: Be careful with large sums, use appropriate data types
3. **Negative Updates**: Ensure the operation supports negative values
4. **Range Queries**: Don't forget to handle l=1 case in range sum
5. **Initialization**: Build tree properly during construction

## References

- [Fenwick Tree - GeeksforGeeks](https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/)
- [Binary Indexed Tree - TopCoder](https://www.topcoder.com/thrive/articles/Binary%20Indexed%20Trees)
- [Fenwick Tree Tutorial - CP-Algorithms](https://cp-algorithms.com/data_structures/fenwick.html)