# https://leetcode.com/problems/reverse-words-in-a-string-iii/

# @param {String} s
# @return {String}
def reverse_words(s)
  s.split.map(&:reverse).join(" ")
end