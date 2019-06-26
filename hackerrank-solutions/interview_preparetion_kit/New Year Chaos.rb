#!/bin/ruby

require 'json'
require 'stringio'

# Complete the minimumBribes function below.
def minimumBribes(q)
  num_of_bribe = 0
  a_size = q.size

  q.each_with_index do |n, i|
    if n - (i + 1) > 2
      print("Too chaotic")
      print("\n")
      return
    else
      j = [q[i] - 2, 0].max
      while(j < i) do
        if q[j] > q[i]
          num_of_bribe += 1
        end

        j += 1
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
