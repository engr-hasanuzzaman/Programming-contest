#!/bin/ruby

require 'json'
require 'stringio'

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries)
  arr = Array.new(n, 0)
  max_sum = 0

  queries.each do |q|
    #p "query is #{q}"
    a, b, k = q[0] - 1, q[1] - 1 , q[2]

    arr[a] += k
    arr[b + 1] -= k  if b + 1 < n 
  end

  arr.each do |e|
   max_sum = [max_sum, max_sum + e].max 
  end

  max_sum
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')
nm = gets.rstrip.split
n = nm[0].to_i
m = nm[1].to_i
queries = Array.new(m)

m.times do |i|
  queries[i] = gets&.rstrip&.split(' ')&.map(&:to_i)
end

result = arrayManipulation n, queries
fptr.write result
fptr.write "\n"
fptr.close()
