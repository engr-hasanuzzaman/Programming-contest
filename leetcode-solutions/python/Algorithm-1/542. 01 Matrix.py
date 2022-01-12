# https://leetcode.com/problems/01-matrix/

from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        distance = []
        r_size = len(mat)
        c_size = len(mat[0])
        q = deque([])
        for row in range(r_size):
            data = []
            for col in range(c_size):
                if mat[row][col] == 1:
                    data.append(float('inf'))
                else:
                    data.append(0)
                    q.append([row, col])
            distance.append(data)

        neighbors = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        while q:
            row, col = q.popleft()
            dis = distance[row][col]
            for r, c in neighbors:
                n_row = row + r
                n_col = col + c
                if n_row >= 0 and n_row < r_size and n_col >= 0 and n_col < c_size and distance[n_row][n_col] > dis + 1:
                    distance[n_row][n_col] = dis + 1
                    q.append([n_row, n_col])
        
        return distance
