# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {TreeNode}

def bst_to_gst(root, sum=0)
  total = 0
      
  node = root
  stack = []
  
  while !stack.empty? || node
      # puts "current node is #{node&.val}"
      # push all nodes up to (and including) this subtree's maximum on
      # the stack.
      while node
          stack << node
          node = node.right
      end
      # puts "---current stack #{stack.map{|s| s.val}}\n"
      
      node = stack.pop()
      total += node.val
      node.val = total

      # all nodes with values between the current and its parent lie in
      # the left subtree.
      node = node.left
  end

  return root
end
