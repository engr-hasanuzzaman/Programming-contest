# https://leetcode.com/problems/most-common-word/

# @param {String} paragraph
# @param {String[]} banned
# @return {String}
def most_common_word(paragraph, banned)
  paragraph = paragraph.gsub(/[^0-9A-Za-z ]/, ' ')
  w_count = Hash.new(0)
  
  paragraph.split.each do |w|
      w = w.downcase
      w_count[w] += 1 unless banned.include?(w)
  end
  # puts w_count.sort_by{|_, v| -v }
  w_count.sort_by{|_, v| -v }.first.first
end