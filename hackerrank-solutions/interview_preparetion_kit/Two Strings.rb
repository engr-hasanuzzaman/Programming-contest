#!/bin/ruby

require 'json'
require 'stringio'

# Complete the twoStrings function below.
def twoStrings(s1, s2)
  char_dict = {}

  s1.each_char do |c|
    char_dict[c] = 1
  end  

  s2.each_char{|c| return 'YES' if char_dict[c] == 1 }
  return 'NO'
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

q = gets.to_i

q.times do |q_itr|
    s1 = gets.to_s.rstrip

    s2 = gets.to_s.rstrip

    result = twoStrings s1, s2

    fptr.write result
    fptr.write "\n"
end

fptr.close()
