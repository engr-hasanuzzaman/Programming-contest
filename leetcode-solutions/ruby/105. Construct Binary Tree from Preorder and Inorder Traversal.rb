# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {Integer[]} preorder
# @param {Integer[]} inorder
# @return {TreeNode}
def build_tree(preorder, inorder)
  return [] if preorder.empty? || inorder.empty?
  
  node = TreeNode.new(preorder.first)
  node_i = inorder.index(node.val)
  
  # build left tree part
  if node_i == 1
      node.left = TreeNode.new(inorder[0])
  elsif inorder[0...node_i].size > 1
      node.left = build_tree(preorder[1..node_i], inorder[0...node_i])
  end
  
  # build right tree part
  if node_i == inorder.size - 2
      node.right = TreeNode.new(inorder.last)
  elsif inorder[node_i+1..-1].size > 1
      node.right = build_tree(preorder[node_i+1..-1], inorder[node_i+1..-1])
  end
  
  node
end