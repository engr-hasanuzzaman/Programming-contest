# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# @param {Integer[]} nums
# @return {Integer}
def find_min(nums)
  left = 0
  right = nums.size - 1
  
  while left < right
      mid = (left + right) / 2
      if nums[mid] > nums[right]
          left = mid + 1
      else
          right = mid
      end
  end
  
  nums[left]
end