# @param {Integer} area
# @return {Integer[]}
def construct_rectangle(area)
    return [] if area.zero?
    
    max_div = Math.sqrt(area).to_i
    
    while max_div >= 2
        if area % max_div == 0
            return [area / max_div, max_div]
        end
        max_div -= 1
    end
    
    return [area, 1]
end
