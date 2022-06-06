def permutation(arr, visited = {}, cur_per = [], ans = [])
  if cur_per.size == arr.size
    ans << cur_per[0..-1]
  else
    arr.each do |num|
      next if visited[num]

      visited[num] = true
      cur_per.push num
      permutation(arr, visited, cur_per, ans)

      visited[num] = false
      cur_per.pop
    end
  end

  ans
end

# check Python implementation which seems easier

puts "-----permutation of 1,2,3 is #{permutation([1, 2, 3])}"
