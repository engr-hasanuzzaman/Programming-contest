# https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # if reshep is not possible         
        if len(mat) * len(mat[0]) != r * c:
            return mat
        
        new_row =[]
        new_matrix = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                new_row.append(mat[i][j])
    
                if len(new_row) == c:
                    new_matrix.append(new_row)
                    # resetting
                    new_row = []
                    
        return new_matrix
