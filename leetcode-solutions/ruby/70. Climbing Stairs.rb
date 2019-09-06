# https://leetcode.com/problems/climbing-stairs/

# @param {Integer} n
# @return {Integer}
#fibonacci series
def climb_stairs(n)
  return n if n == 1 || n == 2 || n == 3
  result = 0
  n1 = 2
  n2 = 3
  
  (n-3).times do
      result = n1 + n2
      n1, n2 = n2, result
  end
  
  result
end