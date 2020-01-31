# https://leetcode.com/problems/subarray-sum-equals-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def subarray_sum(nums, k)
  ans = 0
  sum = {}
  sum[0]= 1
  acc = 0
  nums.each do |n|
      acc += n
      if sum[acc-k]
          ans += sum[acc-k]
      end
      
      if sum[acc]
          sum[acc] += 1
      else
          sum[acc] = 1
      end
  end
  
  ans
end
