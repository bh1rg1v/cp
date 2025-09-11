# Red-Black Tree Implementation

class COLOR:
    RED = "RED"
    BLACK = "BLACK"

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = COLOR.RED

    def isOnLeft(self):
        return self.parent is not None and self.parent.left == self

    
    def hasRedChild(self):
        return (self.left and self.left.color == COLOR.RED) or (self.right and self.right.color == COLOR.RED)
    
    def sibling(self):
        if self.parent is None:
            return None
        
        if self.isOnLeft():
            return self.parent.right
        else:
            return self.parent.left
        
    def uncle(self):
        if self.parent is None or self.parent.parent is None:
            return None

        if self.parent.isOnLeft():
            return self.parent.parent.right
        else:
            return self.parent.parent.left
        
    def moveDown(self, newParent):
        if self.parent is not None:
            if self.isOnLeft():
                self.parent.left = newParent
            else:
                self.parent.right = newParent

        newParent.parent = self.parent
        self.parent = newParent

class RBT:
    def __init__(self):
        self.root = None

    def leftRotate(self, node):
        newParent = node.right
        node.moveDown(newParent)
        node.right = newParent.left

        if newParent.left:
            newParent.left.parent = node

        newParent.left = node
        
        if node == self.root:
            self.root = newParent

    def rightRotate(self, node):
        newParent = node.left
        node.moveDown(newParent)
        node.left = newParent.right

        if newParent.right:
            newParent.right.parent = node

        newParent.right = node
        
        if node == self.root:
            self.root = newParent

    def insertHelper(self, root, key):
        if root is None:
            return Node(key)

        if key < root.val:
            root.left = self.insertHelper(root.left, key)
            root.left.parent = root
        elif key > root.val:
            root.right = self.insertHelper(root.right, key)
            root.right.parent = root
        elif key == root.val:   # Duplicate keys are ignored
            return root
        
        return root
    
    def findNode(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self.findNode(root.left, key)
        return self.findNode(root.right, key)

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            self.root.color = COLOR.BLACK
            return
        
        self.root = self.insertHelper(self.root, key)
        
        # Find the newly inserted node and fix violations
        newNode = self.findNode(self.root, key)
        if newNode:
            self.fixRedRed(newNode)
        
        # Update root to actual root
        while self.root.parent:
            self.root = self.root.parent


    def swapColors(self, node1, node2):
        node1.color, node2.color = node2.color, node1.color



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
            # Case 1: Uncle is red - recolor
            parent.color = COLOR.BLACK
            uncle.color = COLOR.BLACK
            grandparent.color = COLOR.RED
            self.fixRedRed(grandparent)
        else:
            # Case 2: Uncle is black - rotate
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

    def successor(self, node):
        temp = node
        while temp.left:
            temp = temp.left
        return temp
    
    def BSTReplace(self, node):
        if node.left and node.right:
            return self.successor(node.right)

        if not node.left and not node.right:
            return None

        if node.left:
            return node.left
        else:
            return node.right
        
    def deleteNode(self, node):
        replaceNode = self.BSTReplace(node)
        
        # Store original colors
        nodeColor = node.color
        
        if node == self.root and replaceNode is None:
            self.root = None
            return node
            
        # Replace node with replaceNode
        if replaceNode:
            # Copy value instead of replacing structure for two children case
            if node.left and node.right:
                node.val = replaceNode.val
                # Now delete the successor
                return self.deleteNode(replaceNode)
            else:
                # Single child case
                if node.parent:
                    if node.isOnLeft():
                        node.parent.left = replaceNode
                    else:
                        node.parent.right = replaceNode
                    replaceNode.parent = node.parent
                else:
                    self.root = replaceNode
                    replaceNode.parent = None
        else:
            # No children case
            if node.parent:
                if node.isOnLeft():
                    node.parent.left = None
                else:
                    node.parent.right = None
            else:
                self.root = None

        # Fix violations if deleted node was black
        if nodeColor == COLOR.BLACK:
            if replaceNode and replaceNode.color == COLOR.RED:
                replaceNode.color = COLOR.BLACK
            elif replaceNode is not None:
                self.fixBlackBlack(replaceNode)

        return node
    
    def fixBlackBlack(self, node):
        if node == self.root or node is None:
            return

        sibling = node.sibling()
        parent = node.parent

        if sibling is None:
            # No sibling, fix parent
            self.fixBlackBlack(parent)
        else:
            if sibling.color == COLOR.RED:
                # Case 1: Red sibling
                parent.color = COLOR.RED
                sibling.color = COLOR.BLACK
                if sibling.isOnLeft():
                    self.rightRotate(parent)
                else:
                    self.leftRotate(parent)
                self.fixBlackBlack(node)
            else:
                # Case 2: Black sibling
                if sibling.hasRedChild():
                    # Case 2a: Black sibling with red child
                    if sibling.left and sibling.left.color == COLOR.RED:
                        if sibling.isOnLeft():
                            # Left Left Case
                            sibling.left.color = sibling.color
                            sibling.color = parent.color
                            self.rightRotate(parent)
                        else:
                            # Right Left Case
                            sibling.left.color = parent.color
                            self.rightRotate(sibling)
                            self.leftRotate(parent)
                    else:
                        if sibling.isOnLeft():
                            # Left Right Case
                            sibling.right.color = parent.color
                            self.leftRotate(sibling)
                            self.rightRotate(parent)
                        else:
                            # Right Right Case
                            sibling.right.color = sibling.color
                            sibling.color = parent.color
                            self.leftRotate(parent)
                    parent.color = COLOR.BLACK
                else:
                    # Case 2b: Black sibling with black children
                    sibling.color = COLOR.RED
                    if parent.color == COLOR.BLACK:
                        self.fixBlackBlack(parent)
                    else:
                        parent.color = COLOR.BLACK