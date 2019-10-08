# https://leetcode.com/problems/divide-two-integers/

# slow implementaion
# subtruct divisor and check remaining num is bigger than divisor
# @param {Integer} dividend
# @param {Integer} divisor
# @return {Integer}
def divide(dividend, divisor)
  if dividend > 0 && divisor > 0
      sign = true
  elsif dividend < 0 && divisor < 0
      sign = true
      dividend = -dividend
      divisor = -divisor
  elsif dividend < 0
      sign = false
      dividend = -dividend
  else
      sign = false
      divisor = -divisor
  end
  
  result = 0
  
  while dividend > divisor
      dividend -= divisor
      result += 1
  end
  
  sign ? result : -result
end

# faser approch: using bit manipulation
# @param {Integer} dividend
# @param {Integer} divisor
# @return {Integer}
def divide(dividend, divisor)
  sign = (dividend < 0) ^ (divisor < 0) ? -1 : 1
  dividend = dividend.abs
  divisor = divisor.abs
  temp = 0
  quotient = 0
  # 32 bit interger so, 0..31 2^
  31.downto(0) do |i|
      if (temp + (divisor << i)) <= dividend
          temp += (divisor << i)
          quotient |= 1 << i
      end
  end 
  
  (sign * quotient) > 2147483647 ? 2147483647 : (sign * quotient)
end