# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# limelimit exceed code
# @param {Integer[]} nums
# @return {Integer}
def remove_duplicates(nums)
  size = 0
  prev_num = nums.first
  left = 0
  count = 0
  arr_length = nums.size
  
  while(count < nums.size)
      current = nums[left]
      end_i = left
      
      # find duplicate 
      while end_i < arr_length - 1 && nums[end_i+1] == current
          end_i += 1
      end
      
      # duplicate found         
      if end_i - left > 0
          dup_size = end_i - left
          start = left+1
          
          while start < arr_length
              nums[start] = nums[start+dup_size]
              start += 1
          end
          
          arr_length -= dup_size
      end
      
      count = count + end_i - left + 1
      left += 1
  end
  
  arr_length
end