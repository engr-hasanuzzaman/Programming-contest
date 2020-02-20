# find the max sum of contiguous sub-array with size k
def c_max_sum(a, k)
  
  sum = a[0...k].sum
  max_sum = sum 
  l = 0
  for i in k...a.size
    sum = sum + a[i] - a[l]
    max_sum = [max_sum, sum].max
    l += 1
  end

  max_sum
end

input = [4,2,1,7,8,1,2,8,1,0]
puts c_max_sum(input, 4)
