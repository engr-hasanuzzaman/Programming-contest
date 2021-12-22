# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s = []
        cur = head
        size = 0
        while cur:
            s.append(cur)
            cur = cur.next
            size += 1
        half = size // 2
        i = 1
        cur = head
        while i <= half:
            temp = cur.next
            cur.next = s.pop()
            cur.next.next = temp
            cur = temp
            i += 1
        cur.next = None

        if size % 2 == 1:
            cur.next = s.pop()
            cur = cur.next
        cur.next = None
        return head
