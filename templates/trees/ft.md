# Fenwick Tree (Binary Indexed Tree)

A Fenwick Tree efficiently supports prefix sum queries and point updates using bit manipulation. Each index is responsible for a range determined by its Least Significant Bit (LSB).

## Key Properties

- **1-indexed**: Uses 1-based indexing for bit manipulation
- **LSB Trick**: `i & (-i)` determines range responsibility
- **O(log n)**: All operations in logarithmic time
- **O(n) Space**: Minimal memory overhead

## Implementation

```python
class BIT:

    def __init__(self, nums):
        # Initialize BIT with input array
        self.n = len(nums)
        self.bit = [0] * (self.n + 1)  # 1-indexed array

        for idx, val in enumerate(nums, 1):
            self.update(idx, val)  # Build tree by updating each element

    def update(self, idx, val):
        # Add val to index idx, propagate up the tree
        while idx <= self.n:
            self.bit[idx] += val
            idx += idx & (-idx)  # Move to next responsible index

    def prefixQuery(self, idx):
        # Get sum of elements from index 1 to idx
        res = 0
        while idx > 0:
            res += self.bit[idx]
            idx -= idx & (-idx)  # Move to parent index

        return res
    
    def rangeQuery(self, l, r):
        # Get sum of elements from index l to r
        return self.prefixQuery(r) - self.prefixQuery(l - 1)
```

## How It Works

**LSB Trick**: `i & (-i)` gives the Least Significant Bit
- Update: Move up tree with `idx += idx & (-idx)`
- Query: Move down tree with `idx -= idx & (-idx)`
- Each index covers a range of size equal to its LSB

## Usage Examples

```python
# Basic operations
bit = BIT([1, 2, 3, 4, 5])          # Initialize with array
bit.update(3, 10)                    # Add 10 to index 3 (1-indexed)
print(bit.prefixQuery(3))            # Sum [1..3] = 16
print(bit.rangeQuery(2, 4))          # Sum [2..4] = 19
```

### Frequency Counting
```python
# Count occurrences of elements
bit = BIT([0] * 1001)                # For values 1-1000
bit.update(x, 1)                     # Increment count for value x
print(bit.prefixQuery(x))            # Count elements ≤ x
```

### Inversion Counting
```python
def countInversions(arr):
    # Coordinate compression for large values
    vals = sorted(set(arr))
    compress = {v: i+1 for i, v in enumerate(vals)}
    
    bit = BIT([0] * len(vals))       # Initialize empty BIT
    inversions = 0
    
    for num in reversed(arr):        # Process array from right to left
        compressed = compress[num]
        inversions += bit.prefixQuery(compressed - 1)  # Count smaller elements
        bit.update(compressed, 1)    # Add current element
    
    return inversions
```

## When to Use BIT

**Problem Keywords:**
- Prefix sum, cumulative sum
- Count elements ≤ x, smaller elements
- Inversions, reverse pairs
- Frequency tables, dynamic counting
- Order statistics, k-th element
- Range sum + point updates

**Applications:**
- Range sums with updates
- Frequency counting
- Inversion counting
- Order statistics
- 2D submatrix sums

## ✅ What's Possible / ❌ What's Not

**✅ Possible:**
- Add/Subtract values: `bit.update(i, val)`
- Set values: `bit.update(i, new_val - old_val)`
- Frequency counting, inversions, order statistics
- Any associative, invertible operation (sum, XOR)

**❌ Not Possible:**
- Range min/max queries
- Non-invertible operations (multiply, bitwise AND/OR)
- Direct replace without knowing old value

## Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Build | O(n log n) | O(n) |
| Update/Query | O(log n) | O(1) |

## BIT vs Alternatives

| Structure | Update | Query | Space | Use Case |
|-----------|--------|-------|-------|----------|
| BIT | O(log n) | O(log n) | O(n) | Sum, XOR, frequency |
| Segment Tree | O(log n) | O(log n) | O(4n) | Min/max, complex ops |
| Prefix Array | O(n) | O(1) | O(n) | Static queries only |

**Choose BIT when:** Need sum/XOR operations with updates, memory matters, simple implementation
**Choose Segment Tree when:** Need min/max/gcd, range updates, complex operations

## Extensions

**2D BIT**: For submatrix sum queries
**Range Updates**: Using difference arrays
**Multiple BITs**: For different operations simultaneously

## Common Pitfalls

- **1-indexed**: Internal array uses 1-based indexing
- **Set operations**: Need old value to compute delta
- **Overflow**: Use appropriate data types for large sums
- **Coordinate compression**: Compress large value ranges