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
def add_two_numbers(l1, l2)
    result = []
    num1, num2 = l1, l2
    list = nil
    remainder = 0
    
    while num1 || num2
        a, b = 0, 0
        
        if num1
            a = num1.val
            num1 = num1.next
        end
        
        if num2
            b = num2.val
            num2 = num2.next
        end
        sum = a + b + remainder
        
        if sum > 9
            sum %= 10
            remainder = 1
        else
            remainder = 0
        end
        
        result << sum
    end
    
    result << remainder if remainder != 0
    
    return nil if result.size < 0
    head = ListNode.new(result.first)
    list = head
    result.each_with_index do |n, i|
        next if i == 0
        
        list.next = ListNode.new(n)
        list = list.next
    end
    
    return head
    
end
