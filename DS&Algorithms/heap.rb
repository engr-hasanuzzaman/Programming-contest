# array => heap
# normal procedure that take nlogn time but actual heapify take logn time (last to first)
def make_heap(arr)
    # h_size is current h_size
    1.upto(arr.size-1) do |h_size|
        add_element(arr, h_size, arr[h_size])
    end
end

def heapify(arr)
    max_index = arr.size
    max_index.downto(0) do |i|
        if left(i) > max_index && right(i) > max_index
            next
        elsif left(i) < max_index && right(i) < max_index
            if arr[left(i)] <= arr[i] && right(i) <= arr[i]
                next
            else
                if arr[left(i)] > arr[right(i)]
                    arr[left(i)], arr[i] = arr[i], arr[left(i)]
                else
                    arr[right(i)], arr[i] = arr[i], arr[right(i)]
                end
            end
            arr[left(i)], arr[i] = arr[i], arr[left(i)]
        else

        end
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
make_heap(input)
p input