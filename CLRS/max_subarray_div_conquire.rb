require 'pry'
# [left_index_start_point_of_max_sub_array, right_index_start_point_of_max_sub_array, max_sum]
def max_sub_array_with_middle_crosse(a, min, mid, max)
    # process the left part including mid element
    left_max = -Float::MAX
    left_index = min
    sum = 0
    mid.downto(min) do |i|
        sum += a[i]
        if left_max < sum
            left_max = sum
            left_index = i
        end
    end

    # process of the right part
    right_max = -Float::MAX
    sum = 0
    right_index = mid + 1
    (mid + 1).upto(max) do |j|
        sum += a[j]
        if sum > right_max
            right_max = sum
            right_index = j
        end
    end

    [left_index, right_index, left_max + right_max]
end

def max_sub_array(a, min, max)
    # handle base case, one element
    return [min, max, a[max]] if min == max

    mid = ((max + min)/ 2).floor
    left_max_sub_array = max_sub_array(a, min, mid)
    right_max_sub_array = max_sub_array(a, mid+1, max)
    middle_cross_sub_array = max_sub_array_with_middle_crosse(a, min, mid, max)
    max_sum = [left_max_sub_array.last, right_max_sub_array.last, middle_cross_sub_array.last].max
    if left_max_sub_array.last === max_sum
        left_max_sub_array
    elsif right_max_sub_array.last === max_sum
        right_max_sub_array
    else
        middle_cross_sub_array
    end
end

input = [2, -3, 6, 12, -9, 21, -2, -5, 9]
p max_sub_array(input, 0, input.size - 1)