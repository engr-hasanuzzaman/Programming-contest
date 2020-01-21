# https://leetcode.com/problems/longest-common-subsequence/

# @param {String} text1
# @param {String} text2
# @return {Integer}
def longest_common_subsequence(text1, text2)
  m = Array.new(text1.size + 1){ Array.new(text2.size + 1)}
  
  (text1.size+1).times do |i|
      c1 = text1[i-1]
      (text2.size+1).times do |j|
          c2 = text2[j-1]
          if i.zero? || j.zero?
              # puts m
              m[i][j] = 0
          elsif c1 == c2
              m[i][j] = m[i-1][j-1] + 1
          else
              m[i][j] = [m[i][j-1], m[i-1][j]].max
          end
      end
  end
  
  # puts m.inspect
  m[-1][-1]
end