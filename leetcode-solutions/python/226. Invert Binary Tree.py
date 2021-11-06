# https://leetcode.com/problems/invert-binary-tree/

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return root
        q = deque([root])
        
        while q:
            cur_size = len(q)
            for _ in range(cur_size):
                cur_node = q.popleft()
                # swap left & right
                temp = cur_node.left
                cur_node.left = cur_node.right
                cur_node.right = temp
                
                if cur_node.left: q.append(cur_node.left)
                if cur_node.right: q.append(cur_node.right)
        return root
