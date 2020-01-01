# https://leetcode.com/problems/find-k-closest-elements/

# @param {Integer[]} arr
# @param {Integer} k
# @param {Integer} x
# @return {Integer[]}
def find_closest_elements(arr, k, x)
    left = 0
    right = arr.size
    
    while left < right
        mid = (left + right) / 2
        if arr[mid] == x
            left = mid
        elsif x > arr[mid]
          left = mid + 1
        else
            right = mid
        end
    end
    
    puts left
    
    if left == arr.size
        arr[arr.size-k..-1]
    elsif left == 0 && arr[left] != x
        arr[0...k]
    elsif arr[left] == x
        find_x_near(arr, left, k)
    end
end
  
def find_x_near(arr, i, x)
    left = i
    right = i
    l = true
    (x - 1).times do
        if l && left > 0
            left -= 1
            l = false
        elsif right < arr.size - 1 && !l
            right += 1
            l = true
        elsif l && left == 0
            right += 1
        elsif !l && right == arr.size - 1
            left -= 1
            l = true
        end
    end
    puts "#{left}, #{right}"
    arr[left..right]
end