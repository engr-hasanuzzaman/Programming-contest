# https://leetcode.com/problems/fibonacci-number/

# dynamic programming
class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def findFebo(n):
            if n <= 1:
                return n
            
            if n in memo:
                return memo[n]
            
            febo = findFebo(n - 1) + findFebo(n - 2)
            memo[n] = febo
            return febo
        return findFebo(n)

# shoter code with dynamic programming
class Solution:
    def fib(self, n: int) -> int:
        dp = [0, 1]
        
        for i in range(2, n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]

# normal solution with const memory
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
    
        f_prev = 0
        s_prev = 1
        for i in range(2, n+1):
            temp = s_prev
            s_prev = s_prev + f_prev
            f_prev = temp
        return s_prev