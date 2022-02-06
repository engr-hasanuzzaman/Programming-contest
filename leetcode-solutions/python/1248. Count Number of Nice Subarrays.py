# https://leetcode.com/problems/count-number-of-nice-subarrays/
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = right = 0
        count = 0
        prfix_counter = [0] * len(nums)
        cur_count = 0
        # keep the information of how many consecutive even number has
        for i in range(len(nums)-1, -1, -1):
            if nums[i] % 2 == 1:
                cur_count = 0
            else:
                cur_count += 1
            prfix_counter[i] = cur_count

        while right < len(nums):
            if nums[right] % 2 == 1:
                k -= 1
            # shirk the window
            if k == 0:
                if right == len(nums) - 1:
                    count += (prfix_counter[left] + 1)
                else:
                    count += ((prfix_counter[left] + 1) * (prfix_counter[right+1] + 1))
                # move left to after first odd number
                left += (prfix_counter[left] + 1)
                k += 1
            right += 1
        return count
                    