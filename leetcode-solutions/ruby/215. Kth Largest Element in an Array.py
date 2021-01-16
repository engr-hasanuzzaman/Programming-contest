# using min heap
# Find the kth largest element in an unsorted array. 
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# if we create a min heap size k then our expected value will be the root of the heap
from heapq import heapify, heappushpop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      hp = nums[:k]
      heapify(hp)
      for i in range(k, len(nums)):
        if nums[i] > hp[0]:
          heappushpop(hp, nums[i])
      return hp[0]
      
