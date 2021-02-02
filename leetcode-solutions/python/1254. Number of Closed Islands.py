from functools import reduce
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
      self.grid = grid
      self.r_size = len(grid)
      if self.r_size == 0:
        return 0
        
      self.c_size = len(grid[0])
      if self.c_size == 0:
        return 0
      
      i_land = 0
      self.visited = [[False] * self.c_size for _ in range(self.r_size)]
      self.visited[0][0] = True
      for i in range(self.r_size):
        for j in range(self.c_size):
          if not self.visited[i][j] and self.grid[i][j] == 0:
            self.visited[i][j] = True
            ws = self.dfs(i, j)
            # if is was close iland, update counter
            if ws:
              i_land += 1

      return i_land
    
    def dfs(self, r, c):
      ng, ws = self.visit_neighbours(r, c)
      ng_ws = [ws]
      for rr, cc in ng:
        ng_ws.append(self.dfs(rr, cc))
        
      return reduce(lambda acc, e: acc and e, ng_ws)
    
    def visit_neighbours(self, r, c):
      col = [-1, 1, 0, 0]
      row = [0, 0, 1, -1 ]
      ng = []
      w_surroundad = True
      for i in range(4):
        cc = c + col[i]
        rr = r + row[i]
        
        # check boundary
        if cc >= self.c_size or rr >= self.r_size:
          w_surroundad = False
          continue
          
        if cc < 0 or rr < 0:
          w_surroundad = False
          continue
          
        # already visited or water  
        if self.visited[rr][cc] or self.grid[rr][cc] == 1:
          continue
        
        self.visited[rr][cc] = True
        ng.append([rr, cc])
    
      return (ng, w_surroundad)