# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {Integer[]} nums
# @return {TreeNode}
def sorted_array_to_bst(nums)
    return nil if nums.empty?
    
    mid = nums.size / 2
    node = TreeNode.new(nums[mid])
    node.left = sorted_array_to_bst(nums[0...mid])
    node.right = sorted_array_to_bst(nums[mid+1..-1])
    node
end