# https://leetcode.com/problems/merge-k-sorted-lists/

import heapq 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(heap)
        head = ListNode(0)
        cur = head
        while heap:
            val, index, node = heapq.heappop(heap)
            cur.next = ListNode(node.val)
            cur = cur.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, index, node))
        return head.next
