# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.dfs(root, 0, [])
    def dfs(self, root, height, ancestors):
        l_val = r_val = 0
        ancestors.append(root.val)
        if root.left:
            l_val = self.dfs(root.left, height + 1, ancestors)
        if root.right:
            r_val = self.dfs(root.right, height + 1, ancestors)
        # removed the last ancestor
        ancestors.pop()
        if height >= 2 and ancestors[height - 2] % 2 == 0:
            return root.val + l_val + r_val
        else:
            return l_val + r_val
