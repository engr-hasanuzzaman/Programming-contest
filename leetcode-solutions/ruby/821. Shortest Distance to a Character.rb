# https://leetcode.com/problems/shortest-distance-to-a-character/

# @param {String} s
# @param {Character} c
# @return {Integer[]}
def shortest_to_char(s, c)
  result = []
  last_e_position = 10001
  
  s.each_char.with_index do |ch, i|
      if ch == c
          last_e_position = i
          result << 0
      else
          result << (i - last_e_position).abs
      end
  end
  
  last_e_position = 10001
  (s.size - 1).downto(0) do |i|
      ch = s[i]
      
      if ch == c
          last_e_position = i
          #result[i] = 0
      else
          result[i] = [(last_e_position - i), result[i]].min 
      end
  end
  
  result
end