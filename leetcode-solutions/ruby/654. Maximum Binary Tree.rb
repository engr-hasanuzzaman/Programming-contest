# https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
class TreeNode
  attr_accessor :val, :left, :right
  def initialize(val)
      @val = val
      @left, @right = nil, nil
  end
end

# @param {Integer[]} nums
# @return {TreeNode}
def construct_maximum_binary_tree(nums)
  mx_num = -Float::INFINITY
  mx_index = 0
  # max_num and index
  nums.each_with_index do |n, i|
      if n > mx_num
          mx_num = n
          mx_index = i
      end
  end
  
  root = TreeNode.new(mx_num)
  
  # left node
  unless mx_index.zero?
      root.left = construct_maximum_binary_tree(nums[0...mx_index])
  end
  
  unless mx_index == nums.size - 1
      root.right = construct_maximum_binary_tree(nums[mx_index+1..-1])
  end
  
  root
end