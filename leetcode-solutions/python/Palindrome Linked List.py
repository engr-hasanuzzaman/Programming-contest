# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Use recursion to go the end of the link, then compare with the head
If both have same value, returen true and update the head to next value
'''
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
        