=begin
You are given a sorted array with repeated numbers. [1,1,1,3,3,3,3,3,4,5,6,6,6]
Your task is to return the array by not repeating any number more than twice. And the array count. (In place)
Output : [1,1,3,3,4,5,6,6]
=end

def remove_extra_duplicate(arr)
    last_number = nil
    left = right = 0
    counter = 0
    while right < arr.size
      if arr[right] != last_number || counter < 2
        # reset counter
        if arr[right] != last_number
          counter = 0
        end
        counter += 1
        arr[left] = arr[right]
        left += 1
        last_number = arr[right]
      end
      
      right += 1
    end
    arr[0...left]
  end