# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        # print(inorder, postorder)
        root = TreeNode(postorder.pop())
        left_nodes = []
        i = 0
        while inorder[i] != root.val:
            left_nodes.append(inorder[i])
            i += 1
        right_nodes = inorder[i+1:]
        # print(left_nodes, right_nodes)
        root.right = self.buildTree(right_nodes, postorder)
        root.left = self.buildTree(left_nodes, postorder)
        return root

