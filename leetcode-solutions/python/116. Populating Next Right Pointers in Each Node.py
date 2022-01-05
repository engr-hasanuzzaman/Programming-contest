# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        
        s = deque([root])
        while s:
            size = len(s)
            # print("size is ", size)
            temp = []
            prev = None
            for _ in range(size):
                cur = s.popleft()
                if prev:
                    prev.next = cur
                prev = cur
                if cur.left:
                    s.append(cur.left)
                if cur.right:
                    s.append(cur.right)
        return root
