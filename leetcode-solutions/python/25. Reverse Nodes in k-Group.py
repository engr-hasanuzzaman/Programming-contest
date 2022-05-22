# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next

        return self.reverse(head, k, size)

    def reverse(self, head, k, size):
        if not head or size < k:
            return head

        # prev will hold last processed node which will be new head for this part
        prev = None
        cur = head
        num = k
        while num > 0 and cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            num -= 1

        # head is the tail of this batch so remaing will be attached with the head node
        head.next = self.reverse(cur, k, size - k)

        return prev
