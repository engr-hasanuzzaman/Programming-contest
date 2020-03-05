# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Boolean}
def is_valid_bst(root)
  check(root, Float::MAX.to_i, -Float::MAX-1)
end

def check(root, max_val, min_val)
  return true if root.nil?
  return false unless (root.val > min_val && root.val < max_val)
  
  left = check(root.left, root.val, min_val)
  right = check(root.right, max_val, root.val)
  
  left && right
end