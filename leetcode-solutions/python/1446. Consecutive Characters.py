# https://leetcode.com/problems/consecutive-characters/

class Solution:
    def maxPower(self, s: str) -> int:
        max_power = 0
        cur_power = 0
        prev = s[0]
        for i in range(len(s)):
            if s[i] == prev:
                cur_power += 1
                max_power = max(max_power, cur_power)
            else:
                prev = s[i]
                cur_power = 1
        return max(max_power, max_power)
