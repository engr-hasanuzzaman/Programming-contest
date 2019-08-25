# https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {Integer} k
# @return {Integer}
def kth_smallest(root, k)
  stack = []
  node = root
  
       
  while !stack.empty? || node
      # push all the left sub tree node
      while node
          stack << node
          node = node.left
      end
      
      k -= 1
      node = stack.pop
      return node.val if k.zero?
      
      #right node of last processed node         
      node = node.right
  end
end