# https://leetcode.com/problems/design-an-ordered-stream/

class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * n
        self.cur_idx = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey-1] = value
        if not self.stream[self.cur_idx]:
            return []
        right = self.cur_idx
        while right + 1 < len(self.stream) and self.stream[right + 1]:
            right += 1

        old_idx = self.cur_idx
        self.cur_idx = right + 1
        return self.stream[old_idx:right+1]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
