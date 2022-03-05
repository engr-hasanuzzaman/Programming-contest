# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} head
# @return {ListNode}
def delete_middle(head)
    prev = nil
    slow = head
    fast = head
    while fast && fast.next
        fast = fast.next.next
        prev = slow
        slow = slow.next
    end
    
    unless prev.nil?
        prev.next = prev.next.next
    else
        return nil
    end
    head
end