# https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        sum_with_exclusive_or = 0
        
        for i in range(len(nums)):
            sum_with_exclusive_or = sum_with_exclusive_or ^ nums[i]
        
        # so last set bit of sum_with_exclusive_or is the first bit which is diff for two numbers
        # get the last set bit
        last_set_bit = sum_with_exclusive_or & -sum_with_exclusive_or
        
        first_number = 0
        for i in range(len(nums)):
            if (nums[i] & last_set_bit) != 0:
                first_number ^= nums[i]
        return [first_number, sum_with_exclusive_or ^ first_number]
