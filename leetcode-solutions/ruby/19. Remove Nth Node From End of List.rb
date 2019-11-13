# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @param {Integer} n
# @return {ListNode}
def remove_nth_from_end(head, n)
  slow, fast = head, head
  
  n.times do
      fast = fast.next
  end
  
  prev = slow
  while fast != nil
      prev = slow
      slow = slow.next
      fast = fast.next
  end
  
  if slow == head
      head = head.next
      return head
  else
      # puts slow.inspect
      prev.next = slow.nil? ? nil : slow.next
      head
  end
end