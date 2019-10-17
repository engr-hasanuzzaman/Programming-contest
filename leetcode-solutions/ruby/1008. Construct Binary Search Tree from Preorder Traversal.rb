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
      
      if stack[-1].val > temp.val
          stack[-1].left = temp
      else
          while stack.size > 0 && stack[-1]&.val.to_i < temp.val
              prev = stack.pop
          end
         
          prev.right = temp
      end
      
      stack << temp
  end
  
  root
end