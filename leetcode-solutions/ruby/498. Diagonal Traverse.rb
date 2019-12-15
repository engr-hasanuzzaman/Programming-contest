# https://leetcode.com/problems/diagonal-traverse/

# @param {Integer[][]} matrix
# @return {Integer[]}
def find_diagonal_order(matrix)
  return [] if matrix.size.zero?
  
  top = true
  row_size = matrix.size
  col_size = matrix.first.size
  num_of_elm = row_size * col_size
  c_r = 0
  c_c = 0
  result = []
  
  num_of_elm.times do |i|
      # puts "--#{i} #{c_r} #{c_c}, #{top}"
      result << matrix[c_r][c_c]
      if (top && c_r.zero?) || (top && c_c == col_size - 1)
          if c_c == col_size - 1
              c_r += 1
          else
              c_c += 1
          end
          
          top = false
      elsif (!top && c_c.zero?) || (!top && c_r == row_size - 1)
          if c_r == row_size -1
              c_c += 1
          else
              c_r += 1
          end
          
          top = true
      elsif top # go to top
          c_r -= 1
          c_c += 1
      else
          c_r += 1
          c_c -= 1
      end
  end
  
  result
end