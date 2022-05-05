# https://leetcode.com/problems/add-two-numbers-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_one = []
        num_two = []
        while l1:
            num_one.append(l1.val)
            l1 = l1.next

        while l2:
            num_two.append(l2.val)
            l2 = l2.next
        # print(num_one, num_two)
        rem = 0
        new_head = None
        while num_one or num_two:
            f_digit = num_one.pop() if num_one else 0
            s_digit = num_two.pop() if num_two else 0
            total = f_digit + s_digit + rem
            node = ListNode(total % 10)
            node.next = new_head
            new_head = node
            rem = total // 10
            # cur = cur.next

        if rem > 0:
            node = ListNode(rem)
            node.next = new_head
            new_head = node

        return new_head
