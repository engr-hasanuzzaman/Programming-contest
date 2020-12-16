=begin
Alogorithm: (1 based index)
1. j = 2 to A.size
2. i = j - 1, key = A[j]
3. while i >= 1 & A[i] > key
4.      A[i+1] = A[i]
5.  a[i+1] = key
=end
def insertion_sort(a)
    1.upto(a.size - 1) do |j|
        key = a[j]
        i = j - 1
        while i >= 0 && a[i] > key
            a[i+1] = a[i]
            i -= 1
        end 
        a[i+1] = key
    end

    a
end

p insertion_sort([1,10,7,4,7,2,-2,-5,0,9090,12,-76])