# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# solution: 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        cur = head
        # find the list size
        while cur:
            size += 1
            cur = cur.next
        
        # find the target node from head
        cur = head
        target_position = size - n

        # remove nth node from the head
        if target_position == 0:
            return head.next
        cur = head
        prev = None
        while target_position > 0:
            prev = cur
            cur = cur.next
            target_position -= 1
        prev.next = cur.next
        return head
            
