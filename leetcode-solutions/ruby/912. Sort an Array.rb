# https://leetcode.com/problems/sort-an-array/

# @param {Integer[]} nums
# @return {Integer[]}
def sort_array(nums)
  nums.sort{|a,b| a <=> b}
end