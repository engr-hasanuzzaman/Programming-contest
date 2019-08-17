#!/bin/ruby

require 'json'
require 'stringio'
require 'set'

# Complete the maxCircle function below.
def maxCircle(queries)
  friendship_dict = Hash.new{|h, k| h[k] = Set.new }
  max_circle_size = 0
  resuls = []

  queries.each do |q|
    i, j = q
    current_f_circle = Set.new

    # puts "i #{i} #{friendship_dict[i]}, j #{j} #{friendship_dict[j]}"
    # append j to i's friends
    friendship_dict[i] do |i_friend|
      # prevend self friend   
      next if i_friend == j
      friendship_dict[i_friend] << j
      current_f_circle = current_f_circle | friendship_dict[i_friend]
    end
    
    friendship_dict[i] << j
    # puts "i_set #{friendship_dict[i]}"
    current_f_circle = current_f_circle | friendship_dict[i]


    # append i to j's friends
    friendship_dict[j] do |j_friend|
      # prevend self friend   
      next if j_friend == i
      friendship_dict[j_friend] << i
      current_f_circle = current_f_circle | friendship_dict[j_friend]
    end
    
    friendship_dict[j] << i
    # puts "j_set #{friendship_dict[j]}"
    current_f_circle = current_f_circle | friendship_dict[j]
    puts "#{current_f_circle}"
    max_circle_size = [current_f_circle.size, max_circle_size].max

    # puts "#{friendship_dict}"
    resuls << max_circle_size
  end
#   puts "qu #{queries}"
  resuls
end

# def add_friend(firend_dict, f, )

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

q = gets.to_i

queries = Array.new(q)

q.times do |i|
    queries[i] = gets.rstrip.split(' ').map(&:to_i)
end

ans = maxCircle queries

fptr.write ans.join "\n"
fptr.write "\n"

fptr.close()

