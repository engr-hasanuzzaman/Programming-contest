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

# with lineratime and without extra space
=begin
a) XOR of a number with itself is 0.
b) XOR of a number with 0 is number itself.
c) XOR is associative and commutative
res = 7 ^ 3 ^ 5 ^ 4 ^ 5 ^ 3 ^ 4 => 7 ^ (3 ^ 3) ^ (4 ^ 4) ^ (5 ^ 5)  
=end
rescue => exception
    
end
def single_number(nums)
    res = nums.first
    nums[1..-1].each do |n|
        res ^= n
    end
    
    res
end