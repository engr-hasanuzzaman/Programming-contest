  # https://leetcode.com/problems/play-with-chips/

  # @param {Integer[]} chips
# @return {Integer}
def min_cost_to_move_chips(chips)
  chip_counter = Hash.new(0)
  chips.each do |i|
      chip_counter[i] += 1
  end
  
  counter = 0
  m_index = chip_counter.sort_by{|k, v| -v}.first[0]
  chips.each do |i|
      if (m_index - i).abs % 2 == 1
          counter += 1
      end
  end
  counter
end

# fail test input [1,234,567,7,89,12,345,134,12,34,5]