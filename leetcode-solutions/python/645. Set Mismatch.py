# https://leetcode.com/problems/set-mismatch/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d_num = 0
        sum_without_dup = 0
        size = len(nums)
        for i, n in enumerate(nums):
            if n < 0:
                n = abs(n)
            # alredy visited number n             
            if nums[n-1] < 0:
                d_num = n
            else:
                sum_without_dup += n
                nums[n-1] = -nums[n-1]
        nth_sum = (size * (size + 1)) // 2
        return [d_num, nth_sum - sum_without_dup]
