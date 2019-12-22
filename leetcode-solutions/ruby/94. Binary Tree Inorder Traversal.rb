# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# recursive solution

# @param {TreeNode} root
# @return {Integer[]}
def inorder_traversal(root)
  result = []
  dfs(root, result)
  result
end

def dfs(root, result)
  return if root.nil?
  
  dfs(root.left, result)
  result << root.val
  dfs(root.right, result)
end

# iterative solution