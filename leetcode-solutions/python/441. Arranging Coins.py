# https://leetcode.com/problems/arranging-coins/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        start, end = 1, n
        
        while start <= end:
            mid = (end - start) // 2 + start
            sum_of_n = (mid * (mid + 1)) / 2
            if sum_of_n == n:
                return mid
            if sum_of_n > n:
                end = mid - 1
            else:
                start = mid + 1
        return start - 1 
