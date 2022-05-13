# https://practice.geeksforgeeks.org/problems/rod-cutting0840/1/#

class Solution:
    def cutRod(self, price, n):
        P = len(price)
        dp = [0] * (n+1)

        for idx, p in enumerate(price):
            p_length = idx + 1
            for length in range(1, n+1):
                if length >= p_length:
                    dp[length] = max(dp[length], dp[length-p_length] + p)

        return dp[-1]
