def has_cycle(head):
    if head == None or head.next == None:
        return 0
    
    slow = head
    fast = head.next
    while fast:
        if slow == fast:
            return 1
        fast = fast.next
        fast = fast.next if fast != None else None
        slow = slow.next
    return 0