# @param {Integer[]} numbers
# @param {Integer} target
# @return {Integer[]}
def two_sum(numbers, target)
    last_number = nil
    
    numbers.each_with_index do |n, i|
        other_num = target - n
        temp = i + 1
        
        next if last_number == n 
        
        while temp < numbers.size
            
            if numbers[temp] == other_num
                return [i + 1, temp + 1]
            end
            
            if numbers[temp] >= other_num
                break
            end
            
            
            temp += 1
            last_number = n
        end
    end
    
    return []
end


# tow pointer solution
# @param {Integer[]} numbers
# @param {Integer} target
# @return {Integer[]}
def two_sum(numbers, target)
    i, j = 0, numbers.size-1
    
    while i < j
        sum = numbers[i] + numbers[j]
        return [i+1, j+1] if  sum == target
        if sum > target
            j -= 1
        else
            i += 1
        end
    end
end
