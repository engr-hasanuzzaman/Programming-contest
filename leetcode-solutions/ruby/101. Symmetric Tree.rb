# https://leetcode.com/problems/symmetric-tree/

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
def is_symmetric(root)
  return true if root.nil? || (root.left.nil? && root.right.nil?)
  
  is_symatric(root.left, root.right)
end

def is_symatric(node1, node2)
  return true if node1.nil? && node2.nil?
  # puts "1 #{node1.val}, #{node2.val}"
  if node1 && node2 && (node1.val == node2.val)
      return is_symatric(node1.left, node2.right) && is_symatric(node1.right, node2.left)    
  else
      return false
  end
end