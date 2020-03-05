# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Float[]}
def average_of_levels(root)
  ans = []
  q = []
  q << root
  
  while q.any?
      c_sum = 0
      l_size = q.size
      l_size.times do
          c_node = q.pop
          c_sum += c_node.val
          q.unshift(c_node.left) if c_node.left
          q.unshift(c_node.right) if c_node.right
      end
      
      ans << c_sum.to_f / l_size
  end
  
  ans
end

