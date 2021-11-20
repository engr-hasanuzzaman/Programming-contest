# https://leetcode.com/problems/surrounded-regions/
# we will flip all the 'O' which do not have any bounding 'O' neighbours
# in other work, we will keep those 'O' which has bounding 'O' neighbours

# @param {Character[][]} board
# @return {Void} Do not return anything, modify board in-place instead.
def solve(board)
    return if board.size.zero?
    
    # find all the 'O' which has bound neighbours and mark with 1

    # first row
    row = 0
    for col in 0...board.first.size
        next if board[row][col] != 'O'
        bfs(board, row, col)    
    end
    
    # last row
    row = board.size - 1
    for col in 0...board.first.size
        next if board[row][col] != 'O'
        bfs(board, row, col)    
    end
    
    # first col
    col = 0
    for row in 0...board.size
        next if board[row][col] != 'O'
        bfs(board, row, col)    
    end
    
    # last col
    col = board.first.size - 1
    for row in 0...board.size
        next if board[row][col] != 'O'
        bfs(board, row, col)    
    end
    
    # if the value is 1 that means that has bounding 'O' neighbours
    # so, that will be 'O' or convernt 'O' to 'x'
    for i in 0...board.size
        for j in 0...board.first.size
                board[i][j] = 'O'
            elsif board[i][j] == 'O'
                board[i][j] = 'X'
            end
        end
    end
    
    board        
end

def bfs(board, i, j)
    q = [[i, j]]
    max_row = board.size - 1
    max_col = board.first.size
    neighbours = [[-1, 0], [0,-1], [0, 1], [1, 0]]
    board[i][j] = 1
    while q.any?
        x, y = q.pop
        neighbours.each do |r, c|
            if x + r >= 0 && x + r <= max_row && y + c >=0 && y + c <= max_col && board[x+r][y+c] == 'O'
                board[x+r][y+c] = 1
                q << [x+r, y+c]
            end
                
        end
    end
end