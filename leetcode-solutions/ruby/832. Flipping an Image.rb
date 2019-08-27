# https://leetcode.com/problems/flipping-an-image/

# @param {Integer[][]} a
# @return {Integer[][]}
def flip_and_invert_image(a)
  a.each_with_index do |row, i|
      r_size = row.size
      s_index = 0
      e_index = r_size - 1
      
      while(s_index < e_index)
          # puts
          row[e_index], row[s_index] = flip(row[s_index]), flip(row[e_index])
          s_index += 1
          e_index -= 1
      end
      
      row[s_index] = flip(row[s_index]) if s_index == e_index        
  end
  
  a
end

def flip(n)
  # return "n_#{n}"
  n.zero? ? 1 : 0
end