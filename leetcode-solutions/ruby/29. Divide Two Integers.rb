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
