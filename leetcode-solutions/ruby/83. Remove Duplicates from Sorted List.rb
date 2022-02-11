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

# diff solution
def delete_duplicates(head)
    prev = nil
    cur = head
    while cur
        if prev && prev.val == cur.val
            # remove all the duplicate
            while cur && cur.val == prev.val
                cur = cur.next
            end
            prev.next = cur
            prev = cur
            # if cur is nil
            cur = cur.next if cur
        else
            prev = cur
            cur = cur.next
        end
    end
    
    head
end