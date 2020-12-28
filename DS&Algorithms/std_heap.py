# in-defalut heapq is min heap. If we need max heap we can mul each element with -1 
from heapq import heapify, heappop, heappush
hp = [19,4, 4,13,20,2]
heapify(hp)
print("after heapify", hp)