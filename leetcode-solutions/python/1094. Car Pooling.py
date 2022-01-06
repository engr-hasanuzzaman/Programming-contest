# https://leetcode.com/problems/car-pooling/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        visit = [0] * 1001
        
        for t in trips:
            visit[t[1]] += t[0]
            visit[t[2]] -= t[0]

        sum = 0
        for v in visit:
            sum += v
            if sum > capacity:
                return False
        return True
