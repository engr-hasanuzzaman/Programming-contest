# https://leetcode.com/problems/partition-array-into-disjoint-intervals/

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        min_to_right = [0] * len(nums)
        index = len(nums) - 2
        min_to_right[-1] = nums[-1]

        while index >= 0:
            num = nums[index]
            min_to_right[index] = min(num, min_to_right[index+1])
            index -= 1
        max_num = 0
        for i in range(len(nums)):
            max_num = max(max_num, nums[i])
            
            if max_num <= min_to_right[i+1]:
                return i + 1
