# @param {String} s
# @param {String} t
# @return {Boolean}
def backspace_compare(s, t)
    stackify(s) == stackify(t)
end

def stackify(str)
    stack = []
    
    str.chars do |c|
        if c == '#'
            stack.pop
        else
            stack << c
        end
    end
    
    stack
end