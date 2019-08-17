# @param {Integer[][]} grid
# @return {Integer}
def max_increase_keeping_skyline(grid)
  left_right_skylines = []
  top_bottom_skylines = []
  sum = 0
    
  grid.each do |row|
      left_right_skylines << row.max
  end
    
  grid.transpose.each do |row|
      top_bottom_skylines << row.max
  end
    
  left_right_skylines.each_with_index do |lr, i|
      top_bottom_skylines.each_with_index do |tb, j|
          min_skyline = [lr, tb].min
          sum += (min_skyline - grid[i][j])
      end
  end

  sum  
end