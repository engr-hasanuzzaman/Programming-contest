# https://leetcode.com/problems/letter-tile-possibilities/

# @param {String} tiles
# @return {Integer}
def num_tile_possibilities(tiles)
    result = []
    comb = []
    1.upto(tiles.size) do |i|
        combination(result, comb, tiles, i)    
    end
    # puts "-#{result}"
    result.uniq.size
end

def combination(result, comb, tiles, length)
    if length == 0
        result << comb.map{|n| n} if comb.size > 0
    end
    
    tiles.each_char.with_index do |c, i|
        comb << c
        combination(result, comb, tiles[0...i] + tiles[i+1..-1], length - 1)
        comb.pop
    end
end