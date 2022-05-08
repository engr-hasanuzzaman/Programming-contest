# https://leetcode.com/problems/lru-cache/

from collections import OrderedDict

# by defalult OrderedDict works as stack, pop, push happened on the end


class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1

        # move to first abc ->cba (key is c)
        self._cache.move_to_end(key, last=False)
        # print(f"get {key}, {self._cache}")
        return self._cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self._cache and len(self._cache) == self._capacity:
            self._cache.popitem()

        self._cache[key] = value
        # move element to top
        self.get(key)
        # print(f"put {key}, {self._cache}")


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
