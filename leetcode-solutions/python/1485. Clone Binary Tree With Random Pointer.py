# https://leetcode.com/problems/clone-binary-tree-with-random-pointer/

# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        container = {}

        def copy(root):
            if not root:
                return root
            if root in container:
                return container[root]

            new_node = NodeCopy(root.val)
            container[root] = new_node

            new_node.left = copy(root.left)
            new_node.right = copy(root.right)
            new_node.random = copy(root.random)
            return new_node

        return copy(root)
