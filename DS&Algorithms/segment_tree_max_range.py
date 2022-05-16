class SegmentTree:
    def __init__(self, arr):
        self.input_arr = arr
        self.low = 0
        self.hight = len(arr) - 1
        self.root = 0
        self._tree = [float('inf')] * (4 * len(arr))
        self.__build_tree(0, len(arr) - 1, 0)

    # pos is the root's postion for the current recursion
    # if we have more element left recursively builds left & right sub-tree then update
    # root node's value based on the min/max/sum range logic
    def __build_tree(self, low, high, pos):
        if low == high:
            self._tree[pos] = self.input_arr[low]
            return

        mid = (low + high) // 2
        # build left part
        self.__build_tree(low, mid, self._left_node(pos))
        # build right part
        self.__build_tree(mid + 1, high, self._right_node(pos))
        # update parent node value according to the logic
        self._tree[pos] = max(self._tree[self._left_node(pos)], self._tree[self._right_node(pos)])

    def _left_node(self, parent):
        return parent * 2 + 1

    def _right_node(self, parent):
        return parent * 2 + 2

    def range_quiry(self, ql, qr):
        return self._find_max(0, self.hight, ql, qr, self.root)


    def _find_max(self, low, high, ql, qr, pos):
        # out of range. Since we are looking for max element return very small number
        # for min range, return very large number
        if ql > qr:
            # raise Exception('Wrong range')
            return float('-inf')
        
        if low == ql and high == qr:
            return self._tree[pos]

        mid = (low + high) // 2
        return max(
            self._find_max(low, mid, ql, min(qr, mid), self._left_node(pos)),
            self._find_max(mid + 1, high, max(ql, mid+1), qr, self._right_node(pos)),
            )

input = [5,3,-1,5,10,2,7,9,20]
st = SegmentTree(input)
assert st.range_quiry(1, 6) == 10 
assert st.range_quiry(1, 1) == 3 
assert st.range_quiry(0, 2) == 5 
assert st.range_quiry(0, 8) == 20 

"""
- all the operation will be perform on the original array index
- all the comparison will be based on original & passing range value
- if our range on the right part of the array and mid be less than ql that means qr will be < ql
"""
