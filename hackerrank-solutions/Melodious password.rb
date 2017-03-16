#!/bin/ruby

n = gets.strip.to_i

vowel = %w(a e i o u)

# since y is not allow
consonant = ('a'..'z').to_a - vowel - ['y']

result = []

vowel.each{|c| result << c.to_s }
consonant.each{|c| result << c.to_s }

def is_vowel?(vowel, char)
  vowel.include? char
end

while(n >= 2)
    temp_result = []
    
    result.each do |pass|
        if is_vowel?(vowel, pass[-1])
            consonant.each{|c| temp_result << "#{pass}#{c}"}
        else
            vowel.each{|c| temp_result << "#{pass}#{c}"}
        end
    end
    
    result = temp_result
    
    n -= 1
end

puts result
        
        
