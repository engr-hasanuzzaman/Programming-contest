# @param {Integer[]} nums
# @return {Integer}
def total_hamming_distance(nums)
    total_distance = 0
    
    nums.size.times do |i|
        (i + 1).upto(nums.size - 1) do |j|
            total_distance += hamming_distance(nums[i], nums[j])
        end
    end
    
    return total_distance
end

def hamming_distance(x, y)
    (x ^ y).number_of_set_bits
end

class Integer
    def number_of_set_bits
        count = 0
        number = self
        
        while(number != 0)
            number = number & (number - 1)
            count += 1
        end
        
        return count
    end
end
