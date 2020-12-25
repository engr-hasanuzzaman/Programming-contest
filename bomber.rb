def max_val(arr, k)
    # track is there bomb on row, col
    r_size = arr.size
    c_size = arr.first.size
    b_matrix = get_m_matrix(arr, r_size, c_size)
    s_cells = get_non_safe_pos(arr, b_matrix, r_size, c_size)
end

def get_m_matrix(arr, r_size, c_size)
    b_matrix = Array.new(r_size){Array.new(c_size){nil}}
    r_size.times do |i|
        c_size.times do |j|
            if arr[i][j] == -1
                b_matrix[i] =  Array.new(c_size){-1}
                r_size.times do |k|
                    b_matrix[k][j] = -1
                end
            end
        end
    end
    b_matrix
end

# original matrix, m indicating m b_m
def get_non_safe_pos(m, b_m, r_size, c_size)
    cells = []
    r_size.times do |i|
        c_size.times do |j|
            if m[i][j] != -1 && b_m[i][j] == -1
                cells << [m[i][j], i, j]
            end
        end
    end
    cells.sort_by{|e| -e.first}
end
#def mark_bomb_row_col(i, j)
#    arr[i].
#end
# testing area
input = [
    [-1, 8, -1, 3, -1],
    [5, 3, 2, 4, 3],
    [3, 2, 4, 5, 2]
]
max_val(input)