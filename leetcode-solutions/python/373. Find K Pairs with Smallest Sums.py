# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

from heapq import heappop, heappush


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        M = len(nums1)
        N = len(nums2)
        heap = []
        ans = []
        # first take all the element from nums1
        for i in range(M):
            self.add(heap, nums1, nums2, i, 0)

        while k > 0 and heap:
            _, i, j = heappop(heap)
            ans.append([nums1[i], nums2[j]])
            self.add(heap, nums1, nums2, i, j+1)
            k -= 1

        return ans

    def add(self, heap, nums1, nums2, i, j):
        if j >= len(nums2):
            return
        heappush(heap, (nums1[i] + nums2[j], i, j))
