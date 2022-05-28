class Solution:
    def reverse(self, head, k):
        if not head or not head.next or k == 0:
            return head

        cur = head
        num = 1
        prev = None
        while num <= k and cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            num += 1

        head.next = self.reverse(cur, k)
        return prev
