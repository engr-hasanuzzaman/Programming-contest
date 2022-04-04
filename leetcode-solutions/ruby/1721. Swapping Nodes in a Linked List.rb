# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} head
# @param {Integer} k
# @return {ListNode}
def swap_nodes(head, k)
  cur = head
  (k - 1).times do
    cur = cur.next
  end

  kth_from_first = cur
  kth_from_last = head
  # find kth from the last
  until cur.nil? || cur.next.nil?
    kth_from_last = kth_from_last.next
    cur = cur.next
  end

  temp = kth_from_first.val
  kth_from_first.val = kth_from_last.val
  kth_from_last.val = temp

  head
end
