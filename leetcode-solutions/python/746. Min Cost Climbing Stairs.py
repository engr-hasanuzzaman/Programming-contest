# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [cost[0], cost[1]]
        
        for i in range(2, len(cost)):
            cost[i] = min(cost[i-1], cost[i - 2]) + cost[i]
        # print(cost)
        return min(cost[-1], cost[-2])
