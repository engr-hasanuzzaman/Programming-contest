# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def search_range(nums, target)
  f_i = find_index(nums, target)
  
  if f_i == nums.size || nums[f_i] != target
      return [-1,-1]
  end
  
  [f_i, find_index(nums, target, false) - 1]
end

def find_index(nums, target, left = true)
  l = 0
  r = nums.size
  
  while l < r
      mid = (l + r) / 2
      
      if target < nums[mid] || (left && nums[mid] == target)
          r = mid
      else
          l = mid + 1
      end
  end
  
  l
end