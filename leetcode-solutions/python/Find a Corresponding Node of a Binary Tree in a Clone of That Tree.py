# use BFS for traversing the tree
from collections import deque

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q = deque([cloned])
        while q:
            current = deque.pop(q)
            if current.val == target.val:
                return current
            if current.left:
                deque.appendleft(q, current.left)
            if current.right:
                deque.appendleft(q, current.right)