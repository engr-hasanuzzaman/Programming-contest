# @param {String[]} words
# @param {String} chars
# @return {Integer}
def count_characters(words, chars)
  words.select{|w| good?(w, chars) }.join.size
end

def good?(t_str, r_str)
   return false if t_str.size > r_str.size
   
   s_h = Hash.new(0)
   t_str.each_char do |c|
       s_h[c] += 1
   end
   
   r_str.each_char do |c|
       s_h[c] -= 1 if s_h[c] > 0
   end
   puts s_h
   s_h.values.sum.zero?
end