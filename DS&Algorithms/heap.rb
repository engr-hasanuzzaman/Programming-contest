# array => heap
def heapify(arr)
    heap_size = 1
    2.upto(arr.size - 1) do |i|
        heap_size += 1
        while 
    end
end

def add_element(heap, h_size, element)
    heap[h_size-1] = element

    while heap[((h_size - 1)/2).floor] >= 0 && heap[((h_size - 1)/2).floor] > element
        heap  
end

def head(i)
    ((i - 1) / 2).floor
end