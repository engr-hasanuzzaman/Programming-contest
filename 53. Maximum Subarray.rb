# https://leetcode.com/problems/maximum-subarray/

# @param {Integer[]} nums
# @return {Integer}
def max_sub_array(nums)
  s_a = Array.new(nums.size+1){0}
  
  # calculate max sonsicutive sum from last num to first
  (nums.size - 1).downto(0) do |i|
      if s_a[i+1] + nums[i] > nums[i]
          s_a[i] = s_a[i+1] + nums[i]
      else
          s_a[i] = nums[i]
      end
  end
  
  s_a[0...-1].max
end