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

# Using Cyclic Replacements Algorithm
# rotate by k means every value will be shift by k 
# if current index is i then new index for ith value will be (k+i) % n where 
# n is num of element in array
# k rotate factor
def rotate(nums, k)
  # handle empty array     
  return nums if nums.size.zero?
  
  k = k % nums.size
  return nums if k.zero?
  count = 0 # indicate num of value rotated
  start = 0
  
  while count < nums.size
      current = start
      previous = nums[start]
      # replace (current+k)th interval value to correct postion
      loop do
          current = (k+current) % nums.size
          temp = nums[current]
          nums[current] = previous
          previous = temp
          count += 1 # keep tracking how many num has been replaced
          break if current == start # replaced all the values of this cycle
      end
      
      start += 1 
  end
end