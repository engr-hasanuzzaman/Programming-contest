# https://leetcode.com/problems/partition-array-according-to-given-pivot/

# @param {Integer[]} nums
# @param {Integer} pivot
# @return {Integer[]}
def pivot_array(nums, pivot)
    lower_count = 0
    pivot_count = 0
    higher_count = 0
    
    nums.each do |num|
        if num == pivot
            pivot_count += 1
        elsif num > pivot
            higher_count += 1
        else
            lower_count += 1
        end
    end
    
    ans = Array.new(nums.size)
    l_idx = 0
    p_idx = lower_count
    h_idx = lower_count + pivot_count
    
    nums.each do |num|
        if num == pivot
            ans[p_idx] = num
            p_idx += 1
        elsif num > pivot
            ans[h_idx] = num
            h_idx += 1
        else
            ans[l_idx] = num
            l_idx += 1
        end
    end
    ans
end
