# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

# @param {Integer} n
# @return {Integer[]}
def sum_zero(n)
  ans = []
   n.times do |i|
       ans << i * 2 - n + 1
   end
   
   ans
end