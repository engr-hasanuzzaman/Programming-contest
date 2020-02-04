# https://leetcode.com/problems/group-anagrams/

# @param {String[]} strs
# @return {String[][]}
def group_anagrams(strs)
  map = {}
  strs.each do |s|
      ss = s.split("").sort.join("")
      if map[ss]
          map[ss] << s
      else
          map[ss] = [s]
      end
  end
  
  map.values
end