# https://leetcode.com/problems/rotate-list/
def rotate_right(head, k)
    list_length = 0
    temp = head
    
    # find the length of linked list
    while temp do
        temp = temp.next
        list_length += 1
    end
    
    # if only one valu no need to rotate
    return head if k == 0 || list_length < 2
    
    rotate = k % list_length
        
    return head if rotate == 0
    
    # fid kth element that will be last value of new list  
    kth_node = temp = head 
    counter = list_length - rotate
    
    (counter - 1).times do |i|
        kth_node = kth_node.next
    end
    
    #  head contain tail and hew_head contain new head part
    new_head = kth_node.next

    # make tail for new link, so now head contain tailing part and new_head contain head part
    kth_node.next = nil
    temp = new_head 
    
    # find place where we will keep tail part   
    while(temp.next) do
        temp = temp.next
    end    
    
    # temp->next will contain taining part
    temp.next = head
    
    return new_head
end
