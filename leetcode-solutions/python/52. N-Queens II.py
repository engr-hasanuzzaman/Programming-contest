# https://leetcode.com/problems/n-queens-ii/

       
from collections import defaultdict

class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        ans = [0]
        c_visited = defaultdict(bool)
        d1_visited = defaultdict(bool)
        d2_visited = defaultdict(bool)
        
        self.back_tracking(0, n, c_visited, d1_visited, d2_visited, ans)
        return ans[0]

    def back_tracking(self, row, n, c_visited, d1_visited, d2_visited, ans):
        if row == n:
            ans[0] += 1
            return
        
        for col in range(n):
            if c_visited[col] or d1_visited[row+col] or d2_visited[col - row + n]:
                continue
            
           
            c_visited[col] = d1_visited[row+col] = d2_visited[col - row + n] = True
            self.back_tracking(row + 1, n, c_visited, d1_visited, d2_visited, ans)
            c_visited[col] = d1_visited[row+col] = d2_visited[col - row + n] = False

        
        