class TreeNode():
    def __init__(self, val = None) -> None:
        self.val = val
        self.children = []
        self.parent = None

# create the root node
def to_rooted_tree(g, node):
    root = TreeNode(node)
    return build_tree(g, root, None)

# pass the root node to build_tree which use DFS
# for each child, create child node, append to node and call dfs(child_node) to build tree
# N.B: we are passing parent info here to disconnect circular referen child to parent
def build_tree(g, node, parent):
    for child in g[node.val]:
        # prevent circular reference child to parent 
        if parent and parent.val == child:
            continue
        c_node = TreeNode(child)
        node.children.append(c_node)
        build_tree(g, c_node, node)
    return node

def inorder_traverse(root, values = []):
    if not root: return values
    values.append(root.val)
    for child in root.children:
        inorder_traverse(child, values)
    return values
"""
Unrooted tree
g = [[]]
"""
g = [[2,1,5], [0], [3, 0], [2], [5], [4, 6, 0], [5]]
root = to_rooted_tree(g, 0)
print(inorder_traverse(root))