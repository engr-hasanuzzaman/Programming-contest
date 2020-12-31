# https://leetcode.com/problems/container-with-most-water/
# brute forse solution. Consider all pair and find the max
# Time complexity O(n*2)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_val = 0
        left = 0
        right = 0
        for i in range(len(height)):
            left_line = height[i]
            for j in range(i+1, len(height)):
                if (j-i) * min([left_line, height[j]]) > max_val:
                    left = i
                    right = j
                    max_val = (j-i) * min([left_line, height[j]])
        return max_val
    