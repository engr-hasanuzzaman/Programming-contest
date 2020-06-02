# https://leetcode.com/problems/random-pick-with-weight/

# use cumulative sum array with binary search for finding correct position
class Solution

  =begin
      :type w: Integer[]
  =end
      def initialize(w)
          @cumulative_weight =  w.each_index.inject([]) do |arr, i|
              arr << arr[i-1].to_i + w[i]
          end
      end
  
  
  =begin
      :rtype: Integer
  =end
      def pick_index()
          target = rand(1..@cumulative_weight.last)
          i = 0
          j = @cumulative_weight.size
          
          while i < j
              mid = (i+j) / 2
              if @cumulative_weight[mid] == target
                  return mid
              elsif @cumulative_weight[mid] > target
                  j = mid
              else
                  i = mid + 1
              end
          end
          
          return i == @cumulative_weight.size ? i - 1 : i
      end
  end