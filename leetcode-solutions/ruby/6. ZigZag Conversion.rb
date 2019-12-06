# https://leetcode.com/problems/zigzag-conversion/

# @param {String} s
# @param {Integer} num_rows
# @return {String}
def convert(s, num_rows)
  r_i = 0
  c_i = 0
  dir = true # increment
  answer = [[]]
  max_i = num_rows - 1
  
  s.size.times do |i|
      # c_n = i % max_i
      unless answer[r_i]
          answer[r_i] = []
      end
      print "#{r_i}#{c_i} "
      answer[r_i][c_i] = s[i]
      
      if dir && r_i == max_i
          dir = false
          r_i -= 1
          c_i += 1
      elsif !dir && r_i == 0
          r_i += 1
          dir = true
      elsif !dir
          r_i -= 1
          c_i += 1
      else
          r_i += 1
      end
          
          
      # answer[r_i] << s[i]
      
  end
  answer.flatten.compact.join("")
end

# index out of index for num 1
