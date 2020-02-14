# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

def sherlockAndAnagrams(s)
  size = s.size
  a_sub_str = []
  # construct all the sub-string
  size.times do |i|
      for j in i+1...size
          a_sub_str << s[i..j].split('').sort.join('')
      end
  end 

  # string of single char
  a_sub_str += s.split('')
  map = {}
  count = 0
  # count same word
  a_sub_str.each do |s|
      if map[s]
          map[s] += 1
      else
       map[s] = 1
      end 
  end 

 map.each do |k, n|
      # count palindrom
      count += (n * (n-1) / 2)
  end 

  count 
end