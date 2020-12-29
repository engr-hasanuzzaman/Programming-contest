# https://leetcode.com/problems/top-k-frequent-words/
from heapq import heapify, heappop
import collections
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        heap = [(-val, key) for key, val in count.items()]
        heapify(heap)
        return [heappop(heap)[1] for _ in range(k)]