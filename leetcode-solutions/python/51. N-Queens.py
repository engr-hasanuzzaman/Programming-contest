# https://leetcode.com/problems/n-queens/

from collections import defaultdict

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        c_visited = defaultdict(bool)
        d1_visited = defaultdict(bool)
        d2_visited = defaultdict(bool)
        
        self.back_tracking(0, n, c_visited, d1_visited, d2_visited, ans)
        return ans

    def back_tracking(self, row, n, c_visited, d1_visited, d2_visited, ans, cur_path = []):
        if row == n:
            ans.append(["".join(row) for row in cur_path])
            return
        
        for col in range(n):
            if c_visited[col] or d1_visited[row+col] or d2_visited[col - row + n]:
                continue
            
            row_str = ['.' for _ in range(n)]
            row_str[col] = 'Q'
            
            c_visited[col] = d1_visited[row+col] = d2_visited[col - row + n] = True
            cur_path.append(row_str)
            self.back_tracking(row + 1, n, c_visited, d1_visited, d2_visited, ans)
            c_visited[col] = d1_visited[row+col] = d2_visited[col - row + n] = False
            cur_path.pop()
