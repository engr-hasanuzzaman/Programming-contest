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
    
# linear solution
# Algorith
# 1. Start with the max width (first & last item) and calculate the area
# 2. find the next larget element of the min val side and recalculate area and update if current one is max
# 3. repeate the step 2 untill left & right same
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_val = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if min([height[left], height[right]]) * (right - left) > max_val:
                max_val = min([height[left], height[right]]) * (right - left)
            if height[left] > height[right]:
                c_right = height[right]
                right -= 1
                while right > left and height[right] <= c_right:
                    right -= 1
            else:
                c_left = height[left]
                left += 1
                while left < right and height[left] <= c_left:
                    left += 1
        return max_val