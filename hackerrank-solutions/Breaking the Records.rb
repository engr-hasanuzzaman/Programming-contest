#!/bin/ruby

# problem link https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
require 'json'
require 'stringio'

# Complete the breakingRecords function below.
def breakingRecords(scores)
    low, high = scores.first, scores.first
    size = scores.size
    high_count = 0
    low_count = 0
    # puts "--size #{size}"
    (1...size).each do |i|
    #   puts "--i #{i}"
      num = scores[i]
      if num < low
        low_count += 1
        low = num
      elsif num > high
        high_count += 1
        high = num    
      end     
    end
    [high_count, low_count]
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

n = STDIN.gets.to_i

scores = STDIN.gets.rstrip.split(' ').map(&:to_i)

result = breakingRecords scores

fptr.write result.join " "
fptr.write "\n"

fptr.close()
