# @param {String} a
# @param {String} b
# @return {String}
def add_binary(a, b)
    if a.size.zero? && b.size.zero?
        return '0' 
    end
    
    if a.size.zero? || b.size.zero?
        return a + b
    end 
    
    a = a.chars
    b = b.chars
    result = []
    remainder = 0
    max_len = a.size > b.size ? a.size : b.size
    
    max_len.times do
        num1 = (a.pop || 0).to_i
        num2 = (b.pop || 0).to_i
        sum = num1 ^ num2 ^ remainder
        # puts "--- num1 #{num1}, num2 #{num2}, remainder #{remainder}"
        if (num1 == 1 && num2 == 1) || (num1 == 1 && remainder == 1) || (remainder == 1 && num2 == 1)
            remainder = 1
        else
            remainder = 0
        end
        # puts "--- num1 #{num1}, num2 #{num2}, remainder #{remainder}"
        result.unshift sum
    end
    
    result.unshift remainder if remainder == 1
    return result.join('')    
end
