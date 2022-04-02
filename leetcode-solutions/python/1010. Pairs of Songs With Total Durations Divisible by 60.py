# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        memo = {}
        for t in time:
            normalized_time =  t % 60
            rem = 60 - normalized_time

            if normalized_time == 0:
                rem = 0
            ans += memo.get(rem, 0)
            
            if normalized_time in memo:
                memo[normalized_time] += 1
            else:
                memo[normalized_time] = 1
                
        return ans
    