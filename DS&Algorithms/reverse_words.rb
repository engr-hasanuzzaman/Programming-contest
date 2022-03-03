def reverse_word(arr)
    left = 0
    right = arr.size - 1
    while left < right
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    end
    puts "---after first swap #{arr}"
    left = right = 0
    while right < arr.size
        if arr[right] == ' ' || right == arr.size - 1
            puts "---right is #{right}, #{arr[right]}"
            # reverse
            right2 = (right == arr.size - 1) ? right : right - 1
            while left < right2
                arr[left], arr[right2] = arr[right2], arr[left]
                left += 1
                right2 -=1
            end
            left = right = right + 1
        else
            right += 1
        end
    end

    puts "---after conver is #{arr}"
    arr
end





input = ['t', 'h','i','s',' ', 'i','s',' ', 'f','o','o']
puts reverse_word(input) == ['f','o','o',' ','i','s',' ','t','h','i','s']