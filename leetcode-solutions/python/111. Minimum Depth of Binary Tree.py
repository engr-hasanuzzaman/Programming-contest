# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        s = [root]
        depth = 0
        while s:
            depth += 1
            size = len(s)
            temp = []
            for _ in range(size):
                node = s.pop()
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            s = temp
        return depth
