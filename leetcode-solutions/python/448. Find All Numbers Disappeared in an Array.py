# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums) + 1):
            
            pos = nums[i - 1] - 1
            # already visited             
            if nums[pos] == -1:
                continue
            
            while pos >= 0:
                new_pos = nums[pos] - 1
                nums[pos] = -1
                pos = new_pos
        ans = []

        # position which were not marked as -1, was missing
        for i in range(len(nums)):
            if nums[i] != -1:
                ans.append(i + 1)
        return ans
