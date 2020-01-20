# https://leetcode.com/problems/first-unique-character-in-a-string/

# @param {String} s
# @return {Integer}
def first_uniq_char(s)
  map = {}
  s.each_char.with_index do |c,i|
      if map[c]
          map[c] += 1
      else
          map[c] = 1
      end
  end
  
  s.each_char.with_index do |c, i|
      return i if map[c] == 1
  end
  
  -1
end