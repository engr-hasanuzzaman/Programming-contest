# @param {Integer} left
# @param {Integer} right
# @return {Integer[]}
def self_dividing_numbers(left, right)
  left.upto(right).select{ |n|  self_dividing?(n) }  
end

def self_dividing?(n)
    return true if n < 10
    num = n
    
    while(n != 0)
      last_digit = n % 10
      return false if last_digit.zero? || !(num % last_digit).zero?
      n /= 10 
    end
    
    true
end
