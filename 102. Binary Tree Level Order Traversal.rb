# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# Breath First Search
# @param {TreeNode} root
# @return {Integer[][]}
def level_order(root)
  return [] unless root
  ans = []
  q = [root]
  
  until q.empty?
      tmp = []
      q.size.times do
          c = q.shift
          tmp << c.val
          q << c.left if c.left
          q << c.right if c.right
      end
      
      ans << tmp
  end
  
  ans
end