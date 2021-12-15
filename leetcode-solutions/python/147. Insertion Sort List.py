# https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we have one sorted list where we will put element one by one on the correct position
        # sort is correctly sorted list and we will put one element one at a time to it using cur
        sort = ListNode() # this is sortede node
        cur = head
        while cur:
            curSort = sort
            while curSort.next and cur.val >= curSort.next.val:
                curSort = curSort.next
            temp, curSort.next = curSort.next, cur
            cur = cur.next
            curSort.next.next = temp
        return sort.next
    