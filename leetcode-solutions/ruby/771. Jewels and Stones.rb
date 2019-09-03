# https://leetcode.com/problems/jewels-and-stones/

# @param {String} j
# @param {String} s
# @return {Integer}
def num_jewels_in_stones(j, s)
  j_d = Hash.new
  
  j.each_char do |c|
      j_d[c] = 0
  end
  
  s.each_char do |c|
      j_d[c] += 1 if j_d[c]
  end
  
  j_d.values.sum
end