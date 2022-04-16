# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1] * n

        for row in range(1, m):
            temp = []
            for col in range(n):
                if col == 0:
                    temp.append(1)
                else:
                    temp.append(temp[col-1] + prev[col])
            prev = temp

        return prev[-1]
