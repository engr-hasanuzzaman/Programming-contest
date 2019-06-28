#!/bin/ruby

require 'json'
require 'stringio'

# Complete the freqQuery function below.
def freqQuery(queries)
  e_dict = Hash.new(0)
  c_dict = Hash.new(0)
  q_array = []
  
  queries.each do |query|
    q, v = query[0], query[1]

    if q == 1
      insert(v, e_dict, c_dict)
    elsif q == 2
      delete(v, e_dict, c_dict)
    else 
      q_array << query(v, c_dict)
    end
  end
  
  q_array   
end

def insert(e, e_dict, c_dict)
  c_dict[e_dict[e]] -= 1
  e_dict[e] += 1
  c_dict[e_dict[e]] += 1
end

def delete(e, e_dict, c_dict)
  c_dict[e_dict[e]] -= 1
  e_dict[e] -= 1
  c_dict[e_dict[e]] += 1
end

def query(count, c_dict)
  return 1 if c_dict[count] >= 1
  0
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

q = gets.strip.to_i

queries = Array.new(q)

q.times do |i|
    queries[i] = gets.rstrip.split.map(&:to_i)
end

ans = freqQuery queries

fptr.write ans.join "\n"
fptr.write "\n"

fptr.close()
