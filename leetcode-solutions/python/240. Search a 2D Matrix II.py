# https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = len(matrix)
        N = len(matrix[0])

        # start from top right corner
        row = 0
        col = N - 1

        while row >= 0 and row < M and col >= 0 and col < N:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                # in lowere we have higher value
                row += 1
            else:
                col -= 1
        return False
