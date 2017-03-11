#!/bin/ruby

m,n = gets.strip.split(' ')
m = m.to_i
n = n.to_i
magazine = gets.strip
magazine = magazine.split(' ')
ransom = gets.strip
ransom = ransom.split(' ')
r_hash = ransom.each_with_object(Hash.new(0)){|n, h| h[n] += 1}
result_hash = magazine.each_with_object(r_hash){|n, h| h[n] -= 1}

if result_hash.values.select{|n| n > 0}.size > 0
    print 'No'
else
    print 'Yes '
end
