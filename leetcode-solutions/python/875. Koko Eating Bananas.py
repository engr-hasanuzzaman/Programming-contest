# https://leetcode.com/problems/koko-eating-bananas/

import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        start, end = 1, piles[-1]
        
        while start < end:
            speed = (start + end) // 2
            if self.canEatAllWithCount(piles, speed, h):
                end = speed
            else:
                start = speed + 1
        return start
            
    def canEatAllWithCount(self, piles, speed, hours):
        for pile in piles:
            hours -= math.ceil(pile / speed)
            if hours < 0:
                return False
        return True
