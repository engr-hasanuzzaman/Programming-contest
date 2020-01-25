# https://leetcode.com/problems/degree-of-an-array/

# @param {Integer[]} nums
# @return {Integer}
def find_shortest_sub_array(nums)
  i_map = {}
  c_map = {}
  m_n = []
  max_f = 0
  nums.each_with_index do |n, i|
      if i_map[n]
          i_map[n][1] = i
          c_map[n] += 1
      else
          c_map[n] = 1
          i_map[n] = [i,i]
      end
      
      if c_map[n] > max_f
          max_f = c_map[n]
          m_n = [n]
      elsif c_map[n] == max_f
          m_n << n
      end
  end
  
  res = nums.size
  m_n.each do |n|
      if i_map[n].last - i_map[n].first + 1 < res
          res = i_map[n].last - i_map[n].first + 1
      end
  end
  
  res
end