# https://leetcode.com/problems/set-matrix-zeroes/

from collections import defaultdict


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = defaultdict(bool)
        cols = defaultdict(bool)
        # left, right, top, bottom
        self.neighbors = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    rows[row] = True
                    cols[col] = True

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if rows[row] or cols[col]:
                    matrix[row][col] = 0
