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
