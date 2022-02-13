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
  return s if num_rows == 1 || s.size <= num_rows
  
  s.size.times do |i|
      unless answer[r_i]
          answer[r_i] = []
      end
      
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
      
  end
  
  answer.flatten.compact.join("")
end

# simpler implementation
def convert(s, num_rows)
    return s if num_rows == 1 || s.size < num_rows
    # create rows
    rows = Array.new(num_rows){ [] }
    step = 1
    row_num = 0
    
    # itirate throug each char and put on the row_num
    s.each_char do |char|
        rows[row_num] << char
        row_num += step
        
        # since this is the last row, from next, go up
        if row_num == num_rows - 1
            step = -1
        end
        
        #  since this is the first row, from the next go down
        if row_num == 0
            step = 1
        end
    end
    rows.map{|row| row.join}.join
end