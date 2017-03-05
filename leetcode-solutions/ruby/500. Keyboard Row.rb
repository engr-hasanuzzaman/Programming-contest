# @param {String[]} words
# @return {String[]}
def find_words(words)
    row_1 = 'qwertyuiop'.chars
    row_2 = 'asdfghjkl'.chars
    row_3 = 'zxcvbnm'.chars
    
    result = []
    
    words.each do |w|
      result << w if (w.downcase.chars - row_1).size == 0 || (w.downcase.chars - row_2).size == 0 || (w.downcase.chars - row_3).size == 0
    end
    
    return result
end
