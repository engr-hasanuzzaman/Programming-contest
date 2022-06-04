# https://practice.geeksforgeeks.org/problems/subset-sum-problem2014/1/

class Solution:
    def equalPartition(self, N, arr):
        total = sum(arr)
        if total % 2 == 1:
            return False

        half = total // 2
        dp = [False] * (half + 1)
        dp[0] = True

        for num in arr:
            # high to low to ensure, num is being used only one time
            for target in range(half, num - 1, -1):
                if num > half:
                    continue

                if dp[target - num]:
                    dp[target] = True

        return dp[half]
