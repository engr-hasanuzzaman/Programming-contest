// https://leetcode.com/problems/linked-list-cycle/

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func hasCycle(head *ListNode) bool {
	slow, fast := head, head
	
	for ; fast != nil; {
			slow = slow.Next
			if fast.Next != nil {
					fast = fast.Next.Next    
			}else {
					return false
			}
			
			if slow == fast {
					return true
			}
			// fmt.Println(fast)
	}
	
	return false
}
