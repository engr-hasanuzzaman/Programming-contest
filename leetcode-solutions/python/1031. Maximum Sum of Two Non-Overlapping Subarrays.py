# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix_sum = []
        cur_total = 0
        for n in nums:
            cur_total += n
            prefix_sum.append(cur_total)
        
        left = 0
        right = firstLen - 1
        ans = 0
        memo = {}
        while right < len(nums):
            first_total = self.get_max(firstLen, left, right, prefix_sum, memo)
            second_max_total = max(
                self.get_max(secondLen, 0, left - 1, prefix_sum, memo),
                self.get_max(secondLen, right+1, len(prefix_sum) - 1, prefix_sum, memo)
            )
            ans = max(ans, first_total + second_max_total)
            left += 1
            right += 1
        
        return ans
    # cal max_sum with gived size
    def get_max(self, size, left, right, prefix_sum, memo):
        if left < 0 or right >= len(prefix_sum):
            return 0
        key = str(size) + "_" + str(left) + "_" + str(right)
        if key in memo:
            return memo[key]
        start = left
        end = start + size - 1
        cur_sum = 0
        while end <= right:
            if start > 0:
                cur_sum = max(cur_sum, prefix_sum[end] - prefix_sum[start-1])
            else:
                cur_sum = prefix_sum[end]
            start += 1
            end += 1
        memo[key] = cur_sum
        return cur_sum