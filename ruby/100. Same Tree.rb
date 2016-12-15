# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} p
# @param {TreeNode} q
# @return {Boolean}
def is_same_tree(p, q)
    return true if p.nil? && q.nil?
    
    return false if p.nil? || q.nil?     
    # p and q equal if that have same value and same valued node
    (p.val == q.val) && (is_same_tree(p.left, q.left)) && (is_same_tree(p.right, q.right))
end
