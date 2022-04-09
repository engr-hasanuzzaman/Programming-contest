# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_k_difference(nums, k)
    memo = Hash.new(0)
    ans = 0
    nums.each do |num|
        if memo.key?(num - k)
            ans += memo[(num - k)]
        end
        
        if memo.key?(num + k)
            ans += memo[num + k]
        end
        # puts "num #{num}, #{memo}, #{ans}"
        memo[num] += 1
    end
    ans
end
