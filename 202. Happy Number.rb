# https://leetcode.com/problems/happy-number/

# @param {Integer} n
# @return {Boolean}
def is_happy(n)
  hear = sqr(n)
  tortoise = sqr(sqr(n))
  
  while hear != 1 || tortoise != 1
      if hear == tortoise
          return false
      end
      
      hear = sqr(hear)
      tortoise = sqr(sqr(tortoise))
  end
  
  true
end

def sqr(n)
  sum = 0
  n.to_s.each_char do |num|
      sum += (num.to_i * num.to_i)
  end
  
  sum
end