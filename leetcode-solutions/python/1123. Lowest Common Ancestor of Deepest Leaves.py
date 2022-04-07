# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth = {None: -1}

        def mark_depth(root, parent = None):
            if not root:
                return
            
            depth[root] = depth[parent] + 1
            mark_depth(root.left, root)
            mark_depth(root.right, root)

        mark_depth(root)
        max_depth = max(depth.values())
        
        def find_lca(node):
            if not node or depth[node] == max_depth:
                return node
            
            left, right = find_lca(node.left), find_lca(node.right)
            return node if left and right else left or right
        
        return find_lca(root)
