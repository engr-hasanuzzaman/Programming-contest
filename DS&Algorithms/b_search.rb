def find_first_index(arr, target)
    return -1 if arr.empty? || arr.first > target || target > arr.last
    return 0 if arr.first == target

    left = 0
    right = arr.size

    while left <= right
        mid = left + (right - left) / 2
        if arr[mid] == target && arr[mid-1] < target
            return mid
        elsif arr[mid] < target
            left = mid + 1
        else
            right = mid - 1
        end
    end

    return -1
end

arr = [1,2,2,2,3,3,3,3,3,3,4,6,7,7,7,7,7,9]
puts "--------[1,2,2,2,3,3,3,3,3,3,4,5,6,7,7,7,7,7,9] for 2 #{find_first_index(arr, 2)}"
puts "--------[1,2,2,2,3,3,3,3,3,3,4,5,6,7,7,7,7,7,9] for 3 #{find_first_index(arr, 3)}"
puts "--------[1,2,2,2,3,3,3,3,3,3,4,5,6,7,7,7,7,7,9] for 4 #{find_first_index(arr, 4)}"
puts "--------[1,2,2,2,3,3,3,3,3,3,4,5,6,7,7,7,7,7,9] for 0 #{find_first_index(arr, 0)}"
puts "--------[1,2,2,2,3,3,3,3,3,3,4,5,6,7,7,7,7,7,9] for 9 #{find_first_index(arr, 9)}"
puts "--------[1,2,2,2,3,3,3,3,3,3,4,5,6,7,7,7,7,7,9] for 5 #{find_first_index(arr, 5)}"
puts "--------[1,2,2,2,3,3,3,3,3,3,4,5,6,7,7,7,7,7,9] for 10 #{find_first_index(arr, 10)}"