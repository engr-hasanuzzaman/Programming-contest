# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def sort_colors(nums)
  count = [0, 0, 0]
  nums.each do |n|
      count[n] += 1
  end
  
  index = 0
  count.each_with_index do |num, color|
      num.times { nums[index] = color; index += 1 }
  end
  
  nums
end