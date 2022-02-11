# https://leetcode.com/problems/linked-list-cycle-ii/

# using cycle detection technique
# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @return {ListNode}
def detectCycle(head)
    slow = head
    fast = head
    while fast && fast.next
        fast = fast.next.next
        slow = slow.next
        break if fast == slow
    end
    
    return nil if !fast || !fast.next

    slow = head
    while slow != fast
        slow = slow.next
        fast = fast.next
    end
    
    fast
end

#