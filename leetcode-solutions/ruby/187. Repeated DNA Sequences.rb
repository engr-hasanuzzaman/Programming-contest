# https://leetcode.com/problems/repeated-dna-sequences/

# @param {String} s
# @return {String[]}
def find_repeated_dna_sequences(s)
  return [] if s.size < 10
  
  result = []
  m = {}
  i = 0
  while i + 10 <= s.size
      if m[s[i...i+10]]
          result << s[i...i+10]
      else
          m[s[i...i+10]] = true
      end
      i += 1
  end
  
  result.uniq
end