# @param {Integer} num
# @return {Boolean}
# Using binary search
def is_perfect_square(num)
    return true if num == 1
    
    low, high = 1, num / 2 + 1
    
    while( high - low > 1)
        mid = (low + high) / 2
        temp_num = mid * mid
        
        # puts "low is #{low}, high is #{high}, mid is #{mid}"
        
        if temp_num == num
            return true
        elsif temp_num > num
            high = mid
        else
            low = mid
        end
    end
    
    return false
end
