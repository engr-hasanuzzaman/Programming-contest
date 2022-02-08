# https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans.insert(index[i], nums[i])
        return ans[:len(nums)]
