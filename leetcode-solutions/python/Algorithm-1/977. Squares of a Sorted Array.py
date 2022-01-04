# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        k = j
        ans = [0] * (j + 1)
        
        while i <= j:
            if nums[j] ** 2 >= nums[i] ** 2:
                ans[k] = nums[j] ** 2
                j -= 1
            else:
                ans[k] = nums[i] ** 2
                i += 1
            k -= 1
        return ans
