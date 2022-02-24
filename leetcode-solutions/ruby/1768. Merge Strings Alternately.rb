# https://leetcode.com/problems/merge-strings-alternately/

# @param {String} word1
# @param {String} word2
# @return {String}
def merge_alternately(word1, word2)
    idx1 = 0
    idx2 = 0
    ans = ""
    while idx1 < word1.size && idx2 < word2.size
        ans += (word1[idx1] + word2[idx2])
        idx1 += 1
        idx2 += 1
    end
    
    ans += word1[idx1..-1]
    ans += word2[idx2..-1]
    ans
end
