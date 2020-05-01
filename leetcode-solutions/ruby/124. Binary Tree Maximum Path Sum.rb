# https://leetcode.com/problems/binary-tree-maximum-path-sum/

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
# @return {Integer}

def max_path_sum(root)
    @max = -2**32
    dfs(root)
    @max
end

def dfs(root)
    return -2**32 if root.nil?
    
    left = dfs(root.left)
    right = dfs(root.right)
    @max = [@max, left, right, left+right+root.val, root.val, left + root.val, right + root.val].max
    [left + root.val, right + root.val, root.val].max
end
