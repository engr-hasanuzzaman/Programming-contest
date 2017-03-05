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
