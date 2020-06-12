require 'benchmark'

iterations = 10_000
small      = 10
big        = 1_000_00

small_hash = {}
big_hash   = {}

(1..small).each do |i|
  small_hash[i] = i
end

(1..big).each do |i|
  big_hash[i] = i
end

Benchmark.bmbm do |bm|
  bm.report('Small Hash') do
    iterations.times { small_hash.keys }
  end

  bm.report('Big Hash') do
    iterations.times { big_hash.keys }
  end
end