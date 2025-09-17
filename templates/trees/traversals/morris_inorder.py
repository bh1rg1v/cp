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