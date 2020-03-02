# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB
        r = 0
        while headA != None and headB != None and headA != headB:
            if headA.next == None:
                headA = b
                if r == 1:
                    return None
                else:
                    r = 1
            else:
                headA = headA.next
                
            if headB.next == None:
                headB = a
            else:
                headB = headB.next
                
        if headA == headB:
            return headA
        else:
            return None
                
        