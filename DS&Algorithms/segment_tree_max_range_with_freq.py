class Element:
    def __init__(self, elm, freq = 1) -> None:
        self.data = elm
        self.freq = freq

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
            self._tree[pos] = Element(self.input_arr[low])
            return

        mid = (low + high) // 2
        # build left part
        self.__build_tree(low, mid, self._left_node(pos))
        # build right part
        self.__build_tree(mid + 1, high, self._right_node(pos))
        # update parent node value according to the logic
        self._tree[pos] = self._combine(self._tree[self._left_node(pos)], self._tree[self._right_node(pos)])

    def _left_node(self, parent):
        return parent * 2 + 1

    def _right_node(self, parent):
        return parent * 2 + 2

    def range_quiry(self, ql, qr):
        return self._find_max(0, self.hight, ql, qr, self.root)

    def _combine(self, elm1, elm2):
        if elm1.data > elm2.data:
            return elm1
        elif elm2.data > elm1.data:
            return elm2
        else:
            return Element(elm1.data, elm1.freq + elm2.freq)
    
    def _find_max(self, low, high, ql, qr, pos):
        # print(f"{low}, {high}, {ql}, {qr}, {pos}")
        # out of range. Since we are looking for max element return very small number
        # for min range, return very large number
        if ql > qr:
            # raise Exception('Wrong range')
            return Element(float('-inf'))
        
        if low == ql and high == qr:
            return self._tree[pos]

        mid = (low + high) // 2
        left_node = self._find_max(low, mid, ql, min(qr, mid), self._left_node(pos))
        right_node = self._find_max(mid + 1, high, max(ql, mid+1), qr, self._right_node(pos))
        # print(f"left {left_node.data}, {right_node.data}")
        # print(f"right {left_node.data}, {right_node.data}")
        return self._combine(left_node, right_node)

input = [5,-1,5,10,2,7,10,20,20]
st = SegmentTree(input)
# print(st.range_quiry(1, 6).data)
# print(st.range_quiry(1, 6).freq)
assert st.range_quiry(1, 6).data == 10
assert st.range_quiry(1, 6).freq == 2
assert st.range_quiry(1, 1).data == -1
assert st.range_quiry(1, 1).freq == 1
assert st.range_quiry(0, 2).data == 5 
assert st.range_quiry(0, 8).data == 20 
assert st.range_quiry(0, 8).freq == 2 

"""
- all the operation will be perform on the original array index
- all the comparison will be based on original & passing range value
- if our range on the right part of the array and mid be less than ql that means qr will be < ql
"""
