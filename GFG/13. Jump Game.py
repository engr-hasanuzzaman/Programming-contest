# keep track of max reachable index and iterate each element at a time
# if current index is > max reachable at that time, that means not reachable
class Solution:
    def canReach(self, A, N):
        max_reach = A[0]
        i = 1
        for i in range(1, N):
            if i > max_reach:
                return 0
            
            max_reach = max(max_reach, i + A[i])
        if max_reach >= N - 1:
            return 1
        else:
            return 0