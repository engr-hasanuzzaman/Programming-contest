# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {Integer[]} inorder
# @param {Integer[]} postorder
# @return {TreeNode}
def build_tree(inorder, postorder)
  return nil if inorder.empty? || postorder.empty?
  
  node = TreeNode.new(postorder.last)
  return node if postorder.size == 1
  
  root_i = inorder.index(node.val)
  
  # construct left root section
  if root_i == 1
      node.left = TreeNode.new(inorder[0])
  elsif inorder[0...root_i].size > 1
      node.left = build_tree(inorder[0...root_i], postorder[0...root_i])
  end
  
  # right root section
  if root_i == inorder.size - 2
      node.right = TreeNode.new(inorder[root_i+1])
  elsif inorder[root_i+1..-1].size > 1
      node.right = build_tree(inorder[root_i+1..-1], postorder[root_i..-2])
  end
  
  node
end
