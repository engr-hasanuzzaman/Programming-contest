# https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        
        while True:
            target = (right+left) // 2
            g = guess(target)
            if g == 0:
                return target
            elif g == 1:
                left = target + 1
            else:
                right = target - 1
            