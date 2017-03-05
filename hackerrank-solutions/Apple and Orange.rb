#!/bin/ruby

s,t = gets.strip.split(' ')
s = s.to_i
t = t.to_i
a,b = gets.strip.split(' ')
a = a.to_i
b = b.to_i
m,n = gets.strip.split(' ')
m = m.to_i
n = n.to_i
apple = gets.strip
apple = apple.split(' ').map(&:to_i)
orange = gets.strip
orange = orange.split(' ').map(&:to_i)
num_of_apple = 0
num_of_orange = 0

apple.each do |ap|
    num_of_apple += 1 if (s..t) === (ap + a)
end

orange.each do |o|
    num_of_orange += 1 if (s..t) === (o + b)
end

puts num_of_apple
puts num_of_orange

