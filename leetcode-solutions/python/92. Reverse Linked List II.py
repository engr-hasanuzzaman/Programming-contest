# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        idx = 1
        cur = head
        # track prev-node of the left node so that after reversing we have update old_perv.next = head_of_rev
        old_pev = None
        while left > idx:
            old_prev = cur
            cur = cur.next
            idx += 1

        # tail of the reverse part. If we have more nodes after revering we have to add as next of this node
        rev_tail = cur
        prev = None
        while right >= idx:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            idx += 1

        # add the remainging nodes at the end of rev_tail
        rev_tail.next = cur

        # add rev-part with the head part
        if left > 1:
            old_prev.next = prev
            return head

        # main head get reversed
        return prev
