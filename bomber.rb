def max_val(arr)
    # track is there bomb on row, col
    r_size = arr.size - 1
    c_size = arr.first.size - 1
    b_matrix = Array.new(r_size+1){Array.new(c_size+1){nil}}
    puts "i m #{b_matrix}"
    r_size.times do |i|
        c_size.times do |j|
            if arr[i][j] == -1
                b_matrix[i] =  Array.new(c_size+1){-1}
                r_size.times do |k|
                    b_matrix[k][j] = -1
                end
            end
        end
    end
    puts "b_matrix is #{b_matrix}"
end

#def mark_bomb_row_col(i, j)
#    arr[i].
#end
# testing area
input = [
    [-1, 8, -1, 3, -1],
    [5, 3, 2, 4, 3],
    [2, 2, 4, 5, 2]
]
max_val(input)