# https://leetcode.com/problems/decompress-run-length-encoded-list/

# @param {Integer[]} nums
# @return {Integer[]}
def decompress_rl_elist(nums)
  ans = []
  i = 0
  while i < nums.size - 1
      nums[i].times { ans << nums[i+1]}
      
      i += 2
  end
  
  ans
end