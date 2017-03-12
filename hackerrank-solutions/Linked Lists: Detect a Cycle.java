/*
Detect a cycle in a linked list. Note that the head pointer may be 'null' if the list is empty.
A Node is defined as: 
*/

class Node {
    int data;
    Node next;
}

boolean hasCycle(Node head) {
    if(head == null)
        return false;
        
    Node hare = head;
    Node tortoise = head;
    
    while(true){        
        if(hare.next != null){
            hare = hare.next.next;
        }else{
            return false;
        }
        
        tortoise = tortoise.next;
        
        if(hare == null || tortoise == null){
            return false;
        }
        
        if(hare == tortoise){
            return true;
        }
    }
}
