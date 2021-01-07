class Solution:
    def minOperation(self, n):
        arr = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            if i % 2 == 0:
                arr[i] = arr[i // 2] + 1
            else:
                arr[i] = min(arr[i//2]+2, arr[i-1]+1)
        return arr[n]
