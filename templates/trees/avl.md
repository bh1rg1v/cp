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

**When**: Left subtree is heavier (balance > 1)

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

**When**: Right subtree is heavier (balance < -1)

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
    # LL Case
    if balance > 1 and key < root.left.val:
        return rightRotate(root)

    # RR Case
    if balance < -1 and key > root.right.val:
        return leftRotate(root)

    # LR Case
    if balance > 1 and key > root.left.val:
        root.left = leftRotate(root.left)
        return rightRotate(root)

    # RL Case
    if balance < -1 and key < root.right.val:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root
```

### Rotation Cases
1. **LL Case**: Left-Left → Right Rotation
2. **RR Case**: Right-Right → Left Rotation  
3. **LR Case**: Left-Right → Left + Right Rotation
4. **RL Case**: Right-Left → Right + Left Rotation

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

- **Guaranteed Balance**: Height is always O(log n)
- **Predictable Performance**: All operations in O(log n)
- **Self-Balancing**: Automatically maintains balance

## Use Cases

- Database indexing
- Memory management systems
- Applications requiring guaranteed O(log n) operations
- Real-time systems where worst-case performance matters

## AVL vs Other Trees

| Tree Type | Search | Insert | Delete | Balance |
|-----------|--------|--------|--------|---------|
| AVL | O(log n) | O(log n) | O(log n) | Strict |
| Red-Black | O(log n) | O(log n) | O(log n) | Relaxed |
| BST | O(n) | O(n) | O(n) | None |

AVL trees are more rigidly balanced than Red-Black trees, making them faster for lookup-intensive applications.