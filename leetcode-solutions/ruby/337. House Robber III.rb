# https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {Integer}
def rob(root)
  solve(root)
end

def solve(node, memo = {})
  return 0 if node.nil?
  return memo[node] if memo[node]

  with_node = node.val
  # if we take current node, will be able to take grandchild
  if node.left
    with_node += solve(node.left.left, memo)
    with_node += solve(node.left.right, memo)
  end

  if node.right
    with_node += solve(node.right.left, memo)
    with_node += solve(node.right.right, memo)
  end

  # if not take current node, will be able to take direct child
  without_node = 0
  without_node += solve(node.left, memo)
  without_node += solve(node.right, memo)
  memo[node] = [without_node, with_node].max
  memo[node]
end
