# https://leetcode.com/problems/array-partition-i/

# @param {Integer[]} nums
# @return {Integer}
def array_pair_sum(nums)
  nums.sort!
  n = (nums.size / 2)
  n_size = nums.size - 1
  sum = 0
  i = 0
  while i <= n_size
      sum += [nums[n_size-i], nums[n_size-i-1]].min
      i += 2
  end
  
  sum
end