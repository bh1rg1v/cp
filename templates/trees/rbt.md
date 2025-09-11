# Red-Black Tree (RBT)

A Red-Black Tree is a self-balancing Binary Search Tree where each node has a color (red or black) and follows specific properties to maintain balance.

## Red-Black Properties

1. **Every node is either red or black**
2. **Root is always black**
3. **All leaves (NIL nodes) are black**
4. **Red nodes cannot have red children** (no two red nodes adjacent)
5. **Every path from root to leaf has the same number of black nodes**

## Node Structure

```python
class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = COLOR.RED  # New nodes are red by default
```

**Key Methods:**
- `isOnLeft()`: Check if node is left child
- `sibling()`: Get sibling node
- `uncle()`: Get uncle node (parent's sibling)
- `hasRedChild()`: Check if node has red children
- `moveDown()`: Update parent-child relationships during rotations

## Core Operations

### Rotations

#### Left Rotation
```python
def leftRotate(self, node):
    newParent = node.right
    node.moveDown(newParent)
    node.right = newParent.left

    if newParent.left:
        newParent.left.parent = node

    newParent.left = node
    
    if node == self.root:
        self.root = newParent
```

#### Right Rotation
```python
def rightRotate(self, node):
    newParent = node.left
    node.moveDown(newParent)
    node.left = newParent.right

    if newParent.right:
        newParent.right.parent = node

    newParent.right = node
    
    if node == self.root:
        self.root = newParent
```

## Insertion

### Process
1. **Standard BST insertion** (new node is red)
2. **Fix red-red violations** using rotations and recoloring
3. **Ensure root is black**

```python
def insert(self, key):
    if self.root is None:
        self.root = Node(key)
        self.root.color = COLOR.BLACK
        return
    
    self.root = self.insertHelper(self.root, key)
    
    # Find and fix violations
    newNode = self.findNode(self.root, key)
    if newNode:
        self.fixRedRed(newNode)
    
    # Update root
    while self.root.parent:
        self.root = self.root.parent
```

### Fixing Red-Red Violations

```python
def fixRedRed(self, node):
    if node == self.root:
        node.color = COLOR.BLACK
        return

    parent = node.parent
    if parent.color == COLOR.BLACK:
        return
        
    grandparent = parent.parent
    uncle = node.uncle()
    
    if uncle and uncle.color == COLOR.RED:
        # Case 1: Red uncle - Recolor
        parent.color = COLOR.BLACK
        uncle.color = COLOR.BLACK
        grandparent.color = COLOR.RED
        self.fixRedRed(grandparent)
    else:
        # Case 2: Black uncle - Rotate
        if parent.isOnLeft():
            if node.isOnLeft():
                # LL Case
                self.swapColors(parent, grandparent)
                self.rightRotate(grandparent)
            else:
                # LR Case
                self.leftRotate(parent)
                self.swapColors(node, grandparent)
                self.rightRotate(grandparent)
        else:
            if node.isOnLeft():
                # RL Case
                self.rightRotate(parent)
                self.swapColors(node, grandparent)
                self.leftRotate(grandparent)
            else:
                # RR Case
                self.swapColors(parent, grandparent)
                self.leftRotate(grandparent)
```

### Insertion Cases
1. **Red Uncle**: Recolor parent, uncle to black; grandparent to red
2. **Black Uncle**: Perform rotations based on node positions
   - **LL**: Right rotation on grandparent
   - **LR**: Left rotation on parent, then right on grandparent
   - **RL**: Right rotation on parent, then left on grandparent
   - **RR**: Left rotation on grandparent

## Deletion

### Process
1. **Standard BST deletion**
2. **Fix black-black violations** if deleted node was black
3. **Maintain red-black properties**

```python
def deleteNode(self, node):
    replaceNode = self.BSTReplace(node)
    nodeColor = node.color
    
    # Handle replacement
    if replaceNode:
        if node.left and node.right:
            # Two children: copy value and delete successor
            node.val = replaceNode.val
            return self.deleteNode(replaceNode)
        else:
            # Single child: replace node
            # Update parent-child links
    else:
        # No children: remove node
    
    # Fix violations if deleted node was black
    if nodeColor == COLOR.BLACK:
        if replaceNode and replaceNode.color == COLOR.RED:
            replaceNode.color = COLOR.BLACK
        elif replaceNode is not None:
            self.fixBlackBlack(replaceNode)
```

### Fixing Black-Black Violations

```python
def fixBlackBlack(self, node):
    if node == self.root or node is None:
        return

    sibling = node.sibling()
    parent = node.parent

    if sibling is None:
        self.fixBlackBlack(parent)
    else:
        if sibling.color == COLOR.RED:
            # Case 1: Red sibling
            parent.color = COLOR.RED
            sibling.color = COLOR.BLACK
            # Rotate to make sibling black
            if sibling.isOnLeft():
                self.rightRotate(parent)
            else:
                self.leftRotate(parent)
            self.fixBlackBlack(node)
        else:
            # Case 2: Black sibling
            if sibling.hasRedChild():
                # Case 2a: Black sibling with red child
                # Perform rotations based on red child position
            else:
                # Case 2b: Black sibling with black children
                sibling.color = COLOR.RED
                if parent.color == COLOR.BLACK:
                    self.fixBlackBlack(parent)
                else:
                    parent.color = COLOR.BLACK
```

### Deletion Cases
1. **Red Sibling**: Rotate to convert to black sibling case
2. **Black Sibling with Red Child**: Rotate based on red child position
3. **Black Sibling with Black Children**: Recolor sibling to red

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Search | O(log n) | O(log n) |
| Insert | O(log n) | O(log n) |
| Delete | O(log n) | O(log n) |
| Height | O(1) | O(1) |

## Advantages

- **Guaranteed O(log n)**: All operations in logarithmic time
- **Less Rigid Balancing**: Fewer rotations than AVL trees
- **Better for Insertions**: More efficient for write-heavy workloads
- **Widely Used**: Standard in many libraries (Java TreeMap, C++ map)
- **Good Cache Performance**: Reasonable balance with fewer rotations
- **Practical**: Good balance between performance and implementation complexity

## Disadvantages

- **Complex Implementation**: More complex than basic BST
- **Memory Overhead**: Extra color bit per node
- **Slower Lookups**: Slightly slower searches than AVL trees
- **Debugging Difficulty**: Hard to visualize and debug violations
- **Not Optimal for Reads**: AVL trees better for read-heavy workloads

## Use Cases

### Database Systems
- **B-Tree Alternatives**: When simpler structure needed
- **Transaction Logs**: Efficient insertions with good search
- **Index Structures**: Balanced performance for mixed workloads

### System Programming
- **Operating Systems**: Process scheduling, memory management
- **Compilers**: Symbol tables with frequent updates
- **File Systems**: Directory structures, metadata indexing

### Application Development
- **Standard Libraries**: Java TreeMap, C++ std::map
- **Game Development**: Dynamic object management
- **Network Systems**: Routing tables, connection management

### Specialized Applications
- **Real-Time Systems**: Predictable performance with fewer rotations
- **Embedded Systems**: Good balance of performance and complexity
- **Caching Systems**: LRU implementations with mixed access patterns
- **Priority Queues**: When balanced insertions/deletions needed
- **Event Scheduling**: Time-based event management

## RBT vs AVL Comparison

| Aspect | Red-Black Tree | AVL Tree |
|--------|---------------|----------|
| **Balance** | Relaxed (height ≤ 2×log n) | Strict (height ≤ 1.44×log n) |
| **Rotations** | Fewer (≤3 for insert, ≤3 for delete) | More (≤2 for insert, ≤log n for delete) |
| **Search Speed** | Slightly slower | Faster |
| **Insert/Delete** | Faster | Slower |
| **Memory** | 1 bit per node | 1 int per node |
| **Use Case** | Write-heavy, general purpose | Read-heavy, lookup intensive |

## When to Choose Red-Black Trees

**Choose RBT when:**
- Mixed read/write workloads (40-60% split)
- Frequent insertions and deletions
- Memory usage is a concern
- Need predictable performance with fewer rotations
- Using standard library implementations

**Choose AVL when:**
- Read-heavy workloads (70%+ reads)
- Need fastest possible lookups
- Can tolerate more complex rebalancing
- Memory for height storage is available

## References

- [Red-Black Tree - GeeksforGeeks](https://www.geeksforgeeks.org/red-black-tree-set-1-introduction-2/)
- [Red-Black Tree Insertion - GeeksforGeeks](https://www.geeksforgeeks.org/red-black-tree-set-2-insert/)
- [Red-Black Tree Deletion - GeeksforGeeks](https://www.geeksforgeeks.org/red-black-tree-set-3-delete-2/)