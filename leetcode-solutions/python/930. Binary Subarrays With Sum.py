# https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = [0] * len(nums)
        cur_count = 0
        one_count = 0
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            if num == 0:
                cur_count +=1
            else:
                one_count
                cur_count = 0
            prefix_sum[i] = cur_count
        left = right = 0
        remNum = goal
        ans = 0
        if goal == 0:
            return sum(prefix_sum)
        while right < len(nums):
            num = nums[right]
            if num == 1:
                remNum -= 1
            
            # shirnk window size
            if remNum == 0:
                if right == len(nums) - 1:
                    ans += (prefix_sum[left] + 1)
                else:
                    ans += ((prefix_sum[left] + 1) * (prefix_sum[right+1] + 1))
                left += prefix_sum[left] + 1
                remNum += 1
            right += 1
        return ans
