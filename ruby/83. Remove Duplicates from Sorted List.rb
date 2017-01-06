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
def delete_duplicates(head)
    current_node = head
    previous_node = nil
    
    while(current_node && current_node.next)
        # remove next node if current val and next value is equal
        if current_node.val == current_node.next.val
            current_node.next = current_node.next.next
        else
            current_node = current_node.next  
        end
        
    end
    
    return head
end
