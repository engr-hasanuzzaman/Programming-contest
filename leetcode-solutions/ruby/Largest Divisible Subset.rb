# https://leetcode.com/problems/largest-divisible-subset/

# @param {Integer[]} nums
# @return {Integer[]}
def largest_divisible_subset(nums)
  return nums if nums.size.zero?
  
  nums = nums.sort
  result = []
  nums.each {|n| result << [n]}
  for i in 0...nums.size
      for j in 0...i
          if nums[i] % nums[j] == 0 && result[i].size < result[j].size + 1
              result[i] = result[j] + [nums[i]]
          end
      end
  end
  result.sort_by{|a| a.size}.last
end