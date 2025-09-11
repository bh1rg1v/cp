
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