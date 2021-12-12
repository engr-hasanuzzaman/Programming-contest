# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        ans_digit = sorted(nums)[-k:]
        memo = {}
        for _, n in enumerate(ans_digit):
            if n in memo:
                memo[n] += 1
            else:
                memo[n] = 1
        ans = []
        for _, n in enumerate(nums):
            if memo.get(n, 0) >= 1:
                ans.append(n)
                memo[n] -= 1
        return ans
