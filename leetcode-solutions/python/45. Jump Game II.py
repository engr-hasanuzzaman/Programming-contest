# https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        max_reach = 0
        left = 0
        right = 0
        
        while right < len(nums) - 1:
            for index in range(left, right + 1):
                max_reach = max(max_reach, index + nums[index])
            left = right + 1
            right = max_reach
            count += 1
        return count
