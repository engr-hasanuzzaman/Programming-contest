#!/bin/ruby

require 'json'
require 'stringio'

# Complete the timeInWords function below.
def timeInWords(h, m)


end

def hour(h)
  h = h % 12

  case h
  when 0 then "twelve"
  when 1 then "one"
  when 2 then "two"
  when 3 then "three"
  when 4 then "four"
  when 5 then "five"
  when 6 then "six"
  when 7 then "seven"
  when 8 then "eight"
  when 9 then "nine"
  when 10 then "ten"
  when 11 then "eleven"
end

def minutes(m)
  m = m.to_i
  
  if m <= 30
    
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

h = gets.to_i

m = gets.to_i

result = timeInWords h, m

fptr.write result
fptr.write "\n"

fptr.close()
