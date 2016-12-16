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
def reverse_list(head)
    list = []
    
    # take all value into list
    temp = head
    while(temp) do 
        list << temp.val
        temp = temp.next
    end
    
    # reverse list value and create new list and return
    if list.size <= 1
        return head
    else
        list.reverse!
        # creat new head note and preserve
        head = ListNode.new(list.first)
        
        # create temp node for furthuer node creation
        temp = head
        list.each_with_index do |val, i|
            next if i == 0
            
            # for first iteration temp, head are same
            # using temp.next we change inner value not ref
            temp.next = ListNode.new(val)
            temp = temp.next
        end
    end
    
    return head
end
