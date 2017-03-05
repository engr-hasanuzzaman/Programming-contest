# Definition for singly-linked list.
class ListNode
    attr_accessor :val, :next
    def initialize(val)
        @val = val
        @next = nil
    end
end

# @param {ListNode} node
# @return {Void} Do not return anything, modify node in-place instead.
def delete_node(node)
    return node unless node || node.next
    
    node = node.next
end

head = ListNode.new(1)
middle = ListNode.new(2)
last = ListNode.new 3
head.next = middle
middle.next = last

puts delete_node middle
puts "-------- after delete the list is #{head.inspect}"