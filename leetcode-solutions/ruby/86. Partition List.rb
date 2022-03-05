# https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} head
# @param {Integer} x
# @return {ListNode}
def partition(head, x)
    q = []
    left = cur = head
    until cur.nil?
        if cur.val < x
            left.val, cur.val = cur.val, left.val
            left = left.next
        else
            q << cur.val
        end
        cur = cur.next
    end

    cur = head
    until cur.nil?
        if cur.val >= x
            cur.val = q.shift
        end
        
        cur = cur.next
    end
    
    head
end
