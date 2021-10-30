# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for row in range(1, numRows + 1):
            triangle.append([])
            for col in range(row):
                if col == 0 or col == row - 1:
                    triangle[-1].append(1)
                else:
                    triangle[-1].append(triangle[row - 2][col] + triangle[row - 2][col - 1])
        return triangle