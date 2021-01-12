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