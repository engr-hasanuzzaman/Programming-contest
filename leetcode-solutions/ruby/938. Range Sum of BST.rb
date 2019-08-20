# https://leetcode.com/problems/range-sum-of-bst/
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def range_sum_bst(root, l, r)
    stack = [root]
    sum = 0
    
    until stack.empty?
        node = stack.pop
        sum += node.val if node.val >= l && node.val <= r
        stack << node.left if node.left
        stack << node.right if node.right
    end
    
    sum
end
