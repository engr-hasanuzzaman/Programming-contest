# https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        i, j = 0, n
        while j < len(nums):
            ans.append(nums[i])
            ans.append(nums[j])
            i += 1
            j += 1
        return ans
