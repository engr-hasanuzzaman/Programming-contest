# https://leetcode.com/problems/powx-n/

# solve using builtin function
# @param {Float} x
# @param {Integer} n
# @return {Float}
def my_pow(x, n)
  x**n
end

# alternative solution
# @param {Float} x
# @param {Integer} n
# @return {Float}
def my_pow(x, n)
  if n < 0
      n = n.abs
      x = 1 / x
  end
  
  ans = 1
  
  until n.zero?
      if n % 2 != 0
          ans = ans * x
      end
      
      n /= 2
      x *= x
  end
  
  ans
end

# 2**8 = (2 * 2) * (2 * 2) each etaration we are doubling our x and resetting n by 2