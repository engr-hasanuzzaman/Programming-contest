# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        size = len(mat)
        for _ in range(4):
            self.rotate(mat)
            if mat == target: 
                return True
        return False

    def rotate(self, mat):
        size = len(mat)
        for i in range(size // 2 + size % 2):
            for j in range(size // 2):
                temp = mat[size - 1 - j][i]
                mat[size - 1 - j][i] = mat[size - 1 - i][size - 1 - j]
                mat[size - 1 - i][size - 1 - j] = mat[j][size - 1 - i]
                mat[j][size - 1 - i] = mat[i][j]
                mat[i][j] = temp
