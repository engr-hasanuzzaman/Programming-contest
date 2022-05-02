# https://leetcode.com/problems/find-median-from-data-stream/

from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        # max_heap will contain first part of the sorted array, so all the number here will be
        # smaller then min_heap
        # min_heap will contains last part of the sorted array, so all the number here will be
        # larger then max_heap
        self.max_heap = []
        self.min_heap = []

    # 9, 3, 5 10, 6, 7, 2 -> 2, 3, 5, 6,7,9,10
    def addNum(self, num: int) -> None:
        if len(self.max_heap) == 0:
            return heappush(self.max_heap, -num)
        
        # min_heap value have to be > max_heap value
        if self.min_heap and self.min_heap[0] < num:
            heappush(self.min_heap, num)
            if len(self.min_heap) > len(self.max_heap):
                heappush(self.max_heap, -heappop(self.min_heap))
        else:
            heappush(self.max_heap, -num)
            if len(self.max_heap) - len(self.min_heap) > 1:
                heappush(self.min_heap, -heappop(self.max_heap))
    

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + -self.max_heap[0]) / 2
        
        return -self.max_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()