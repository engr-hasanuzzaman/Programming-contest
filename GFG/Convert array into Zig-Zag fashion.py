# https://practice.geeksforgeeks.org/problems/convert-array-into-zig-zag-fashion1638/1/?page=1&company[]=Amazon&curated[]=1&sortBy=submissions#

class Solution:

    def zigZag(self, arr, n):
        idx = 1
        while idx < n:
            if arr[idx] < arr[idx-1]:
                arr[idx], arr[idx-1] = arr[idx-1], arr[idx]

            if idx + 1 >= n:
                break
            if arr[idx] < arr[idx+1]:
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
            idx += 2
