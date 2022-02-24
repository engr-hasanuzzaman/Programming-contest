# https://leetcode.com/problems/valid-palindrome-ii/

# @param {String} s
# @return {Boolean}
def valid_palindrome(s)
    is_palindrom?(s, 1)
end

def is_palindrom?(str, num_of_remove)
    return true if str.empty?
    
    left = 0
    right = str.size - 1
    while left < right
        if str[left] != str[right]
            if num_of_remove.zero?
                return false
            else
                return is_palindrom?(str[left...right], 0) || is_palindrom?(str[left+1..right], 0)
            end
        end
        
        left += 1
        right -= 1
    end
    true
end
