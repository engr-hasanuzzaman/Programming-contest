# find the smallest sub-array with sum >= k

def min_subarray(a, k)
  min_size = a.size
  l = 0
  c_sum = 0

  a.each_with_index do |n, r|
    c_sum += n

    while c_sum >= k
      min_size = [min_size, r - l + 1].min
      c_sum -= a[l]
      l += 1
    end
  end

  min_size
end

input = [4,2,2,7,8,1,2,8,1,0]
k = 8
puts min_subarray(input, k)