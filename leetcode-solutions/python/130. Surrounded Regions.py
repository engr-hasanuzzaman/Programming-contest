# https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    self.flip(board, i, j)
        
    def flip(self, board, i, j):
        m_row = 0
        m_rol= 0
        m_row = len(board) - 1
        m_col = len(board[0]) - 1
        ans = []
        visited = {}
        # mark visited
        visited[str(i) + str(j)] = True
        
        # keep as row, col         
        stack = [[i, j]]
        on_edge = False
        n_points = [
            [0, -1],
            [0, 1],
            [-1, 0],
            [1, 0]
        ]
        while stack:
            current = stack.pop()
            ans.append(current)
            # check element on the edge or not
            if current[0] == 0 or current[1] == 0 or current[0] == m_row or current[1] == m_col:
                on_edge = True
            
            # pick 4 neighbout
            for i, points in enumerate(n_points):
                n_row = current[0] + points[0]
                n_col = current[1] + points[1]
                key = str(n_row) + str(n_col)
                if n_row >= 0 and n_row <= m_row and n_col >= 0 and n_col <= m_col and key not in visited and board[n_row][n_col] == 'O':
                    # mark visited
                    visited[str(n_row) + str(n_col)] = True
                    stack.append([current[0] + points[0], current[1] + points[1]])
        if not on_edge:
            for i, points in enumerate(ans):
                board[points[0]][points[1]] = 'X'
            
        