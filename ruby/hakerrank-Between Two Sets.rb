#!/bin/ruby

n,m = gets.strip.split(' ')
n = n.to_i
m = m.to_i
a = gets.strip
a = a.split(' ').map(&:to_i)
b = gets.strip
b = b.split(' ').map(&:to_i)
a.sort!
b.sort!

def calculateGCD(numbers)
    if numbers.size <= 2
        if numbers[1].nil?
            return numbers[0]
        else
            return numbers[0].gcd numbers[1]
        end
        
    else 
        half = numbers.size / 2
        left = calculateGCD numbers[0...half]
        right = calculateGCD numbers[half..-1]
        return left.gcd right
    end    
end

def calculateLCM(numbers)
    if numbers.size <= 2
        if numbers[1].nil?
            return numbers[0]
        else
            return numbers[0].lcm numbers[1]
        end
        
    else 
        half = numbers.size / 2
        left = calculateLCM numbers[0...half]
        right = calculateLCM numbers[half..-1]
        return left.lcm right
    end    
end

puts calculateGCD b
puts calculateLCM a

