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
def inorder_traversal(root)
  result = []
  dfs(root)
end

def dfs(root)
  return [] if root.nil?
  result = []
  stack = []
  node = root
  
  while !stack.empty? || node
      while node
          stack << node
          node = node.left
      end
      
      node = stack.pop
      result << node.val
      node = node.right
  end
  
  result
end