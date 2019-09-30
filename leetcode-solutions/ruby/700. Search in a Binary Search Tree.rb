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
def search_bst(root, val)
  node = root
  
  while node
      if node.val == val
          break
      else
          if val > node.val
              node = node.right
          else
              node = node.left
          end
      end
  end
  
  node 
end