def MatchingCharacters(str)
 max_seq_size = 0
 max_uniq_seq = ''
 (0...str.size - 1).each do |i| 
     (1...str.size).each do |j|
         sub_str = str[i..j]
         
         if sub_str.size > 2 && sub_str[0] == sub_str[-1]
            uniq_sub_str = sub_str[1..-2].chars.uniq
            max_seq_size = uniq_sub_str.size if uniq_sub_str.size > max_seq_size
         end 
     end 
 end 
 
 return max_seq_size
end

puts MatchingCharacters("Argument goes here")