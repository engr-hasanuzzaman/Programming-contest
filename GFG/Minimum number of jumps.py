class Solution:
    def minJumps(self, arr, n):
        if n <= 1:
            return 0
        if arr[0] == 0:
            return -1

        left = right = 0
        count = 0
        max_reach = 0
        while right < n - 1:
            for i in range(left, right + 1):
                max_reach = max(max_reach, i+arr[i])
            if right >= max_reach:
                return -1
            left = right + 1
            count += 1
            right = max_reach

        return count
