#!/bin/ruby

require 'json'
require 'stringio'

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b)
    # Write your code here
    min_num = a.min
    max_num = b.min
    count = 0
    while min_num <= max_num
      count += 1 if check_arr_factor(a, min_num) && num_factor(b, min_num)
      min_num += 1
    end

    count
end

def check_arr_factor(arr, num)
  arr.each do |n|
    return false if num % n != 0
  end

  true
end

def num_factor(arr, num)
  arr.each do |n|
    return false if n % num != 0
  end

  true
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

first_multiple_input = gets.rstrip.split

n = first_multiple_input[0].to_i

m = first_multiple_input[1].to_i

arr = STDIN.gets.rstrip.split.map(&:to_i)

brr = STDIN.gets.rstrip.split.map(&:to_i)

total = getTotalX arr, brr

fptr.write total
fptr.write "\n"

fptr.close()
