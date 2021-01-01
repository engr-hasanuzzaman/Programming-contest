# important SDL for competetive programming

## collections
- `collections.Counter(words)` where is `words` list of strings that return dictionary containing `word` as key and the frequency as value
- `for index, val in enumerate([2,3,4])` for accessing both index and item
- `a, *b = [1,2,3]` will be `a: 1, b: [2,3]`

## heapq
### provide heap DS (min heap) with the helper function `heapify, heappush, heappop, heapreplace`

## collctions.deque for pop & push on the both end with constant time O(1)
- under the hood, deque use the doubly linked list that is optimized for push, pop from both end
- popleft & appendleft are the operation for shift & unshitf operation