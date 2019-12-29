# https://leetcode.com/problems/deepest-leaves-sum/

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Integer}
def deepest_leaves_sum(root)
  return 0 unless root

  q = []
  q << root
  sum = 0
  
  until q.empty?
      sum = 0
      s = q.size
      s.times do
          n = q.shift
          sum += n.val
          q << n.left if n.left
          q << n.right if n.right
      end
  end
  
  sum
end
