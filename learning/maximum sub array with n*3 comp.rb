def max_subarray(arr)
  size = arr.size
  sum = 0
  (size - 1).times do |a|
    a.upto(size-1) do |b|
      s = 0
      i = a
      while i <= b
        s += arr[i]
        i += 1
      end
      sum = [sum, s].max
    end
  end

  sum
end

# complexity O(n)
def max_subarray_n(arr)
  p = 0
  s = 0
  k = 0

  while k < arr.size - 1
    s = arr[k] > s + arr[k] ? arr[k] : arr[k] + s
    p = [p, s].max
    k += 1
  end
  
  p
end

puts max_subarray([-1,2,4,-3,5,2,-5,2])
puts max_subarray_n([-1,2,4,-3,5,2,-5,2])