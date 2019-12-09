# https://leetcode.com/problems/longest-common-prefix/

# @param {String[]} strs
# @return {String}
def longest_common_prefix(strs)
  return '' if strs.size.zero?
  
  ans = ''
  l_str = strs.first
  l_size = l_str.size
  
  strs.each do |s|
      t_s = s.size
      if t_s > l_size
          l_size = t_s
          l_str = s
      end
  end
  
  c_str = ''
  l_size.times do |i|
      match = true
      c_chr = l_str[i]
      
      strs.each do |s|
          if c_chr != s[i]
              match = false
              c_str = ''
              break
          end
      end
      
      if match
          c_str << c_chr
      else
          ans = c_str if c_str.size > ans.size
          break
      end
      
      ans = c_str if c_str.size > ans.size
  end
  
  ans
end