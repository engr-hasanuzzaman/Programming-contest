class Solution:
    def nearestPowerOf2(self,N):
        # if original N is power of tow
        if N & (N - 1) == 0:
            return N
        
        # if not power of two
        while N & (N-1) != 0:
            # (N & -N) extract lower set bit means if N == 1100
            # (N & -N) will be = 100, that leads to N - (N & -N) -> 1100 - 100 = 1000
            # in this process we will extract lower set bit untill only one set bit present
            # that is lower number power of two of the original N 
            N = N - (N & -N)
        
        # return double of lower power of original N
        return 2*N