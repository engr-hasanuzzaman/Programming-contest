# https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {Integer} val
# @return {TreeNode}
def insert_into_bst(root, val)
  node = root
  while node 
      if node.val > val
          unless node.left
              node.left = TreeNode.new(val)
              break 
          end
          node = node.left
      else
          unless node.right
              node.right = TreeNode.new(val)
              break 
          end
          node = node.right
      end
  end
  
  root
end