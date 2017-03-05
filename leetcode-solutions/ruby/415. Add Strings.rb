# @param {String} num1
# @param {String} num2
# @return {String}
def add_strings(num1, num2)
    # make sure num1 alway contain bigger array
    num1, num2 = num2, num1 if num1.size < num2.size
    
    result = []
    remainder = 0
    
    # convert string to array
    num1 = num1.split('')
    num2 = num2.split('')
    
    while(num1.size > 0) do
        
        sum = num1.delete_at(-1).to_i + (num2.delete_at(-1) || 0).to_i + remainder
        
        if sum > 9
            result.unshift sum % 10
            remainder = 1
        else
            result.unshift(sum)
            remainder = 0
        end
    end
    
    result.unshift(remainder) if remainder == 1
    return result.join('')
end
