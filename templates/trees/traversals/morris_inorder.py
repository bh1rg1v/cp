def morrisInorder(root):
    res = []
    cur = root
    
    while cur:
        if not cur.left:
            # If no left child, visit this node
            res.append(cur.data)
            # Move to right child
            cur = cur.right
        else:
            # Find inorder predecessor of cur
            pre = cur.left
            while pre.right and pre.right != cur:
                pre = pre.right
            
            # Make cur the right child of its inorder predecessor
            if not pre.right:
                pre.right = cur
                cur = cur.left
            else:
                # Revert changes (fix right pointer)
                pre.right = None
                # Visit current node
                res.append(cur.data)
                # Move to right child
                cur = cur.right
    
    return res