# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.row_size = len(matrix)
        self.col_size = len(matrix[0])
        self.matrix = matrix
        self.prefix_sum = [[0] * self.col_size for _ in range(self.row_size)]
        self.prepare_prefix_sum()

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # in b and c d is included that means we are removing d two times
        # that's way we are adding d again
        a = self.prefix_sum[row2][col2]
        b = self.prefix_sum[row2][col1-1] if col1 - 1 >= 0 else 0
        c = self.prefix_sum[row1-1][col2] if row1-1 >= 0 else 0
        d = self.prefix_sum[row1-1][col1-1] if col1 - \
            1 >= 0 and row1 - 1 >= 0 else 0

        return a - b - c + d

    def prepare_prefix_sum(self):
        # first row
        self.prefix_sum[0][0] = self.matrix[0][0]
        for j in range(1, self.col_size):
            self.prefix_sum[0][j] = self.prefix_sum[0][j-1] + self.matrix[0][j]

        # first col
        for i in range(1, self.row_size):
            self.prefix_sum[i][0] = self.prefix_sum[i-1][0] + self.matrix[i][0]

        for i in range(1, self.row_size):
            for j in range(1, self.col_size):
                # self.prfix_sum[i-1][j-1] has added on both self.prfix_sum[i-1][j] and self.prfix_sum[i][j-1]
                self.prefix_sum[i][j] = self.prefix_sum[i-1][j] + \
                    self.prefix_sum[i][j-1] - \
                    self.prefix_sum[i-1][j-1] + self.matrix[i][j]
