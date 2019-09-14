# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

require 'prime'
# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def count_prime_set_bits(l, r)
    sum = 0
    (l..r).each do |n|
        sum += 1 if Prime.prime?(count_set_bit(n))
    end
    
    sum
end

def count_set_bit(n)
    if n == 0
        return 0
    else
        1 + count_set_bit(n & (n -1))
    end
end
