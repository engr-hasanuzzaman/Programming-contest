# https://leetcode.com/problems/my-calendar-i/

class MyCalendar:

    def __init__(self):
        self.st = SegmentTree()

    def book(self, start: int, end: int) -> bool:
        node = Node(start, end)
        return self.st.add(node)


class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self):
        self.root = None

    def add(self, node):
        if not self.root:
            self.root = node
            return True
        return self._add(self.root, node) != False

    def _add(self, root, node):
        if not root:
            return node

        if root.end <= node.start:
            r_val = self._add(root.right, node)
            if r_val == False:
                return False
            root.right = r_val
        elif root.start >= node.end:
            l_val = self._add(root.left, node)
            if l_val == False:
                return False
            root.left = l_val
        else:
            return False

        return root

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
