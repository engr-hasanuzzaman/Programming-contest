=begin
// algorithm
=end
def merge_sort(q, p, r)
end

def merge(a, p, q, r)
    left_array = []
    right_array = []
    p.upto(q) do |i|
        left_array << a[i]
    end

    (q+1).upto(r) do |i|
        right_array << a[i]
    end

    
end