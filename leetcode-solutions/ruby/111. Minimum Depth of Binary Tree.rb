# https://leetcode.com/problems/minimum-depth-of-binary-tree/

def min_depth(root)
    return 0 unless root
 
    if root.left && root.right 
         return [min_depth(root.left), min_depth(root.right)].min + 1
    elsif root.left
        return min_depth(root.left) + 1
    else
        return min_depth(root.right) + 1
    end
 end