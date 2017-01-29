# @param {Integer[]} nums
# @return {Boolean}
def find132pattern(nums)
    l = nums.size
    i = 0
    
    while i < l - 2
        first_num = nums[i]
        j = i + 1
        
        while j < l - 1
            mid_num = nums[j]
            if mid_num < first_num
                j += 1
                next
            end    
            
            k = j + 1
            
            while k < l
                last_num = nums[k]
                return true if (first_num < last_num) && (last_num < mid_num)
                k += 1
            end
            
            j += 1
        end
        i += 1
    end
    
    return false
end
