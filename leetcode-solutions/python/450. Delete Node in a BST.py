# https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        
        # if root is the target value
        if root.val == key:
            if root.left is None and root.right is None:
                return None
            elif root.right:
                self.insertNode(root.right, root.left)
                return root.right
            else:
                return root.left
        
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        return root

    def insertNode(self, root, node):
        if root is None or node is None:
            return root
        
        if node.val > root.val and root.right is None:
            node.right = node
        elif node.val > root.val:
            self.insertNode(root.right, node)
        elif node.val < root.val and root.left is None:
            root.left = node
        else:
            self.insertNode(root.left, node)
        return root
