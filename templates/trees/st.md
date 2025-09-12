# Segment Tree

A Segment Tree is a binary tree data structure that allows efficient range queries and point updates on an array. Each node represents a segment (range) of the array and stores aggregate information about that segment.

## Key Properties

- **Complete Binary Tree**: Each internal node has exactly two children
- **Leaf Nodes**: Represent individual array elements
- **Internal Nodes**: Store aggregate values of their children's ranges
- **Height**: O(log n) for n elements
- **Array Representation**: Uses 4n space for simplicity

## Tree Structure

```
Array: [1, 3, 2, 7, 9]
Segment Tree (min):

        1
      /   \
     1     2
   /  \   /  \
  1    3 2    7
 /\   /\ /\   /\
1  3 3  2 2  7 7 9
```

**Node Indexing:**
- Root at index 1
- Left child of node i: 2*i
- Right child of node i: 2*i+1
- Parent of node i: i/2

## Implementation Details

### Constructor
```python
def __init__(self, arr, mode="min"):
    self.n = len(arr)
    self.arr = arr
    self.mode = mode
    self.tree = [0] * (4 * self.n)
    self.build(1, 0, self.n - 1)
```

**Process:**
1. Store original array and mode
2. Allocate 4n space for tree (safe upper bound)
3. Build tree recursively from root

### Combine Function
```python
def combine(self, left, right):
    return min(left, right) if self.mode == "min" else max(left, right)
```

**Purpose:** Determines how to merge two child values based on query type

### Build Operation
```python
def build(self, idx, l, r):
    if l == r:
        self.tree[idx] = self.arr[l]
        return
    mid = (l + r) // 2
    self.build(2 * idx, l, mid)
    self.build(2 * idx + 1, mid + 1, r)
    self.tree[idx] = self.combine(self.tree[2 * idx], self.tree[2 * idx + 1])
```

**Process:**
1. **Base Case**: If l == r, node represents single element
2. **Recursive Case**: Build left and right subtrees
3. **Combine**: Set current node value using combine function

**Time Complexity:** O(n) - visits each node once

### Update Operation
```python
def update(self, idx, l, r, pos, val):  # set arr[pos] = val
    if l == r:
        self.tree[idx] = val
        return
    mid = (l + r) // 2
    if pos <= mid:
        self.update(2 * idx, l, mid, pos, val)
    else:
        self.update(2 * idx + 1, mid + 1, r, pos, val)
    self.tree[idx] = self.combine(self.tree[2 * idx], self.tree[2 * idx + 1])
```

**Process:**
1. **Base Case**: Update leaf node directly
2. **Navigate**: Go to left or right child based on position
3. **Update Path**: Recalculate all nodes on path to root

**Time Complexity:** O(log n) - traverses height of tree

### Query Operation
```python
def query(self, idx, l, r, ql, qr):  # min/max in [ql, qr]
    if ql > r or qr < l:
        return float("inf") if self.mode == "min" else float("-inf")
    if ql <= l and r <= qr:
        return self.tree[idx]
    mid = (l + r) // 2
    left = self.query(2 * idx, l, mid, ql, qr)
    right = self.query(2 * idx + 1, mid + 1, r, ql, qr)
    return self.combine(left, right)
```

**Process:**
1. **No Overlap**: Return neutral value (∞ for min, -∞ for max)
2. **Complete Overlap**: Return current node value
3. **Partial Overlap**: Query both children and combine results

**Time Complexity:** O(log n) - visits at most 4 nodes per level

## Usage Examples

### Range Minimum Query
```python
# Initialize with array [1, 3, 2, 7, 9]
st_min = SegmentTree([1, 3, 2, 7, 9], "min")

# Query minimum in range [1, 3] (0-indexed)
print(st_min.query(1, 0, 4, 1, 3))  # Output: 2 (min of [3, 2, 7])

# Update position 2 to value 5
st_min.update(1, 0, 4, 2, 5)  # Array becomes [1, 3, 5, 7, 9]

# Query again
print(st_min.query(1, 0, 4, 1, 3))  # Output: 3 (min of [3, 5, 7])
```

### Range Maximum Query
```python
# Initialize for maximum queries
st_max = SegmentTree([1, 3, 2, 7, 9], "max")

# Query maximum in range [0, 4]
print(st_max.query(1, 0, 4, 0, 4))  # Output: 9 (max of entire array)

# Query maximum in range [1, 2]
print(st_max.query(1, 0, 4, 1, 2))  # Output: 3 (max of [3, 2])
```

### Helper Functions
```python
class SegmentTreeHelper:
    def __init__(self, arr, mode="min"):
        self.st = SegmentTree(arr, mode)
        self.n = len(arr)
    
    def update_point(self, pos, val):
        """Update single position (0-indexed)"""
        self.st.update(1, 0, self.n - 1, pos, val)
    
    def query_range(self, l, r):
        """Query range [l, r] (0-indexed, inclusive)"""
        return self.st.query(1, 0, self.n - 1, l, r)
```

