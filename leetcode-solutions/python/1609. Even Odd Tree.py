# https://leetcode.com/problems/even-odd-tree/

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = 0
        queue = deque([root])

        while queue:
            level_size = len(queue)
            last_val = None

            for _ in range(level_size):
                cur = queue.popleft()

                # check odd/even
                if level % 2 == 0:
                    if cur.val % 2 == 0 or (last_val and cur.val <= last_val):
                        return False
                else:
                    if cur.val % 2 == 1 or last_val and cur.val >= last_val:
                        return False
                last_val = cur.val

                # add child on the queue
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            level += 1
        return True
