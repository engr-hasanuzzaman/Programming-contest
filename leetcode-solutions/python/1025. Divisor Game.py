# https://leetcode.com/problems/divisor-game/
# it will return true is any of the divisors will return true

class Solution:
    def divisorGame(self, N: int) -> bool:
      result = [False, False, True, False, True]
      for num in range(5, N+1):
        divisors = []
        d = 1
        own = False
        while d * d <= num:
          if num % d == 0:
            if result[d]:
              own = True
              break
          d += 1
        result.append(own)
      return result[N]
        