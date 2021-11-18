# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, ns: List[int]) -> int:
        if len(ns) <= 3:
            return max(ns)

        def linear_rob(nums):
            dp = [nums[0]]
            for i in range(1, len(nums)):
                if i == 1:
                    dp.append(max(nums[i], dp[i - 1]))
                    continue
                dp.append(max(nums[i] + dp[i - 2], dp[i - 1]))
            return dp[-1]
        # pick first one or skip
        # if pick first one, have to skip last one
        # without first one, with first one
        return max(linear_rob(ns[1:]), linear_rob(ns[:-1]))
