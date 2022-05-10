# https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1/#

# User function Template for python3

class Solution:

    # Function to return max value that can be put in knapsack of capacity W.
    # calculate max price taking 1...w weight considering all the available weights
    def knapSack(self, W, wt, val, n):
        dp = [0] * (W + 1)
        for idx, w in enumerate(wt):
            temp = [0]
            for target in range(1, W+1):
                if w > target:
                    temp.append(dp[target])
                else:
                    # max(previous max, sum of value of current weight + value of the rest weight)
                    temp.append(max(dp[target], val[idx] + dp[target - w]))
            dp = temp
        return dp[-1]
