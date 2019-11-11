# https://leetcode.com/problems/move-zeroes/

# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
# two pointer solution, 
# start with both zero but one will increment everytime but other will
# only non zero found
def move_zeroes(nums)
  left = 0
  right = 0
  
  while right < nums.size
      if nums[right] != 0
          nums[left], nums[right] = nums[right], nums[left]
          left += 1
      end
      
      right += 1
  end
end