
class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    if node is None:
        return 0
    return node.height

def rightRotate(root):

    newRoot = root.left
    root.left = newRoot.right
    newRoot.right = root

    root.height = 1 + max(height(root.left), height(root.right))
    newRoot.height = 1 + max(height(newRoot.left), height(newRoot.right))

    return newRoot

def leftRotate(root):

    newRoot = root.right
    root.right = newRoot.left
    newRoot.left = root

    root.height = 1 + max(height(root.left), height(root.right))
    newRoot.height = 1 + max(height(newRoot.left), height(newRoot.right))

    return newRoot

def getBalance(root):
    if root is None:
        return 0
    return height(root.left) - height(root.right)

def insert(root, key):

    if root is None:
        return Node(key)

    if key < root.val:
        root.left = insert(root.left, key)
    elif key > root.val:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(height(root.left), height(root.right))

    balance = getBalance(root)

    if balance > 1 and key < root.left.val:
        return rightRotate(root)

    if balance < -1 and key > root.right.val:
        return leftRotate(root)

    if balance > 1 and key > root.left.val:
        root.left = leftRotate(root.left)
        return rightRotate(root)

    if balance < -1 and key < root.right.val:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root

def minValueNode(node):
    current = node

    while current.left is not None:
        current = current.left

    return current

def deleteNode(root, key):

    if root is None:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)

    if root is None:
        return root

    root.height = 1 + max(height(root.left), height(root.right))

    balance = getBalance(root)

    if balance > 1 and getBalance(root.left) >= 0:
        return rightRotate(root)

    if balance < -1 and getBalance(root.right) <= 0:
        return leftRotate(root)

    if balance > 1 and getBalance(root.left) < 0:
        root.left = leftRotate(root.left)
        return rightRotate(root)

    if balance < -1 and getBalance(root.right) > 0:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root