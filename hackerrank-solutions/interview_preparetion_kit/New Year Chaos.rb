#!/bin/ruby

require 'json'
require 'stringio'

# Complete the minimumBribes function below.
def minimumBribes(q)
    num_of_bribe = 0
    q.each_with_index do |n, i|
      if n - (i + 1) > 2
        print("Too chaotic")
        print("\n")
        return
      else
        position_diff = n - (i + 1)
        if position_diff > 0
          num_of_bribe += position_diff
        end
      end      
    end

   p num_of_bribe 
end

t = gets.to_i

t.times do |t_itr|
    n = gets.to_i

    q = gets.rstrip.split(' ').map(&:to_i)

    minimumBribes q
end
