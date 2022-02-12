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

# updated solution 
def reverse_list(head)
    last_node = nil
    node = head
    while node
        nn = node.next
        node.next = last_node
        last_node = node
        node = nn
    end
    
    last_node
end

# recursive solution
# updated recursive solution
# we do not need to return for reversing list
# if current node is head that means we hant to make head.next or
# current head so, head.next.next = head will reverser node order
# we are returning node only to return head node
def reverse_list(head)
    return head unless head && head.next
    # this will always contain new head
    nn = reverse_list(head.next)
    head.next.next = head
    head.next = nil
    nn
end

# using stack
def reverse_list(head)
    return head unless head
    
    stack = []
    cur = head
    while cur
        stack.push(cur)
        cur = cur.next
    end

    new_head = cur = stack.pop
    until stack.empty?
        cur.next = stack.pop
        cur = cur.next
    end

    cur.next = nil
    new_head
end