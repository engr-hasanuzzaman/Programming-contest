# https://leetcode.com/problems/ugly-number-ii/

# @param {Integer} n
# @return {Integer}
def nth_ugly_number(n)
    ugly = [0] * n
    ugly[0] = 1
    idx2 = 0
    idx3 = 0
    idx5 = 0
    
    (1...n).each do |i|
        number = [ugly[idx2]*2, ugly[idx3]*3, ugly[idx5]*5].min
        ugly[i] = number

        # same number can be generated from multiple numbers so, we have to increment all
        idx2 += 1 if number == ugly[idx2]*2
        idx3 += 1 if number == ugly[idx3]*3
        idx5 += 1 if number == ugly[idx5]*5
    end

    ugly[-1]
end
