# https://leetcode.com/problems/perfect-number/

import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        total = 1
        sqrt = math.floor(math.sqrt(num))
        n = 2
        while n <= sqrt:
            if num % n == 0:
                if num / n == n:
                    total += n
                else:
                    total += n
                    total += (num / n)
            n += 1
        return total == num
    