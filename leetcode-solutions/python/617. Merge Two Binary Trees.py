# https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        new_node = None
        if root1 and root2:
            new_node = TreeNode(root1.val + root2.val)
            new_node.left = self.mergeTrees(root1.left, root2.left)
            new_node.right = self.mergeTrees(root1.right, root2.right)
        elif root1:
            new_node = TreeNode(root1.val)
            new_node.left = root1.left
            new_node.right = root1.right
        elif root2:
            new_node = TreeNode(root2.val)
            new_node.left = root2.left
            new_node.right = root2.right
        
        return new_node
