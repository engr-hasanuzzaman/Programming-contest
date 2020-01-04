# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {Integer} sum
# @return {Boolean}
def has_path_sum(root, sum)
  # check leaf and condition
  return true if root && root.left.nil? && root.right.nil? && (sum - root.val) == 0
  return false if root.nil?
  left = false
  right = false
  
  left = has_path_sum(root.left, sum - root.val) if root.left
  right = has_path_sum(root.right, sum - root.val) if root.right
   
  left || right
end
