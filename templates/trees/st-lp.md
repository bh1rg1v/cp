# Segment Tree with Lazy Propagation

A Segment Tree with Lazy Propagation is an extension of the standard Segment Tree that efficiently handles range updates. Instead of updating each element individually, it uses "lazy" propagation to defer updates until they are actually needed.

## Key Properties

- **Range Updates**: Update entire ranges in O(log n) time
- **Lazy Propagation**: Defer updates to avoid unnecessary work
- **Range Queries**: Maintain O(log n) query time
- **Space Efficient**: Only O(n) extra space for lazy array

## Core Concept

**Lazy Propagation** works by:
1. **Marking**: Instead of updating all nodes immediately, mark the node as "lazy"
2. **Deferring**: Store the pending update in a separate lazy array
3. **Pushing**: Apply the update only when the node is accessed later
4. **Propagating**: Pass the update to children when needed

## Implementation Details

### Constructor
```python
def __init__(self, arr):
    self.n = len(arr)
    self.arr = arr
    self.tree = [0] * (4 * self.n)
    self.lazy = [0] * (4 * self.n)  # Lazy propagation array
    self.build(1, 0, self.n - 1)
```

**Key Components:**
- `tree[]`: Stores segment sums
- `lazy[]`: Stores pending updates for each node
- Both arrays use 4n space for safety

### Build Operation
```python
def build(self, idx, l, r):
    if l == r:
        self.tree[idx] = self.arr[l]
        return
    mid = (l + r) // 2
    self.build(2 * idx, l, mid)
    self.build(2 * idx + 1, mid + 1, r)
    self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]
```

**Process:** Same as standard segment tree, builds bottom-up

### Push Operation (Lazy Propagation)
```python
def push(self, idx, l, r):  # apply lazy updates
    if self.lazy[idx] != 0:
        self.tree[idx] += self.lazy[idx] * (r - l + 1)
        if l != r:
            self.lazy[2 * idx] += self.lazy[idx]
            self.lazy[2 * idx + 1] += self.lazy[idx]
        self.lazy[idx] = 0
```

**Process:**
1. **Apply Update**: Add lazy value × range size to current node
2. **Propagate**: Pass lazy value to children (if not leaf)
3. **Clear**: Reset lazy value to 0

**Key Insight:** Multiply by range size because we're adding the same value to all elements in the range

### Range Update Operation
```python
def update(self, idx, l, r, ql, qr, val):  # add val to [ql, qr]
    self.push(idx, l, r)
    if ql > r or qr < l:
        return
    if ql <= l and r <= qr:
        self.lazy[idx] += val
        self.push(idx, l, r)
        return
    mid = (l + r) // 2
    self.update(2 * idx, l, mid, ql, qr, val)
    self.update(2 * idx + 1, mid + 1, r, ql, qr, val)
    self.push(2 * idx, l, mid)
    self.push(2 * idx + 1, mid + 1, r)
    self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]
```

**Process:**
1. **Push Current**: Apply any pending updates to current node
2. **No Overlap**: Return if query range doesn't intersect
3. **Complete Overlap**: Mark as lazy and push
4. **Partial Overlap**: Recursively update children
5. **Update Current**: Recalculate current node value

**Time Complexity:** O(log n) - visits at most 2 nodes per level

### Range Query Operation
```python
def query(self, idx, l, r, ql, qr):  # sum in [ql, qr]
    if ql > r or qr < l:
        return 0
    self.push(idx, l, r)
    if ql <= l and r <= qr:
        return self.tree[idx]
    mid = (l + r) // 2
    left = self.query(2 * idx, l, mid, ql, qr)
    right = self.query(2 * idx + 1, mid + 1, r, ql, qr)
    return left + right
```

**Process:**
1. **No Overlap**: Return 0 (neutral for sum)
2. **Push**: Apply pending updates before reading
3. **Complete Overlap**: Return current node value
4. **Partial Overlap**: Query children and combine

**Time Complexity:** O(log n)

## Usage Examples

### Basic Range Updates
```python
# Initialize with array [1, 2, 3, 4, 5]
st = SegmentTreeLP([1, 2, 3, 4, 5])

# Add 10 to range [1, 3] (0-indexed)
st.update(1, 0, 4, 1, 3, 10)
# Array becomes [1, 12, 13, 14, 5]

# Query sum in range [1, 3]
print(st.query(1, 0, 4, 1, 3))  # Output: 39 (12+13+14)

# Query sum of entire array
print(st.query(1, 0, 4, 0, 4))  # Output: 45 (1+12+13+14+5)
```

### Multiple Range Updates
```python
st = SegmentTreeLP([0, 0, 0, 0, 0])  # Start with zeros

# Multiple range updates
st.update(1, 0, 4, 0, 2, 5)   # Add 5 to [0, 2]
st.update(1, 0, 4, 1, 4, 3)   # Add 3 to [1, 4]
st.update(1, 0, 4, 2, 3, -2)  # Subtract 2 from [2, 3]

# Final array: [5, 8, 6, 1, 3]
print(st.query(1, 0, 4, 0, 4))  # Output: 23
```

### Helper Class
```python
class LazySegmentTreeHelper:
    def __init__(self, arr):
        self.st = SegmentTreeLP(arr)
        self.n = len(arr)
    
    def range_add(self, l, r, val):
        """Add val to range [l, r] (0-indexed, inclusive)"""
        self.st.update(1, 0, self.n - 1, l, r, val)
    
    def range_sum(self, l, r):
        """Get sum of range [l, r] (0-indexed, inclusive)"""
        return self.st.query(1, 0, self.n - 1, l, r)
    
    def point_query(self, pos):
        """Get value at single position"""
        return self.st.query(1, 0, self.n - 1, pos, pos)
```

## Lazy Propagation Explained

