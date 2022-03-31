def gen_subset(n, k = 1, sub_set = [], ans = [])
  if k == n + 1
    ans << sub_set[0..1]
  else
    gen_subset(n, k + 1, sub_set, ans)
    sub_set << k
    gen_subset(n, k + 1, sub_set, ans)
    sub_set.pop
  end

  ans
end

puts "----with input 3 #{gen_subset(3)}"
puts "----with input 1 #{gen_subset(1)}"
puts "----with input 5 #{gen_subset(5)}"