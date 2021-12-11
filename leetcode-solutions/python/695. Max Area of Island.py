# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.bfs(grid, i, j))
        return max_area
        
    def bfs(self, grid, i, j):
        s = [[i,j]]
        grid[i][j] = 0 # mark visited
        m_row = len(grid)
        m_col = len(grid[0])
        count = 0
        ng = [
            [0, -1],
            [0, 1],
            [1, 0],
            [-1, 0]
        ]
        while s:
            size = len(s)
            temp = []
            for _ in range(size):
                i, j = s.pop()
                count += 1
                # visit the neighbours          
                for _, points in enumerate(ng):
                    n_row = i + points[0]
                    n_col = j + points[1]
                    if n_row >= 0 and n_row < m_row and n_col >= 0 and n_col < m_col and grid[n_row][n_col] == 1:
                        s.append([n_row, n_col])
                        grid[n_row][n_col] = 0 # mark visited
        return count
    