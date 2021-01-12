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