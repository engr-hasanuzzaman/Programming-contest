# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @return {Integer}
def get_decimal_value(head)
  return 0 unless head
  
  ans = [0, 0]
  sum(ans, head)
  ans[0]
end

def sum(ans, node)
  if node.next.nil?
      ans[0] += (node.val * (2 ** ans[1]))
      ans[1] += 1
      return
  end
  
  sum(ans, node.next)
  ans[0] += (node.val * (2 ** ans[1]))
  ans[1] += 1
end