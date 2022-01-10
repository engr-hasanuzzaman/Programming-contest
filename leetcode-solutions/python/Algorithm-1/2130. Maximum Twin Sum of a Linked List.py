# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # keep pair sum
        sum_array = []
        size = 0
        cur = head
        # find the size
        while cur:
            size += 1
            cur = cur.next
        half = size // 2
        
        # vigit first half and append on sum_array
        cur = head
        while half > 0:
            half -= 1
            sum_array.append(cur.val)
            cur = cur.next

        # visit the remaining nodes and sum the value to sum_array with reversed order
        half = size // 2 - 1
        while cur:
            sum_array[half] += cur.val
            half -= 1
            cur = cur.next
        return max(sum_array)
