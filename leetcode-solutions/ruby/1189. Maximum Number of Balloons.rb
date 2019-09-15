# @param {String} text
# @return {Integer}
def max_number_of_balloons(text)
  b_c = 'balloon'
  c_hash = {}
  
  b_c.each_char do |c|
      c_hash[c] = 0
  end
  
  text.each_char do |c|
      c_hash[c] += 1 if c_hash[c]
  end
  
  c_hash['l'] = c_hash['l'] / 2
  c_hash['o'] = c_hash['o'] / 2
  
  c_hash.values.min || 0
end