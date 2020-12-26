# array => heap
def heapify(arr)
    # h_size is current h_size
    1.upto(arr.size-1) do |h_size|
        add_element(arr, h_size, arr[h_size])
    end
end

# h_size is current heap size
def add_element(heap, h_size, element)
    e_index = h_size
    while head(e_index) >= 0 && heap[head(e_index)] < element
        heap[head(e_index)], heap[e_index] = heap[e_index], heap[head(e_index)]
        e_index = head(e_index)
    end
end

# if i is node position then it return head position
def head(i)
    ((i - 1) / 2).floor
end

# if root is 0 then left child is 0*2+1 = 1
def left(i)
    i * 2 + 1
end

# if root is 0 then right child is 0*2+2 = 2
def right(i)
    i * 2 + 2
end

# testing areasize
input = [4, 10, 3, 5, 1]
heapify(input)
p input