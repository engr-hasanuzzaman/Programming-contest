# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        level = 1
        max_sum = root.val
        min_level = 1

        while queue:
            level_size = len(queue)
            cur_sum = 0
            for _ in range(level_size):
                cur = queue.popleft()
                cur_sum += cur.val
                if cur.left:
                    queue.append(cur.left)

                if cur.right:
                    queue.append(cur.right)
            if cur_sum > max_sum:
                max_sum = cur_sum
                min_level = level
            level += 1
        return min_level
