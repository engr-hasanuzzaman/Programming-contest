# https://leetcode.com/problems/single-element-in-a-sorted-array/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = (high - low) // 2 + low
            # is index is odd that should be last item of the pair 
            # otherwise next item should be the last item of the pair
            # if index is odd, it has previous and next value as last index must be ever
            if mid % 2 == 1:
                if nums[mid - 1] != nums[mid] and nums[mid + 1] != nums[mid]:
                    # no element on the either size, means this is uniq number
                    return nums[mid]
                elif nums[mid - 1] != nums[mid]:
                    # targe is on the left size of the part including 
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if mid == len(nums) - 1:
                    return nums[mid]
                elif nums[mid + 1] != nums[mid]:
                    # mid could be the unique number
                    high = mid
                else:
                    low = mid + 1

        return nums[high]
     