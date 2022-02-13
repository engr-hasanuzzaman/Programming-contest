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

=begin
The idea behind this approach is as follows: 
If the cumulative sum(represented by sum[i]sum[i] for sum up to i^{th}ith  index) up to two indices is the same, 
the sum of the elements lying in between those indices is zero. Extending the same thought further, 
if the cumulative sum up to two indices, say ii and jj is at a difference of kk i.e. if sum[i] - sum[j] = ksum[i]−sum[j]=k, the sum of elements lying between indices ii and jj is kk.
=end

def subarray_sum(nums, k)
    sum_frequency_counter = Hash.new(0)
    sum_frequency_counter[0] = 1
    count = 0
    prefix_sum = 0
    nums.each do |num|
        prefix_sum += num
        count += sum_frequency_counter[prefix_sum - k]
        sum_frequency_counter[prefix_sum] += 1
    end
    
    return count
end
