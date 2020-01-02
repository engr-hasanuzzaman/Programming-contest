# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Integer[]}
def preorder_traversal(root)
  p_t(root).flatten
end

def p_t(root)
  return [] unless root
  return [root.val] if root.left.nil? && root.right.nil?
  
  if root.left && root.right
      [root.val, preorder_traversal(root.left), preorder_traversal(root.right)]
  elsif root.left
      [root.val, preorder_traversal(root.left)]
  else
      [root.val, preorder_traversal(root.right)]
  end
end

# use array 
def preorder_traversal(root)
  return [] if root.nil?
  
  @result = []
  
  traverse(root)
  
  return @result
end

def traverse(root)
  return if root.nil?
  
  @result << root.val
  traverse(root.left)
  traverse(root.right)
end

# with passing ans array
def preorder_traversal(root)
  ans = []
  p_t(root, ans)
  ans
end

def p_t(root, ans)
  return unless root
  return ans << root.val  if root.left.nil? && root.right.nil?
  
  ans << root.val
  if root.left && root.right
      p_t(root.left, ans)
      p_t(root.right, ans)
  elsif root.left
      p_t(root.left, ans)
  else
      p_t(root.right, ans)
  end
end

# iterative method with STACK
def preorder_traversal(root)
  ans = []
  s = []
  s << root if root
  
  until s.empty?
      r = s.pop
      ans << r.val
      
      if r.left && r.right
        s << r.right
        s << r.left
      elsif r.left
        s << r.left
      elsif r.right
        s << r.right
      end
  end

  ans
end