# this solution will not work for all the coins 
# ex. 9, 6, 5, 1 and for 11 it will return 3: 9 + 1 + 1 but optimal one is 2: 5 + 6
# for general solution we have to compute all the possible solution and pick optimal one
class Solution:
    def minPartition(self, N):
        coins = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
        ans = []
        i = 0
        while N > 0:
            if N >= coins[i]:
                ans += [coins[i]] *  (N // coins[i])
                N = N % coins[i]
            i += 1
        return ans

# general solution to find the min coins to make provided amount using DP
class Solution:
    def minCoins(self, coins, M, V):
        # initialize number of combination with the max possible number
        dp = [10000001] * (V+1)
        # to make 0 we need 0 number of coin
        dp[0] = 0
        # for each coin, calculate min number of coin needed for 1-Amount
        # min number of coin is min[current_number_of_coin, num_of_coin_needed for amount-coint]]
        for coin in coins:
            for amount in range(1, V+1):
                if amount >= coin:
                    dp[amount] = min(dp[amount], dp[amount-coin] + 1)
        if dp[V] == 10000001:
            return -1
        return dp[V]
