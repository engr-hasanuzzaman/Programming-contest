# https://leetcode.com/problems/single-number/

# using bit manipulation
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            ans ^= n
        return ans
