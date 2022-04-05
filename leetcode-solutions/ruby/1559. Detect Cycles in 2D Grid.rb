# https://leetcode.com/problems/detect-cycles-in-2d-grid/

# @param {Character[][]} grid
# @return {Boolean}
def contains_cycle(grid)
  row_size = grid.size
  col_size = grid.first.size
  visited = Array.new(row_size) { Array.new(col_size) { false } }
  neighbors = [[0, -1], [0, 1], [-1, 0], [1, 0]]

  row_size.times do |i|
    col_size.times do |j|
      next if visited[i][j]

      cycle = has_cycle?(grid, i, j, [-1, -1], 0, visited, neighbors)
      return cycle if cycle
    end
  end

  false
end

def has_cycle?(grid, i, j, parent, count, visited, neighbors)
  visited[i][j] = true
  count += 1
  neighbors.each do |row, col|
    n_row = row + i
    n_col = col + j
    next if n_row >= grid.size || n_row < 0 || n_col >= grid.first.size || n_col < 0 || grid[n_row][n_col] != grid[i][j]

    if visited[n_row][n_col] && (n_row != parent.first || n_col != parent.last) && count >= 4
      return true
    elsif visited[n_row][n_col]
      next # already processed
    end

    cycly = has_cycle?(grid, n_row, n_col, [i, j], count, visited, neighbors)
    return cycly if cycly
  end
  false
end
