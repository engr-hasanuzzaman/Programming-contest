# https://leetcode.com/problems/subrectangle-queries/

class SubrectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        self.rec = rectangle
        self.operations = []
    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.operations.append([row1, col1, row2, col2, newValue])

    def getValue(self, row: int, col: int) -> int:
        for i in range(len(self.operations) - 1, -1, -1):
            if row >= self.operations[i][0] and row <= self.operations[i][2] and col >= self.operations[i][1] and col <= self.operations[i][3]:
                return self.operations[i][4]
        return self.rec[row][col]
