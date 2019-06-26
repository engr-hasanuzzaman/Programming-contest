#!/bin/ruby

require 'json'
require 'stringio'

# Complete the hourglassSum function below.
def hourglassSum(arr)
  max_sum = -100
  4.times do |i|
    4.times do |j|
      sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
      p("i: #{i}, j: #{j}, sum #{sum}")      
      max_sum = [max_sum, sum].max
    end
  end
  max_sum
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

arr = Array.new(6)

6.times do |i|
    arr[i] = gets.rstrip.split(' ').map(&:to_i)
end

result = hourglassSum arr

fptr.write result
fptr.write "\n"

fptr.close()
