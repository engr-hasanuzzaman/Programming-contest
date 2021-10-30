# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku = {
            'r0': {},'r1': {},'r2': {},'r3': {},'r4': {},'r5': {},'r6': {},'r7': {},'r8': {},
            'c0': {},'c1': {},'c2': {},'c3': {},'c4': {},'c5': {},'c6': {},'c7': {},'c8': {},
            's00': {},'s01': {},'s02': {},'s10': {},'s11': {},'s12': {},'s20': {},'s21': {},'s22': {},
        }
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                r = 'r' + str(i);
                c = 'c' + str(j);
                s = 's' + str(i // 3) + str(j // 3);
                number = board[i][j]
                if number != '.':
                    if  number in sudoku[r] or number in sudoku[c] or number in sudoku[s]:
                        print(sudoku)
                        return False
                    sudoku[r][number] = True
                    sudoku[c][number] = True
                    sudoku[s][number] = True
        return True
