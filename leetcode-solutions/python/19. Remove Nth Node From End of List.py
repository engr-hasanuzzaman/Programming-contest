# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        # move fast n times, so that it reached to last node when slow will be before target node
        while n > 0:
            fast = fast.next
            n -= 1

        # have to remove head
        if fast is None:
            return head.next

        # untill find the last node so that slow point to target's previous node
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head
