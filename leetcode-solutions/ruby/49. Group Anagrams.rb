# https://leetcode.com/problems/group-anagrams/

# time complexity is O(n.mlogm)
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

# since str contains only lowercase char, we can take frequency as the key
# now solution is O(n.m) where n number of string and m max size of string

# @param {String[]} strs
# @return {String[][]}
def group_anagrams(strs)
    hash = Hash.new{|h, k| h[k] = []}
    strs.each_with_object(hash){|s, h| h[frequency(s)] << s}.values
end

def frequency(str)
    arr = Array.new(26, 0)
    str.each_char do |chr|
        idx = chr.ord - 'a'.ord
        arr[idx] += 1
    end
    
    arr.join('-')
end