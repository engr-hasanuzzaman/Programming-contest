# https://leetcode.com/problems/maximum-sum-circular-subarray/
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def max_sum_linear(nums):
            total_max = max_so_far = nums[-1]
            for i in range(len(nums) - 2, -1, -1):
                max_so_far = max(nums[i], max_so_far + nums[i])
                total_max = max(total_max, max_so_far)
            return total_max
            
        # max contigious sum without circle
        max_total_linear = max_sum_linear(nums)
        
        # max sum with circle = array_sum - abs(min_sum)
        # to find the min_sum we will rever the array element sign and apply kanades algorithm
        array_sum = 0
        for i in range(len(nums)):
            array_sum += nums[i]
            nums[i] = -nums[i]
            
        # here we are using + sing, we are inverting the element 
        # so array_max - (mix_sum) -> array_sum - (- max_sum_with_invert_sign) -> array_sum + max_sum_with_inver_sign
        min_sum_with_rev_sign = max_sum_linear(nums)
        # if all the number are negetive, then max_total_linear is the answer
        if abs(array_sum) == min_sum_with_rev_sign:
            return max_total_linear
        else:
            return max(min_sum_with_rev_sign + array_sum, max_total_linear)
        
