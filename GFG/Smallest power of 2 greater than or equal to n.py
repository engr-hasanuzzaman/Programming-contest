class Solution:
    def nearestPowerOf2(self,N):
        if N & (N - 1) == 0:
            return N
        
        p = N
        while p & (p-1) != 0:
            print("the p is {}", p)
            p = p - (p & -p)
        
        return 2*p