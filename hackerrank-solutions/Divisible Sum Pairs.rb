#!/bin/ruby

n,k = gets.strip.split(' ')
n = n.to_i
k = k.to_i
a = gets.strip
a = a.split(' ').map(&:to_i)

result = 0

n.times do |i|
    j = i.next
    
    while j < n
        result += 1 if (a[i] + a[j]) % k == 0
        j += 1
    end
end

print result
