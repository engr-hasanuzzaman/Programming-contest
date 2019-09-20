# https://leetcode.com/problems/swap-nodes-in-pairs/

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
def swap_pairs(head)
  return head unless head && head.next
  # store node temp     
  t_h = head
  t_nn = head.next.next
  
  # swap node
  head = head.next
  head.next = t_h
  head.next.next = swap_pairs(t_nn)
  head
end 