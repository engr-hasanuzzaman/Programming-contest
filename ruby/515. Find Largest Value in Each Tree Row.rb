# Definition for a binary tree node.
class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val)
        @val = val
        @left, @right = nil, nil
    end
end

# @param {TreeNode} root
# @return {Integer[]}
def largest_values(root)
    return [] if root.nil?
    
    result = []
    stack = [root]
    temp_stack = []
    temp_val = []
    
    while stack.size > 0
        node = stack.shift
        temp_val << node.val
        
        temp_stack << node.left if node.left
        temp_stack << node.right if node.right
        
        if stack.size == 0
            result << temp_val.max
            temp_val = []
            stack = temp_stack
            temp_stack = []
        end
    end
    
    return result
end
