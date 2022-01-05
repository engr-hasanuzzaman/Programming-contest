# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right, size = 0, 0, len(nums)
        while right < size:
            if nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
            else:
                right += 1
        return left
