# https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

# solution using heapq
from heapq import heapify, heappop, heappush
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(n) for _, n in enumerate(nums)]
        min_heap = nums[:k]
        heapify(min_heap)
      
        for i in range(k, len(nums)):
            num = nums[i]
            if num > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, num)
        return str(min_heap[0])
        