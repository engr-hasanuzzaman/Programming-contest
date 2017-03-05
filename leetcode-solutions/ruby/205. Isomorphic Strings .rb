# @param {String} s
# @param {String} t
# @return {Boolean}
def is_isomorphic(s, t)
    s_used_char = {}
    t_used_char = {}
    
    s.size.times do |i|
        if s_used_char[s[i]]
            return false unless s_used_char[s[i]] == t[i]
        end
        s_used_char[s[i]] = t[i]
        
        if t_used_char[t[i]]
            return false unless t_used_char[t[i]] == s[i]
        end
        t_used_char[t[i]] = s[i]
    end
    
    return true
end
