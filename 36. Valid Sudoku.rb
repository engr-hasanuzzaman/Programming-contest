#  https://leetcode.com/problems/valid-sudoku/

# @param {Character[][]} board
# @return {Boolean}
def is_valid_sudoku(board)
  valid_row?(board) && valid_column?(board) && valid_all_trio?(board)
end

def valid_row?(board)
  9.times do |i|
      map = {}
      
      9.times do |j|
          next if board[i][j] == '.'
          
          return false  if map[board[i][j]]
          map[board[i][j]] = true
      end
  end
  
  true
end

def valid_column?(board)
  9.times do |j|
      map = {}
      
      9.times do |i|
          next if board[i][j] == '.'
          
          return false  if map[board[i][j]]
          map[board[i][j]] = true
      end
  end
  
  true
end

def valid_trio?(board, s_row, s_col)
  map = {}
  3.times do |i|
      3.times do |j|
         next if board[s_row + i][s_col + j] == '.'
          
          return false if map[board[s_row + i][s_col + j]]
          map[board[s_row + i][s_col + j]] = true
      end
  end
  
  true
end

def valid_all_trio?(board)
  row = 0
  3.times do |i|
      col = 0
      3.times do |j|
          return false unless valid_trio?(board, row, col)
          col += 3
      end
      
      row += 3
  end
  
  true
end

