# @param {Integer[]} nums
# @return {Integer}
def num_identical_pairs(nums)
    dict = {}
    num_of_pairs = 0
    nums.each do |num|
        if dict[num]
            num_of_pairs += dict[num]
            dict[num] += 1
        else
            dict[num] = 1
        end
    end
    
    num_of_pairs
end