# https://leetcode.com/problems/get-equal-substrings-within-budget/
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs = [0] * len(s)
        for i in range(len(s)):
            costs[i] = abs(ord(s[i]) - ord(t[i]))
        
        left = right = 0
        remCost = maxCost
        ans = 0
        while right < len(s):
            remCost -= costs[right]
            #over spend
            if remCost < 0:
                while remCost < 0:
                    remCost += costs[left]
                    left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans
    