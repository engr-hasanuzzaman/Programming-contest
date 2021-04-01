# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        self.head = head
        return self.isPalindromeRec(head)
        
    def isPalindromeRec(self, node) -> bool:
        if not node:
            return True
        
        isPalindrom = self.isPalindromeRec(node.next)
        
        if not isPalindrom:
            return False
        
        if node.val == self.head.val:
            self.head = self.head.next
            return True
        
        return False
        