# https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] and grid1[i][j] == 1:
                    ans += self.bfs(grid2, i, j, grid1)
        return ans
    
    def bfs(self, grid, r, c, grid1):
        s = [[r,c]]
        grid[r][c] = 0 # mark visited
        m_row = len(grid)
        m_col = len(grid[0])
        sub_island = 1
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
                # visit the neighbours          
                for _, points in enumerate(ng):
                    n_row = i + points[0]
                    n_col = j + points[1]
                    if n_row >= 0 and n_row < m_row and n_col >= 0 and n_col < m_col and grid[n_row][n_col] == 1:
                        if grid1[n_row][n_col] != 1:
                            sub_island = 0
                        s.append([n_row, n_col])
                        grid[n_row][n_col] = 0 # mark visited
        # print(i, j)
        return sub_island
