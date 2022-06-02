# https://www.geeksforgeeks.org/boundary-traversal-of-binary-tree

class Solution:
    def printBoundaryView(self, root):
        if not root:
            return []

        self.ans = [root.data]
        # left traversal will come from only left side (could be right child of left child)
        self.left_traverse(root.left)

        # making separate call to handle single node condition otherwise single node will print two times
        self.leaf_traverse(root.left)
        self.leaf_traverse(root.right)

        # right side will come from right sub-tree
        self.right_traverse(root.right)
        return self.ans

    def left_traverse(self, root):
        if not root:
            return
        # skip leaf node
        if not root.left and not root.right:
            return

        self.ans.append(root.data)
        self.left_traverse(root.left)
        if not root.left:
            self.left_traverse(root.right)

    def right_traverse(self, root):
        if not root:
            return
        # skip leaf node
        if not root.left and not root.right:
            return

        # traverse in reverse order
        self.right_traverse(root.right)
        if not root.right:
            self.right_traverse(root.left)
        self.ans.append(root.data)

    def leaf_traverse(self, root):
        if not root:
            return

        if not root.left and not root.right:
            self.ans.append(root.data)

        self.leaf_traverse(root.left)
        self.leaf_traverse(root.right)
