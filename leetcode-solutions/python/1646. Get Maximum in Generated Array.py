# https://leetcode.com/problems/get-maximum-in-generated-array/
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
          return n
        
        ans = [0, 1]
        i = 2
        while n-1 > 0:
          if i % 2 == 0:
            ans.append(ans[i//2])
          else:
            ans.append(ans[i//2] + ans[i//2+1])
          n -= 1
          i += 1
        return max(ans)
