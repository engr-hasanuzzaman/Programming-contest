# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {Integer[]} preorder
# @return {TreeNode}
def bst_from_preorder(preorder)
  root = TreeNode.new(preorder[0])
  stack = [root]
  
  1.upto(preorder.size-1) do |i|
      temp = TreeNode.new(preorder[i])
      # puts "-temp #{temp.val}"
      if stack[-1].val > temp.val
          stack[-1].left = temp
      else
          prev = nil
          
          while stack.size > 0 && stack[-1]&.val.to_i < temp.val
              prev = stack.pop
          end
         # puts "-- prev is #{prev.val}, tv #{temp.val}"
          prev.right = temp
      end
      
      stack << temp
  end
  
  root
end