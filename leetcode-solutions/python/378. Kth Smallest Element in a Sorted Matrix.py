# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

from heapq import heappop, heappush, heapify, heappushpop

# complexity is (n*m) * klogk
# improvement point?: we are visiting all the elements but can we check only required elements?
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pop = heappop
        push = heappush
        heap = []
        heapify(heap)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                val = matrix[i][j]
                if len(heap) == k:
                    if -heap[0] > val:
                        heappushpop(heap, -val)
                else:
                    heappush(heap, -val)
        return -heap[0]

# alternative approach
# if we consider each row as sorted individual list, then this problem is 
# similar to merge n sorted list problem