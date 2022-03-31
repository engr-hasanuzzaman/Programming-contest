# recursive ways to generate sub-set
def gen_subset(n, k = 1, sub_set = [], ans = [])
  if k == n + 1
    ans << sub_set[0..-1]
  else
    gen_subset(n, k + 1, sub_set, ans)
    sub_set << k
    gen_subset(n, k + 1, sub_set, ans)
    sub_set.pop
  end

  ans
end

# puts "----with input 3 #{gen_subset(3)}"
# puts "----with input 1 #{gen_subset(1)}"
# puts "----with input 5 #{gen_subset(5)}"

# iterative ways to generate sub-set
# Each subset of a set of n elements can be represented as a sequence of n bits,
# which corresponds to an integer between 0...2 ** n - 1
# The ones in the bit sequence
# indicate which elements are included in the subset.

# for (int b = 0; b < (1<<n); b++) {
#     vector<int> v;
#     for (int i = 0; i < n; i++) {
#         if (b&(1<<i)) v.push_back(i+1);
#     }
# }
def get_it_subset(n)
  ans = []
  max = (1 << n) # 2 ** n - 1
  max.times do |num|
    sub_set = []
    n.times do |i|
      sub_set << i + 1 if (num & (1 << i)).positive?
    end
    ans << sub_set[0..-1]
  end

  ans
end

puts "----with input 3 #{get_it_subset(3).sort == gen_subset(3).sort}"
puts "----with input 1 #{get_it_subset(1).sort == gen_subset(1).sort}"
puts "----with input 5 #{get_it_subset(5).sort == gen_subset(5).sort}"
