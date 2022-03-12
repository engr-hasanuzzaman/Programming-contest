# https://leetcode.com/problems/balance-a-binary-search-tree/

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
def balance_bst(root)
    nodes = in_order_traverse(root, [])
    build_bst(nodes)
end

def in_order_traverse(tree, nodes)
    return nodes if tree.nil?

    in_order_traverse(tree.left, nodes)
    nodes << tree.val
    in_order_traverse(tree.right, nodes)
end

def build_bst(nodes)
    return nil if nodes.empty?
    
    mid = nodes.size / 2
    node = TreeNode.new(nodes[mid])
    node.left = build_bst(nodes[0...mid])
    node.right = build_bst(nodes[mid+1..-1])
    node
end
