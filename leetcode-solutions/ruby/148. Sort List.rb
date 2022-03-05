# https://leetcode.com/problems/sort-list/

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
def sort_list(head)
    arr = []
    cur = head
    until cur.nil?
        arr << cur.val
        cur = cur.next
    end

    arr.sort!
    cur = head
    arr.each do |n|
        cur.val = n
        cur = cur.next
    end

    head
end
