# https://practice.geeksforgeeks.org/problems/edit-distance3702/1/#

# 
class Solution:
    def editDistance(self, s, t):
        S = len(s)
        T = len(t)
        dp = [[0] * (T+1) for _ in range(S+1)]
        # with empty string we need 1 step to make str with size 1, similarly 2,3,4..
        dp[0] = list(range(T+1))

        # first col initial value
        # with str size 1, to make empty we have to remove 1, similar from 2 -> 2, 3 -> 3 steps need
        for i in range(S+1):
            dp[i][0] = i

        # if cur char same, that means if we ignore both that will be result top left corner dp[i-1][j-1]
        # otherwise it will be min (of without one char) + 1
        for i in range(1, S+1):
            for j in range(1, T+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[-1][-1]
