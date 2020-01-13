# https://leetcode.com/problems/single-number/

# @param {Integer[]} nums
# @return {Integer}
def single_number(nums)
  s_map = {}
  
  nums.each do |n|
      if s_map[n]
          s_map.delete(n)
      else
          s_map[n] = n
      end
  end
  
  s_map.first.last
end