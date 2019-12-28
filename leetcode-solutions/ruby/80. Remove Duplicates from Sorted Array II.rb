# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

# @param {Integer[]} nums
# @return {Integer}
def remove_duplicates(nums)
  return nums.size if nums.size <= 2
  
  count = 1
  left = 0

  # left hold last valid position
 1.upto(nums.size-1) do |right|
      if nums[left] == nums[right]
        # since max 2 same num are allowd
        # increment left and replace with right other wise 
        # only increment count
          if count <= 1
              left += 1
              # left increment and replace with right otherwse
              # invalid value will contain on array
              nums[left] = nums[right]
          end
          
          count += 1
      else
          left += 1
          nums[left] =  nums[right]
          count = 1
      end
  
  end
  
  left + 1
end