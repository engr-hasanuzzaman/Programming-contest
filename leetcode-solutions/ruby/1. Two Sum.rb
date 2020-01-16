# https://leetcode.com/problems/two-sum/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
  n_map = {}
  nums.each_with_index {|n, i| n_map[n] = i }
  
  nums.each_with_index do |n, i|
      rem = target - n
      return [i, n_map[rem]] if n_map[rem] && n_map[rem] != i
  end
end