# https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1/#

# recurrent relation
# dp[0] = True as we can create sum 0 always
# if num > target (ex. not possible make 2 with > 2) dp[i][j] = dp[i-1][j] // temp[j] = dp[j]
# else temp[j] = dp[j] or dp[j-n]
class Solution:
    def isSubsetSum(self, N, arr, sum):
        dp = [False] * (sum + 1)
        dp[0] = True

        for i in range(1, N+1):
            n = arr[i-1]
            temp = [True]
            for j in range(1, sum+1):
                if n > j:
                    temp.append(dp[j])
                else:
                    temp.append(dp[j] or dp[j - n])
            dp = temp
        return dp[-1]
