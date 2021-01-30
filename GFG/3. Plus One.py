class Solution:
    def increment(self, arr, N):
        rem = 1
        for i in range(N-1, -1, -1):
            # print()
            if arr[i]  == 9:
                arr[i] = 0
                rem = 1
            else:
                arr[i] += rem
                rem = 0
                break
        if rem == 1:
            arr.insert(0, 1)
        return arr