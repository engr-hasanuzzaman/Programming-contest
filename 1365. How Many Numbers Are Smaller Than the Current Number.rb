# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

# @param {Integer[]} nums
# @return {Integer[]}
def smaller_numbers_than_current(nums)
  s_nums = nums.sort
  l_uniq_count = 0
  c_map = {}
  s_nums.each_with_index do |n, i|
      if i == 0
          c_map[n] = l_uniq_count
      else
          if s_nums[i] == s_nums[i-1]
              c_map[n] = l_uniq_count
          else
              c_map[n] = i
              l_uniq_count = i
          end
      end
  end
  ans = []
  nums.each {|n| ans << c_map[n]}
  ans
end