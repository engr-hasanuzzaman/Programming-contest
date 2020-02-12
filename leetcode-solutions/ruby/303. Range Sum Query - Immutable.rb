# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray

  =begin
      :type nums: Integer[]
  =end
      def initialize(nums)
          @nums = nums
          prepare
      end
  
  
  =begin
      :type i: Integer
      :type j: Integer
      :rtype: Integer
  =end
      def sum_range(i, j)
          if i.zero?
              @nums[j]
          else
              @nums[j] - @nums[i-1]
          end
      end
  
      def prepare
          @nums.each_with_index do |n, i|
              next if i.zero?
              
              @nums[i] = @nums[i] + @nums[i-1]
          end
      end
  end
  
  # Your NumArray object will be instantiated and called as such:
  # obj = NumArray.new(nums)
  # param_1 = obj.sum_range(i, j)