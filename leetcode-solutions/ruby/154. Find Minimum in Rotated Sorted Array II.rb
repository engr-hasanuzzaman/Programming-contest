# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

# @param {Integer[]} nums
# @return {Integer}
def find_min(nums)
  left = 0
  right = nums.size - 1
  
  while left < right
      mid = (left + right) / 2
      
      if nums[mid] > nums[right]
          left = mid + 1
      elsif nums[mid] < nums[right]
          right = mid
      else
          # when nums[mid] == nums[right] 
          # not sure on which part contain smallest val
          # [3,3,1,3] & [1,3,3]
          right -= 1
      end
  end
  
  nums[left]
end