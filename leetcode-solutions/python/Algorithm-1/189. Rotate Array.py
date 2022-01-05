# https://leetcode.com/problems/rotate-array/

# solution 1: without using builtin language feature and extra space
# steps: rotate i + k, i + 2k ...i + nk for i = 0, 1, 2 .... len(s) and track the swap count
# untill all the elements are on the correct positions
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        k = k % size
        if k == 0:
            return
        count = 0
        start = 0
        while count < len(nums):
            current = start
            prev = nums[current]
            while True:
                current = (current + k) % size
                temp = nums[current]
                nums[current] = prev
                prev = temp
                count += 1
                if current == start:
                    break
            start += 1
            
        