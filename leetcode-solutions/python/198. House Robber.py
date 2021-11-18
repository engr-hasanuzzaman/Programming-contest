# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        last = len(nums) - 1
        
        # taking 2 extra element so that we can access i, i+1, i+2 as max profit for ith house will be
        # max(nums[i] + profit[i+1], profit[i+1])
        profit = [0] * (last + 3)
        
        for i in range(last, -1, -1):
            # max between pick ith house or not
            # if we pick we will be able to pick (i+1) max profit also 
            profit[i] = max(nums[i] + profit[i+2], profit[i+1])

        return profit[0]
