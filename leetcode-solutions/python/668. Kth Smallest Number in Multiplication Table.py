# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # the range of the number in this table is 1 to m * n
        # we will looking how many number existin in the table which are less or equal to a certain number
        # and based on that we will find the k the smallest number
        low, high, mid, ans = 1, m * n, 0, 0
        
        while low <= high:
            mid = (high - low) // 2 + low
            count = self.count(mid, m, n)
            if count < k:
                low = mid + 1
            else:
                high = mid - 1
                # mid could be the potential candidate ans or might find lower number
                ans = mid
        return ans
    # how many number exist in the table which are smaller or equal to x
    # if i is row the then number in row i is i, 2*i, 3*i ....n*i
    # if N is the number smaller or equal to x then N*i <= x, so, N <= x / i
    def count(self, x, m, n):
        count = 0
        for i in range(1, m+1):
            # since x // i coult be larger then n
            count += min( x // i, n)
        return count
