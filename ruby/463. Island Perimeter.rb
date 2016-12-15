# @param {Integer[][]} grid
# @return {Integer}
# since there is only one island so every 1 grid will participate on making island
# grid perimeter = number of water side of this grid
def island_perimeter(grid)
    perimeter = 0
    grid.size.times do |i|
        grid[i].size.times do |j|
            perimeter += cal_perimeter(grid, i, j) if grid[i][j] == 1
        end
    end
    
    return perimeter
end

def cal_perimeter(grid, i, j)
    perimeter = 0
    # top
    # check where top grid is outside of board or it 1 grid
    if (i - 1) < 0 || grid[i - 1][j] == 0
        perimeter += 1
    end
    
    # left
    # check where top grid is outside of board or it 1 grid
    if j - 1 < 0 || grid[i][j - 1] == 0 
        perimeter += 1
    end
    
    # right
    # check where top grid is outside of board or it 1 grid
    if (j + 1) >= grid[i].size || grid[i][j + 1] == 0
        perimeter += 1
    end
    
    # bottom
    # check where top grid is outside of board or it 1 grid
    if (i + 1) >= grid.size || grid[i + 1][j] == 0
        perimeter += 1
    end
    
    return perimeter
end
