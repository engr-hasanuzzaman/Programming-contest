# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, n in enumerate(nums):
            rem = target - nums[i]
            if rem in memo:
                return [memo[rem], i]
            memo[n] = i
        return []
        
        