# https://leetcode.com/problems/symmetric-tree/

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        def same(r1, r2):
            if r1 is None and r2 is None:
                return True
            if r1 is None or r2 is None:
                return False
            
            return r1.val == r2.val and same(r1.left, r2.right) and same(r1.right, r2.left)
        return same(root.left, root.right)
