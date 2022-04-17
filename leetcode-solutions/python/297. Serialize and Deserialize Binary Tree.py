# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "null,"
        # pre-order traversal
        return str(root.val) + ',' + self.serialize(root.left) + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(',')
        # remove last extra ,
        nodes.pop()
        # revering to perform pop otherwise have to use deque for popleft
        nodes = nodes[::-1]

        def build_tree(nodes):
            val = nodes.pop()
            if val == 'null':
                return None
            node = TreeNode(int(val))
            node.left = build_tree(nodes)
            node.right = build_tree(nodes)

            return node
        return build_tree(nodes)
