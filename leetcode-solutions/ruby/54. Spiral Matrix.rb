# https://leetcode.com/problems/spiral-matrix/

# @param {Integer[][]} matrix
# @return {Integer[]}
def spiral_order(matrix)
  return [] if matrix.size.zero?
  
  result = []
  i, j = 0, 0
  m, n = matrix.size - 1, matrix.first.size - 1
  print_spiral(i, j, m, n, matrix, result)
  result
end

def print_spiral(i, j, m, n , matrix, result)
  puts "#{i}, #{j}, #{m}, #{n}, #{result}" 
  return if(i > m || j > n)
      
  # first row
  (j..n).each do |c|
      result << matrix[i][c]
  end
  
  # last column
  (i+1..m).each do |r|
      result << matrix[r][n]
  end
  
  # if first row and last row are not same
  if i != m
      (n-1).downto(j) do |c|
          result << matrix[m][c]
      end
  end
  
  # if first colum and last column are not same
  if j != n
      (m-1).downto(i+1) do |r|
          result << matrix[r][j]
      end
  end
  
  print_spiral(i+1, j+1, m-1, n-1, matrix, result)
end