# https://www.hackerrank.com/challenges/sherlock-and-valid-string/copy-from/142858334

def isValid(s)
  map = {}
  # count the word frequencies
  s.each_char do |c|
      if map[c]
          map[c] += 1
      else
          map[c] = 1
      end
  end

  # count the count of frequecies
  v_map = {}
  map.values.each do |v|
      if v_map[v]
          v_map[v] += 1
      else
          v_map[v] = 1
      end
  end

  ks = v_map.keys
  if ks.size > 2
      return 'NO'
  elsif ks.size == 1
      return 'YES'
  else
      sk = v_map.keys.min
      bk = v_map.keys.max
      if v_map[sk] == 1
       return 'YES'
      end

      if v_map[bk] > 1 || bk - sk > 1
       return 'NO'
      end
  end 
  
  return 'YES'
end