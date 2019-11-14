# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @param {Integer} val
# @return {ListNode}
def remove_elements(head, val)
  prev = nil
  curr = head
  
  while curr != nil
      if curr.val == val
          # need to remove head
          if prev == nil
              curr = curr.next
              head = curr
          else
              prev.next = curr.next
              curr = curr.next
          end
      else
          prev = curr
          curr = curr.next
      end
  end
  
  head
end