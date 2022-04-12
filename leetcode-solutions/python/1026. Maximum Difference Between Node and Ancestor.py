# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return max(self.dfs(root.left, root.val, root.val), self.dfs(root.right, root.val, root.val)) 
    
    def dfs(self, node, max_v, min_v):
        if not node:
            return 0

        val = max(abs(node.val - max_v), abs(node.val - min_v))
        left = self.dfs(node.left, max(node.val, max_v), min(min_v, node.val))
        right = self.dfs(node.right, max(node.val, max_v), min(min_v, node.val))
        return max(val, left, right) 
