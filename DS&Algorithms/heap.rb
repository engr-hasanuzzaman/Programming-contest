# array => heap
# normal procedure that take nlogn time but actual heapify take logn time (last to first)
def make_heap(arr)
    # puts "input is #{arr}"
    last_index = arr.size - 1
    (arr.size - 1).downto(0) do |s_index|
        heapify(arr, s_index, last_index)
      #  puts "aster #{s_index}, #{arr}"
    end
end

# update heap property s_index to e_index
def heapify(arr, s_index, e_index)
    return if s_index == e_index
    i = s_index

    while left(i) <= e_index
        puts "#{left(i)}, #{e_index}"
        if left(i) == e_index # only left child
            if arr[left(i)] > arr[i]
                arr[left(i)], arr[i] = arr[i], arr[left(i)]
            end
            return
        elsif [arr[left(i)], arr[right(i)]].max < arr[i]
            return
        else
            if arr[right(i)] > arr[left(i)]
                arr[right(i)], arr[i] = arr[i], arr[right(i)]
                i = right(i)
            else
                arr[left(i)], arr[i] = arr[i], arr[left(i)]
                i = left(i)
            end
        end
    end
end

# h_size is current heap size, add element to end of the 
def add_element(heap, h_size, element)
    e_index = h_size
    while head(e_index) >= 0 && heap[head(e_index)] < element
        heap[head(e_index)], heap[e_index] = heap[e_index], heap[head(e_index)]
        e_index = head(e_index)
    end
end

def delete(arr, h_size)
    return if h_size == 1
    arr[0], arr[h_size-1] = arr[h_size-1], arr[0]
    heapify(arr, 0, h_size - 2)
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

def heap_sort(arr)
    make_heap(arr)
    h_size = arr.size
    arr.size.times do |i|
        delete(arr, h_size)
        h_size -= 1
    end
end
# testing areasize
input = [8,6,3,10, 5, 4,9]
heap_sort(input)
p input