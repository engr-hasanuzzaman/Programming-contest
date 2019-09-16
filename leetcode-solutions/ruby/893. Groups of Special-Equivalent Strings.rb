# https://leetcode.com/problems/groups-of-special-equivalent-strings/

# @param {String[]} a
# @return {Integer}
def num_special_equiv_groups(a)
  result = []
  
  a.each do |s|
      odd_a = Array.new(26, 0)
      even_a = Array.new(26, 0)
      
      s.each_char.with_index do |c, i|
          if i.even?
              # puts "-- #{c.ord - 65}"
              even_a[c.ord - 'a'.ord] += 1 
          else
              odd_a[c.ord - 'a'.ord] += 1
          end
      end
      
      result << even_a.to_s + odd_a.to_s
  end
  
  result.uniq.size
end

