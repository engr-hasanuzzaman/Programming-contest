# https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

# Time limit exceed solution n ** 2 solution

# @param {Integer} n
# @param {Integer[]} start_pos
# @param {String} s
# @return {Integer[]}
def execute_instructions(n, start_pos, s)
    ans = []
    start = 0
    while start < s.size
        ans << count_moves(n, start_pos[0], start_pos[1], s[start..])
        start += 1
    end
    ans
end

def count_moves(size, row, col, ins, cur_count = 0)
    return cur_count if ins.size.zero?
    moves = {
        "R" => [0, 1],
        "L" => [0, -1],
        "U" => [-1, 0],
        "D" => [1, 0]
    }
    new_row = row + moves[ins[0]][0]
    new_col = col + moves[ins[0]][1]
    ins = ins[1..] 
    if new_row >= size || new_row < 0 || new_col >= size || new_col < 0
        return cur_count
    end
    return count_moves(size, new_row, new_col, ins, cur_count + 1)
end

# LTE with more passing cases
def execute_instructions(n, start_pos, s)
    ans = []
    start = 0
    moves = {
        "R" => [0, 1],
        "L" => [0, -1],
        "U" => [-1, 0],
        "D" => [1, 0]
    }
    while start < s.size
        ans << count_moves(n, start_pos[0], start_pos[1], s[start..], moves)
        start += 1
    end
    ans
end

def count_moves(size, row, col, instructions, moves)
    cur_count = 0
    instructions.each_char do |ins|
        row = row + moves[ins[0]][0]
        col = col + moves[ins[0]][1]
        if row >= size || row < 0 || col >= size || col < 0
            return cur_count
        end
        cur_count += 1
    end
    cur_count
end