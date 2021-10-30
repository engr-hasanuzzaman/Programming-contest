# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        memo = {}
        for i, c in enumerate(magazine):
            if c in memo:
                memo[c] += 1
            else:
                memo[c] = 1

        for i, c in enumerate(ransomNote):
            if c not in memo or memo[c] == 0:
                return False
            memo[c] -= 1
        return True
                