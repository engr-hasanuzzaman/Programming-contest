# https://leetcode.com/problems/binary-search/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def search(nums, target)
  return -1 if nums.size.zero?
  left = 0
  right = nums.size - 1
  
  while right >= left
      mid = (left + right) / 2
      
      if nums[mid] == target
          return mid
      elsif target > nums[mid]
          left = mid + 1
      else
          right = mid - 1
      end
  end

  -1
end