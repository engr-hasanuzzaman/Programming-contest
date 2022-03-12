# https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

# @param {String} s
# @param {Integer} max_letters
# @param {Integer} min_size
# @param {Integer} max_size
# @return {Integer}
def max_freq(s, max_letters, min_size, max_size)
    letter_counter = 0
    let_freq = Hash.new(0)
    left = 0
    right = 0
    str_freq_counter = Hash.new(0)
    while right < s.size
        chr = s[right]
        let_freq[chr] += 1
        
        # track counter
        if let_freq[chr] == 1
            letter_counter += 1
        end
        
        # window shrink condition
        while letter_counter > max_letters || (right - left + 1) > max_size
            let_freq[s[left]] -= 1
            if let_freq[s[left]] == 0
                letter_counter -= 1
            end
            left += 1
        end
        
        t_left = left
        t_right = right
        while t_right - t_left + 1 >= min_size
            str_freq_counter[s[t_left..t_right]] += 1
            t_left += 1
        end
        
        right += 1
    end
    
    str_freq_counter.values.max || 0
end


