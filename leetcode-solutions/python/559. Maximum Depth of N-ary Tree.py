# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        s = [root]
        height = 0
        while s:
            size = len(s)
            temp = []
            height += 1
            for _ in range(size):
                cur = s.pop()
                temp += cur.children
            s = temp
        return height
