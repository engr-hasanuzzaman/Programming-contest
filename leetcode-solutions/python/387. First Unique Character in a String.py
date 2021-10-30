# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        memo = {}
        for i, c in enumerate(s):
            if c in memo:
                memo[c] += 1
            else:
                memo[c] = 1
        for i, c in enumerate(s):
            if memo[c] == 1:
                return i
        return -1
