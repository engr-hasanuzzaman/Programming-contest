# https://leetcode.com/problems/stone-game/

# Greedy choice (First move alway win based on the provided conditions)
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        stones = [0, 0]
        turn = 0 # even means Alice's turn
        while piles:
            # base cases
            if len(piles) == 2:
                if piles[0] > piles[1]:
                    stones[0] += piles[0]
                    stones[1] += piles[1]
                else:
                    stones[1] += piles[0]
                    stones[0] += piles[1]
                piles = []
            elif (piles[0] - piles[1]) > (piles[-1] - piles[-2]):
                stones[turn % 2] += piles[0]
                piles = piles[1:]
            else:
                stones[turn % 2] += piles[-1]
                piles = piles[:-1]
        return stones[0] > stones[1]
