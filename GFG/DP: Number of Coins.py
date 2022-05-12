class Solution:
    def minCoins(self, coins, M, V):
        dp = [float('inf')] * (V+1)
        dp[0] = 0

        for coin in coins:
            for amount in range(1, V+1):
                if amount >= coin:
                    rem = amount - coin
                    dp[amount] = min(dp[rem] + 1, dp[amount])

        return -1 if dp[-1] == float('inf') else dp[-1]
