# Ruby pry binding like debugging
```python
impory code
code.interact(local=dict(globals(), **locals()))
```
# important SDL for competetive programming
- python follow **alllowercase** naming convention
## collections
- `collections.Counter(words)` where is `words` list of strings that return dictionary containing `word` as key and the frequency as value
- `for index, val in enumerate([2,3,4])` for accessing both index and item
- `a, *b = [1,2,3]` will be `a: 1, b: [2,3]`

## heapq
### provide heap DS (min heap) with the helper function `heapify, heappush, heappop, heapreplace`
- `heapq.nlargest(n, list)` will return heap containing n largest element
- `heapq.nsmallest(n, list)` will return heap containing n smallest element

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
 - `for i, n in enumerate(li)` will return list element with index 
 ## tuple
 - 3 ways to create tuple `t1 = (1,2,3)`, `t2 = 4,5,6` and `t3 = tuple([7,8,9])`. N.B: `t4 = (10,)`
 ### diff btw list & tuple
 - tuple is immutable but list emutable as a resutl tuple take small memory and faster operation time `timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]", number=10000000)` take time `0.5227536740003416` but `timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)", number=10000000)` take time `0.08346654900014983` that is much faster

 ## dictionary
 - create dictionary. `d = {'a': 1, 'b': 2}` and `d2 = dict('a'=1, 'b'=2)`. N.B: for later one do not need to use string close
 - delete item from dic
    - del dict['key']
    - dict.pop('key')
    - dict.popitems() (python 3.7 it will remove last insert item)
- loop over dict
    - `for key in dict`
    - `for key in dict.keys()`
    - `for value in dict.values()`
    - `for key, val in dict.items()`
## sets
- `s1 = {1,2,3,4}` `s2=set([1,2,3])`. N.B: `ss = {}` will create empty dict, correct way to create empty set is `es = set()`
- `set.add(elm)`, `set.remove(elm)` this will raise error if element is not in set. Safer method is `s.discard()`
- `sc = set("hello")` will create set `{'h', 'l', 'o', 'e'}`
- set method `clear, pop, union, intersection, update, s1.intersection_update(s2), s1.difference_update(s2), s1.issubset(s2) s1.issuperset(s2), s1.isdisjoint(s2)`,
- `s1.difference(s1)` will show diff from s1 only but `s1.symmetric_difference(s2)` will list non-common element from both sets`
- `frozenset`

## string (immutable datastructure)
- N.B: since string is immutable, all the string method return new string
- `str.upper(), str.lower(), startwith, endwith, find, count, replace, split()`
- str formatting `"the price is {:.2f}".format(p)` after point two value. Using `f` string (from python 3.6) `f"the price is {p:.10f}"`

## collections
- important iteams from `collections` are `Counter,namedtuple, OrderedDict, defaultdict, deque`
- `Counter(stc).most_common(1)` [] of tuple
- `namedtuple` like `structure`
- `defaultdict(int/list)` 

## itertools
- common usefull itertools are `product, permutation, accumulate, combinations, groupby and infinite iterators`
- `list(product([1,2], [3,4]))` is `[1,3], [1,4], [2,3], [2,4]`. `product` take another optional parameter called `repead=number`
- `permutation` will run permutaion over all the possibles position. `permutation([1,2,3], 2)` will take 2 elements at a time and made permutation `[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]`
- `list(itertools.combinations_with_replacement([1,2,3], 2))` is `[(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]` here same element will be used to make combination also
- `list(itertools.accumulate([1,2,3,4]))` is `[1, 3, 6, 10]`. `list(itertools.accumulate([1,2,3,4], func=operator.mul))` is `[1, 2, 6, 24]`, `list(itertools.accumulate([1,4,3,4], func=max))` is `[1, 4, 4, 4]`. If we use min instead it will be `[1,1,1,1]`
- `dict(itertools.groupby([{'name': 'a', 'age': 25}, {'name': 'b', 'age': 26}, {'name': 'c', 'age': 25}], key=lambda o: o['age']))` that will group the elements by age
