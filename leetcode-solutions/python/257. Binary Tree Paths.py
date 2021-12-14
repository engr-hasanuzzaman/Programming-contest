# https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root.left is None and root.right is None:
            return [str(root.val)]
        ans = []
        if root.left:
            ans += [str(root.val) + "->" + str(path) for path in self.binaryTreePaths(root.left)]
        if root.right:
            ans += [str(root.val) + "->" + path for path in self.binaryTreePaths(root.right)]
        return ans
