# https://leetcode.com/problems/word-ladder-ii/

# @param {String} begin_word
# @param {String} end_word
# @param {String[]} word_list
# @return {String[][]}
def find_ladders(begin_word, end_word, word_list)
    # keeping path
    queue = [[begin_word]]
    ans = []
    words = Set.new(word_list)
    words.delete(begin_word)
    found = false
    visited = 
    until queue.empty? || found
        level_size = queue.size
        visited = {}
        level_size.times do
            cur_path = queue.shift
            n_words = neighbors(cur_path.last)
            ans << cur_path if cur_path.last == end_word
            
            n_words.each do |neighbor|
                if words.include?(neighbor)
                    new_path = cur_path + [neighbor]
                    queue << new_path
                    visited[neighbor] = true
                end
            end
        end
        # remove all the visited elment of this level to prevent infinite loop
        visited.keys.each do |word|
            words.delete(word)
        end
    end
    ans
end

def neighbors(str)
    chars = str.split("")
    neighbors = []
    chars.size.times do |i|
        temp = chars[i]
        ('a'..'z').each do |char|
            chars[i] = char
            neighbors << chars.join
        end
        chars[i] = temp
    end
    neighbors
end
