class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        ans = arr[-1] - arr[0]
        smallest = arr[0] + k
        largest = arr[-1] - k

        for i in range(n-1):
            c_min = min(smallest, arr[i+1] - k)
            c_max = max(largest, arr[i] + k)
            ans = min(ans, c_max - c_min)
        return ans
