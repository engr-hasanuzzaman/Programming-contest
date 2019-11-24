# https://leetcode.com/problems/number-of-islands/

# @param {Character[][]} grid
# @return {Integer}
# run bsf and mark point visited
# on each bfs run mark neighboring point for future skiping
# so, on each bsf run one iland will be marked 
def num_islands(grid)
  return 0 if grid.size.zero?
  
  # keep mark of visited node         
  visited = []
  # grid row, col size     
  row_size = grid.size
  col_size = grid.first.size
  
  # create all rows beforehand
  row_size.times do
      visited << []
  end
  
  # imcrement with number of bfs run
  result = 0
  
  # traverse each point and mark all neighbour using bfs     
  row_size.times do |i|
      col_size.times do |j|
          if safe?(grid, row_size, col_size, i.to_i, j.to_i, visited)
              bfs(grid, i.to_i, j.to_i, row_size, col_size, visited)
              result += 1
          end
      end
  end
  
  result
  
end

def bfs(grid, x, y, row_end, col_end, visited)
  # mark 8 neighbours point    
  n_rows = [-1,0,0,1]
  n_cols = [0,-1,1,0]
  
  # queue for bfs      
  q = [Point.new(x, y)]
  
  until q.empty?
      size = q.size
      
      size.times do
          p = q[0]
          # visit each neiboring point and mark them visited
          4.times do |i|
              if safe?(grid, row_end, col_end, p.x + n_rows[i], p.y + n_cols[i], visited)
                  q << Point.new(p.x + n_rows[i], p.y+n_cols[i])
                  visited[p.x+n_rows[i]][p.y+n_cols[i]] = true
              end
          end
          
          q.shift    
          visited[p.x][p.y] = true
          
      end # end of nei visiting
      
  end
end

# decide before adding to BFS queue or running bfs
def safe?(grid, row_end, col_end, i, j, visited)
  i >= 0 && i < row_end && j >= 0 && j < col_end && grid[i][j].to_i == 1 && !visited[i][j]
end

# for keeping position
class Point
  attr_accessor :x, :y
  
  def initialize(x, y)
      self.x = x
      self.y = y
  end
  
  def to_a
      [x, y]
  end
  
  def to_s
      to_a
  end
end