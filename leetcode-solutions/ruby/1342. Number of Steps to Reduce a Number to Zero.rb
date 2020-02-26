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
