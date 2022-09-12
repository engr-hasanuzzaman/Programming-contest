def getNthFromLast(head, n):
    cur = head
    ans = head
    while n > 0 and cur:
        cur = cur.next
        n -= 1

    if n > 0:
        return -1

    while cur:
        ans = ans.next
        cur = cur.next

    return ans.data
