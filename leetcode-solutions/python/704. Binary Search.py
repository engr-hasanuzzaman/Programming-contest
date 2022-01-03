# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums) - 1
        
        while s <= e:
            mid = (e - s) // 2 + s
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                e = mid - 1
            else:
                s = mid + 1
        return -1
