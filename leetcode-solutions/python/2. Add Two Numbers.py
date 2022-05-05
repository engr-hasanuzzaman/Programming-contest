# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem = 0
        new_head = cur = ListNode()

        while l1 or l2:
            first_digit = l1.val if l1 else 0
            second_digit = l2.val if l2 else 0
            total = first_digit + second_digit + rem
            cur.next = ListNode(total % 10)
            cur = cur.next
            rem = total // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # if we have rem
        if rem > 0:
            cur.next = ListNode(rem)

        return new_head.next
