# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        max_sum = total = nums[-1]
        
        for i in range(size - 2, -1, -1):
            total = max(total + nums[i], nums[i])
            max_sum = max(total, max_sum)
        
        return max_sum
