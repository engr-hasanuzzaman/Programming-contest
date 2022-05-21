class Node:
    def __init__(self, key) -> None:
        self.data = key
        self.left = None
        self.right = None
        self.height = 1


class AvlTree:
    def __init__(self) -> None:
        self.root = None

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
        if balance > 1 and key < root.left:
            self._rotate_right(root)
        elif balance > 1 and key > root.left:
            root.left = self._rotate_left(root.left)
            self._rotate_right(root)
        elif balance < -1 and key > root.right:
            self._rotate_left(root)
        elif balance < -1 and key < root.right:
            root.right = self._rotate_right(root.right)
            self._rotate_left(root)

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
