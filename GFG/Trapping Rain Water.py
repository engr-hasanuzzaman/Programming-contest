# https://practice.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1/?page=1&company[]=Amazon&curated[]=1&sortBy=submissions#

class Solution:
    def trappingWater(self, arr, n):
        # Code here
        max_lefts = [0] * n
        max_rights = [0] * n
        max_left = arr[0]
        max_right = arr[-1]
        left = 0
        right = n - 2
        for _ in range(1, n):
            max_lefts[left] = max_left
            max_left = max(arr[left], max_left)

            max_rights[right] = max_right
            max_right = max(arr[right], max_right)
            left += 1
            right -= 1
        ans = 0
        for idx in range(1, n - 1):
            min_wall_size = min(max_lefts[idx], max_rights[idx])
            ans += max(min_wall_size - arr[idx], 0)
        return ans
