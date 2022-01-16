# https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        s = []
        m_r = len(grid)
        m_c = len(grid[0])
        neighbors = [[0, -1],[0, 1],[-1, 0],[1, 0]]
        freshOrg = 0
        for r in range(m_r):
            for c in range(m_c):
                status = grid[r][c] 
                if abs(status) == 1:
                    freshOrg += 1

                if status == 2:
                    for _, [row, col] in enumerate(neighbors):
                        n_r = row + r
                        n_c = col + c
                        if n_r >= 0 and n_r < m_r and n_c >= 0 and n_c < m_c and grid[n_r][n_c] == 1:
                            s.append([n_r, n_c])
                            grid[n_r][n_c] = -1
 
        while s:
            count += 1
            size = len(s)
            temp = []
            for _ in range(size):
                r, c = s.pop()
                freshOrg -= 1
                for _, [row, col] in enumerate(neighbors):
                    n_r = row + r
                    n_c = col + c
                    if n_r >= 0 and n_r < m_r and n_c >= 0 and n_c < m_c and grid[n_r][n_c] == 1:
                        temp.append([n_r, n_c])
                        grid[n_r][n_c] = 2
            s = temp

        if freshOrg > 0:
            return -1
        return count

        