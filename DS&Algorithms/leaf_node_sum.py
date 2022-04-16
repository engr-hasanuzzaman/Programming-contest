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
neg_five = TreeNode(-5)
one = TreeNode(1)

four.children.append(three)
four.children.append(five)
four.children.append(ten)

root = TreeNode(10)
root.children.append(neg_five)
root.children.append(four)

assert sub_of_leaf(root) == 13

def max_height(node):
    if not node: return 0
    if is_leaf(node): return 0
    return max([max_height(child) + 1 for child in node.children])

def is_leaf(node):
    return node and len(node.children) == 0

assert max_height(root) == 2

# re-declare all the nodes
three = TreeNode(3)
five = TreeNode(5)
four = TreeNode(4)
ten = TreeNode(10)
neg_five = TreeNode(-5)
one = TreeNode(1)

three.children.append(one)
five.children.append(four)
five.children.append(three)

# root
ten.children.append(five)
ten.children.append(neg_five)

assert max_height(ten) == 3