  # https://leetcode.com/problems/height-checker/

  # @param {Integer[]} heights
# @return {Integer}
def height_checker(heights)
  s_h = heights.sort
  m_count = 0
  
  s_h.size.times do |i|
      m_count += 1 unless s_h[i] == heights[i]
  end
  
  m_count
end