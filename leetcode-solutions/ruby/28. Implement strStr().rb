# https://leetcode.com/problems/implement-strstr/

# @param {String} haystack
# @param {String} needle
# @return {Integer}
def str_str(haystack, needle)
  haystack.index(needle) || -1
end