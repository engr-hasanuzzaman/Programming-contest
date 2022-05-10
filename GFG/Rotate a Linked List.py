
# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:

    # Function to rotate a linked list. (left rotate)
    def rotate(self, head, k):
        if not head or not head.next or k <= 0:
            return head

        cur = head
        length = 1

        # find last element and list size
        while cur.next:
            length += 1
            cur = cur.next

        if k % length == 0:
            return head

        # point the head, after rotate last node will point to head
        cur.next = head

        # find the new head my removing first k element
        cur = head
        k -= 1
        while k > 0:
            cur = cur.next
            k -= 1

        head = cur.next
        cur.next = None
        return head
