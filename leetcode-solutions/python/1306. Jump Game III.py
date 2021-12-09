# https://leetcode.com/problems/jump-game-iii/

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        s = [start]
        visited = [None] * len(arr)
        visited[start] = True
        while s:
            size = len(s)
            temp = []
            for _ in range(size):
                cur = s.pop()
                visited[cur] = True
                if arr[cur] == 0:
                    return True
                r_neighbour = arr[cur] + cur
                l_neighbour = cur - arr[cur]
                if r_neighbour >= 0 and r_neighbour < len(arr) and not visited[r_neighbour]:
                    temp.append(r_neighbour)
                if l_neighbour >= 0 and l_neighbour < len(arr) and not visited[l_neighbour]:
                    temp.append(l_neighbour)
            s = temp
        return False
