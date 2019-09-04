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

puts max_subarray([-1,2,4,-3,5,2,-5,2])