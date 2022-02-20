# https://leetcode.com/problems/word-break/

# @param {String} s
# @param {String[]} word_dict
# @return {Boolean}
def word_break(s, word_dict)
    dict = {}
    word_dict.each do |word|
        dict[word] = true
    end
    memo = {}
    is_valid_words?(dict, s, memo)
end

def is_valid_words?(dict, string, memo)
    return true if string.empty?
    if memo.key? string
        return memo[string]
    end
    size = string.size
    size.times do |i|
        if dict[string[0..i]] && is_valid_words?(dict, string[i+1..-1], memo)
            memo[string] = true
            return true
        end
    end
    memo[string] = false
    false
end
