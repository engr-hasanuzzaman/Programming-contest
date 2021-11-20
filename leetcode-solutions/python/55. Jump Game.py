# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_possible_steps = 0
        last_step = len(nums) - 1
        i = 0
        while i <= max_possible_steps:
            step = nums[i]
            max_possible_steps = max(i + step, max_possible_steps)
            if max_possible_steps >= last_step:
                return True
            i += 1
        return False
