# @param {Character[][]} board
# @return {Boolean}
# 9*9 size board.
# There are just 3 rules to Sudoku.
# 1. Each row must have the numbers 1-9 occuring just once.
# 2. Each column must have the numbers 1-9 occuring just once.
# And the numbers 1-9 must occur just once in each of the 9 sub-boxes of the grid.
def is_valid_sudoku(board)
    sudoku_box_index = [0, 3, 6]
    
    # make 2d array from input with empty field wtih nil
    # so that we can use compact to remove nil easily
    9.times do |i|
        board[i] = board[i].map{|n| n == '.' ? nil : n}
    end
    
    # check each row & column
    9.times do |index|
      # row check  
      valid_row = valid_sudoku_array(board[index].compact)
      
      # column check 
      # take all first row element for making column
      valid_column = valid_sudoku_array(board.map{|row| row[index]}.compact)
      
      return false unless valid_row && valid_column
    end
    
    # check each sub 3*3 array
    sudoku_box_index.each do |i|
        sudoku_box_index.each do |j|
            return false unless valid_sudoku_array(sudoku_box(board, i, j))
        end
    end

    return true
end

# check duplicate value in array
def valid_sudoku_array(nums)
    nums.each_with_object(Hash.new(0).merge dup: []){|n, h| h[:dup] << n if (h[n] +=1) == 2}[:dup].size == 0
end

# i,j with in 0,3,6
def sudoku_box(box, i, j)
    return [
        box[i][j],     box[i][j + 1],     box[i][j + 2],
        box[i + 1][j], box[i + 1][j + 1], box[i + 1][j + 2],
        box[i + 2][j], box[i + 2][j + 1], box[i + 2][j + 2]
       ].compact
end
    
    
    
