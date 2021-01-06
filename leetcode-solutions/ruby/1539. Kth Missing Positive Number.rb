# Task link: https://leetcode.com/problems/kth-missing-positive-number/
# @param {Integer[]} arr
# @param {Integer} k
# @return {Integer}
def find_kth_positive(arr, k)
    prev_n = 0
    i = 0
    while k > 0
      if arr[i] == prev_n + 1
        i += 1
      else
        k -= 1
      end
      
      prev_n += 1
    end
    
    prev_n
  end