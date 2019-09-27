# https://leetcode.com/problems/3sum/
# TODO: lime limite exceed submission

# @param {Integer[]} nums
# @return {Integer[][]}
def three_sum(nums)
  res = []
  comb = []
  combination(res, comb, nums.sort, 0)
  res
end

def combination(res, comb, nums, s_index)
  return if comb.sum > 0
  
  if comb.size == 3 && comb.sum.zero?
      res << comb.map{|n| n}
      return
  end
  
  if comb.size == 3
      return 
  end
  
  s_index.upto(nums.size-1) do |n|
      next if (n > s_index  && nums[n] == nums[n-1]) || nums[n] > 0
      comb << nums[n]
      combination(res, comb, nums, n+1)
      comb.pop
  end
end