from collections import deque
# Your task is to complete this function
# Function should return the level order of the tree in the form of a list of integers
def levelOrder( root ):
    if not root:
        return []
    
    ans = []
    q = deque([root])
    while q :
        current = q.pop()
        if current.left:
            deque.appendleft(q, current.left)
        if current.right:
            deque.appendleft(q, current.right)
        ans.append(current.data)
    return ans