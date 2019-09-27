# https://leetcode.com/problems/3sum-closest/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def three_sum_closest(nums, target)
  result 0 if nums.size < 3
  
  result = []
  comb = []
 combination(result, comb, nums.sort, target, 3, 0) 
  result.sum
end

def combination(result, comb, nums, target, rem_num, s_index)
  # base condition
  if rem_num == 0
      if result.size == 0
          3.times do |i|
              result[i] = comb[i] 
          end
      else
          # puts "---#{target} #{comb} #{result}"
          if (target - comb.sum).abs < (target - result.sum).abs
              3.times do |i|
                  result[i] = comb[i] 
              end
          end
      end
      return
  end
  
  s_index.upto(nums.size-1) do |i|
      next if i > s_index && nums[i] == nums[i-1]
      comb << nums[i]
      combination(result, comb, nums, target, rem_num - 1, i+1)
      comb.pop
  end
      
end