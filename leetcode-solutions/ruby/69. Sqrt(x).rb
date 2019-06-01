# https://leetcode.com/problems/sqrtx/

# @param {Integer} x
# @return {Integer}
def my_sqrt(x)
  return x if x <= 1
  
  left = 1
  right = x / 2
  
  while left <= right
      mid = (right + left) / 2
      temp = mid * mid
      
      if temp == x
          return mid
      elsif temp < x 
          left = mid + 1
      else
          right = mid - 1
      end
  end
  
  left - 1
end