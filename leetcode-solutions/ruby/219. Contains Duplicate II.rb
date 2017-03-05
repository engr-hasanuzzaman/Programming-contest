# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def contains_nearby_duplicate(nums, k)
    return false if k < 0 || nums.size < 1
    hash = Hash.new
    
    nums.each_with_index do |number, index|
        return true if hash[number] && index - hash[number] <= k
        hash[number] = index    
    end
    
    return false
end
