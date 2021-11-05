# https://leetcode.com/problems/maximum-depth-of-binary-tree/
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        
        queue = deque([root])
        depth = 0
        
        while queue:
            current_size = len(queue)
            depth += 1
            
            for _ in range(current_size):
                current = queue.popleft()
                if current.left: queue.append(current.left)
                if current.right: queue.append(current.right)
        return depth