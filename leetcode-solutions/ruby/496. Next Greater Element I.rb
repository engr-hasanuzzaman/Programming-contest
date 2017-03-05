# @param {Integer[]} find_nums
# @param {Integer[]} nums
# @return {Integer[]}
def next_greater_element(find_nums, nums)
    result = []
    nums_hash = {}
    
    nums.each_with_index do |n, i|
      nums_hash[n] = i 
    end
    
    find_nums.each_with_index do |n, i|
        next_num = -1
        (nums_hash[n] + 1).upto(nums.size - 1) do |j|
            if nums[j] > n
                next_num = nums[j]
                break
            end
        end
        # puts "----------- first largest value is #{first_largest_val}"
        result << next_num
    end
    
    return result
end
