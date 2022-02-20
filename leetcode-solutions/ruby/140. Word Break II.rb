# https://leetcode.com/problems/word-break-ii/

# @param {String} s
# @param {String[]} word_dict
# @return {String[]}
def word_break(s, word_dict)
    dict = {}
    word_dict.each do |word|
        dict[word] = true
    end
    memo = {}
    get_valid_words(dict, s, memo)
end

def get_valid_words(dict, string, memo)
    return [] if string.empty?
    if memo.key? string
        return memo[string]
    end
    
    size = string.size
    words = []
    size.times do |i|
        sub_string = string[0..i]
        
        if dict.key?(sub_string)
            if i == size - 1
                words << sub_string
                next
            end
            
            strings = get_valid_words(dict, string[i+1..-1], memo)
            unless strings.empty?
                words += strings.map{|s| sub_string + " " + s}
            end
        end
    end
    memo[string] = words
    memo[string]
end
