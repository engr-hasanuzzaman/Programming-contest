# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
# @param {Integer} n
# @return {Integer}
def subtract_product_and_sum(n)
  digits = n_to_digits(n)
  product = 1
  sum = 0
  
  digits.each do |d|
      product *= d
      sum += d
  end
  
  product - sum
end

def n_to_digits(n)
  digits = []
  
  while n > 9
      digits << n % 10
      n = n / 10
  end
  
  digits << n
  digits
end