class Node:
    def __init__(self, key) -> None:
        self.data = key
        self.left = None
        self.right = None
        self.height = 1


class AvlTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if not root:
            return Node(key)

        if key > root.data:
            root.right = self._insert(root.right, key)
        else:
            root.left = self._insert(root.left, key)

        root.height = self._calculate_height(root)
        balance = self._get_height(root.left) - self._get_height(root.right)

        # rotate if in-balance
        # LL
        if balance > 1 and key < root.left.data:
            return self._rotate_right(root)
        elif balance > 1 and key > root.left.data:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)
        elif balance < -1 and key > root.right.data:
            return self._rotate_left(root)
        elif balance < -1 and key < root.right.data:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def _calculate_height(self, node):
        return 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _get_height(self, node):
        if not node:
            return 0

        return node.height

    def _rotate_right(self, root):
        new_root = root.left
        t3 = new_root.right

        new_root.right = root
        root.left = t3

        # calculare new height of child then parent
        root.height = self._calculate_height(root)
        new_root.height = self._calculate_height(new_root)

        return new_root

    def _rotate_left(self, root):
        new_root = root.right
        t3 = new_root.left

        new_root.left = root
        root.right = t3

        # calculare new height of child then parent
        root.height = self._calculate_height(root)
        new_root.height = self._calculate_height(new_root)

        return new_root

# check 
class TestAvl:
    def __init__(self) -> None:
        self.check_left_left_rotate(AvlTree())
        self.check_right_right_rotate(AvlTree())
        self.check_right_left_rotate(AvlTree())
        self.check_left_right_rotate(AvlTree())

    def check_left_left_rotate(self, a):
        a.insert(3)
        a.insert(2)
        a.insert(1)

        assert a.root.data == 2

    def check_right_right_rotate(self, a):
        a.insert(1)
        a.insert(2)
        a.insert(3)

        assert a.root.data == 2

    def check_left_right_rotate(self, a):
        a.insert(7)
        a.insert(4)
        a.insert(6)

        assert a.root.data == 6

    def check_right_left_rotate(self, a):
        a.insert(3)
        a.insert(8)
        a.insert(6)

        assert a.root.data == 6


if __name__ == '__main__':
    TestAvl()