### Without Lazy Propagation
```python
# Naive approach: O(n) per update
def naive_range_update(arr, l, r, val):
    for i in range(l, r + 1):
        arr[i] += val  # O(n) time
```

### With Lazy Propagation
```python
# Efficient approach: O(log n) per update
# Mark nodes as lazy instead of updating immediately
# Apply updates only when nodes are accessed
```

### Lazy Array States
- `lazy[i] = 0`: No pending updates
- `lazy[i] > 0`: Add this value to all elements in range
- `lazy[i] < 0`: Subtract this value from all elements in range

## Advanced Operations

### Range Set (instead of Range Add)
```python
class RangeSetLazyTree:
    def __init__(self, arr):
        # Additional array to track if lazy value is "set" or "add"
        self.lazy_type = [0] * (4 * len(arr))  # 0=none, 1=add, 2=set
    
    def push(self, idx, l, r):
        if self.lazy_type[idx] == 2:  # Set operation
            self.tree[idx] = self.lazy[idx] * (r - l + 1)
        elif self.lazy_type[idx] == 1:  # Add operation
            self.tree[idx] += self.lazy[idx] * (r - l + 1)
```

### Range Minimum with Lazy Updates
```python
class LazyMinTree:
    def __init__(self, arr):
        # For min queries with range additions
        self.tree = arr.copy()  # Store actual minimums
        self.lazy = [0] * (4 * len(arr))  # Store additions
    
    def combine(self, left, right):
        return min(left, right)
```

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Build | O(n) | O(4n) = O(n) |
| Range Update | O(log n) | O(log n) |
| Range Query | O(log n) | O(log n) |
| Point Query | O(log n) | O(log n) |
| Space | - | O(8n) = O(n) |

**Comparison with Standard Segment Tree:**
- Standard: O(n) per range update
- Lazy: O(log n) per range update
- **Speedup**: O(n/log n) times faster for range updates

## Advantages

- **Efficient Range Updates**: O(log n) instead of O(n)
- **Maintains Query Speed**: Still O(log n) for range queries
- **Memory Efficient**: Only doubles space requirement
- **Versatile**: Can handle various range operations (add, set, multiply)
- **Batch Updates**: Multiple updates before queries are very efficient
- **Real-World Applicable**: Many practical problems need range updates

## Disadvantages

- **Implementation Complexity**: More complex than standard segment tree
- **Space Overhead**: Requires additional lazy array
- **Push Overhead**: Every operation requires push calls
- **Debugging Difficulty**: Lazy state makes debugging harder
- **Limited Operations**: Not all operations can be efficiently lazily propagated
- **Recursion Depth**: Still limited by stack size for very large arrays

## Use Cases

### Competitive Programming
- **Range Update Range Query**: Most common application
- **Difference Arrays**: Alternative to difference array technique
- **Coordinate Compression**: Handle large coordinate ranges efficiently
- **Dynamic Programming**: Optimize DP transitions with range updates

### System Applications
- **Database Systems**: Bulk updates, batch processing
- **Financial Systems**: Portfolio rebalancing, bulk price updates
- **Game Development**: Area-of-effect updates, terrain modification
- **Graphics**: Image processing, region-based operations

### Advanced Applications
- **Computational Geometry**: Range updates on coordinate spaces
- **Network Systems**: Bandwidth allocation, QoS updates
- **Scientific Computing**: Grid-based simulations
- **Machine Learning**: Batch gradient updates, feature scaling

## Extensions

### 2D Lazy Propagation
```python
class Lazy2DSegmentTree:
    def __init__(self, matrix):
        # 2D lazy propagation for matrix range updates
        pass
    
    def range_update_2d(self, r1, c1, r2, c2, val):
        # Update rectangle [r1,c1] to [r2,c2]
        pass
```

### Multiple Lazy Operations
```python
class MultiLazyTree:
    def __init__(self, arr):
        self.add_lazy = [0] * (4 * len(arr))
        self.mult_lazy = [1] * (4 * len(arr))
    
    def push(self, idx, l, r):
        # Apply multiplication first, then addition
        # Order matters for non-commutative operations
        pass
```

## Lazy Propagation vs Other Techniques

| Technique | Range Update | Range Query | Space | Implementation |
|-----------|-------------|-------------|-------|----------------|
| Lazy Segment Tree | O(log n) | O(log n) | O(n) | Complex |
| Difference Array | O(1) | O(n) | O(n) | Simple |
| Square Root | O(√n) | O(√n) | O(n) | Medium |
| Fenwick Tree | O(log n) | O(log n) | O(n) | Medium |

**When to Choose Lazy Segment Tree:**
- Need both efficient range updates AND range queries
- Updates and queries are intermixed
- Range operations are more complex than simple addition
- Can tolerate implementation complexity

**When to Choose Difference Array:**
- Only need range updates followed by queries
- Updates are simple additions
- Implementation simplicity is important

## Common Pitfalls

1. **Forgetting Push**: Always push before accessing node values
2. **Lazy Propagation Order**: Apply lazy updates in correct order
3. **Range Size**: Remember to multiply by range size for sum operations
4. **Neutral Values**: Use correct neutral values for different operations
5. **Update vs Set**: Distinguish between adding and setting values
6. **Child Updates**: Don't forget to push children before combining

## References

- [Lazy Propagation - GeeksforGeeks](https://www.geeksforgeeks.org/lazy-propagation-in-segment-tree/)
- [Segment Tree with Lazy Propagation - CP-Algorithms](https://cp-algorithms.com/data_structures/segment_tree.html#toc-tgt-11)
- [Range Updates with Lazy Propagation - TopCoder](https://www.topcoder.com/thrive/articles/Range%20Minimum%20Query%20and%20Lowest%20Common%20Ancestor)