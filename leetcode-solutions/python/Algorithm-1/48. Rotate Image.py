# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for i in range(size // 2 + size % 2):
            for j in range(size // 2):
                temp = matrix[size - 1 - j][i]
                matrix[size - 1 - j][i] = matrix[size - 1 - i][size - 1 - j]
                matrix[size - 1 - i][size - 1 - j] = matrix[j][size - 1 - i]
                matrix[j][size - 1 - i] = matrix[i][j]
                matrix[i][j] = temp


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        m_row = m_col = size - 1
        # row will be ceil of half
        # col will be floor of half
        for r in range(size // 2 + size % 2):
            for c in range(size // 2):
                temp = matrix[r][c]
                matrix[r][c] = matrix[m_row-c][r]
                matrix[m_row-c][r] = matrix[m_row-r][m_col-c]
                matrix[m_row-r][m_col-c] = matrix[c][m_col-r]
                matrix[c][m_col-r] = temp
