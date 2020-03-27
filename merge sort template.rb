def merge_sort(nums)
  return nums if nums.size <= 1
  
  pivot = nums.size / 2 
  left_list = merge_sort(nums[0...pivot])
  right_list = merge_sort(nums[pivot..-1])
  return merge(left_list, right_list)
end

def merge(left_list, right_list)
  left_cursor = right_cursor = 0
  ret = []
  while left_cursor < left_list.size && right_cursor < right_list.size
      if left_list[left_cursor] < right_list[right_cursor]
          ret << left_list[left_cursor]
          left_cursor += 1
      else
          ret << right_list[right_cursor]
          right_cursor += 1
      end
  end
  # append what is remained in either of the lists
  ret += left_list[left_cursor..-1]
  ret += right_list[right_cursor..-1]
  
  return ret
end