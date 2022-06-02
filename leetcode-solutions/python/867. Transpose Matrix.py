# https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row_size = len(matrix)
        col_size = len(matrix[0])
        new_matrix = [[0] * row_size for _ in range(col_size)]

        for col in range(col_size):
            for row in range(row_size):
                new_matrix[col][row] = matrix[row][col]

        return new_matrix
