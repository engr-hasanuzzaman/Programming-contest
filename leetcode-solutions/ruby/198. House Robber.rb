# https://leetcode.com/problems/house-robber/

# @param {Integer[]} nums
# @return {Integer}
def rob(nums)
    right_index = nums.size - 1
    firstLast = secondLast = 0
    
    right_index.downto(0) do |i|
        cur_amount = [nums[i] + secondLast, firstLast].max
        secondLast = firstLast
        firstLast = cur_amount
    end
    
    return [firstLast, secondLast].max
end