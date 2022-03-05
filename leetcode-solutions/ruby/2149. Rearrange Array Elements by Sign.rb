# https://leetcode.com/problems/rearrange-array-elements-by-sign/
# @param {Integer[]} nums
# @return {Integer[]}
def rearrange_array(nums)
    p_arr = []
    n_arr = []
    nums.each do |n|
        if n >= 0
            p_arr << n
        else
            n_arr << n
        end
    end
    
    p_idx = 0
    n_idx = 0
    nums.size.times do |idx|
        if idx % 2 == 0
            nums[idx] = p_arr[p_idx]
            p_idx += 1
        else
            nums[idx] = n_arr[n_idx]
            n_idx += 1
        end
    end
    nums
end
