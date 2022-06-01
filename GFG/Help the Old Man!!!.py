class Solution:
    def shiftPile(self, N, n):
        moves = []
        self.move(N, 1, 3, 2, moves)
        return moves[n-1]

    def move(self, N, start, dest, mid, moves):
        if N == 0:
            return

        # move N-1 plate start to mid using dest
        self.move(N-1, start, mid, dest, moves)
        # move last element from start to dest
        moves.append([str(start), str(dest)])

        # move N-1 plates from mid to dest using start
        self.move(N-1, mid, dest, start, moves)
