#!/bin/ruby

n = gets.strip.to_i
arr = gets.strip
arr = arr.split(' ').map(&:to_i)
hash = { positive: 0, negetive: 0, zero: 0}
arr.each do |n|
    if n.zero?
        hash[:zero] += 1
    elsif n > 0
       hash[:positive] += 1
    else
      hash[:negetive] += 1  
    end
end

puts hash[:positive] / n.to_f
puts hash[:negetive] / n.to_f
puts hash[:zero] / n.to_f
