# https://leetcode.com/problems/integer-break/

# @param {Integer} n
# @return {Integer}
# Try to to use as much as possible 3
def integer_break(n)
  return 1 if n == 2
  return 2 if n == 3
  product = 1
  
  while n > 4
      product *= 3
      n -= 3
  end
  
  product *= n
  product
end