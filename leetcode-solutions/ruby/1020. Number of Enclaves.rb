# https://leetcode.com/problems/number-of-enclaves/

# @param {Integer[][]} grid
# @return {Integer}
def num_enclaves(grid)
  r_size = grid.size
  c_size = grid.first.size

  # first and last row
  [0, r_size - 1].each do |row|
    c_size.times do |col|
      dfs(grid, row, col) if grid[row][col] == 1
    end
  end

  # fisrt and last col
  [0, c_size - 1].each do |col|
    r_size.times do |row|
      dfs(grid, row, col) if grid[row][col] == 1
    end
  end
  count = 0
  r_size.times do |row|
    c_size.times do |col|
      count += 1 if grid[row][col] == 1
    end
  end
  count
end

def dfs(grid, i, j)
  neighbors = [[0, -1], [0, 1], [-1, 0], [1, 0]]
  grid[i][j] = 0
  neighbors.each do |row, col|
    n_row = row + i
    n_col = col + j
    next if n_row >= grid.size || n_row < 0 || n_col >= grid.first.size || n_col < 0 || grid[n_row][n_col] == 0

    dfs(grid, n_row, n_col)
  end
end
