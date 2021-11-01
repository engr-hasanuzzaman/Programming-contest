# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        new_head = ListNode()
        new_tail = new_head

        while head != None:
            if head.val != val:
                new_tail.next = head
                new_tail = new_tail.next
            head = head.next
        new_tail.next = None
        return new_head.next
