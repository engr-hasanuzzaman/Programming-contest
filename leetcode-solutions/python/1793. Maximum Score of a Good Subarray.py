# https://leetcode.com/problems/maximum-score-of-a-good-subarray/
# Similar to histogra area calculation problem

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        stack = []
        max_sum = 0
        n = len(nums)
        i = 0
        while i < n:
            while stack and stack[-1][1] > nums[i]:
                idx, num = stack.pop()
                if stack and stack[-1][0] < k and i > k:
                    max_sum = max(max_sum, (i - stack[-1][0] - 1) * num)
                elif not stack and i > k:
                    max_sum = max(max_sum, i * num)

            stack.append((i, nums[i]))
            i += 1

        while stack:
            idx, num = stack.pop()
            if stack and stack[-1][0] < k:
                max_sum = max(max_sum, (i - stack[-1][0] - 1) * num)
            elif not stack:
                max_sum = max(max_sum, i * num)
        return max_sum
