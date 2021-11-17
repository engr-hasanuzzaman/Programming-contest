# https://leetcode.com/problems/climbing-stairs/

# since we can go one or two steps at a time, we can reach to nth from eight n - 1 or n - 2
# so distinct ways to reach n = distinct ways to reach  n - 1 + distinct ways to reach n - 2
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2, 3]
        
        for i in range(4, n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]
