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


# solution using Eulerian path
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # e_ -> Eulerian depth/index
        e_depth = []
        e_nodes = []
        last_visit = {}
        # 1 -> 2 -> 3 ->2 ->
        def eulerian_tour(root, depth=0):
            if not root: return
            visit(root, depth)
            # root node
            if not root.left and not root.right: return
            if root.left:
                eulerian_tour(root.left, depth+1)
                visit(root, depth)
            if root.right:
                eulerian_tour(root.right, depth+1)
                visit(root, depth)
        
        # update e_depth & e_nodes array
        # also keep tracking of last visited e_index
        def visit(node, depth):
            e_depth.append(depth)
            e_nodes.append(node)
            # keep last e-index 
            last_visit[node.val] = len(e_depth) - 1
        
        # eulerian_tour
        eulerian_tour(root, 0)
        
        # get the max depth value
        max_depth = max(e_depth)

        # nodes' last e-index with max_depth
        indexs = [last_visit[e_nodes[index].val] for index, depth in enumerate(e_depth) if depth == max_depth]
        min_index = min(indexs)
        max_index = max(indexs)
        
        # lowers node between indices is the root node
        return min(e_nodes[min_index:max_index+1], key=lambda n: n.val)