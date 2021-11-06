# https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None: return TreeNode(val)
        current = root
        while current:
            if current.val > val:
                if current.left is None:
                    current.left = TreeNode(val)
                    return root
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(val)
                    return root
                current = current.right
        return root
