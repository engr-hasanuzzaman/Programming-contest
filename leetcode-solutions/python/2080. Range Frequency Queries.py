from collections import defaultdict
from copy import copy

# Memory Limit Exceed solution


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.frequencies = []
        frequency = defaultdict(int)
        frequency[arr[0]] += 1
        self.frequencies.append(frequency)
        for i in arr[1:]:
            pre_freq = copy(self.frequencies[-1])
            pre_freq[i] += 1
            self.frequencies.append(pre_freq)

    def query(self, left: int, right: int, value: int) -> int:
        l_freq, r_freq = self.frequencies[max(
            left-1, 0)], self.frequencies[right]
        if left == 0:
            return r_freq[value]
        else:
            return r_freq[value] - l_freq[value]


# using binary search
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.frequency = defaultdict(list)
        for i, n in enumerate(arr):
            self.frequency[n].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        idxs = self.frequency[value]
        # bisect_right return right most position for new insertion that means
        # if right most index for target is j, it will j+1
        # bisect_left will return left most postion for insertion
        # if value exist, will return first occurence of value otherwise idx of lower number
        return bisect.bisect_right(idxs, right) - bisect.bisect_left(idxs, left)
