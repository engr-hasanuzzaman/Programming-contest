# https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/

from collections import defaultdict

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        counter = defaultdict(int)

        cur = head
        while cur:
            counter[cur.val] += 1
            cur = cur.next

        new_head = cur = ListNode()
        while head:
            if counter[head.val] == 1:
                cur.next = head
                cur = cur.next
            head = head.next
        # remove the last link
        cur.next = None
        return new_head.next
