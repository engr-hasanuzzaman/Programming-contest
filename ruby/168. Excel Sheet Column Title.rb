# @param {Integer} n
# @return {String}
# we are here converting base 26 number to 10 number 
# since here there is no char for 0 and if number is multiple of 26 then 
# zero means Z and we will - 1 with new value after n /= base
def convert_to_title(n)
    return '' if n <= 0
    
    char_base = 64
    base = 26
    result = []
    
    while(n > 26)
        remainder = n % base
        
        if remainder == 0
            result.unshift (char_base + base).chr
            n = (n / base) - 1
        else
            result.unshift (char_base + remainder).chr
            n /= base
        end
    end
    
    # add char for remaining value
    result.unshift (char_base + n).chr
    
    return result.join('')
end
