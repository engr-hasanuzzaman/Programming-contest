# https://leetcode.com/problems/odd-even-linked-list/

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
def odd_even_list(head)
  return head unless head && head.next && head.next.next
  odd = head
  even = head.next
  even_head = even
  current = head.next.next
  i = 3
  while current != nil
      if i % 2 == 0
          even.next = current
          even = even.next
          # puts "--even #{i}, #{current.val},  #{even&.val}"
      else
          odd.next = current
          odd = odd.next
          # puts "odd #{i}, #{current.val}, #{odd.val}"
      end
      
      current = current.next
      i += 1
      # puts "---i #{i}"
  end
  # puts "#{odd.inspect}, #{even.inspect}"
  odd.next = even_head
  even.next = nil
  head
end