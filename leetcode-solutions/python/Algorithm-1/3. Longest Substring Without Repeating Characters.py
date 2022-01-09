# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = deque([])
        memo = {}
        max_size = 0
        for _, c in enumerate(s):
            if memo.get(c, 0) > 0:
                # remove chars till duplicate
                while True:
                    temp = q.popleft()
                    memo[temp] -= 1
                    if temp == c:
                        break
                # insert new char
                memo[c] = 1
                q.append(c)
            else:
                memo[c] = 1
                q.append(c)
                max_size = max(max_size, len(q))
        return max_size
