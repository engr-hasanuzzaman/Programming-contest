class TreeNode:
    def __init__(self, val = None) -> None:
        self.val = val
        self.children = []

def sub_of_leaf(at):
    if not at: return 0
    if len(at.children) == 0: return at.val
    total = 0
    for to in at.children:
        total += sub_of_leaf(to)
    return total

"""
    10
   /   \
 -5     4  \
       /  \  \ 
      3    5  10
"""
 

three = TreeNode(3)
five = TreeNode(5)
four = TreeNode(4)
ten = TreeNode(10)
four.children.append(three)
four.children.append(five)
four.children.append(ten)

neg_five = TreeNode(-5)

root = TreeNode(10)
root.children.append(neg_five)
root.children.append(four)

assert sub_of_leaf(root) == 13

def max_height(node):
    if not node: return 0
    if is_leaf(node): return 1
    return max([max_height(child) + 1 for child in node.children])

def is_leaf(node):
    return node and len(node.children) == 0

assert max_height(root) == 3