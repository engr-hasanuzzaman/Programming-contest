# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        last_sum = 0
        ans = []
        for i in range(len(nums)):
            ans.append(last_sum + nums[i])
            last_sum = last_sum + nums[i]
        return ans
