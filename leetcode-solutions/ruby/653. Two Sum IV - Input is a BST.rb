# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

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
# @param {Integer} k
# @return {Boolean}
def find_target(root, k, top_root = nil)
    return false if root.nil?
    top_root ||= root
    rem_number = k - root.val
    if rem_number == root.val
        return find_target(root.left, k, top_root) || find_target(root.right, k, top_root)
    end
    
    exist = is_exist?(top_root, rem_number)
    if exist
        return exist
    else
        find_target(root.left, k, top_root) || find_target(root.right, k, top_root)
    end
end

def is_exist?(root, target)
    return false if root.nil?
    return true if root.val == target

    if target > root.val
        is_exist?(root.right, target)
    else
        is_exist?(root.left, target)
    end
end