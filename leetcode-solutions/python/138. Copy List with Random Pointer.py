# https://leetcode.com/problems/copy-list-with-random-pointer/

from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        container = defaultdict(lambda: None)

        new_head = new_cur = Node(-1)
        cur = head
        # build the normal linked list
        while cur:
            new_node = Node(cur.val)
            new_cur.next = new_node
            container[id(cur)] = new_node

            new_cur = new_cur.next
            cur = cur.next

        # establish random link
        cur = head
        while cur:
            new_node = container[id(cur)]
            new_random = container[id(cur.random)]
            new_node.random = new_random

            cur = cur.next

        return new_head.next
