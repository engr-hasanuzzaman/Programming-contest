# Remove loop in Linked List
class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
            
        if fast is None or fast.next is None: return
        # has loop, find the start point of the loop
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        # fast is start point of the loop
        while fast.next != slow:
            fast = fast.next
        fast.next = None
