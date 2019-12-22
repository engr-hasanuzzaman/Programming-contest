# https://leetcode.com/problems/target-sum/

# @param {Integer[]} nums
# @param {Integer} s
# @return {Integer}
def find_target_sum_ways(nums, s)
  memo = {}
  nums.size.times {|i| memo[i] = {} }
  dp(nums, 0, s, memo)
end

def dp(nums, i, target, memo)
  return 1 if i == nums.size && target == 0
  return 0 if i == nums.size
  # if not in memo then keep it on memo
  unless memo.dig(i) && memo.dig(i).dig(target)
      memo[i][target] = dp(nums, i+1, target -  nums[i], memo) + dp(nums, i+1, target + nums[i], memo)
  end
  # return from memo
 memo.dig(i).dig(target) 
end