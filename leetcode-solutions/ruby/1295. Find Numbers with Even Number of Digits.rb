#  https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

# @param {Integer[]} nums
# @return {Integer}
def find_numbers(nums)
  count = 0
  memo = {}
  
  nums.each do |n|
      
      if num_digit(n, memo).even?
          count += 1
      end
  end
  
  count
end

def num_digit(n, memo)
  return memo[n] if memo[n]
  nn = n
  count = 1
  
  while n > 9
      n = n / 10
      count += 1
  end
  
  memo[nn] = count
  count
end