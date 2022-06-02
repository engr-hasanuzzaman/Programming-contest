'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return True is Tree is SumTree else return False

# Flag based solution


class Solution:
    def isSumTree(self, root):
        # flag to indicate sub-node full-fill sum tree property or not
        # to prevent re-visiting the nodes
        self.sum_tree = True
        self.cal_sum(root)
        return self.sum_tree

    def cal_sum(self, root):
        if not self.sum_tree or not root:
            return 0

        if not root.left and not root.right:
            return root.data

        left_sum = self.cal_sum(root.left)
        right_sum = self.cal_sum(root.right)
        if root.data != (left_sum + right_sum):
            self.sum_tree = False

        return root.data + left_sum + right_sum


# O(N) solution without flag
class Solution:
    def isSumTree(self, root):
        return self.cal_sum(root) != float('inf')

    def cal_sum(self, root):
        if not root:
            return 0

        # handle leaf node
        if not root.left and not root.right:
            return root.data

        left_sum = self.cal_sum(root.left)
        if left_sum == float('inf'):
            return float('inf')

        right_sum = self.cal_sum(root.right)
        if right_sum == float('inf'):
            return float('inf')

        if root.data != (left_sum + right_sum):
            return float('inf')

        return root.data + left_sum + right_sum
