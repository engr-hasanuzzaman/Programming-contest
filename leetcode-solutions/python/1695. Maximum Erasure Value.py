# https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        left = right = 0
        max_sum = 0
        cur_sum = 0
        while right < len(nums):
            num = nums[right]
            counter[num] += 1
            cur_sum += num
            # print(num, cur_sum)
            if counter[num] > 1:
                # shrink the window size
                while counter[num] > 1:
                    counter[nums[left]] -= 1
                    cur_sum -= nums[left]
                    left += 1
            max_sum = max(max_sum, cur_sum)
            right += 1
        return max_sum
