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

# with constant memory
# @param {Integer[]} nums
# @return {Integer}
def find_lhs(nums)
    
    nums.sort!
    cur_num = nums.first
    index = 1
    cur_count = 1
    max_count = 0
    while index < nums.size
        num = nums[index]
        # same number 
        if num == cur_num
            cur_count += 1
            index += 1
        else
            if num == cur_num + 1
                next_count = 0
                while index < nums.size && nums[index] == cur_num + 1
                    index += 1
                    next_count += 1
                end
                max_count = [max_count, cur_count + next_count].max
                cur_count = next_count
            else
                cur_count = 1
                index += 1
            end
            
            cur_num = num
        end
    end
    max_count
end