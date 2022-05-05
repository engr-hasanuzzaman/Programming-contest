# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        size_a = size_b = 0
        cur = headA
        while cur:
            size_a += 1
            cur = cur.next

        cur = headB
        while cur:
            size_b += 1
            cur = cur.next

        # headA will contain larget list
        if size_a < size_b:
            headA, headB = headB, headA
            size_a, size_b = size_b, size_a

        # move extra steps first
        cur_a = headA
        for _ in range(size_a - size_b):
            cur_a = cur_a.next

        cur_b = headB
        while cur_a and cur_b:
            if cur_a == cur_b:
                return cur_a
            cur_a = cur_a.next
            cur_b = cur_b.next

        return None
