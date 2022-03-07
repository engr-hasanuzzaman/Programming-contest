# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

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
def get_minimum_difference(root)
    nodes = []
    in_order(root, nodes)
    min_dif = Float::MAX
    index = 0
    while index < nodes.size - 1
        min_dif = [min_dif, (nodes[index].val - nodes[index+1].val).abs].min
        index += 1 
    end
    min_dif
end

def in_order(node, nodes)
    return if node.nil?

    in_order(node.left, nodes)
    nodes << node
    in_order(node.right, nodes)
end
