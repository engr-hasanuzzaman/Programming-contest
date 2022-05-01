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
from heapq import heappop, heappush, heapify,
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pop = heappop
        push = heappush
        # consider n number of sorted list and pick first column
        heap = [(matrix[i][0], i, 0) for i in range(len(matrix))]
        heapify(heap)
        
        for _ in range(k-1):
            # pop the min element and pick elemen from the same row
            _, row, col = pop(heap)
            # last col
            if col == len(matrix[0]) - 1: continue
            # pick next element from the same row as that is potential next smallest value
            push(heap, (matrix[row][col+1], row, col+1))
        return heap[0][0]