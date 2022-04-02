# https://leetcode.com/problems/sum-of-beauty-in-the-array/

class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        right_min = [0] * len(nums)
        right_min[-1] = nums[-1]
        for i in range(len(nums) - 2, 0, -1):
            right_min[i] = min(nums[i], right_min[i+1])

        left_max = nums[0]
        total_beauty = 0
        for i in range(1, len(nums) - 1):
            num = nums[i]
            if num > left_max and num < right_min[i+1]:
                total_beauty += 2
            elif num > nums[i-1] and num < nums[i+1]:
                total_beauty += 1
            
            left_max = max(left_max, num)
            
        return total_beauty
