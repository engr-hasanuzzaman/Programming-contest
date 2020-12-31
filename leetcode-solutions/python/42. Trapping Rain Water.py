# https://leetcode.com/problems/trapping-rain-water/
# Algorithm: 
# find the max neighbour for i (left neighbour with max, right neighbour with max)
# ith contribution is max(min left & gith neighbour - ith height, 0)
# zero (o) for ensure discard negetive contribution
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
             return 0
        max_n = [[0, 0] for _ in range(len(height))] 
        
        max_left = height[0]
        for i in range(1, len(height) - 1):
             max_n[i][0] += max_left
             max_left = max([max_left, height[i]])
        
        max_right = height[-1]
        for j in range(len(height) - 2, -1, -1):
            max_n[j][1] = max_right
            max_right = max([max_right, height[j]])
        
        total_water = 0
        for i in range(1, len(height) - 1):
            val = max([min(max_n[i]) - height[i], 0])
            total_water += val
        return total_water