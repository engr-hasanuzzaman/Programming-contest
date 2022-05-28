class Solution:
    # Function to find the height of a binary tree.
    def height(self, root):
        if not root:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return max(left_height, right_height) + 1
