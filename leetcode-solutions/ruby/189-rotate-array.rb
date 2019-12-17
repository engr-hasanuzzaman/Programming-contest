# @param {Integer[]} nums
# @param {Integer} k
# @return {Void} Do not return anything, modify nums in-place instead.
def rotate(nums, k)
    # return if nums has only one value or actual rotation is zero
    return nums if nums.size < 1 || (k % nums.size) == 0
    
    actual_rotation = k % nums.size
    
    # use ruby array rotate method that defaultly rotate left
    nums.rotate!(-actual_rotation)
end

# rotate using extra array without builtin method
# @param {Integer[]} nums
# @param {Integer} k
# @return {Void} Do not return anything, modify nums in-place instead.
def rotate(nums, k)
  return nums if k % nums.size == 0
  
  # create new array and fill with result array element
  temp_a = []
  nums.each_with_index do |n, i|
      temp_a[(i+k)%nums.size] = nums[i]
  end
  
  # fill answer array with new values
  nums.size.times do |i|
      nums[i] = temp_a[i]
  end
end