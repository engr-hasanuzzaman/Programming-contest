def combine(char, str_array)
  return [char] if str_array.size <= 0 
  
  result = []
  
  # put given char in every position of given str_array
  # since final str will be one size bigger that's why 
  # we use size + 1 for position
  str_array.each do |s|
     (s.size + 1).times do |i|
      if i == 0 
        result << char + s
      elsif i == s.size
        result << s + char
      else
         result << (s[0..i-1] + char + s[i..-1])
      end 
    end
  end  
  
  result
end
