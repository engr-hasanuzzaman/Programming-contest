# @param {Character[][]} board
# @return {Integer}
def count_battleships(board)
  size = board.size
  sign_of_ship = 'X'
  sign_of_empty = '.'

  s_num = 0

  size.times do |i|
    board[0].size.times do |j|
      next if board[i][j] != sign_of_ship
        
      if board[i][j + 1] == sign_of_ship
        remove_ship_sign(board, i, j, 0)
      else
        remove_ship_sign(board, i, j, 1)
      end

      s_num += 1
    end
  end

  return s_num
end

# 0 = row, 1 = column
def remove_ship_sign(board, x, y, row_or_column)
  if row_or_column.zero?
    y.upto(board[x].size - 1) do |i|
      if board[x][i] != 'X'
        break
      end
    
      puts "------row remove x for i = #{i}, j = #{y}"    
      board[x][i] = '.'
    end
  else
    x.upto(board.size - 1) do |i|
      if board[i][y] != 'X'
        break
      end
     puts "------column remove x for i = #{x}, j = #{i}"      
      board[i][y] = '.'
    end
  end
end
