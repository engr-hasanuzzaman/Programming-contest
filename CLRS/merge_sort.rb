=begin
// algorithm
=end
def merge_sort(a, p, r)
    return unless p < r

    q = ((r + p)/2).floor
    merge_sort(a, p, q)
    merge_sort(a,q+1, r)
    merger(a, p, q, r)
end

def merger(a, p, q, r)
    left_array = []
    right_array = []
    p.upto(q) do |i|
        left_array << a[i]
    end

    (q+1).upto(r) do |i|
        right_array << a[i]
    end
    left_array << Float::MAX
    right_array << Float::MAX
    i = 0
    j = 0
    p.upto(r) do |k|
        if left_array[i] <= right_array[j]
            a[k] = left_array[i]
            i += 1
        else
            a[k] = right_array[j]
            j += 1
        end
    end
end
a = [1,3,2, 45, 2, -2, 98, 3, 0, 2, -21]
merge_sort(a, 0, a.size - 1)
p a