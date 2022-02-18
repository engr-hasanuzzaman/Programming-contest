# https://leetcode.com/problems/house-robber-ii/

# @param {Integer[]} nums
# @return {Integer}
def rob(nums)
    return nums.max if nums.size <= 2
    
    [max_rob_amount(nums[1..-1]), max_rob_amount(nums[0...-1])].max
end

def max_rob_amount(nums)
    max_amount_at = Array.new(nums.size+2){0}
    right_index = nums.size - 1
    right_index.downto(0) do |i|
        max_amount_at[i] = [nums[i] + max_amount_at[i+2], max_amount_at[i+1]].max
    end
    max_amount_at.first
end