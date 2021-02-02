# https://leetcode.com/problems/number-of-closed-islands/
from collections import deque
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
      if not dungeon:
        return
      
      r_size = len(dungeon)
      c_size = len(dungeon[0])
      rq = deque([0]) 
      cq = deque([0])
      visited = [[False] * c_size for _ in range(r_size)]
      life = [[0] * c_size for _ in range(r_size)]
      visited[0][0] = True
      life[0][0] = dungeon[0][0]
      while rq:
        r, c = rq.pop(), cq.pop()
        
        if c - 1 >= 0 and r - 1 >= 0:
          dungeon[r][c] = dungeon[r][c] + max(dungeon[r-1][c], dungeon[r][c-1])
        elif r - 1 >= 0:
          dungeon[r][c] = dungeon[r][c] + dungeon[r-1][c]
        elif c - 1 >= 0:
          dungeon[r][c] = dungeon[r][c] + dungeon[r][c-1]
        print(r, c, dungeon)
        # add down neighbour to the q
        if r + 1 < r_size and not visited[r+1][c]:
          rq.appendleft(r+1)
          cq.appendleft(c)
          visited[r+1][c] = True
          
        # add right neighbour to q
        if c + 1 < c_size  and not visited[r][c+1]:
          rq.appendleft(r)
          cq.appendleft(c+1)
          visited[r][c+1] = True
      print(dungeon)
          
      
        