# take next 2nd letter
str = 'abc dez'.downcase
result = ''
letter = ('a'..'z').to_a
range = (1..26).to_a

str.chars.each_with_index do |c, i|
  if c == ' '
    result << ' '
  else
    result << letter[(letter.index(c) + 2) % 26]
  end
end

p result

# conver each char with 2 digit number
str = 'abc q'.downcase
result = ''
letter = ('a'..'z').to_a
range = (1..26).to_a

str.chars.each_with_index do |c, i|
  if c == ' '
    result << ' '
  else
    
    result << "%02d" % letter.index(c).next
  end
end

p result

# first letter capitalize, even position take next char, odd position prev number

str = 'a bb'.downcase
result = ''
letter = ('a'..'z').to_a
range = (1..26).to_a

str.chars.each_with_index do |c, i|
  if i.zero?
    result << c.upcase
  elsif c == ' '
    result << ' '
  elsif i % 2 == 1
    next_index = letter.index(c).next % 26
    result << letter[next_index]
  else 
    prev_index = letter.index(c) - 1
    result << letter[prev_index]
  end
end

p result

# ---------------------------- 
str = 'sumon a'.downcase
result = ''
letter = ('a'..'z').to_a
range = (1...26).to_a

str.chars.each_with_index do |c, i|
  if c == ' '
    result << ' '
  else
    rand_n = range.sample
    f_index = (rand_n - i) % 26
    p f_index
    result << "#{letter[f_index]}#{"%02d" % f_index}"
  end
end

print result
