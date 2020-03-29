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

# bottom up fashion

# @param {Integer[]} nums
# @return {Integer[]}
def sort_array(nums)
  results = nums.map{|n| [n] }
  
  until results.size == 1
      temp = []
      results.each_slice(2) do |s|
          if s.size == 1
              temp << s.first
          else
              temp << merge(s.first, s.last)
          end
      end
      
      results = temp
  end
  
  results.first
end

def merge(l1, l2)
  i1 = 0
  i2 = 0
  result = []
  
  while i1 < l1.size && i2 < l2.size
      if l1[i1] < l2[i2]
          result << l1[i1]
          i1 += 1
      else
          result << l2[i2]
          i2 += 1
      end
  end
  
  result += l1[i1..-1]
  result += l2[i2..-1] 
  result
end