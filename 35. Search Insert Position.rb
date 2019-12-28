# https://leetcode.com/problems/search-insert-position/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def search_insert(nums, target)
  low = 0
  high = nums.size - 1
  
  if target > nums.last
      return nums.size
  elsif target < nums.first
      return 0
  end
  
  while low < high
      mid = (low + high) / 2
      
      if nums[mid] == target
          return mid
      elsif nums[mid] > target
          high = mid
      else
          low = mid + 1
      end
  end
  
  low
end