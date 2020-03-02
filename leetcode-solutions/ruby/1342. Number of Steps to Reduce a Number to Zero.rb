# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

# @param {Integer} num
# @return {Integer}
def number_of_steps (num)
  count = 0
  
  while num > 0
      if num % 2 == 0
          num /= 2
      else
          num -= 1
      end
      
      count += 1
  end
  
  count
end

# ----------- solve problem using bit manupulation ------

# @param {Integer} num
# @return {Integer}
# if bit is 1 then we need to sub 1 then div so need 2 step otherwith one step
# except leftmost 1 that only need one step substruct
def number_of_steps (num)
  return num if num <= 1
  
  count = -1
  b_str = num.to_s(2)
  
  b_str.each_char do |b|
      count += b == '0' ? 1 : 2
  end
  
  count
end