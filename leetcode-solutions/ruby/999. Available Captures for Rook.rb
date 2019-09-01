# https://leetcode.com/problems/available-captures-for-rook/

# @param {Character[][]} board
# @return {Integer}
def num_rook_captures(board)
  8.times do |i|
      8.times do |j|
          return num_of_p(i, j, board) if board[i][j] == 'R'
      end
  end
  
  0
end

def num_of_p(b_i, b_j, board)
  p_count = 0
  
  # check right row
  j = b_j + 1
  while(j >=0 && j < 8)
      if board[b_i][j] == 'p'
          p_count += 1 
          break
      elsif board[b_i][j] != '.'
          break
      end
      
      j += 1
  end
  
  # check left row
  j = b_j - 1
  while(j >=0 && j < 8)
      if board[b_i][j] == 'p'
          p_count += 1 
          break
      elsif board[b_i][j] != '.'
          break
      end
      
      j -= 1
  end
  
  # check top row
  i = b_i + 1
  while(i >=0 && i < 8)
      if board[i][b_j] == 'p'
          p_count += 1 
          break
      elsif board[i][b_j] != '.'
          break
      end
      
      i += 1
  end
  
  # check top row
  i = b_i - 1
  while(i >=0 && i < 8)
      if board[i][b_j] == 'p'
          p_count += 1 
          break
      elsif board[i][b_j] != '.'
          break
      end
      
      i -= 1
  end
  
  p_count
end