## Advanced Operations

### Range Sum Segment Tree
```python
class SumSegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1)
    
    def combine(self, left, right):
        return left + right
    
    # build, update, query methods similar but use sum
```

### Multiple Query Types
```python
class MultiSegmentTree:
    def __init__(self, arr):
        self.min_tree = SegmentTree(arr, "min")
        self.max_tree = SegmentTree(arr, "max")
        self.n = len(arr)
    
    def update(self, pos, val):
        self.min_tree.update(1, 0, self.n - 1, pos, val)
        self.max_tree.update(1, 0, self.n - 1, pos, val)
    
    def range_min(self, l, r):
        return self.min_tree.query(1, 0, self.n - 1, l, r)
    
    def range_max(self, l, r):
        return self.max_tree.query(1, 0, self.n - 1, l, r)
```

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Build | O(n) | O(4n) = O(n) |
| Update | O(log n) | O(log n) |
| Query | O(log n) | O(log n) |
| Space | - | O(4n) = O(n) |

## Advantages

- **Versatile**: Supports any associative operation (min, max, sum, gcd, etc.)
- **Efficient**: O(log n) updates and queries
- **Range Queries**: Handles arbitrary range queries efficiently
- **Point Updates**: Fast single element updates
- **Intuitive**: Tree structure is easy to understand and visualize
- **Extensible**: Can be modified for lazy propagation, persistent versions
- **No Restrictions**: Works with any array size and data type

## Disadvantages

- **Space Overhead**: Uses 4n space (more than Fenwick Tree's n space)
- **Implementation Complexity**: More complex than Fenwick Tree
- **Recursion**: Uses recursion which can cause stack overflow for large inputs
- **Cache Performance**: May have worse cache locality than linear structures
- **Overkill**: Simple prefix sums are better handled by Fenwick Tree

## Use Cases

### Competitive Programming
- **Range Minimum/Maximum Queries**: Most common application
- **Range GCD/LCM**: Mathematical range queries
- **Range Sum with Updates**: Alternative to Fenwick Tree
- **Coordinate Compression**: Handle large coordinate ranges

### System Applications
- **Database Systems**: Range aggregations, OLAP queries
- **Graphics/Gaming**: Collision detection, spatial queries
- **Financial Systems**: Time-series analysis, moving averages
- **Network Systems**: Bandwidth monitoring, QoS management

### Advanced Applications
- **Computational Geometry**: Range searching, nearest neighbor
- **Image Processing**: Region-based operations
- **Machine Learning**: Feature selection, data preprocessing
- **Bioinformatics**: Sequence analysis, pattern matching

## Extensions

### Lazy Propagation
```python
# For range updates - see st-lp.py
class LazySegmentTree:
    def __init__(self, arr):
        # Additional lazy array for pending updates
        self.lazy = [0] * (4 * len(arr))
    
    def push(self, idx, l, r):
        # Apply pending updates to current node
        pass
    
    def range_update(self, l, r, val):
        # Update entire range efficiently
        pass
```

### Persistent Segment Tree
```python
# Maintains multiple versions of the tree
class PersistentSegmentTree:
    def __init__(self, arr):
        self.versions = []
        # Each update creates new version
    
    def update_version(self, version, pos, val):
        # Create new version with update
        pass
```

## Segment Tree vs Other Structures

| Structure | Update | Query | Space | Range Updates |
|-----------|--------|-------|-------|---------------|
| Segment Tree | O(log n) | O(log n) | O(4n) | With Lazy Prop |
| Fenwick Tree | O(log n) | O(log n) | O(n) | Limited |
| Sparse Table | O(n log n) | O(1) | O(n log n) | No |
| Square Root | O(√n) | O(√n) | O(n) | Yes |

**When to Choose Segment Tree:**
- Need range min/max queries
- Operations are not limited to sum/XOR
- Need range updates (with lazy propagation)
- Array size is moderate (< 10^6 elements)
- Implementation complexity is acceptable

**When to Choose Fenwick Tree:**
- Only need sum/XOR operations
- Memory usage is critical
- Simpler implementation preferred
- Working with very large arrays

## Common Pitfalls

1. **Index Management**: Carefully handle 0-indexed arrays with 1-indexed tree
2. **Neutral Values**: Use correct neutral values (∞ for min, -∞ for max)
3. **Array Bounds**: Ensure query ranges are within array bounds
4. **Space Allocation**: Use 4n space to avoid index out of bounds
5. **Recursion Depth**: Be aware of stack limits for very large arrays

## References

- [Segment Tree - GeeksforGeeks](https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/)
- [Segment Tree Tutorial - CP-Algorithms](https://cp-algorithms.com/data_structures/segment_tree.html)
- [Range Minimum Query - TopCoder](https://www.topcoder.com/thrive/articles/Range%20Minimum%20Query%20and%20Lowest%20Common%20Ancestor)