# https://leetcode.com/problems/merge-two-binary-trees/

def merge_trees(root1, root2)
    return nil unless root1 || root2
    
    if root1 && root2
        node = TreeNode.new(root1.val + root2.val)
        node.left = merge_trees(root1.left, root2.left)
        node.right = merge_trees(root1.right, root2.right)
        return node
    end
    
    root1 || root2
end

# itarative solution
def merge_trees(root1, root2)
    if !root1 || !root2
        return root1 || root2
    end
    
    stack = [[root1, root2]]
    
    until stack.empty?
        node1, node2 = stack.pop
        if node1.nil?
            next
        end
        
        node1.val += node2.val
        if node1.left && node2.left
            stack.push([node1.left, node2.left])
        elsif node1.left.nil?
            node1.left = node2.left
        end
        
        if node1.right && node2.right
            stack.push([node1.right, node2.right])
        elsif node1.right.nil?
            node1.right = node2.right
        end
    end
    root1
end