# https://leetcode.com/problems/binary-gap/

# @param {Integer} n
# @return {Integer}
def binary_gap(n)
  b = n.to_s(2)
  distance = 0
  last_one_index = nil
  i = 0
  until n.zero?
      if n & 1 == 1
          if last_one_index
              distance = [distance, i - last_one_index].max
          else
              distance = 0
          end
          
          last_one_index = i
      end
      i += 1
      n = n >> 1
  end
  
  distance
end