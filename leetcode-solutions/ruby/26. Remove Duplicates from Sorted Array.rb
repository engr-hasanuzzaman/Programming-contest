# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# @param {Integer[]} nums
# @return {Integer}
def remove_duplicates(nums)
  return 0 if nums.size.zero?
  
  # left last placement value
  left = 0
  right = 1
  
  while right < nums.size
      # check current value with last placement value
      if nums[right] != nums[left]
          # place next to last placement
          left += 1
          nums[left] = nums[right]
      end
      
      right += 1
  end
  
  left  + 1
end