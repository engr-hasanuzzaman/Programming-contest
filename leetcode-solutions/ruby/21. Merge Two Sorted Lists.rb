# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def merge_two_lists(l1, l2)
  node1 = l1
  node2 = l2
  head, current_node = nil
  
  # empty check    
  return node1 unless node2
  return node2 unless node1
  
  if node1.val > node2.val
      head = node2
      node2 = node2.next 
  else
      head = node1
      node1 = node1.next
  end
  
  current_node = head
  
  while node1 && node2
      if node1.val > node2.val
          current_node.next = node2
          node2 = node2.next
      else
          current_node.next = node1
          node1 = node1.next
      end
      
      current_node = current_node.next
  end
  
  if node1
      current_node.next = node1
  elsif node2 
      current_node.next = node2
  end
  
  head
end