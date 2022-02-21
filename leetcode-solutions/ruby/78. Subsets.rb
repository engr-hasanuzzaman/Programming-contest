# https://leetcode.com/problems/subsets/

# @param {Integer[]} nums
# @return {Integer[][]}
def subsets(nums)
    ans  = []
    combination(nums, 0, ans, [])
    ans
end

def combination(nums, index, ans, cur_com)
    return if index > nums.size
    ans << cur_com[0..-1]
    
    index.upto(nums.size - 0) do |i|
        cur_com << nums[i]
        combination(nums, i+1, ans, cur_com)
        cur_com.pop
    end
end
