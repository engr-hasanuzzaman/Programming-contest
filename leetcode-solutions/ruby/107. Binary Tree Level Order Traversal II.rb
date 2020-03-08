# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Integer[][]}
def level_order_bottom(root)
  result = []
   q = []
   q << root
   
   while q.any?
       c_level = []
       
       q.size.times do
           node = q.pop
           c_level << node.val
           q.unshift(node.left) if node.left
           q.unshift(node.right) if node.right
       end
       
       result.unshift(c_level)
   end
   
   result
end