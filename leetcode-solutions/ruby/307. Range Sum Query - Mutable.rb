# https://leetcode.com/problems/range-sum-query-mutable/

class NumArray

  =begin
      :type nums: Integer[]
  =end
      def initialize(nums)
          @nums = nums
          @bit = Array.new(nums.size + 1){0}
          prepare_bit
      end
  
  
  =begin
      :type i: Integer
      :type val: Integer
      :rtype: Void
  =end
      def add(i, val)
          current = i + 1
          
          while current < @bit.size
              @bit[current] += val
              current += (current & -current)
          end
      end
  
      def get_sum(i)
          current = i+1
          sum = 0
          while current >= 1
              sum += @bit[current]
              current -= (current & -current)
          end
          
          sum
      end
  =begin
      :type i: Integer
      :type j: Integer
      :rtype: Integer
  =end
      def sum_range(i, j)
          get_sum(j) - get_sum(i-1)
      end
  
      def prepare_bit
          @nums.each_with_index do |n, i|
              add(i, n)
          end
      end
      
      def update(i, n)
          diff = n - @nums[i]
          @nums[i] = n
          add(i, diff)
      end
  end
  
  # Your NumArray object will be instantiated and called as such:
  # obj = NumArray.new(nums)
  # obj.update(i, val)
  # param_2 = obj.sum_range(i, j)