# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {TreeNode} p
# @param {TreeNode} q
# @return {TreeNode}
def lowest_common_ancestor(root, p, q)
  return nil if root.nil?
  return root if root == p || root == q
  
  left = lowest_common_ancestor(root.left, p, q)
  right = lowest_common_ancestor(root.right, p, q)
  
  if left && right
      return root
  else
      left || right
  end
end