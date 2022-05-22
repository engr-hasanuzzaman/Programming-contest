
# Heap with remove method that remove element from heap O(logn) time
# keep idx in a map for constant time access
class Heap:
    def __init__(self, ):
        self.arr = []
        self.idx_map = {}

    def push(self, val):
        new_idx = self.size
        if not val in self.idx_map:
            self.idx_map[val] = {new_idx}
        else:
            self.idx_map[val].add(new_idx)
        self.arr.append(val)
        self._bubble_up(new_idx)

    def pop(self):
        if self.size <= 0:
            raise Exception("pop on empty heap")
            return -1

        self._swap(0, self.size - 1)

        # remove and adjust idx_map
        min_value = self.arr.pop()
        self.idx_map[min_value].remove(self.size)

        # remove mapping if not required anymore
        if len(self.idx_map[min_value]) == 0:
            del self.idx_map[min_value]

        self._bubble_down(0)
        return min_value

    def remove(self, elm):
        if elm not in self.idx_map or len(self.idx_map[elm]) == 0:
            print(f"remove: {elm}, {self.idx_map}")
            raise Exception("Try to remove unknown element")

        idx = list(self.idx_map[elm])[0]
        if idx == 0:
            return self.pop
        elif idx == self.size - 1:
            return self.arr.pop

        self._swap(idx, self.size - 1)
        self.arr.pop()

        self._bubble_up(idx)
        self._bubble_down(idx)

    def _bubble_up(self, idx):
        if idx == 0:
            return

        p_idx = self._parent_idx(idx)
        if self._value(p_idx) > self._value(idx):
            self._swap(p_idx, idx)
            return self._bubble_up(p_idx)

    def _bubble_down(self, idx):
        min_child_idx = self._get_min_child_idx(idx)
        if min_child_idx == -1:
            return

        if self._value(min_child_idx) < self._value(idx):
            self._swap(min_child_idx, idx)
            self._bubble_down(min_child_idx)

    def _get_min_child_idx(self, idx):
        left_child_idx = self._left_child_idx(idx)
        right_child_idx = self._right_child_idx(idx)

        if right_child_idx >= self.size:
            if left_child_idx >= self.size:
                return -1
            else:
                return left_child_idx
        else:
            if self._value(right_child_idx) < self._value(left_child_idx):
                return right_child_idx
            else:
                return left_child_idx

    def _value(self, idx):
        return self.arr[idx]

    def _parent_idx(self, idx):
        return (idx - 1) // 2

    def _left_child_idx(self, idx):
        return 2 * idx + 1

    def _right_child_idx(self, idx):
        return 2 * idx + 2

    def _swap(self, idx1, idx2):
        val1 = self._value(idx1)
        val2 = self._value(idx2)

        if idx1 not in self.idx_map[val1] or idx2 not in self.idx_map[val2]:
            print(
                f"idx_map {self.idx_map}, val1: {val1}, {idx1}, val2: {val2}, {idx2}")
            raise Exception("wrong index, value mapping")

        # update idx mapping
        self.idx_map[val1].remove(idx1)
        self.idx_map[val1].add(idx2)

        self.idx_map[val2].remove(idx2)
        self.idx_map[val2].add(idx1)

        # swap value in arrayt
        self.arr[idx1], self.arr[idx2] = self.arr[idx2], self.arr[idx1]

    @property
    def size(self):
        return len(self.arr)


heap = Heap()
heap.push(4)
heap.push(6)
heap.push(1)
heap.push(10)
heap.push(-10)
print(heap.arr)
print(heap.idx_map)
heap.pop()
print("after pop ", heap.arr, heap.idx_map)
