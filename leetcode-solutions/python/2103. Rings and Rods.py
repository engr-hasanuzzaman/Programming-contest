# https://leetcode.com/problems/rings-and-rods/

class Solution:
    def countPoints(self, rings: str) -> int:
        dic = {}
        i = 0
        ans = []
        while i < len(rings):
            c, r = rings[i:i+2]
            if r in dic:
                if c not in dic[r]:
                    dic[r].append(c)
            else:
                dic[r] = [c]
            
            if len(dic[r]) == 3 and r not in ans:
                ans.append(r)
            i += 2
        return len(ans)
