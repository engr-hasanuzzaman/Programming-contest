# https://leetcode.com/problems/contains-duplicate-iii/

# TLE solution with complexity N*K where N is the size of array
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums) and j <= i+k:
                if abs(nums[j] - nums[i]) <= t:
                           return True
                j += 1
        return False
