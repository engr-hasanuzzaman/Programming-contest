# https://leetcode.com/problems/robot-bounded-in-circle/

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # up, left, down, right
        direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        rotation = 0
        # rotation counter
        i = 0
        # start from the original point
        x = y = 0
        for _, ins in enumerate(instructions):
            if ins == 'L':
                # left + left = down
                # left + left + left = right
                # if we perform same operation 4 times, that measnt 360 degree
                i = (i + 1) % 4 
            elif ins == 'R':
                # right + right + right = left
                # right + right = down
                i = (i + 3) % 4
            else:
                x = x + direction[i][0]
                y = y + direction[i][1]
        return (x == 0 and y == 0) or i != 0
        