# https://leetcode.com/problems/longest-harmonious-subsequence/

# @param {Integer[]} nums
# @return {Integer}
def find_lhs(nums)
    freq_counter = nums.each_with_object(Hash.new(0)){|num, h| h[num] += 1}
    max_size = 0
    nums.each do |num|
        if freq_counter[num-1] > 0
            max_size = [freq_counter[num] + freq_counter[num - 1], max_size].max
        end
        
        if freq_counter[num+1] > 0
            max_size = [freq_counter[num] + freq_counter[num + 1], max_size].max
        end
    end
    
    max_size
end
