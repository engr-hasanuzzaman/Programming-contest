# https://leetcode.com/problems/largest-rectangle-in-histogram/

# @param {Integer[]} heights
# @return {Integer}
def largest_rectangle_area(heights)
  return 0 if heights.size.zero?
  
  s = [[heights.first, 0]]
  max = 0
  for i in (1...heights.size)
      if heights[i] > heights[i-1]
          s << [heights[i], i] # height, index
      else
          j = nil
          while s.any? && s.last[0] > heights[i]
              h, j = s.pop
              max = [max, h*(i-j)].max
          end
          
          s << [heights[i], j || i]
      end
  end
  
  while s.any?
      h, j = s.pop
      max = [max, h*(heights.size-j)].max
  end
  
  max
end