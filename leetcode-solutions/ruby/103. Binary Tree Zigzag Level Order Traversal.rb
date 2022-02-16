# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

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
# @return {Integer[][]}
def zigzag_level_order(root)
    return [] unless root
    
    level = 1
    queue = [root]
    ans = []
    until queue.empty?
        level_size = queue.size
        level_nodes = []

        level_size.times do 
            cur_node = queue.shift
            if level % 2 == 0
                level_nodes.unshift cur_node.val
            else
                level_nodes.push cur_node.val
            end
            queue.push cur_node.left if cur_node.left
            queue.push cur_node.right if cur_node.right
        end
        level += 1
        ans << level_nodes
    end
    ans
end