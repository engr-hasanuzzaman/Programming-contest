# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        merged_list = ListNode(None)
        new_head = merged_list
    
        while l1 != None and l2 != None:
            if l1.val >= l2.val:
                merged_list.next = l2
                l2 = l2.next
            else:
                merged_list.next = l1
                l1 = l1.next
            merged_list = merged_list.next

        # add remaing nodes
        if l1 != None:
            merged_list.next = l1
        else:
            merged_list.next = l2

        return new_head.next
