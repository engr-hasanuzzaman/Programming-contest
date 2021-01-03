# recursive solution
def insert(root, val):
    if root is None:
        return Node(val)
    
    if root.data == val:
        return root
    elif val > root.data:
        root.right = insert(root.right, val)
    else:
        root.left = insert(root.left, val)
    return root

