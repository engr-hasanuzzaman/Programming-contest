# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
# @param {String} s
# @return {Integer}
def min_add_to_make_valid(s)
    count = 0
    stack = []
    s.each_char do |c|
        if c == "("
            stack << c
        else
            if stack.empty?
                count += 1
            else
                stack.pop
            end
        end
    end
    return count + stack.size
end
