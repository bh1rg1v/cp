def preOrder(root):
    return [root.data] + preOrder(root.left) + preOrder(root.right) if root else []

def inOrder(root):
    return inOrder(root.left) + [root.data] + inOrder(root.right) if root else []

def postOrder(root):
    return postOrder(root.left) + postOrder(root.right) + [root.data] if root else []