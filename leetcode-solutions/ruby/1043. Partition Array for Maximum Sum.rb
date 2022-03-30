# https://leetcode.com/problems/partition-array-for-maximum-sum/

# explanation https://leetcode.com/problems/partition-array-for-maximum-sum/discuss/1621079/Python-Easy-DP-with-Visualization-and-examples
# @param {Integer[]} arr
# @param {Integer} k
# @return {Integer}
def max_sum_after_partitioning(arr, k)
    dp = Array.new(arr.size)
    k.times do |i|
        dp[i] = arr[0..i].max * (i + 1)
    end
    
    k.upto(arr.size - 1) do |i|
        res = []
        k.times do |j|
            res << dp[i - j - 1] + arr[i - j..i].max * (j + 1)
        end
        dp[i] = res.max
    end
    
    dp[-1]
end
