# https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {TreeNode}
def increasing_bst(root)
    roots = []
    q = [root]
    
    until q.empty?
        cur = q.shift
        roots << cur
        q << cur.left if cur.left
        q << cur.right if cur.right
    end
    
    roots.sort_by!{|n| n.val}
    new_head = TreeNode.new(roots.first.val)
    cur = new_head
    roots[1..-1].each do |node|
         cur.right = TreeNode.new(node.val)
         cur = cur.right
    end
    new_head
end
