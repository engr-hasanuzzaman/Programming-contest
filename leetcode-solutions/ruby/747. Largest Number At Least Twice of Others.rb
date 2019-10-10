# https://leetcode.com/problems/largest-number-at-least-twice-of-others/

# @param {Integer[]} nums
# @return {Integer}
def dominant_index(nums)
  large = -1 
  large_i = 0
  i_large = -1
  
  nums.each_with_index do |n, i|
      if n > large
          i_large = large
          large = n
          large_i = i
      elsif n > i_large
          i_large = n
      end
  end
  
  large >= i_large * 2 ? large_i : -1
end