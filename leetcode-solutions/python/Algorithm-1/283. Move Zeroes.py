# https://leetcode.com/problems/move-zeroes/
# using 2 pointers
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, current, size = 0, 0, len(nums)
        while current < size:
            if nums[current] != 0:
                nums[start], nums[current] = nums[current], nums[start]
                start += 1
                current += 1
            else:
                current += 1