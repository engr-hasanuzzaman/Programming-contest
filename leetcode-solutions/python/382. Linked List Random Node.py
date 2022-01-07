# https://leetcode.com/problems/linked-list-random-node/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.list = []
        cur = head
        while cur:
            self.list.append(cur.val)
            cur = cur.next

    def getRandom(self) -> int:
        pick = int(random.random() * len(self.list))
        return self.list[pick]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
