# @param {String} s
# @return {Integer}
def roman_to_int(s)
    rom_int_map = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M:1000 }.freeze
    prev_int, curr_int = 0, 0
    index = s.size - 1
    result = 0
    
    index.downto(0) do |i|
        curr_int = rom_int_map[s[i].to_sym]
        
        if prev_int > curr_int
            result -= rom_int_map[s[i].to_sym] 
        else
            result += rom_int_map[s[i].to_sym] 
        end
        
        prev_int = curr_int
    end
    
    result
end
