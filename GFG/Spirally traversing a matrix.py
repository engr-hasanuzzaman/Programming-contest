# https://practice.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1/?page=1&difficulty[]=1&status[]=unsolved&curated[]=1&sortBy=submissions#

class Solution:

    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix, r, c):
        visited = [[False] * c for _ in range(r)]
        row = col = 0
        step = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        di = 0
        ans = []
        for _ in range(r*c):
            # print("row, col", row, col)
            visited[row][col] = True
            # if row >= min_r and row <= max_r and col >= min_c and col <= max_c and
            ans.append(matrix[row][col])
            n_row = row + step[di][0]
            n_col = col + step[di][1]

            if n_row >= 0 and n_row < r and n_col >= 0 and n_col < c and not visited[n_row][n_col]:
                row = n_row
                col = n_col
            else:
                di = (di + 1) % 4
                row += step[di][0]
                col += step[di][1]
        return ans
