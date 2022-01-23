# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 2):
            if self.uniq(s[i:i+3]):
                count += 1
        return count
            
    def uniq(self, s):
        memo = {}
        for _, char in enumerate(s):
            if char in memo:
                return False
            
            memo[char] = True
        return True
