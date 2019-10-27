# https://leetcode.com/problems/middle-of-the-linked-list/

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
def middle_node(head)
  hear = head
  tottoy = head 
  
  while tottoy && tottoy.next
      hear = hear.next
      tottoy = tottoy.next.next
  end
  
  hear
end