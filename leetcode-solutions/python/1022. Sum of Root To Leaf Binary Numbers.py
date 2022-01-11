# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, str(root.val))
    
    def dfs(self, root, path):
        if not root.left and not root.right:
            return int(path, 2)
        
        left_sum = 0
        right_sum = 0
        if root.left:
            left_sum = self.dfs(root.left, path + str(root.left.val))
        if root.right:
            right_sum = self.dfs(root.right, path + str(root.right.val))
        return left_sum + right_sum
