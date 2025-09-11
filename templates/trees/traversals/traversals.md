# Tree Traversal Algorithms

## DFS (Depth-First Search) Traversals

### 1. Pre-order Traversal
**Order**: Root → Left → Right

```python
def preOrder(root):
    return [root.data] + preOrder(root.left) + preOrder(root.right) if root else []
```

**Explanation**: 
- Visit the root node first
- Recursively traverse the left subtree
- Recursively traverse the right subtree

**Use Cases**: 
- Creating a copy of the tree
- Getting prefix expression of an expression tree
- Tree serialization

**Time Complexity**: O(n)  
**Space Complexity**: O(h) where h is the height of the tree

---

### 2. In-order Traversal
**Order**: Left → Root → Right

```python
def inOrder(root):
    return inOrder(root.left) + [root.data] + inOrder(root.right) if root else []
```

**Explanation**:
- Recursively traverse the left subtree
- Visit the root node
- Recursively traverse the right subtree

**Use Cases**:
- Getting sorted order of elements in a Binary Search Tree
- Converting expression tree to infix expression
- Finding the kth smallest element in BST

**Time Complexity**: O(n)  
**Space Complexity**: O(h) where h is the height of the tree

---

### 3. Post-order Traversal
**Order**: Left → Right → Root

```python
def postOrder(root):
    return postOrder(root.left) + postOrder(root.right) + [root.data] if root else []
```

**Explanation**:
- Recursively traverse the left subtree
- Recursively traverse the right subtree
- Visit the root node

**Use Cases**:
- Deleting nodes from a tree (delete children before parent)
- Getting postfix expression of an expression tree
- Calculating size of directories in file system

**Time Complexity**: O(n)  
**Space Complexity**: O(h) where h is the height of the tree

---

## BFS (Breadth-First Search) Traversal

### Level-order Traversal
**Order**: Level by level from left to right

```python
from collections import deque

def levelOrder(root):
    res = []
    if root is None:
        return []
    
    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        res.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return res
```

**Explanation**:
- Use a queue to process nodes level by level
- Start with root in queue
- For each node: visit it, then add its children to queue
- Continue until queue is empty

**Use Cases**:
- Finding shortest path in unweighted trees
- Level-wise processing of tree nodes
- Finding nodes at a specific level
- Tree serialization by levels

**Time Complexity**: O(n)  
**Space Complexity**: O(w) where w is the maximum width of the tree

---

## Morris In-order Traversal
**Order**: Left → Root → Right (Space Optimized)

```python
def morrisInorder(root):
    res = []
    cur = root
    
    while cur:
        if not cur.left:
            res.append(cur.data)
            cur = cur.right
        else:
            pre = cur.left
            while pre.right and pre.right != cur:
                pre = pre.right
            
            if not pre.right:
                pre.right = cur
                cur = cur.left
            else:
                pre.right = None
                res.append(cur.data)
                cur = cur.right
    
    return res
```

**Explanation**:
Morris traversal uses threading to achieve in-order traversal without recursion or stack:

1. **No left child**: Visit current node and move right
2. **Has left child**: Find inorder predecessor (rightmost node in left subtree)
3. **Create thread**: Make predecessor point to current node, move left
4. **Thread exists**: Remove thread, visit current node, move right

**Key Advantage**: Constant space complexity O(1) instead of O(h)

**Use Cases**:
- Memory-constrained environments
- Large trees where stack overflow is a concern
- When you need in-order traversal with minimal space

**Time Complexity**: O(n)  
**Space Complexity**: O(1) - No recursion stack or additional data structures

---

## Algorithm Comparison

| Algorithm | Time | Space | Recursion | Use Case |
|-----------|------|-------|-----------|----------|
| Pre-order | O(n) | O(h) | Yes | Tree copying, serialization |
| In-order | O(n) | O(h) | Yes | BST sorted order |
| Post-order | O(n) | O(h) | Yes | Tree deletion, directory size |
| Level-order (BFS) | O(n) | O(w) | No | Level-wise processing, shortest path |
| Morris In-order | O(n) | O(1) | No | Memory-efficient in-order |

**Note**: h = height of tree, n = number of nodes, w = maximum width of tree

## References

- [Inorder Tree Traversal without Recursion and without Stack - GeeksforGeeks](https://www.geeksforgeeks.org/dsa/inorder-tree-traversal-without-recursion-and-without-stack/)