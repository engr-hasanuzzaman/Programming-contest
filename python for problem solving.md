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
- deque.rotate(n) will rotate clockwise n times
- deque.rotate(-n) will rotate anti-clock wise n times

## list (mutable, that allowed different type of values)
 - 2 ways to create list `l1 = []` & `l2 = list()`
 - `len(l1)` will return list length
 - if `l = [1,2,3]` `l[1:1] = [100]` will be `1,100,2,3`
 - import list methods are `sort, remove(elm), insert(index, val), pop(), reverse(), clear(), count(elm), index(elm), len(list)`
 - do not use `l1 = l2` to copy `l2` to `l1` that copy the reference
 - 4 ways to copy a list `l2 = l1.copy()`, `l2 = list(l1)`, `l2 = l1[:1]` `l2 = [i for i in l1]`
 - uppacking the list `a, *b, c = [1,2,3,4,5,6]` then `a is 1, b is [2,3,4,5] and c is 6 `

 ## tuple
 - 3 ways to create tuple `t1 = (1,2,3)`, `t2 = 4,5,6` and `t3 = tuple([7,8,9])`. N.B: `t4 = (10,)`
 ### diff btw list & tuple
 - tuple is immutable but list emutable as a resutl tuple take small memory and faster operation time `timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]", number=10000000)` take time `0.5227536740003416` but `timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)", number=10000000)` take time `0.08346654900014983` that is much faster