# https://practice.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1/?page=1&difficulty[]=1&status[]=unsolved&company[]=Amazon&sortBy=submissions#

def intersetPoint(head1, head2):
    # code here
    cur1, cur2 = head1, head2
    while cur1 and cur2:
        if cur1 == cur2:
            break

        cur1 = cur1.next
        cur2 = cur2.next

        if not cur1:
            cur1 = head2

        if not cur2:
            cur2 = head1

    return cur1.data if cur1 else -1
