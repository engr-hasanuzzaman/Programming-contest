# Definition for a binary tree node.
class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val)
        @val = val
        @left, @right = nil, nil
    end
end

# @param {TreeNode} root
# @return {Integer}
def find_bottom_left_value(root)
    stack = [root]
    temp_stack = []
    row_data = []
    
    while stack.size > 0
        node = stack.shift
        temp_stack << node.left if node.left
        temp_stack << node.right if node.right
        row_data << node.val
        
        if stack.size.zero? && temp_stack.size > 0
            stack = temp_stack
            temp_stack = []
            row_data = []    
        end
    end
    
    return row_data.first
end
