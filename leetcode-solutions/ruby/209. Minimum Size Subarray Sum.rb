# https://leetcode.com/problems/minimum-size-subarray-sum/

# @param {Integer} s
# @param {Integer[]} nums
# @return {Integer}
def min_sub_array_len(s, nums)
  min_length = nums.size + 1 # to indicate not sum exist
  c_length = 0
  c_sum = 0
  left = 0
  # loop over each element and check where sum is >= expected value
  # if sum >= loop until sum >= target value and reduce left most from sum
  # 1 5 7 expected value 11. so 1+5+7 = 13 but 5+7 11 is also >= target
  nums.each_with_index do |n, i|
      if s > c_sum + n
          c_sum += n
      else
          c_sum += n
          # reduce to minimum size
          while(c_sum >= s)
              min_length = [min_length, i - left + 1].min
              c_sum -= nums[left]
              left += 1
          end
      end
  end
  
  return 0 if min_length == nums.size + 1
  min_length
end