# https://practice.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1/?page=2&curated[]=1&sortBy=submissions
from collections import deque


class Solution:

    # Function to find maximum of each subarray of size k.
    def max_of_subarrays(self, arr, n, k):
        queue = deque([])
        for idx in range(k):
            while queue and arr[queue[-1]] < arr[idx]:
                queue.pop()
            queue.append(idx)

        ans = []
        for idx in range(k, n):
            ans.append(arr[queue[0]])

            # remove element outside the windo
            while queue and queue[0] <= idx - k:
                queue.popleft()
            while queue and arr[queue[-1]] < arr[idx]:
                queue.pop()
            queue.append(idx)
        ans.append(arr[queue[0]])
        return ans
