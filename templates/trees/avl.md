# AVL Tree (Adelson-Velsky and Landis Tree)

AVL tree is a self-balancing Binary Search Tree where the difference between heights of left and right subtrees cannot be more than 1 for all nodes.

## Key Properties

- **Balance Factor**: height(left) - height(right) ∈ {-1, 0, 1}
- **Height**: O(log n) guaranteed
- **Operations**: Insert, Delete, Search all in O(log n)

## Node Structure

```python
class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.height = 1
```

Each node stores its height to efficiently calculate balance factors.

## Core Functions

### Height Calculation
```python
def height(node):
    if node is None:
        return 0
    return node.height
```

### Balance Factor
```python
def getBalance(root):
    if root is None:
        return 0
    return height(root.left) - height(root.right)
```

Balance factor determines if rotations are needed:
- **> 1**: Left heavy (needs right rotation)
- **< -1**: Right heavy (needs left rotation)

## Rotations

### Right Rotation (LL Case)
```python
def rightRotate(root):
    newRoot = root.left
    root.left = newRoot.right
    newRoot.right = root

    root.height = 1 + max(height(root.left), height(root.right))
    newRoot.height = 1 + max(height(newRoot.left), height(newRoot.right))

    return newRoot
```
```
    z              y
   /              / \
  y       →      x   z
 /
x
```

### Left Rotation (RR Case)
```python
def leftRotate(root):
    newRoot = root.right
    root.right = newRoot.left
    newRoot.left = root

    root.height = 1 + max(height(root.left), height(root.right))
    newRoot.height = 1 + max(height(newRoot.left), height(newRoot.right))

    return newRoot
```
```
  x                y
   \      →       / \
    y            x   z
     \
      z
```

## Insertion

```python
def insert(root, key):
    # 1. Normal BST insertion
    if root is None:
        return Node(key)

    if key < root.val:
        root.left = insert(root.left, key)
    elif key > root.val:
        root.right = insert(root.right, key)
    else:
        return root

    # 2. Update height
    root.height = 1 + max(height(root.left), height(root.right))

    # 3. Get balance factor
    balance = getBalance(root)

    # 4. Perform rotations if unbalanced
    # LL Case: Left-Left imbalance
    if balance > 1 and key < root.left.val:
        return rightRotate(root)

    # RR Case: Right-Right imbalance  
    if balance < -1 and key > root.right.val:
        return leftRotate(root)

    # LR Case: Left-Right imbalance
    if balance > 1 and key > root.left.val:
        root.left = leftRotate(root.left)   # First left rotation
        return rightRotate(root)            # Then right rotation

    # RL Case: Right-Left imbalance
    if balance < -1 and key < root.right.val:
        root.right = rightRotate(root.right)  # First right rotation
        return leftRotate(root)               # Then left rotation

    return root
```

### Rotation Cases

#### 1. LL Case (Left-Left) → Right Rotation
```
Before:          After:
    z              y
   /              / \
  y              x   z
 /
x
```

#### 2. RR Case (Right-Right) → Left Rotation
```
Before:          After:
  x                y
   \              / \
    y            x   z
     \
      z
```

#### 3. LR Case (Left-Right) → Left + Right Rotation
```
Before:          After Left:      After Right:
    z                z                y
   /                /                / \
  x                y                x   z
   \
    y
```

#### 4. RL Case (Right-Left) → Right + Left Rotation
```
Before:          After Right:     After Left:
  x                x                y
   \                \              / \
    z                y            x   z
   /
  y
```

## Deletion

```python
def deleteNode(root, key):
    # 1. Normal BST deletion
    if root is None:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        # Node to be deleted found
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Node with two children
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)

    # 2. Update height
    root.height = 1 + max(height(root.left), height(root.right))

    # 3. Get balance and perform rotations
    balance = getBalance(root)

    # LL Case
    if balance > 1 and getBalance(root.left) >= 0:
        return rightRotate(root)

    # RR Case
    if balance < -1 and getBalance(root.right) <= 0:
        return leftRotate(root)

    # LR Case
    if balance > 1 and getBalance(root.left) < 0:
        root.left = leftRotate(root.left)
        return rightRotate(root)

    # RL Case
    if balance < -1 and getBalance(root.right) > 0:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root
```

### Helper Function
```python
def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current
```

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Search | O(log n) | O(log n) |
| Insert | O(log n) | O(log n) |
| Delete | O(log n) | O(log n) |
| Height | O(1) | O(1) |

## Advantages

- **Guaranteed Balance**: Height is always O(log n), never degrades to linear
- **Predictable Performance**: All operations consistently in O(log n) time
- **Self-Balancing**: Automatically maintains balance without manual intervention
- **Optimal Search**: Faster lookups compared to Red-Black trees due to stricter balancing
- **Cache Efficiency**: Better cache performance due to balanced structure
- **Deterministic**: No randomization, behavior is completely predictable
- **Memory Efficient**: Only stores height information, minimal overhead
- **Thread-Safe Reads**: Multiple concurrent reads are naturally safe

## Disadvantages

- **Insertion/Deletion Overhead**: More rotations needed compared to Red-Black trees
- **Rigid Balancing**: Stricter balance requirements can cause more restructuring
- **Memory Usage**: Extra height field in each node increases memory consumption
- **Complex Implementation**: More complex to implement than basic BST
- **Frequent Rebalancing**: Heavy insertion/deletion workloads trigger many rotations
- **Not Optimal for Write-Heavy**: Red-Black trees perform better for frequent modifications

## Use Cases

### Database Systems
- **B+ Tree Alternatives**: When simpler structure is preferred
- **Index Structures**: For tables with more reads than writes
- **Range Queries**: Efficient in-order traversal for range searches

### Real-Time Systems
- **Embedded Systems**: Predictable O(log n) performance critical
- **Game Engines**: Spatial indexing, collision detection
- **Operating Systems**: Process scheduling, memory management

### Data Analytics
- **Statistical Applications**: Maintaining sorted datasets
- **Time Series Data**: Efficient timestamp-based lookups
- **Financial Systems**: Order book management, price indexing

### Specialized Applications
- **Compiler Design**: Symbol table management
- **Network Routing**: IP address lookup tables
- **Geographic Information Systems**: Spatial data indexing
- **Caching Systems**: LRU cache implementations with guaranteed performance
- **Priority Queues**: When balanced performance is required
- **Auto-complete Systems**: Prefix-based search in dictionaries

## AVL vs Other Trees

| Tree Type | Search | Insert | Delete | Balance |
|-----------|--------|--------|--------|---------|
| AVL | O(log n) | O(log n) | O(log n) | Strict |
| Red-Black | O(log n) | O(log n) | O(log n) | Relaxed |
| BST | O(n) | O(n) | O(n) | None |

**When to Choose AVL:**
- Read-heavy applications (70%+ reads)
- Need guaranteed O(log n) performance
- Memory is not extremely constrained
- Predictable performance is critical

**When to Choose Red-Black:**
- Write-heavy applications
- Need faster insertions/deletions
- Memory usage is critical
- Can tolerate slightly slower searches

## References

- [Introduction to AVL Tree - GeeksforGeeks](https://www.geeksforgeeks.org/dsa/introduction-to-avl-tree/)
- [Insertion in an AVL Tree - GeeksforGeeks](https://www.geeksforgeeks.org/dsa/insertion-in-an-avl-tree/)
- [Deletion in an AVL Tree - GeeksforGeeks](https://www.geeksforgeeks.org/dsa/deletion-in-an-avl-tree/)