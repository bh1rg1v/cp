# Tree Traversal Algorithms

This document explains the different tree traversal algorithms implemented in the traversals directory.

## Depth-First Search (DFS) Traversals

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

### 4. Morris In-order Traversal
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
| Morris In-order | O(n) | O(1) | No | Memory-efficient in-order |

**Note**: h = height of tree, n = number of nodes