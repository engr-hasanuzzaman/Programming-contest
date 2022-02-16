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

# using two stack
# left read left child -> right child, then left child <- right child
def zigzag_level_order(root)
    return [] unless root
    
    stack1 = [root]
    stack2 = []
    ans = []
    order = 0
    until stack1.empty? && stack2.empty?
        level_size = if stack1.size > 0
                        stack1.size
                    else
                        stack2.size
                    end
        level_nodes = []

        level_size.times do 
            if order % 2 == 0
                cur_node = stack1.pop
                stack2.push cur_node.left if cur_node.left
                stack2.push cur_node.right if cur_node.right
            else
                cur_node = stack2.pop
                stack1.push cur_node.right if cur_node.right
                stack1.push cur_node.left if cur_node.left
            end
            
            level_nodes.push cur_node.val
        end
        order += 1
        ans << level_nodes
    end
    ans
end
