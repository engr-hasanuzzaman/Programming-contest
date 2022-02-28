# https://leetcode.com/problems/increasing-triplet-subsequence/

# TLE solution n ^ 3
def increasing_triplet(nums)
    n = nums.size
    memo = {}
    n.times do |i|
        (i+1).upto(n-1) do |j|
            next if nums[j] <= nums[i] || memo[j] == false
        
            (j+1).upto(n-1) do |k|
                if nums[j] < nums[k]
                    return true
                end
            end
            memo[j] = false
        end
    end
    
    false
end