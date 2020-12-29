# https://leetcode.com/problems/kth-largest-element-in-a-stream/
# use python builtin heapq for min-heap implementation to solve this problem
# in this problem we have to find the k-th max number so we are only interested with
# top max k elements. If we create a min heap of the size k and then on the top we will have the
# k-th largest element. During insert, if upcoming value is less then top value discard or 
# replace the top with new value (we do not need old top now as this will be lesser than k-th) and hepify
# so, new top will be k-th element
from heapq import heapify, heapreplace, heappush
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.hp = nums[:k]
        self.k = k
        heapify(self.hp)
        for n in nums[k:]:
            if self.hp[0] < n:
                heapreplace(self.hp, n)

    def add(self, val: int) -> int:
        # ensure hp is not empty (handl k-th is 1 and do not have value now) 
        if len(self.hp) < self.k:
            heappush(self.hp, val)
            return self.hp[0]
        
        if val > self.hp[0]:
            heapreplace(self.hp, val)
            
        return self.hp[0]