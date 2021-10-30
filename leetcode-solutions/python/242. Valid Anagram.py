# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        memo = {}
        for i in range(len(s)):
            if s[i] not in memo:
                memo[s[i]] = 1
            else:
                memo[s[i]] += 1
            
            if t[i] not in memo:
                memo[t[i]] = -1
            else:
                memo[t[i]] -= 1

        for k, v in memo.items():
            if v != 0:
                return False

        return True