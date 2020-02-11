# https://leetcode.com/problems/find-common-characters/

# @param {String[]} a
# @return {String[]}
def common_chars(a)
  a_m = []
  a.each_with_index do |s, i|
      map = {}
      s.each_char do |c|
          if map[c]
              map[c] += 1
          else
              map[c] = 1
          end
      end
      
      a_m << map
  end
  
  result = []
  a_m.first.each do |c, v|
      exist = true
      min_val = v
      
      a_m.each do |m|
          unless m[c]
              exist = false
              break
          end
          
          min_val = [min_val, m[c]].min
      end
      
      if exist
          min_val.times { result << c }
      end 
  end
  
  result
end