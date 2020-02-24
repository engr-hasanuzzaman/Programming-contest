# https://leetcode.com/problems/sliding-window-maximum/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
# we only keeping latest max value on double ended queue as we need max value 
# for every array element pop min value from current value form queue untill found max value 
# push new value (val, index) to queue
# search from q first element where index - c_index <= k
def max_sliding_window(nums, k)
  return nums if k == 1
  windows = []
  q = [[nums.first, 0]]
  w_count = 1
  for i in (1...nums.size)
      n = nums[i]
      while q.any? && q[-1][0] < n
          q.pop
      end
      
      w_count += 1
      q << [n, i]
      while q.any?
          if i - q[0][1] + 1 > k
              q.shift
          else
              break
          end
      end
      
      if w_count >= k
          windows << q[0][0]
      end
  end
  
  windows
end