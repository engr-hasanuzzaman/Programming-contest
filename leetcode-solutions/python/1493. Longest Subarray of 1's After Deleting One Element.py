# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        size = len(nums)
        prefix_counter = [0] * size
        left, right = 0, size - 1
        cur_left_count = cur_right_count = 0
        one_count = 0
        while left < size:
            # precessing left to right
            if nums[left] == 1:
                one_count += 1
                cur_left_count += 1
            else:
                prefix_counter[left] += cur_left_count
                cur_left_count = 0
            left += 1
            
            # right to left
            if nums[right] == 1:
                cur_right_count += 1
            else:
                prefix_counter[right] += cur_right_count
                cur_right_count = 0
            right -= 1
            
        if one_count == size:
            return size - 1
        return max(prefix_counter)

# solution using sliding window technique
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        num_remove = 1
        left = 0
        max_size = 0
        cur_one_counter = 0
        one_counter = 0
        for i, n in enumerate(nums):
            if n == 1:
                cur_one_counter += 1
                one_counter += 1
            else:
                num_remove -= 1

            while num_remove < 0:
                if nums[left] == 0:
                    num_remove += 1
                else:
                    cur_one_counter -= 1
                left += 1
            
            max_size = max(max_size, cur_one_counter)

        if one_counter == len(nums):
            return len(nums) - 1
    
        return max_size