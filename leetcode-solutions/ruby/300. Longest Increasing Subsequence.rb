# https://leetcode.com/problems/longest-increasing-subsequence/

# @param {Integer[]} nums
# @return {Integer}
def length_of_lis(nums)
    dp = Array.new(nums.size){1}
    n = nums.size
    
    n.times do |i|
        0.upto(i-1) do |j|
            if nums[j] < nums[i]
                dp[i] = [dp[i], dp[j] + 1].max
            end
        end
    end
    
    dp.max
end
