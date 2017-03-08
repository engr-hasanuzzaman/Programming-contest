#!/bin/ruby

a = gets.strip
b = gets.strip
size_of_a = a.size
size_of_b = b.size
anagram_size = 0

# make sure a alway contain smaller string
a, b = b, a if size_of_a > size_of_b

hash_a = Hash.new 0
hash_b = Hash.new 0

b.size.times do |i|
 hash_a[a[i]] += 1    
 hash_b[b[i]] += 1    
end

a.chars.uniq.each do |c|
    if hash_b[c] > hash_a[c]
       anagram_size += hash_a[c]
    else
        anagram_size += hash_b[c]
    end
end

print (size_of_a + size_of_b) - anagram_size * 2
