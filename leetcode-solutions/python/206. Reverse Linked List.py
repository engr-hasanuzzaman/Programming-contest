# https://leetcode.com/problems/reverse-linked-list/

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        # always return the new head without modification
        new_head = self.reverseList(head.next)

        # 1 -> 2 to 2 -> 1         
        temp_head = head.next
        temp_head.next = head
        temp_head.next.next = None
        
        return new_head